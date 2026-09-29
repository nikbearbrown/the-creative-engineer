# Editorial Review — the Reader's Report

Read a finished or near-finished book the way a good **developmental + line editor**
would, and return a **constructive reader's report**. This is **advisory only** —
it never rewrites the book; the author decides what to act on (that's the
Human-Rewrite phase). It is distinct from **Fact Check** (accuracy of claims) and
from **voices** (rewriting in a register). Run it any time a draft exists, and
especially before calling a book "done."

> **Where this sits in AI+1:** not a phase and not a gate — an advisory tool,
> runnable whenever `chapters/` has a draft. Its natural moments: before GATE 3
> (the report feeds the Human Rewrite) and before declaring the spine done.
> The report is an artifact: write `editorial-report.md` at the book root, stub
> its sidecar (`python scripts/verify.py stub editorial-report.md --phase review`),
> and stop — the author reads it; no agent acts on it without the author's
> direction.

## Stance (this is the whole game)

- **Editor, not critic.** Every problem you name comes with a concrete, minimal
  fix. *"Chapter 7 has no closing bridge — add one linking co-design to the
  prototyping chapter,"* not *"improve the flow."*
- **Lead with what works.** Name real strengths first; an editor earns trust by
  seeing the good, and the author needs to know what *not* to touch.
- **Judge the book against its own stated intent and audience** — not your taste.
  When a choice is right for one audience and wrong for another, say so (name the
  trade-off) rather than ruling.
- **Be specific and located.** Point to chapter, section, and line. **No
  fabrication** — never invent a flaw; quote or cite the real passage.

## The five levels of edit (cover all)

1. **Developmental / structural (book level).** Does it deliver its promise? Is
   the arc and chapter order doing real work? Does each chapter earn its place?
   Are prerequisites taught before they're used? Scope — gaps and redundancy.
   Chapter-length balance. Is there a throughline, and does the ending land it?
2. **Pedagogical (per chapter).** Motivation / cold open; are objectives clear
   (or deliberately implicit — note which)? Are concepts scaffolded? Worked
   examples? Do the exercises actually assess the objective? Closing / summary?
   *Can the reader DO something they couldn't before?*
3. **Consistency.** If any chapter has a feature (objectives, summary, bridge,
   evidence box, exercises), do all? Terminology, notation, naming, figure
   call-outs. **Do the planning docs and metadata match the actual book** (title,
   TOC, audience)?
4. **Line / clarity (sampled).** Voice consistency, undefined jargon, hedging,
   the forbidden-phrase discipline. Pull a handful of representative passages and
   show a tighter version.
5. **Reader experience.** Pacing and cognitive load; the exact spots where a
   reader would stall, skim, or bounce.

## Method

Read the intent docs (`book.md`, `vision.md`, `outline.md`, `chapters-spec.md` if
present) to learn the **promise**, then read **every chapter**, map structure
(headers, apparatus, objectives, exercises, figures), and judge **delivery vs.
promise**.

Also compute a basic organization audit from the manuscript itself:

- chapter word counts;
- section word counts for every `##` section;
- unusually thin chapters, unusually long chapters, and extreme imbalance;
- one- or two-paragraph sections that read like article fragments rather than
  textbook sections;
- places where a topic is scattered across multiple chapters and wants to be
  consolidated;
- places where a single manuscript is really several books, parts, or modules.

When the book is educational, judge whether the language and scaffolding match
the stated audience. If the stated or likely reader is undergraduate, flag
graduate/professional register, missing prerequisite explanation, undefined
jargon, compressed mechanisms, and article-like prose that needs to become
teaching prose.

Then write the report. Do not edit the chapters.

## Output → `editorial-report.md`

1. **Verdict** — one short paragraph: how close to done, the biggest strength, the
   biggest risk.
2. **Manuscript statistics** — chapter count, total word count, word-count range,
   median chapter length, shortest/longest chapters, number of very short
   sections, and any major imbalance pattern. Use approximate counts if exact
   tooling is unavailable, but say they are approximate.
3. **Organization diagnosis** — whether the manuscript is one coherent textbook,
   a textbook that needs parts, or several books tangled together. Name the
   organizing principle currently missing.
4. **Recommended structure** — propose a concrete reorganization. If the material
   naturally splits into multiple books/volumes, give each proposed book/part:
   title, scope, chapter range or chapter list, reader promise, and what material
   should move into it. Include a brief rationale for each split.
5. **Audience and language adaptation** — especially for undergraduate readers:
   what to simplify, what to scaffold, where to add definitions, worked examples,
   transitions, learning objectives, summaries, or exercises.
6. **Top priorities** — ranked 3–7 highest-leverage fixes; each: what, where, and a
   concrete fix.
7. **What's working** — specific strengths to preserve.
8. **Structural / developmental notes.**
9. **Per-chapter notes** — strengths + specific issues + suggested fix (skip a
   chapter if there's nothing useful to say).
10. **Consistency table** — which chapters have which apparatus → what to standardize.
11. **Line-level samples** — a few passages with before → after suggestions.
12. **Restructure implementation plan** — a practical 1-day / 3-day / 1-week plan
    for applying the reorganization, including what can be moved as-is, what must
    be expanded, and what needs human/domain-expert judgment.
13. **Open questions for the author.**

The report is the deliverable. The author (or a later Human-Rewrite pass) acts on
it; the editor never silently changes the book.

## Optional short email summary

If the user asks for a message to collaborators, also produce a concise email
summary after the report. It should name the main organizational violations,
the recommended split or restructure, the audience-language recommendation, and
the estimated implementation effort. Keep it direct and collegial.
