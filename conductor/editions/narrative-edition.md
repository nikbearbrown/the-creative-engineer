# Narrative Edition  →  built as the *narrative* voice

> **Implemented as a voice.** Produced by the **narrative** voice —
> see `../../voices/narrative/VOICE.md`. Run after the spine is complete (GATE 6).

**Register:** The discovery story — who was wrong first, the real confusion, how it resolved. Documented history only; no invented quotes.

**Inputs:** the finished spine chapters in `chapters/`.
**Outputs:** `voices/narrative/<same-filename>.md` — one per chapter, `chapters/` untouched.
**Preserves:** title (as `# Chapter X — Title`), all markdown comments
(incl. `<!-- → [TABLE: ...] -->`), any LLM exercises, any images.

See `../../voices/narrative/VOICE.md` for the full definition and the invoke block,
and `../../voices/README.md` for how voice rewrites work.
