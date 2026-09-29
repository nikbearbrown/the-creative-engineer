# Pragmatist Voice

Here's the formula, here's when to use it, here are the practice problems. Zero
personality, by design. Doesn't attempt warmth, wonder, or story — it gets the
job done for a reader who needs to solve a problem now.

---

## Conversion contract

**Input:** one chapter file from `chapters/`.
**Output:** a rewrite saved to `voices/pragmatist/<same-filename>.md`. **Markdown only.**
The original in `chapters/` is never modified.

**Preserve exactly:** the title, formatted `# Chapter X — Title`; **all markdown
comments** including `<!-- → [TABLE: ...] -->`; **any LLM exercises** (verbatim);
**any images**.
**No fabrication:** verifiable facts, correct equations, real cases only; label
hypotheticals.
**Output:** markdown only, no preamble.

---

## Structure

For each result the chapter teaches:

1. **State the formula / result** up front. Name every variable in plain words.
2. **When to use it** — the conditions, the assumptions, the failure cases.
3. **One compact worked example** — minimal prose, just the steps.
4. **Practice problems** — about a dozen, graduated, no inline solutions.

Add short decision rules ("use this when…, not when…") where they help. No
opening hook, no narrative, no synthesis essay. Tables and formula blocks over
paragraphs wherever possible.

## Style

Terse and instrumental. No warmth, no jokes, no philosophy, no authorial
presence. Tight sentences, bullets, and equations. Optimize every line for a
reader who wants the answer and the method, fast. Clarity through structure, not
voice. The forbidden vague phrases are still forbidden — be precise, not chatty.

## Finishing pass (after writing)

Run `/done` if it hasn't already:
- **Subtitle:** add a plain, utilitarian italic line under the title if missing.
- **Visual suggestions:** seed `<!-- → [TYPE: ...] -->` comments for formula
  sheets, decision tables, and worked-example diagrams.
- **Exercises:** the voice supplies ~a dozen practice problems by design, so do
  not add a separate graduated set. Keep any existing LLM exercises.

## Invoke

```
Rewrite chapters/<file>.md in the Pragmatist voice per voices/pragmatist/VOICE.md.
Formula → when to use it → compact worked example → ~12 practice problems; zero
personality, tables over prose. Keep the title (as "# Chapter X — Title"), all
markdown comments, any LLM exercises, and any images. Save to
voices/pragmatist/<file>.md — never touch chapters/. Then run the finishing pass
(subtitle + visual comments; the voice supplies the practice problems, so don't
add a separate set). Output markdown only, no preamble.
```
