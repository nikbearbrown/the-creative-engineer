# Generic Edition (OpenStax register)  →  built as the *generic* voice

> **Implemented as a voice.** Produced by the **generic** voice —
> see `../../voices/generic/VOICE.md`. Run after the spine is complete (GATE 6).

**Register:** Warm, inclusive, carefully neutral. Definition → worked example → practice problem, repeat. Accessible but flat.

**Inputs:** the finished spine chapters in `chapters/`.
**Outputs:** `voices/generic/<same-filename>.md` — one per chapter, `chapters/` untouched.
**Preserves:** title (as `# Chapter X — Title`), all markdown comments
(incl. `<!-- → [TABLE: ...] -->`), any LLM exercises, any images.

See `../../voices/generic/VOICE.md` for the full definition and the invoke block,
and `../../voices/README.md` for how voice rewrites work.
