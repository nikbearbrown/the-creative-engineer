#!/usr/bin/env python3
"""extract-facts.py — mine vetted textbooks into a shared fact dictionary.

Reads an OpenStax CNXML book (collection.xml + modules), extracts atomic,
decontextualized facts via the Anthropic API, cites each to its source with a
trust tier, and merges them into facts.json with a DERIVED consensus:

  1 supporting source      -> consensus "unverified"  (candidate)
  2+ supporting sources    -> consensus "agreement"   (corroborated)
  same substance, diff precision -> "partial"
  any refuting source      -> consensus "conflict"    (human review queue)

Sources are named and tiered (facts-sources.yaml); weights are deferred.
Nothing is human-verified by extraction — OpenStax facts are "source-attested".

  python extract-facts.py ../books/osbooks-anatomy-physiology            # calibrate: first module, then STOP
  python extract-facts.py ../books/osbooks-anatomy-physiology --module m45981
  python extract-facts.py ../books/osbooks-anatomy-physiology --all
  python extract-facts.py ../books/osbooks-biology-bundle --collection biology-2e --all

Key from .env (this dir or parent) or ANTHROPIC_API_KEY env var.
"""
import argparse
import datetime
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

try:
    import requests, yaml
except ImportError as e:
    print(f"Missing dependency: {e}\nRun: pip install requests pyyaml")
    sys.exit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
FACTS_JSON = os.path.join(HERE, "facts.json")
SOURCES_YAML = os.path.join(HERE, "facts-sources.yaml")
COL = "{http://cnx.rice.edu/collxml}"
MD = "{http://cnx.rice.edu/mdml}"
CN = "{http://cnx.rice.edu/cnxml}"
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-opus-4-6"
ANTHROPIC_VERSION = "2023-06-01"
TODAY = datetime.date.today().isoformat()

SYSTEM_PROMPT = """You extract atomic, citable FACTS from a vetted textbook section. A fact is a single
declarative claim that is true independent of the surrounding text.

Rules:
- ATOMIC: one claim per fact. Split compound sentences.
- DECONTEXTUALIZED: rewrite into a standalone present-tense statement. Resolve pronouns and
  "this/these" references ("This process needs ATP" -> name the process). A reader must understand
  the fact with no other context.
- GROUNDED: every fact must be directly supported by a sentence in the provided text. Put that exact
  sentence in "verbatim". Do NOT invent facts or add outside knowledge.
- Prefer definitions, constants, quantities, structural/functional relationships, mechanisms, and
  classifications. Skip narrative, motivation, exercises, and figure-only captions.
- Mark "stable": true for definitions, constants, anatomy, historical dates; false for statistics,
  guidelines, approval status, or anything that changes over time.

Return ONLY a JSON array. No preamble, no fences. Schema per fact:
{
  "canonical": "standalone present-tense statement",
  "verbatim": "the exact supporting sentence from the text",
  "domain": ["one or two subject tags"],
  "stable": true,
  "category": "BASIC" | "DEFINITION" | "QUANTITY" | "MECHANISM" | "CLASSIFICATION"
}"""

USER_TEMPLATE = """Book: {book}
Section: {chapter} — {module_title}

Extract the atomic facts from this section text:

{text}"""


# ---------- shared fact model (the one store every fact tool routes through) ----------
sys.path.insert(0, HERE)
from facts_store import load_sources, source_meta, make_fact, merge_fact, recompute_consensus  # noqa: E402


# ---------- env ----------
def load_env():
    for path in (os.path.join(HERE, ".env"), os.path.join(os.path.dirname(HERE), ".env")):
        if os.path.exists(path):
            for line in open(path, encoding="utf-8"):
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


# ---------- collection parsing ----------
def find_collection(book_dir, name=None):
    cdir = os.path.join(book_dir, "collections")
    cols = sorted(f for f in os.listdir(cdir) if f.endswith(".xml"))
    if name:
        cols = [c for c in cols if name in c]
    if not cols:
        sys.exit(f"No collection found in {cdir}" + (f" matching '{name}'" if name else ""))
    return os.path.join(cdir, cols[0])


