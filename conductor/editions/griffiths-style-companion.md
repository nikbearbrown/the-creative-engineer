# Griffiths-Style Companion Edition  →  built as the *sardonic* voice

> **Implemented as a voice.** Produced by the **sardonic** voice —
> see `../../voices/sardonic/VOICE.md`. Run after the spine is complete (GATE 6).

**Register:** Dry, slightly sardonic, treats the reader as a capable adult; jokes in footnotes; hard end-of-chapter problems.

**Inputs:** the finished spine chapters in `chapters/`.
**Outputs:** `voices/sardonic/<same-filename>.md` — one per chapter, `chapters/` untouched.
**Preserves:** title (as `# Chapter X — Title`), all markdown comments
(incl. `<!-- → [TABLE: ...] -->`), any LLM exercises, any images.

See `../../voices/sardonic/VOICE.md` for the full definition and the invoke block,
and `../../voices/README.md` for how voice rewrites work.
