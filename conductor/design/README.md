# conductor/design/

The visual language for this book's figures. Load these into your CLI context
**before** generating any figure (Phase 5 — Images). They define the rules every
SVG and D3 figure must follow so the whole book looks like one book.

| File | What it governs |
|------|-----------------|
| `DESIGN.md` | Visual constitution — palette, type, layout, the no-gradients/no-shadows/rx=0 rules |
| `CLAUDE.md` | D3 v7 coding constitution — how interactive figures are built |
| `VIZ.md` | Data-visualization constitution — chart types, encodings, what makes a figure honest |
| `SaulBass.md` | Cover / poster-grade composition reference |

## How Phase 5 uses these

When generating figures, the agent loads `DESIGN.md` and `CLAUDE.md` first, then
follows them for every SVG (static, for the EPUB) and every D3 HTML file
(interactive). After generating SVGs, render to PNG with
`node ../../scripts/svg-to-png.mjs`, then audit with
`node ../../scripts/svg-visual-audit.mjs`.

> Source: copied from the repo-root `brutalist/` set. `brutalist/PROJECT.md` and
> `brutalist/SLIDES.md` (slide-deck generator) also exist there if you need them.
