# Phase 5 — IMAGES

**Generate the book's figures.** Static SVG for the EPUB (converted to PNG) and
interactive D3 HTML for the web. Use the design system in `conductor/design/`.

## When to run
After GATE 4 is signed (illustrate verified text, not a moving target).

## Inputs
- Finished chapter text with `[FIGURE: ...]` markers.
- Design prompts in `conductor/design/` (CLAUDE.md, DESIGN.md, VIZ.md, SaulBass.md).

## Outputs
- `images/<chapter-slug>-fig-NN.svg` — static figures.
- `d3/<chapter-slug>-fig-NN.html` — interactive figures (where useful).
- `images/<chapter-slug>-fig-NN.png` — via `node scripts/svg-to-png.mjs`.

## Prompt to paste into your CLI

```
Load conductor/design/DESIGN.md and conductor/design/CLAUDE.md into context
first — they define the visual language (palette, type, brutalist grid, rx=0).

For each [FIGURE: ...] marker in the chapters, create:
1. a static SVG at images/<chapter-slug>-fig-NN.svg following the design system,
   with fonts embedded as base64 (no system-font dependency),
2. where the figure benefits from interactivity, a standalone D3 v7 HTML file at
   d3/<chapter-slug>-fig-NN.html.

Use the figure number from the marker order within the chapter, zero-padded.
After generating SVGs, tell me to run the PNG conversion.
```

Then convert:

```bash
node scripts/svg-to-png.mjs
```

## GATE 5 — Figures exist
- [ ] Every `[FIGURE: ...]` marker has a corresponding SVG (and D3 where interactive).
- [ ] PNGs generated for all SVGs and render correctly.

Record sign-off in `STATUS.md` (GATE 5), then move to `conductor/60-check-images/`.
