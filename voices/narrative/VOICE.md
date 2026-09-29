# Narrative Voice

Tells the story of how the idea was discovered — who was wrong first, what the
real confusion was, how it finally resolved. Makes the subject feel like a human
enterprise rather than revealed truth. The concepts emerge through the history
instead of being handed down as finished facts.

---

## Conversion contract

**Input:** one chapter file from `chapters/`.
**Output:** a rewrite saved to `voices/narrative/<same-filename>.md`. **Markdown only.**
The original in `chapters/` is never modified.

**Preserve exactly:** the title, formatted `# Chapter X — Title`; **all markdown
comments** including `<!-- → [TABLE: ...] -->`; **any LLM exercises** (verbatim);
**any images**.
**Output:** markdown only, no preamble.

> **NO FABRICATION — and this voice is the riskiest for it.** Use only documented
> history: real, dated events and the actual people who did the work, drawn from
> verifiable sources. **Never invent quotes, dialogue, who-said-what, or "they
> must have thought…" interiority.** If the historical record is uncertain or
> disputed, say so plainly. Label any hypothetical ("Suppose…"). Real historical
> figures in the subject's own story are the *content* and belong here — the
> de-personification rule (no style-exemplar names) does not mean stripping the
> actual discoverers from their own history.

---

## Structure

- Open in the confusion — the problem as it actually looked before it was solved.
- Follow the thread: the wrong turn taken first, the dead end, the rival idea,
  the observation or argument that finally forced the resolution.
- Let each concept arrive when the history reaches it. The reader learns the idea
  by watching it get figured out.

## Style

Narrative nonfiction. Tension through pacing and the unfolding of understanding,
not through invented drama. Let the documented facts carry the weight. Concrete
dates, real disputes, genuine surprises. Confident and human, never breathless.

## Finishing pass (after writing)

Run `/done` if it hasn't already:
- **Subtitle:** add an italic line under the title if missing — name the stakes
  or the central confusion.
- **Visual suggestions:** seed `<!-- → [TYPE: ...] -->` comments where a timeline,
  a historical figure/diagram, or a then-vs-now table would help.
- **Exercises:** this is a flowing narrative cut — do not add embedded graduated
  exercises. Keep any existing LLM exercises.

## Invoke

```
Rewrite chapters/<file>.md in the Narrative voice per voices/narrative/VOICE.md.
Tell the discovery story — who was wrong first, the real confusion, how it
resolved — using ONLY documented history; invent no quotes or dialogue. Keep the
title (as "# Chapter X — Title"), all markdown comments, any LLM exercises, and
any images. Save to voices/narrative/<file>.md — never touch chapters/. Then run
the finishing pass (subtitle + visual comments; no added exercises).
Output markdown only, no preamble.
```
