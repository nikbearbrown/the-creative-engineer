#!/usr/bin/env python3
"""extract-cards.py — extract Anki flashcards from textbook chapters via the
Anthropic API. Imported and called by build-anki.py; can also run standalone.

Returns a list of card dicts:
  {"type": "term"|"concept", "front": str, "back": str,
   "chapter": stem, "tags": [str, ...]}
"""
import json
import os
import re
import sys
import time

try:
    import requests
except ImportError:
    print("Missing dependency: requests  (pip install requests)")
    sys.exit(1)

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-opus-4-6"
ANTHROPIC_VERSION = "2023-06-01"
MAX_TOKENS = 4096

SYSTEM_PROMPT = """You are an expert educator building Anki flashcards from a textbook chapter.
You extract two types of cards:
1. Term cards: front = the term, back = definition as used in this chapter
2. Concept cards: front = a question requiring explanation or application,
   back = a concise answer (3-6 sentences)

Return ONLY a JSON array. No preamble. No markdown. No explanation.
Schema per card:
{
  "type": "term" | "concept",
  "front": "string",
  "back": "string",
  "chapter": "string",   // chapter filename stem, e.g. "03-thermodynamics"
  "tags": ["string"]     // always include type and chapter:NN
}"""

USER_TEMPLATE = """Chapter: {chapter_stem}
Card count target: {target} cards (mix of term and concept)
Previously seen terms (do not duplicate): {seen_terms_json}

Chapter text:
{chapter_text}"""


def require_api_key():
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print("ERROR: ANTHROPIC_API_KEY not set. Card extraction needs it.")
        print("Set it and re-run:  export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)
    return key


def _chapter_number(stem):
    m = re.match(r"^(\d+)", stem)
    return m.group(1) if m else "00"


def _strip_fences(text):
    text = text.strip()
    text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n?```$", "", text)
    return text.strip()


def call_api(api_key, chapter_stem, chapter_text, target, seen_terms):
    headers = {
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
        "content-type": "application/json",
    }
    body = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": [{
            "role": "user",
            "content": USER_TEMPLATE.format(
                chapter_stem=chapter_stem,
                target=target,
                seen_terms_json=json.dumps(sorted(seen_terms)),
                chapter_text=chapter_text,
            ),
        }],
    }
    for attempt in range(2):
        resp = requests.post(API_URL, headers=headers, json=body, timeout=120)
        if resp.status_code == 429 and attempt == 0:
            time.sleep(10)
            continue
        resp.raise_for_status()
        data = resp.json()
        return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    resp.raise_for_status()


def run(chapters_dir, chapter_files, target, log):
    """chapter_files: list of filenames (in order). Returns list of card dicts."""
    api_key = require_api_key()
    seen_terms = set()
    all_cards = []
    for fname in chapter_files:
        stem = fname[:-3] if fname.endswith(".md") else fname
        nn = _chapter_number(stem)
        path = os.path.join(chapters_dir, fname)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as e:
            log.append(f"ERROR reading {fname}: {e}")
            continue
        try:
            raw = call_api(api_key, stem, text, target, seen_terms)
            cards = json.loads(_strip_fences(raw))
            if not isinstance(cards, list):
                raise ValueError("response was not a JSON array")
        except json.JSONDecodeError as e:
            log.append(f"ERROR {stem}: malformed JSON from API ({e}) — chapter skipped")
            continue
        except Exception as e:
            log.append(f"ERROR {stem}: {e} — chapter skipped")
            continue

        kept = 0
        for c in cards:
            if not isinstance(c, dict):
                continue
            front = str(c.get("front", "")).strip()
            back = str(c.get("back", "")).strip()
            ctype = c.get("type", "concept")
            if not front or not back:
                continue
            if len(front.split()) > 20:
                log.append(f"skip {stem}: front too long ({len(front.split())} words): {front[:40]}...")
                continue
            if ctype == "term":
                key = front.lower()
                if key in seen_terms:
                    continue
                seen_terms.add(key)
            tags = c.get("tags") or []
            if ctype not in tags:
                tags.append(ctype)
            chap_tag = f"chapter:{nn}"
            if chap_tag not in tags:
                tags.append(chap_tag)
            all_cards.append({
                "type": ctype, "front": front, "back": back,
                "chapter": stem, "tags": tags,
            })
            kept += 1
        log.append(f"{stem}: {kept} cards")
    return all_cards


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters-dir", default="chapters")
    ap.add_argument("--target", type=int, default=10)
    args = ap.parse_args()
    files = sorted(f for f in os.listdir(args.chapters_dir) if f.endswith(".md"))
    logs = []
    cards = run(args.chapters_dir, files, args.target, logs)
    print(json.dumps(cards, indent=2, ensure_ascii=False))
    print("\n".join(logs), file=sys.stderr)
