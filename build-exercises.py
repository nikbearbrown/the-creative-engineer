#!/usr/bin/env python3
"""build-exercises.py — generate a practice-exercise suite per chapter.

Each chapter gets one markdown file in editions/exercises/ with, per major
concept: an exploratory problem (productive failure), an annotated worked
example, 2-3 faded examples, then a graduated independent set (Tier 1
Consolidation -> Tier 5 Challenge), plus a Cumulative Review of prior chapters.
Every problem is grounded in the chapter text via the Anthropic API.

Calibration first, then batch (wired to verify.py):
    python build-exercises.py               # calibration: first chapter only, then STOP
    python build-exercises.py --chapter 04  # one specific chapter
    python build-exercises.py --all         # batch — needs the calibration file verified
    python build-exercises.py --all --force # batch without the calibration gate

Keys come from the single .env at the repo root.
"""
import argparse
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
    "output_dir": "editions/exercises",
    "cumulative_review": True,
}

SYSTEM_PROMPT = """You build rigorous practice exercises from textbook chapters. Every exploratory
problem, worked example, faded step, and exercise MUST be grounded in the provided chapter text,
not in general knowledge. Return ONLY the markdown file. No preamble, no fences.

First infer the chapter type (introductory / procedural / conceptual / applied) — it sets where
the weight falls:
  Introductory: Tier 1-2 heavy, Tier 3 light, Tier 4-5 minimal
  Procedural:   Tier 1-2 heavy, Tier 3 medium, Tier 4-5 light (the faded-example arc is critical)
  Conceptual:   Tier 1-2 medium, Tier 3 medium, Tier 4-5 medium (exploratory problems surface misconceptions)
  Applied:      Tier 1-2 medium, Tier 3 heavy, Tier 4-5 heavy

For EACH major (##) concept section, produce in order:

1) EXPLORATORY PROBLEM (before the worked example). The student cannot yet solve it — that is the
   design (productive failure). Frame it: "Before reading further, attempt this problem. You are not
   expected to solve it correctly. The goal is to explore what a solution would need to do." Make it
   ill-structured (multiple reasonable approaches), activating prior knowledge, tied to the concept
   the worked example teaches. One short paragraph. No solution here.

2) WORKED EXAMPLE (annotated — this is the mechanism, not a solution key). Start by naming the
   problem type and why the method applies. Annotate WHY at every non-obvious step. Flag decision
   points where students go wrong and why the wrong path fails. Reference the exploratory problem
   ("you may have tried X; here is why it fails/partially works"). End with the general principle.

3) FADED EXAMPLES (2-3). Systematically remove steps so the student generates the missing parts.
   Fade 1: remove the final step. Fade 2: remove the final two steps. Fade 3 (optional, complex
   procedures): remove a key middle step. Fade only STRUCTURALLY MEANINGFUL steps, never trivial
   arithmetic. For each: present problem + partial solution, mark the gap `[Your work here]`, add a
   self-explanation prompt ("Before filling this in, explain in one sentence what this step must
   accomplish"), and give the complete solution in a clearly marked answer block.

Then ONE independent EXERCISE SET (8-15 problems), every problem labeled with its tier:
  Tier 1 Consolidation (3-5, required): isomorphic to the worked example — same deep structure,
    meaningfully different surface features. Never solvable by copying numbers from the example.
  Tier 2 Extension (3-4, required): same procedure + one complication (novel context, structural
    variation, boundary condition). Optional one-sentence hint.
  Tier 3 Integration (2-3, required from chapter 2 onward; OMIT for chapter 1): combine this
    chapter with 1-2 prior chapters; student must identify which concept applies first. Label
    "Integration — draws on Chapters N and M."
  Tier 4 Transfer (1-2, optional): a type not explicitly covered; student infers the approach.
  Tier 5 Challenge (1, optional): open-ended, no unique answer; give a discussion of productive
    approaches, not a single solution.

CUMULATIVE REVIEW (2-3 problems, from chapter 3 onward; OMIT for chapters 1-2): revisit PRIOR
material directly (distinct from Tier 3). Label "Cumulative Review — Chapter N."

SOLUTIONS: every Tier 1-4 problem gets a complete ANNOTATED solution: name the problem type and
strategy; one-line WHY annotation per step; flag the most common error and why it fails; a section
reference. Tier 2/3 additionally name the distinguishing variation; Tier 3 names which prior-chapter
concept is combined and why.

NEVER: consolidation problems solvable by copying the example's numbers; "list/define" recall items
(every exercise must require DOING something with the concept); integration/cumulative items for a
chapter with no available priors; faded steps that are trivial; challenge problems with a hidden
single answer; worked examples that list steps without reasoning annotation.

OUTPUT STRUCTURE:
# Exercises — Chapter N: [Title]
## [Concept 1]
### Exploratory Problem
### Worked Example
### Faded Examples
#### Faded Example 1 ... #### Faded Example 2
### Exercise Set
#### Tier 1 — Consolidation ... #### Tier 5 — Challenge (optional)
(repeat per concept)
---
## Cumulative Review (from chapter 3 onward)
---
## Solutions
[annotated solutions for all Tier 1-4 problems]"""

