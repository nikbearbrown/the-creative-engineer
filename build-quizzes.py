#!/usr/bin/env python3
"""build-quizzes.py — generate a quiz suite per chapter (Chapter Quizzes edition).

Each chapter gets one markdown file in editions/quizzes/ with three layers:
prequiz (before reading), embedded section checks, and an end-of-chapter quiz
with interleaved review from prior chapters. Every item is grounded in the
chapter text via the Anthropic API.

Calibration first, then batch (the spec's workflow, wired to verify.py):
    python build-quizzes.py                 # calibration: first chapter only, then STOP for review
    python build-quizzes.py --chapter 04    # (re)generate one specific chapter
    python build-quizzes.py --all           # batch — requires the calibration quiz to be verified
    python build-quizzes.py --all --force   # batch without the calibration gate

Keys come from the single .env at the repo root.
"""
import argparse
import datetime
import importlib.util
import os
import re
import sys
from types import SimpleNamespace

try:
    import requests, yaml  # noqa: F401
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install requests pyyaml")
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
SCRIPTS_DIR = os.path.join(ROOT, "scripts")
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-opus-4-6"
ANTHROPIC_VERSION = "2023-06-01"
MAX_TOKENS = 8192

DEFAULTS = {
    "skip_chapters": ["00-frontmatter", "99-back-matter"],
    "output_dir": "editions/quizzes",
    "interleave_review": True,
}

SYSTEM_PROMPT = """You build rigorous chapter quizzes from textbook chapters. Every stem, distractor,
and explanation MUST be grounded in the provided chapter text — never in general knowledge.
Return ONLY the markdown quiz file. No preamble, no fences.

Produce three layers:

LAYER 1 — PREQUIZ (before reading): 2-4 items on the chapter's most important concepts.
Short-answer / fill-in-the-blank only (NO multiple choice — recognition defeats the purpose).
Frame: "Answer before reading. Getting these wrong is expected and useful." Give no answers here.

LAYER 2 — SECTION CHECKS: after each major (##) section, 1-3 fast items (MCQ or 1-3 word answer)
on that section's single most important concept, each with immediate feedback.

LAYER 3 — END-OF-CHAPTER QUIZ: 10-15 items. 8-12 from this chapter covering all section
objectives; 2-3 interleaved review items from prior chapters (only those provided), each
labeled "Review — Chapter N". Apply the Bloom distribution for the chapter type:
  Introductory: 55-65% Remember/Understand, 25-35% Apply/Analyze, 5-10% Evaluate/Create
  Procedural:   15-20% / 55-65% / 15-20%
  Conceptual:   25-35% / 40-50% / 15-20%
  Applied:      10-15% / 50-60% / 25-30%
Every quiz includes at least 2 Apply/Analyze items. Label each item with its Bloom level.
Format mix: mostly MCQ; 2-3 short-answer; at least one "micro-create" (propose a test case,
find the bug, choose between two approaches and justify, extend a derivation one step) for
Evaluate/Create. Mark 3-5 items with a confidence prompt ("How confident? Low/Med/High")
before feedback; flag high-confidence-error items ("you were confident — read this closely").

MCQ RULES: exactly 3 options; one correct; two distractors grounded in REAL misconceptions
(never absurd); stem is a complete answerable question (not "Which is true?"); options parallel
in grammar/length; no all/none/combination options; no negative stems unless the objective is
exception detection; correct option not consistently longer/more hedged; never copy chapter
sentences verbatim into stems or options.

FEEDBACK per section-check and end-of-chapter item: confirm the correct answer; 2-3 sentences
why it's correct; one sentence per distractor naming the misconception; a section reference.

NEVER: dismissable distractors; items that only test a memorized bolded term (>= half the items
must require doing something with the concept); "Which of the following is true/correct?" stems;
all-of-the-above / combination options; more than 3 options; review items from chapters not provided.

OUTPUT STRUCTURE:
# Quiz — Chapter N: [Title]
## Before You Read
[prequiz items, no answers]
---
## Section Checks
### [section heading]
[items + immediate feedback]
---
## End-of-Chapter Quiz
[10-15 items labeled by Bloom level, full feedback, interleaved "Review — Chapter N" items]"""

USER_TEMPLATE = """Chapter file: {stem}
Chapter title: {title}
Chapter type: infer from the content (introductory / procedural / conceptual / applied) and apply the matching Bloom distribution.

Section headings in this chapter (place section checks after these):
{headings}

Learning objectives (use as the item blueprint; if empty, infer from headings/key concepts):
{objectives}

Prior chapters available for interleaved review (use ONLY these; if empty, omit review items):
{prior}

Full chapter text:
{text}"""


def load_env():
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def load_helper(filename):
    path = os.path.join(SCRIPTS_DIR, filename)
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_")[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_config():
    cfg = dict(DEFAULTS)
    path = os.path.join(ROOT, "quiz-config.yaml")
    if os.path.exists(path):
        user = yaml.safe_load(open(path, encoding="utf-8")) or {}
        for k, v in user.items():
            if k == "skip_chapters" and isinstance(v, list):
                cfg[k] = v
            elif k == "interleave_review":
                cfg[k] = bool(v)
            elif v not in (None, ""):
                cfg[k] = v
    return cfg


def chapter_number(stem):
    m = re.match(r"^(\d+)", stem)
    return m.group(1) if m else "00"


def title_of(text, stem):
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else stem


def headings_of(text):
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+)$", text, re.MULTILINE)]


