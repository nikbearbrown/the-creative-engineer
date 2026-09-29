# Phase 0 — BLUEPRINT

**Plan the book before writing it.** BLUEPRINT (formerly Tic TOC) is a
four-part planning method: **Vision → Architecture → Chapter Spec → Risk.**
You fill four planning files; the outline falls out of them.

This file is the quick phase recipe. The full Blueprint consultant — the
complete command library (`/i1`–`/g5`, `/scaffold`, refinement tools, phase
gates, pushback layer) — is in [`blueprint-library.md`](blueprint-library.md).
Load the library for the full interactive consultant; use the prompt below
for the fast path.

## When to run
First. Before any research or drafting.

## Inputs
- `book.md` — your one-sentence pitch, argument, gap, reader, high-level outline.
- Your own intent and expertise.

## Outputs
- `vision.md` — positioning, learner profile, central argument, field comparison.
- `architecture.md` — learning outcomes, sequencing model, three-act arc, **assessment plan** (which assessments are desired/needed: quizzes, exercises, flashcards/Anki, exam bank, Canvas modules — decided here, generated later as editions).
- `chapters-spec.md` — per-chapter spec (capability, outcomes, blocks, exercises).
- `risks.md` — comparable texts, market, scope, adoption risks.
- `outline.md` — the chapter-level TOC, kept in sync with the above.

## Prompt to paste into your CLI

```
Read book.md, then act as a textbook architect running the BLUEPRINT method.

Work through the four phases in order, writing each file as you go. After each
file, STOP and ask me to confirm before continuing:

1. VISION (vision.md): Who is the one specific reader? What capability will they
   have at the end that they lack now? Name 3 comparable texts and how this book
   differs. State the central argument in one sentence.

2. ARCHITECTURE (architecture.md): For each chapter, write measurable learning
   outcomes at a Bloom's level. Choose and justify a sequencing model. Map the
   three-act arc (establish / build / apply). State the ASSESSMENT PLAN: which
   assessments this book's deployment needs — chapter quizzes, practice
   exercises, worked solutions, flashcards/Anki, exam bank, Canvas modules —
   each marked desired / needed / out of scope, and which chapters they apply to.

3. CHAPTER SPEC (chapters-spec.md): For each chapter — the capability it builds
   (not topics covered), its outcomes, 4–6 content blocks, one worked example,
   and at least 3 assessable exercises (one at Apply level or above).

4. RISK (risks.md): Comparable-text analysis, market size, feature priorities,
   out-of-scope list, top 3 adoption risks with mitigations.

Then write outline.md so it reflects the thesis. Flag anything that still needs
my input as [NEEDS HUMAN INPUT] — do not invent answers about my intent.
```

## GATE 0 — TOC approved
Do not proceed to Phase 1 until:
- [ ] Every `[NEEDS HUMAN INPUT]` is resolved.
- [ ] `outline.md` reflects the central argument (chapters are in an order that does real work).
- [ ] The assessment plan is stated (which assessments are desired/needed, or explicitly none).
- [ ] A human has read all four files and agrees this is the right book.

Record the sign-off in `STATUS.md` (GATE 0), then move to `conductor/10-research/`.