USER_TEMPLATE = """Chapter file: {stem}
Chapter title: {title}

Tier 3 Integration: {integration}.  Cumulative Review: {cumulative}.
  - When Integration is OFF, omit Tier 3 entirely (no prior concept chapters to integrate).
  - When Cumulative Review is OFF, omit the Cumulative Review block.
  - When ON, use ONLY the prior concept chapters listed below.

Major section headings (one major concept each — produce the per-concept arc for each):
{headings}

Prior concept chapters available for integration / cumulative review (use ONLY these):
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
    path = os.path.join(ROOT, "exercises-config.yaml")
    if os.path.exists(path):
        user = yaml.safe_load(open(path, encoding="utf-8")) or {}
        for k, v in user.items():
            if k == "skip_chapters" and isinstance(v, list):
                cfg[k] = v
            elif k == "cumulative_review":
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


def quiz_path(cfg, stem):   # output path helper
    return os.path.join(cfg["output_dir"], f"exercises-{stem}.md")


def is_content(fname):
    n = fname.lower()
    return ("frontmatter" not in n and "front-matter" not in n
            and "back-matter" not in n and not n.startswith("99")
            and "appendix" not in n)


def is_introduction(fname):
    return "introduction" in fname.lower()


def _strip_fences(t):
    t = t.strip()
    t = re.sub(r"^```[a-zA-Z]*\n?", "", t)
    t = re.sub(r"\n?```$", "", t)
    return t.strip()


def generate(stem, text, prior_concept_titles, integration, cumulative, cfg):
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print("ERROR: ANTHROPIC_API_KEY not set (needed to generate exercises).")
        sys.exit(1)
    title = title_of(text, stem)
    headings = "\n".join(f"- {h}" for h in headings_of(text)) or "(none — infer concepts from the text)"
    prior = "\n".join(f"- {t}" for t in prior_concept_titles) if prior_concept_titles else "(none)"
    user = USER_TEMPLATE.format(stem=stem, title=title,
                                integration="ON" if integration else "OFF",
                                cumulative="ON" if cumulative else "OFF",
                                headings=headings, prior=prior, text=text)
    body = {"model": MODEL, "max_tokens": MAX_TOKENS, "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": user}]}
    headers = {"x-api-key": key, "anthropic-version": ANTHROPIC_VERSION, "content-type": "application/json"}
    resp = requests.post(API_URL, headers=headers, json=body, timeout=240)
    resp.raise_for_status()
    data = resp.json()
    return _strip_fences("".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text"))


def select(all_files, *, chapter, limit, batch):
    if chapter:
        return [f for f in all_files if f[:-3] == chapter or chapter_number(f[:-3]) == chapter.zfill(2) or f[:-3].startswith(chapter)][:1]
    if batch:
        return all_files
    if limit:
        return all_files[:limit]
    content = [f for f in all_files if is_content(f)]
    return (content or all_files)[:1]


def main():
    ap = argparse.ArgumentParser(description="Generate practice exercises per chapter.")
    ap.add_argument("--all", action="store_true", help="batch all chapters (needs calibration file verified)")
    ap.add_argument("--chapter", help="one chapter (stem / number / prefix)")
    ap.add_argument("--limit", type=int, help="first N chapters")
    ap.add_argument("--force", action="store_true", help="batch without the calibration gate")
    args = ap.parse_args()

    load_env()
    cfg = load_config()
    verify = load_helper("verify.py")
    os.makedirs(cfg["output_dir"], exist_ok=True)

    skip = set(cfg["skip_chapters"])
    all_files = [f for f in sorted(os.listdir(CHAPTERS_DIR)) if f.endswith(".md") and f[:-3] not in skip]
    content_files = [f for f in all_files if is_content(f)]

    if args.all and not args.force:
        calib = (content_files or all_files)[:1]
        if calib:
            cf = quiz_path(cfg, calib[0][:-3])
            code, label = verify.state(cf)
            if code != 0:
                print(f"Calibration exercises not verified ({label}): {cf}")
                print("Review it, run:  python scripts/verify.py sign %s --by <name> --note '...'" % cf)
                print("Then re-run --all  (or use --all --force to override).")
                sys.exit(1)

    targets = select(all_files, chapter=args.chapter, limit=args.limit, batch=args.all)
    if not targets:
        sys.exit("No chapter matched.")

    print(f"Generating {len(targets)} exercise file(s) -> {cfg['output_dir']}/")
    made, skipped = [], []
    for f in targets:
        stem = f[:-3]
        out = quiz_path(cfg, stem)
        code, _ = verify.state(out)
        if code == 0:
            print(f"  ✓ verified, skipping: {out}")
            skipped.append(out)
            continue
        text = open(os.path.join(CHAPTERS_DIR, f), encoding="utf-8").read()
        # prior CONCEPT chapters (exclude the roadmap Introduction): drives integration/cumulative
        prior_concept = []
        for pf in content_files:
            if pf == f:
                break
            if is_introduction(pf):
                continue
            prior_concept.append(title_of(open(os.path.join(CHAPTERS_DIR, pf), encoding="utf-8").read(), pf[:-3]))
        integration = len(prior_concept) >= 1               # Tier 3 from the 2nd concept chapter on
        cumulative = cfg["cumulative_review"] and len(prior_concept) >= 2   # from the 3rd on
        md = generate(stem, text, prior_concept, integration, cumulative, cfg)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(md.rstrip() + "\n")
        verify.cmd_stub(SimpleNamespace(artifact=out, phase="exercises"))
        made.append(out)

    print(f"\nGenerated: {len(made)} | skipped (verified): {len(skipped)}")
    if made and not args.all:
        print(f"""
CALIBRATION CHECK — review {made[0]} against:
  1. Does the exploratory problem require genuine exploration (not a hard quiz item)?
  2. Do faded examples remove structurally meaningful steps, not trivial ones?
  3. Do consolidation problems change surface features meaningfully from the worked example?
  4. Do integration problems require identifying which prior concept applies before solving?
  5. Do annotated solutions explain WHY each step is taken, not just what?
  6. Does every exercise require DOING something with the concept (not recall/define)?
If good:  python scripts/verify.py sign {made[0]} --by <name> --note "calibration ok"
Then:     python build-exercises.py --all
""")


if __name__ == "__main__":
    main()
