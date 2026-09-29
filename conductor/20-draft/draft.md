# Phase 2 — DRAFT

**Write the chapters from the research.** Every chapter should trace back to the
notes gathered in Phase 1 and satisfy its spec from Phase 0.

## When to run
After GATE 1 is signed.

## Inputs
- `research/<slug>.md`, `chapters-spec.md`.

## Outputs
- `chapters/NN-*.md` for every chapter in the outline.

## Prompt to paste into your CLI

```
Draft each chapter listed in outline.md as chapters/NN-<slug>.md.

For each chapter:
- Use ONLY the facts in research/<slug>.md. If you need a fact that isn't there,
  stop and tell me — do not invent it.
- Hit the chapter's spec in chapters-spec.md: open with the stated strategy,
  cover the 4–6 content blocks, include the worked example, and end with the
  assessable exercises and a bridge to the next chapter.
- Write in clear prose. Mark every place that will need a figure as
  [FIGURE: short description] — figures come later in Phase 5.
- Keep citations inline or as footnotes so Phase 4 can verify them.

Draft all chapters before we move on. Don't polish voice yet — that's Phase 3.
```

## GATE 2 — Full draft exists
- [ ] Every outlined chapter has a draft.
- [ ] Each draft uses its research notes and meets its spec.
- [ ] Figure needs are marked `[FIGURE: ...]`; citations are present.

Record sign-off in `STATUS.md` (GATE 2), then move to `conductor/30-human-rewrite/`.
