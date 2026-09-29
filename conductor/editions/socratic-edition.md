# Socratic Discussion Edition  →  built as the *socratic* voice

> **Implemented as a voice.** Produced by the **socratic** voice —
> see `../../voices/socratic/VOICE.md`. Run after the spine is complete (GATE 6).

**Register:** Tells you nothing directly — questions, surfaced confusion, the reader does the reasoning and converges to the idea.

**Inputs:** the finished spine chapters in `chapters/`.
**Outputs:** `voices/socratic/<same-filename>.md` — one per chapter, `chapters/` untouched.
**Preserves:** title (as `# Chapter X — Title`), all markdown comments
(incl. `<!-- → [TABLE: ...] -->`), any LLM exercises, any images.

See `../../voices/socratic/VOICE.md` for the full definition and the invoke block,
and `../../voices/README.md` for how voice rewrites work.