def objectives_of(text):
    m = re.search(r"^#+\s*(Learning\s+)?Objectives?\b.*$", text, re.IGNORECASE | re.MULTILINE)
    if not m:
        return ""
    nxt = re.search(r"^#+\s+", text[m.end():], re.MULTILINE)
    return text[m.end(): m.end() + nxt.start()].strip() if nxt else text[m.end():].strip()


def quiz_path(cfg, stem):
    return os.path.join(cfg["output_dir"], f"quiz-{stem}.md")


def is_content(fname):
    n = fname.lower()
    return ("frontmatter" not in n and "front-matter" not in n
            and "back-matter" not in n and not n.startswith("99")
            and "appendix" not in n)


def _strip_fences(t):
    t = t.strip()
    t = re.sub(r"^```[a-zA-Z]*\n?", "", t)
    t = re.sub(r"\n?```$", "", t)
    return t.strip()


def generate(stem, text, prior_titles, cfg):
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print("ERROR: ANTHROPIC_API_KEY not set (needed to generate quizzes).")
        sys.exit(1)
    title = title_of(text, stem)
    headings = "\n".join(f"- {h}" for h in headings_of(text)) or "(none)"
    objectives = objectives_of(text) or "(none stated — infer)"
    prior = "\n".join(f"- {t}" for t in prior_titles) if (prior_titles and cfg["interleave_review"]) else "(none)"
    user = USER_TEMPLATE.format(stem=stem, title=title, headings=headings,
                                objectives=objectives, prior=prior, text=text)
    body = {"model": MODEL, "max_tokens": MAX_TOKENS, "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": user}]}
    headers = {"x-api-key": key, "anthropic-version": ANTHROPIC_VERSION, "content-type": "application/json"}
    resp = requests.post(API_URL, headers=headers, json=body, timeout=180)
    resp.raise_for_status()
    data = resp.json()
    return _strip_fences("".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text"))


def select(all_files, *, chapter, test, limit, batch):
    if chapter:
        return [f for f in all_files if f[:-3] == chapter or chapter_number(f[:-3]) == chapter.zfill(2) or f[:-3].startswith(chapter)][:1]
    if batch:
        return all_files
    if limit:
        return all_files[:limit]
    # calibration default: first content chapter (or first file)
    content = [f for f in all_files if is_content(f)]
    return (content or all_files)[:1]


def main():
    ap = argparse.ArgumentParser(description="Generate chapter quizzes.")
    ap.add_argument("--all", action="store_true", help="batch all chapters (needs calibration quiz verified)")
    ap.add_argument("--chapter", help="one chapter (stem / number / prefix)")
    ap.add_argument("--limit", type=int, help="first N chapters")
    ap.add_argument("--force", action="store_true", help="batch without the calibration gate")
    ap.add_argument("-y", "--yes", action="store_true", help="(reserved) auto-continue")
    args = ap.parse_args()

    load_env()
    cfg = load_config()
    verify = load_helper("verify.py")
    os.makedirs(cfg["output_dir"], exist_ok=True)

    skip = set(cfg["skip_chapters"])
    all_files = [f for f in sorted(os.listdir(CHAPTERS_DIR)) if f.endswith(".md") and f[:-3] not in skip]
    content_files = [f for f in all_files if is_content(f)]

    # batch gate: the calibration quiz (first content chapter) must be verified
    if args.all and not args.force:
        calib = (content_files or all_files)[:1]
        if calib:
            cq = quiz_path(cfg, calib[0][:-3])
            code, label = verify.state(cq)
            if code != 0:
                print(f"Calibration quiz not verified ({label}): {cq}")
                print("Review it, run:  python scripts/verify.py sign %s --by <name> --note '...'" % cq)
                print("Then re-run --all  (or use --all --force to override).")
                sys.exit(1)

    targets = select(all_files, chapter=args.chapter, test=False, limit=args.limit, batch=args.all)
    if not targets:
        sys.exit("No chapter matched.")

    print(f"Generating {len(targets)} quiz(zes) -> {cfg['output_dir']}/")
    made, skipped = [], []
    for f in targets:
        stem = f[:-3]
        out = quiz_path(cfg, stem)
        # don't regenerate a verified quiz
        code, _ = verify.state(out)
        if code == 0:
            print(f"  ✓ verified, skipping: {out}")
            skipped.append(out)
            continue
        text = open(os.path.join(CHAPTERS_DIR, f), encoding="utf-8").read()
        # prior chapters = content chapters before this one, by order
        prior_titles = []
        for pf in content_files:
            if pf == f:
                break
            ptext = open(os.path.join(CHAPTERS_DIR, pf), encoding="utf-8").read()
            prior_titles.append(title_of(ptext, pf[:-3]))
        md = generate(stem, text, prior_titles, cfg)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(md.rstrip() + "\n")
        verify.cmd_stub(SimpleNamespace(artifact=out, phase="quizzes"))
        made.append(out)

    print(f"\nGenerated: {len(made)} | skipped (verified): {len(skipped)}")
    if made and not args.all:
        print(f"""
CALIBRATION CHECK — review {made[0]} against:
  1. Are distractors grounded in real misconceptions (not obviously wrong)?
  2. Does the Bloom distribution match the chapter type?
  3. Does feedback explain WHY each distractor is wrong?
  4. Are any stems copied verbatim from the chapter?
  5. Do prequiz items cover the chapter's most important concepts?
If good:  python scripts/verify.py sign {made[0]} --by <name> --note "calibration ok"
Then:     python build-quizzes.py --all
""")


if __name__ == "__main__":
    main()
