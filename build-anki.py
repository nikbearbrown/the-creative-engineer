#!/usr/bin/env python3
"""build-anki.py — orchestrate textbook -> Anki .apkg.

Runs from the repo root. Reads anki-config.yaml if present. Keys come from a
single .env file at the repo root (gitignored).

Full build:
    python build-anki.py

Test mode (cheap, fast iteration — especially with ElevenLabs audio):
    python build-anki.py --test                 # first eligible chapter only
    python build-anki.py --chapter 01           # one specific chapter
    python build-anki.py --test --max-audio 2   # cap audio to 2 cards
    python build-anki.py --test -y              # skip the human gate (loop fast)

Test runs write to *-TEST.apkg and a "(test)" deck, so they never clobber the
real deck.

Sequence: list chapters -> extract cards (Anthropic) -> [human gate] ->
generate audio (ElevenLabs, optional, OFF by default) -> build .apkg (genanki).
"""
import argparse
import datetime
import importlib.util
import json
import os
import re
import sys

try:
    import genanki, requests, yaml  # noqa: F401  (presence check)
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install genanki requests pyyaml")
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
SCRIPTS_DIR = os.path.join(ROOT, "scripts")
OUTPUT_DIR = os.path.join(ROOT, "output")

DEFAULTS = {
    "deck_name": "",
    "audio": False,                                # audio OFF by default
    "elevenlabs_voice_id": "21m00Tcm4TlvDq8ikWAM",
    "cards_per_chapter_target": 10,
    "skip_chapters": [],
    "test_chapter": "",                            # default chapter for --test (else first eligible)
}

TEST_AUDIO_DEFAULT = 3   # in --test, voice at most this many cards unless --max-audio given


def load_env():
    """Load keys from a single .env at the repo root. Real env vars win."""
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def load_helper(filename):
    path = os.path.join(SCRIPTS_DIR, filename)
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_")[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_config():
    cfg = dict(DEFAULTS)
    path = os.path.join(ROOT, "anki-config.yaml")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            user = yaml.safe_load(fh) or {}
        for k, v in user.items():
            if k == "audio":
                cfg["audio"] = bool(v)
            elif k == "skip_chapters" and isinstance(v, list):
                cfg["skip_chapters"] = v
            elif v not in (None, ""):
                cfg[k] = v
    return cfg


def _matches(fname, q):
    stem = fname[:-3]
    if q in (fname, stem):
        return True
    if stem.startswith(q + "-") or stem.startswith(q):
        return True
    m = re.match(r"^(\d+)", stem)
    return bool(m) and m.group(1) == q.zfill(len(m.group(1)))


def select_chapters(all_files, *, chapter=None, test=False, limit=None, test_chapter=""):
    """Pick which chapter files to process. Returns (files, mode_label)."""
    if chapter:
        picked = [f for f in all_files if _matches(f, chapter)]
        return picked, f"chapter={chapter}"
    if test:
        if test_chapter:
            picked = [f for f in all_files if _matches(f, test_chapter)]
            if picked:
                return picked[:1], f"test:{test_chapter}"
        # default: first real content chapter (skip front/back matter)
        content = [f for f in all_files
                   if "frontmatter" not in f and "front-matter" not in f
                   and "back-matter" not in f and not f.startswith("99")]
        return (content or all_files)[:1], "test"
    if limit:
        return all_files[:limit], f"limit={limit}"
    return all_files, "full"


