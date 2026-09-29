# Phase 6 — CHECK IMAGES

**Audit the figures.** Catch bad subscripts/superscripts, broken math notation,
and text overflow before they reach a reader. This is the last spine gate.

## When to run
After GATE 5 is signed.

## Inputs
- The generated SVGs in `images/`.

## Outputs
- A clean (or accepted) run of `scripts/svg-visual-audit.mjs`.
- Fixes applied to SVGs; PNGs re-rendered.

## How to run

First, see what's flagged (no changes, no API key needed):

```bash
DRY_RUN=1 node scripts/svg-visual-audit.mjs
```

Then apply fixes. Two paths:
- **Full audit (with API key):** the AI fixer judges context (subscript vs code
  identifier, real multiplication vs `q*`, etc.) and edits in place:
  ```bash
  ANTHROPIC_API_KEY=sk-ant-... node scripts/svg-visual-audit.mjs
  ```
- **Safe auto-fixes only (no key):** convert unicode sub/superscripts to proper
  tspans and fix vertical overflow, leaving context-dependent cases for review.

Re-render any changed figures:

```bash
node scripts/svg-to-png.mjs
```

## Defect classes
`SUB` subscript · `SUP` superscript · `MATH` notation (Greek, →, ≠, ×) · `OVER` overflow.

> Heads-up: the static scan over-flags. `q*` (optimal quantity), code identifiers
> like `uint8_t`, and LaTeX `$x^2$` are NOT defects. Use judgment or the AI pass
> for those; don't blindly convert.

## GATE 6 — Figure audit passes
- [ ] `DRY_RUN=1 node scripts/svg-visual-audit.mjs` reports `0 flagged`, **or**
- [ ] every residual flag is a reviewed, accepted exception (list them here).
- [ ] PNGs re-rendered after fixes.

Record sign-off in `STATUS.md` (GATE 6). **The spine is now complete** — proceed
to `conductor/editions/` for optional editions.
