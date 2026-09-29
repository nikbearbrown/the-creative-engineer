# Generic Voice

Warm, inclusive, carefully neutral. Definition, worked example, practice
problem — repeat. Accessible but flat: designed to offend nobody and exclude
nobody. The pedagogical equivalent of a hotel lobby. When you want a chapter
that any reader can walk into and follow without friction, this is the cut.

---

## Conversion contract

**Input:** one chapter file from `chapters/`.
**Output:** a rewrite saved to `voices/generic/<same-filename>.md`. **Markdown only.**
The original in `chapters/` is never modified.

**Preserve exactly:** the title, formatted `# Chapter X — Title` (keep the words,
fold in the number); **all markdown comments** including `<!-- → [TABLE: ...] -->`;
**any LLM exercises** (verbatim); **any images**.
**No fabrication:** verifiable facts and source text only; label hypotheticals.
**Output:** markdown only, no preamble.

---

## Structure

Modular and predictable. For each concept, in this order, then repeat:

1. **Define it** plainly. Every term is introduced before it's used.
2. **Show a worked example**, every step visible, nothing skipped.
3. **Give a practice problem** the reader can try immediately.

Use clear section headings. Keep concepts in small, digestible units. Examples
are drawn from varied, everyday contexts so no reader feels left out.

## Style

Warm but neutral — friendly without a strong personality. Plain, accessible
language; short paragraphs; consistent rhythm. No edge, no jokes, no provocation,
no authorial swagger. The reader should never feel lost and never feel pushed.
Accessible is the priority even when it costs color. Avoid the forbidden vague
phrases ("obviously", "it seems as though"); say things plainly instead.

## Finishing pass (after writing)

Run the `/done` finishing pass if it hasn't already (no subtitle line under the
title; no `<!-- → [TYPE: ...] -->` comments):
- **Subtitle:** add a plain, welcoming italic line under the title if missing.
- **Visual suggestions:** seed `<!-- → [IMAGE|TABLE|INFOGRAPHIC|CHART: specific content + why here] -->` inline.
- **Exercises:** this voice already includes practice problems by design, so do
  not add a separate graduated set. Keep any existing LLM exercises.
The finishing pass adds only what's missing; it does not rewrite prose.

## Invoke

```
Rewrite chapters/<file>.md in the Generic voice per voices/generic/VOICE.md.
Definition → worked example → practice problem, repeated; warm, neutral,
accessible. Keep the title (as "# Chapter X — Title"), all markdown comments,
any LLM exercises, and any images. Save to voices/generic/<file>.md — never touch
chapters/. Then run the finishing pass (subtitle + visual comments; the voice
already carries practice problems, so don't add a separate exercise set).
Output markdown only, no preamble.
```