def main():
    ap = argparse.ArgumentParser(description="Build an Anki .apkg from the book's chapters.")
    ap.add_argument("--test", action="store_true", help="process only one chapter (fast/cheap iteration)")
    ap.add_argument("--chapter", help="process only this chapter (stem, filename, or leading number)")
    ap.add_argument("--limit", type=int, help="process only the first N chapters")
    ap.add_argument("--max-audio", type=int, dest="max_audio",
                    help="cap audio generation to N cards (default: %d in --test)" % TEST_AUDIO_DEFAULT)
    ap.add_argument("-y", "--yes", action="store_true", help="skip the human gate (auto-continue)")
    args = ap.parse_args()

    load_env()
    cfg = load_config()
    slug = os.path.basename(ROOT)
    is_test = args.test or bool(args.chapter) or bool(args.limit)
    deck_name = (cfg["deck_name"] or slug) + (" (test)" if is_test else "")
    date = datetime.date.today().isoformat()
    suffix = "-TEST" if is_test else ""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cards_json = os.path.join(OUTPUT_DIR, f"{slug}-cards-{date}{suffix}.json")
    apkg_path = os.path.join(OUTPUT_DIR, f"{slug}-anki-{date}{suffix}.apkg")
    log_path = os.path.join(OUTPUT_DIR, f"{slug}-anki-{date}{suffix}.log")
    log = []

    skip = set(cfg["skip_chapters"])
    all_files = [f for f in sorted(os.listdir(CHAPTERS_DIR))
                 if f.endswith(".md") and f[:-3] not in skip]
    chapter_files, mode = select_chapters(
        all_files, chapter=args.chapter, test=args.test,
        limit=args.limit, test_chapter=cfg["test_chapter"])

    if not chapter_files:
        sys.exit(f"No chapter matched (mode: {mode}). Available: {[f[:-3] for f in all_files][:5]}...")

    print(f"Mode: {mode}  |  chapters to process: {len(chapter_files)}")
    if is_test:
        print("  " + ", ".join(f[:-3] for f in chapter_files))

    extract = load_helper("extract-cards.py")
    gen_audio = load_helper("gen-audio.py")
    build_apkg = load_helper("build-apkg.py")

    # extract
    cards = extract.run(CHAPTERS_DIR, chapter_files, cfg["cards_per_chapter_target"], log)
    with open(cards_json, "w", encoding="utf-8") as fh:
        json.dump(cards, fh, indent=2, ensure_ascii=False)

    # ---- HUMAN GATE ----
    term_n = sum(1 for c in cards if c["type"] == "term")
    concept_n = len(cards) - term_n
    per_chapter = {}
    for c in cards:
        per_chapter[c["chapter"]] = per_chapter.get(c["chapter"], 0) + 1
    print(f"\nTotal cards extracted: {len(cards)}  (term: {term_n}, concept: {concept_n})")
    print("\nCards per chapter:")
    for ch in sorted(per_chapter):
        print(f"  {ch:<40} {per_chapter[ch]}")
    print("\nSample (first 5):")
    for c in cards[:5]:
        print(f"  [{c['type']}] {c['front']}")
        print(f"      -> {c['back'][:80]}{'...' if len(c['back']) > 80 else ''}")

    audio_note = "audio ON" if cfg["audio"] else "audio OFF (default)"
    if args.yes:
        print(f"\n[-y] skipping human gate, continuing.  [{audio_note}]")
    else:
        print(f"""
Card extraction complete. Review the sample above.  [{audio_note}]
To continue with the .apkg build, press Enter.
To abort and inspect the full card JSON first, type 'q' and press Enter.
""")
        if input().strip().lower() == "q":
            print(f"Intermediate card JSON: {cards_json}")
            sys.exit(0)

    # audio (optional; OFF by default). In test mode, cap the number of audio cards.
    if cfg["audio"]:
        max_audio = args.max_audio if args.max_audio is not None else (TEST_AUDIO_DEFAULT if is_test else None)
        audio_map = gen_audio.run(cards, cfg["elevenlabs_voice_id"], log, max_cards=max_audio)
    else:
        print("Audio is off (set `audio: true` in anki-config.yaml to enable). Building text-only.")
        log.append("audio: disabled by config (audio: false)")
        audio_map = {}

    stats = build_apkg.run(cards, audio_map, deck_name, apkg_path, log)

    summary = [
        f"Anki build — {slug} — {date}  [mode: {mode}]",
        f"chapters processed : {len(chapter_files)}",
        f"cards extracted    : {len(cards)} (term {term_n} / concept {concept_n})",
        f"cards with audio   : {stats['with_audio']} / {len(cards)}",
        f"deck               : {deck_name}",
        f"apkg               : {apkg_path}",
        "",
        "Per-chapter / events:",
    ] + log
    with open(log_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(summary) + "\n")
    print("\n" + "\n".join(summary))


if __name__ == "__main__":
    main()
