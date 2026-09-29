# Chapter TL;DR Generator

> **Edition / enrichment pass.** Best run after GATE 3 (Human Rewrite) so the
> sections are stable, or any time chapters change structure. Idempotent: if a
> chapter already carries a `> **TL;DR:**` block, replace it rather than add a second.

**What it is:** A standalone TL;DR for each chapter — one 2–3 sentence overall summary plus a one-line preview of every `##` section — dropped in as a blockquote + table right under the chapter title and subtitle.

**When to use:** You want each chapter to open with a navigable, jargon-free preview a stranger can read without opening the chapter.

**Inputs:** one chapter markdown file at a time, from `chapters/`.

**Outputs:** the same file, with a `> **TL;DR:** … | Section | Preview |` block inserted after the `# Title` and any `*subtitle*` line. No other content changes.

**Rule:** all output must be standalone — readable by someone who has never opened the chapter. No jargon, no forward references, no terms that require the chapter to decode. Preview content sections (the teaching arc); standard end-apparatus (Exercises, AI+1 block, AI Wayback Machine, Tags) may be omitted from the table to keep it a crisp preview — but never invent or omit a *content* section.

## The prompt

```
You are processing a single textbook chapter written in markdown. Produce:
1. One overall TL;DR for the chapter (2–3 sentences maximum).
2. One preview one-liner for each `##` section.
All output must be standalone — readable by someone who has never opened the
chapter. No jargon, no forward references, no terms that require the chapter to decode.

STEP 1 — STRUCTURAL AUDIT. Before writing anything, parse the markdown and report:

STRUCTURAL AUDIT
----------------
Chapter title (# level): [title or MISSING]
## sections found: [list each, in order]
### subsections found: [nested under their ## parent]

WARNINGS:
- Any ## section missing a title: FLAG
- Content that looks like a section but is marked ### not ##: FLAG "possible heading level error"
- Any ### with no ## parent: FLAG "orphaned subsection"
- If no ## sections exist at all: FLAG "chapter has no ## sections — TL;DR by section not possible"

Do not proceed to Step 2 until the audit is complete.

STEP 2 — OVERALL TL;DR. 2–3 sentences max. Must answer: what is this chapter about,
and why does it matter to the reader? No term that requires the chapter to understand
(gloss anything technical in plain language). A stranger must find it useful, not confusing.

TL;DR
-----
[2–3 sentences]

STEP 3 — SECTION ONE-LINERS. For each ## section: one sentence only; stands alone (no
unclear pronouns, no ungloss­ed jargon, no "this section shows that…" meta-framing); a
preview (what the reader will learn / why it matters) before they read it. Note any
audit FLAG inline.

SECTION ONE-LINERS
------------------
## [Section Title]: [one sentence]
...

STEP 4 — INSERTION BLOCK. Produce final insertion-ready markdown to drop under the
chapter title + subtitle:

> **TL;DR:** [overall TL;DR here]
>
> | Section | Preview |
> |---|---|
> | [Section Title] | [one-liner] |
> ...

Flag any row whose section had a structural warning in Step 1.

INPUT: the full chapter markdown follows.
```

## Insertion

Place the Step-4 block immediately after the `# Chapter Title` line and the `*italic subtitle*` line (if present), separated by a blank line, before the first body paragraph. If the chapter already has a `> **TL;DR:**` block, replace it in place — never stack two.
