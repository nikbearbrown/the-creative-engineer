# conductor/

LLM instructions for building this book. Paste these into your CLI (Cowork,
Claude Code, or Codex). **Code lives in `scripts/`; prompts live here.**

Start at the top: read `../CONDUCTOR.md`, then work the spine phases in order.
Each phase ends with a gate you record in `../STATUS.md`.

## Spine (in order)

| # | Folder | Phase | Gate |
|---|---|---|---|
| 0 | `00-blueprint/` | Plan the book (Vision→Architecture→Spec→Risk) | TOC approved |
| 1 | `10-research/` | Gather + verify sources | Sources solid |
| 2 | `20-draft/` | Draft chapters from research | Full draft exists |
| 3 | `30-human-rewrite/` | Author makes it theirs | Author sign-off (human only) |
| 4 | `40-factcheck/` | Verify every claim | Claims verified |
| 5 | `50-images/` | Generate figures (SVG + D3 + PNG) | Figures exist |
| 6 | `60-check-images/` | Audit figures | Figure audit passes |

= **the spine**: a complete, fact-checked, illustrated book.

## Advisory tools (any time a draft exists)

`editorial-review/` — the Reader's Report: a developmental + line editor's
read of the whole manuscript, returned as `editorial-report.md`. Advisory
only — it never rewrites the book. Natural moments: before GATE 3 (it feeds
the Human Rewrite) and before calling the book done. Distinct from Fact
Check (claim accuracy) and voices (register rewrite).

## After the spine

`editions/` — optional add-ons the author chooses (quizzes, flashcards,
simulations, alternate voices). See `editions/README.md`.

## design/

Visual-language prompts (brutalist grid, palette, type) loaded during Phase 5.
*(Populate from the repo's `brutalist/` set: CLAUDE.md, DESIGN.md, VIZ.md, SaulBass.md.)*
