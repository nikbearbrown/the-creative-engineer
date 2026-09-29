# Phase 1 — RESEARCH

**Gather and verify the facts each chapter needs — before drafting.** Drafting
from research beats drafting from the model's memory: fewer hallucinations,
real citations, defensible claims.

## When to run
After GATE 0 is signed. Before any drafting.

## Inputs
- Preferred: `TIKTOC.md`.
- If no `TIKTOC.md` exists: the signed GATE 0 Blueprint/TOC. For the AI1 running project, use the copywriting book TOC signed in `books/writing-guide/pantry/ai1-ch1-blueprint-proposal.md` and reproduced in `chapters/01-inventory-research-blueprint-signoff.md`.
- Supporting planning files: `chapters-spec.md`, `outline.md`.

## Outputs
- `research/<chapter-slug>.md` per chapter: key facts, figures, quotes, and a
  source for each, with URLs/DOIs and access dates.

## Prompt to paste into your CLI

```
Read the chapter source first. Prefer TIKTOC.md. If TIKTOC.md is absent, use the signed GATE 0 Blueprint/TOC; do not silently substitute an unsigned outline.

For each chapter in the chapter source, create research/<chapter-slug>.md.

For that chapter's spec in chapters-spec.md, gather the facts, data, examples,
and quotes the chapter will need. For EACH claim you record:
- state the claim plainly,
- attach a real source (title, author, year, URL or DOI),
- note whether the source is primary or secondary,
- mark anything you could NOT verify as [UNVERIFIED] rather than guessing.

Do not write prose for the chapter yet — this phase produces notes and sources
only. Prefer primary sources. If a fact is "common knowledge," still anchor it.
At the end, list any claims that remain [UNVERIFIED] so I can decide whether to
cut them or dig deeper.
```

## GATE 1 — Sources solid
- [ ] Every chapter has a `research/<slug>.md`.
- [ ] Key claims carry a real source (no "as is well known").
- [ ] No citation is a dead link or a hallucinated reference.
- [ ] `[UNVERIFIED]` items are listed and triaged.

Record sign-off in `STATUS.md` (GATE 1), then move to `conductor/20-draft/`.