def parse_collection(path):
    root = ET.parse(path).getroot()
    slug = root.findtext(f".//{MD}slug") or "openstax-book"
    title = root.findtext(f".//{MD}title") or slug
    pairs = []  # (chapter_title, module_id)

    def walk(el, chapter):
        for child in el:
            tag = child.tag.replace(COL, "")
            if tag == "module":
                pairs.append((chapter, child.get("document")))
            elif tag == "subcollection":
                t = child.findtext(f"{MD}title") or chapter
                c = child.find(f"{COL}content")
                if c is not None:
                    walk(c, t)
            elif tag == "content":
                walk(child, chapter)

    content = root.find(f"{COL}content")
    if content is not None:
        walk(content, "(front matter)")
    return slug, title, pairs


def module_text(book_dir, module_id):
    path = os.path.join(book_dir, "modules", module_id, "index.cnxml")
    root = ET.parse(path).getroot()
    mtitle = root.findtext(f"{CN}title") or module_id
    content = root.find(f"{CN}content")
    text = " ".join(t.strip() for t in content.itertext() if t.strip()) if content is not None else ""
    text = re.sub(r"\s+", " ", text).strip()
    return mtitle, text




# ---------- extraction ----------
def call_api(book, chapter, module_title, text):
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print("ERROR: ANTHROPIC_API_KEY not set (needed to extract facts).")
        sys.exit(1)
    body = {"model": MODEL, "max_tokens": 4096, "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": USER_TEMPLATE.format(
                book=book, chapter=chapter, module_title=module_title, text=text)}]}
    headers = {"x-api-key": key, "anthropic-version": ANTHROPIC_VERSION, "content-type": "application/json"}
    resp = requests.post(API_URL, headers=headers, json=body, timeout=120)
    resp.raise_for_status()
    raw = "".join(b.get("text", "") for b in resp.json().get("content", []) if b.get("type") == "text")
    raw = re.sub(r"^```[a-z]*\n?|\n?```$", "", raw.strip())
    return json.loads(raw)


HANDOFF = os.path.join(HERE, "_handoff")


def citation_for(slug, repo, module_id):
    # source = the specific book (two different books = two votes); publisher groups same-publisher
    return {"source": slug, "publisher": "openstax", "book": slug, "repo": repo,
            "module": module_id, "url": f"https://openstax.org/books/{slug}"}


def cmd_prepare(book_dir, slug, title, repo, targets):
    """Handoff mode: write one prompt file per module to run through ANY LLM (no key)."""
    os.makedirs(HANDOFF, exist_ok=True)
    manifest = {}
    n = 0
    for chapter, module_id in targets:
        mtitle, text = module_text(book_dir, module_id)
        if len(text) < 200:
            continue
        prompt = (f"# Fact extraction — paste EVERYTHING below into any LLM (Claude, ChatGPT,\n"
                  f"# Gemini, a local model — a chat window is fine, no API key needed).\n"
                  f"# Save its JSON reply to: facts/_handoff/{module_id}.result.json\n\n"
                  f"===== SYSTEM =====\n{SYSTEM_PROMPT}\n\n"
                  f"===== INPUT =====\n{USER_TEMPLATE.format(book=title, chapter=chapter, module_title=mtitle, text=text)}\n")
        open(os.path.join(HANDOFF, f"{module_id}.prompt.md"), "w", encoding="utf-8").write(prompt)
        manifest[module_id] = {"chapter": chapter, "title": mtitle, "citation": citation_for(slug, repo, module_id)}
        n += 1
    json.dump(manifest, open(os.path.join(HANDOFF, "manifest.json"), "w"), indent=2)
    print(f"Wrote {n} prompt(s) to facts/_handoff/.")
    print("For each <module>.prompt.md: paste it into your LLM of choice, save the JSON")
    print("reply as facts/_handoff/<module>.result.json — then run the same command with --ingest.")


