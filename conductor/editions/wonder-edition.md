# Wonder Edition  →  built as a *voice*

> **This edition is implemented.** The Wonder edition is produced by the
> **Wonder voice** — see `../../voices/wonder/VOICE.md`. Run it after the spine
> is complete (GATE 6 signed).

**What it is:** The purer lecture-register cut — a single hook, ~3,000 words, no
embedded exercises, wonder + first principles. Reads like a lecture you can't put
down rather than a workshop chapter.

**Inputs:** the finished spine chapters in `chapters/`.

**Outputs:** `voices/wonder/<same-filename>.md` — one per chapter, originals in
`chapters/` untouched.

**Preserves:** the title (as `# Chapter X — Title`), all markdown comments
(including `<!-- → [TABLE: ...] -->` visual suggestions), any LLM exercises, and
any images.

## Run it

```
Rewrite chapters/<file>.md in the Wonder voice per voices/wonder/VOICE.md.
Single hook, ~3,000 words, lecture register, no added exercises. Keep the title
(format as "# Chapter X — Title"), all markdown comments, any LLM exercises, and
any images. Save to voices/wonder/<file>.md — never touch chapters/. Then run the
finishing pass (subtitle + visual comments only; do NOT add exercises).
Output markdown only, no preamble.
```

See `voices/README.md` for how voice rewrites work and `voices/wonder/VOICE.md`
for the full voice definition.