def cmd_ingest(sources):
    """Handoff mode: merge the LLM results you saved back into facts.json."""
    mpath = os.path.join(HANDOFF, "manifest.json")
    if not os.path.exists(mpath):
        sys.exit("No facts/_handoff/manifest.json — run with --prepare first.")
    manifest = json.load(open(mpath))
    facts = json.load(open(FACTS_JSON, encoding="utf-8"))
    actions, done = {}, 0
    for module_id, meta in manifest.items():
        rpath = os.path.join(HANDOFF, f"{module_id}.result.json")
        if not os.path.exists(rpath):
            continue
        raw = re.sub(r"^```[a-z]*\n?|\n?```$", "", open(rpath, encoding="utf-8").read().strip())
        try:
            extracted = json.loads(raw)
        except Exception as e:
            print(f"  bad JSON in {module_id}.result.json: {e}"); continue
        cit = meta["citation"]
        tier, _ = source_meta(cit.get("publisher", "unknown"), sources)
        for ex in extracted:
            if not ex.get("canonical") or not ex.get("verbatim"):
                continue
            r = merge_fact(facts, make_fact(ex, cit, tier, sources), sources)
            actions[r] = actions.get(r, 0) + 1
        done += 1
    json.dump(facts, open(FACTS_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Ingested {done} result file(s). facts.json now {len(facts)} facts. actions: {actions}")
    print(f"  review queue: {sum(1 for f in facts if f.get('needs_review'))}")


def main():
    ap = argparse.ArgumentParser(description="Extract facts from an OpenStax CNXML book.")
    ap.add_argument("book_dir", help="path to an osbooks-* repo")
    ap.add_argument("--collection", help="collection name substring (for bundles)")
    ap.add_argument("--module", help="extract one module by id")
    ap.add_argument("--limit", type=int, help="first N modules")
    ap.add_argument("--all", action="store_true", help="all modules in the collection")
    ap.add_argument("--prepare", action="store_true",
                    help="HANDOFF: write prompts to run through ANY LLM (no key, no Claude required)")
    ap.add_argument("--ingest", action="store_true",
                    help="HANDOFF: merge the LLM results you saved back into facts.json")
    args = ap.parse_args()

    load_env()
    sources = load_sources()

    if args.ingest:
        cmd_ingest(sources)
        return

    repo = os.path.basename(os.path.normpath(args.book_dir))
    col_path = find_collection(args.book_dir, args.collection)
    slug, title, pairs = parse_collection(col_path)
    print(f"Book: {title}  | slug: {slug} | repo: {repo} | modules: {len(pairs)}")

    if args.module:
        targets = [(c, m) for c, m in pairs if m == args.module] or [("", args.module)]
    elif args.all:
        targets = pairs
    elif args.limit:
        targets = pairs[:args.limit]
    else:
        # calibration: first real content module (skip front matter)
        content = [(c, m) for c, m in pairs if "front" not in c.lower()]
        targets = (content or pairs)[:1]

    if args.prepare:
        cmd_prepare(args.book_dir, slug, title, repo, targets)
        return

    facts = json.load(open(FACTS_JSON, encoding="utf-8"))
    actions = {}
    for chapter, module_id in targets:
        mtitle, text = module_text(args.book_dir, module_id)
        if len(text) < 200:
            print(f"  skip {module_id} ({mtitle}): too short")
            continue
        url = f"https://openstax.org/books/{slug}"
        # source = the specific book (so two different OpenStax books = two votes);
        # publisher = openstax (so they're still flagged same_publisher).
        citation = {"source": slug, "publisher": "openstax", "book": slug,
                    "repo": repo, "module": module_id, "url": url}
        tier, _ = source_meta("openstax", sources)
        try:
            extracted = call_api(title, chapter, mtitle, text)
        except Exception as e:
            print(f"  ERROR {module_id}: {e}")
            continue
        for ex in extracted:
            if not ex.get("canonical") or not ex.get("verbatim"):
                continue
            r = merge_fact(facts, make_fact(ex, citation, tier, sources), sources)
            actions[r] = actions.get(r, 0) + 1
        print(f"  {module_id} ({mtitle[:40]}): +{len(extracted)} extracted")

    json.dump(facts, open(FACTS_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    review = [f for f in facts if f.get("needs_review")]
    print(f"\nfacts.json now {len(facts)} facts")
    print("  this run: " + ", ".join(f"{k}={v}" for k, v in sorted(actions.items())) or "  (no changes)")
    print(f"  consensus: agreement={sum(1 for f in facts if f['consensus']=='agreement')}"
          f"  partial={sum(1 for f in facts if f['consensus']=='partial')}"
          f"  unverified={sum(1 for f in facts if f['consensus']=='unverified')}"
          f"  conflict={sum(1 for f in facts if f['consensus']=='conflict')}")
    print(f"  human review queue (needs_review): {len(review)}"
          f"  [conflicts, numeric mismatches, possible duplicates]")
    if not args.all and not args.module and not args.limit:
        print("\nCALIBRATION: review the new facts in facts.json — are they atomic, decontextualized,\n"
              "and is each 'verbatim' actually present in the source? Then run --all to batch the book.")


if __name__ == "__main__":
    main()
