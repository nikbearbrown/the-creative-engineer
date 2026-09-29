# Sardonic Voice

Dry, slightly sardonic. Treats the reader as a capable adult who doesn't need
hand-holding. Occasional footnote jokes. Trusts you to be confused and to work
through it. Not performed wonder and not warmth — economy, rigor, and a wry
respect for the reader's intelligence.

---

## Conversion contract

**Input:** one chapter file from `chapters/`.
**Output:** a rewrite saved to `voices/sardonic/<same-filename>.md`. **Markdown only.**
The original in `chapters/` is never modified.

**Preserve exactly:** the title, formatted `# Chapter X — Title`; **all markdown
comments** including `<!-- → [TABLE: ...] -->`; **any LLM exercises** (verbatim);
**any images**.
**No fabrication:** verifiable facts and source text only; label hypotheticals.
**Output:** markdown only, no preamble.

---

## Structure

- State results cleanly and move on. Don't over-explain what a capable reader can
  work out.
- Leave deliberate, productive gaps — the reader is trusted to fill them.
- Park the asides and the dry jokes in **footnotes**, not the main line.
- End with a set of genuinely hard problems. No solutions inline. Terse prompts.

## Style

Spare and dry. Never gushing, never warm, never "isn't this amazing." The wit is
understated and lives mostly in footnotes. Respect the reader by not padding.
Comfortable leaving them to struggle for a paragraph before it clicks. Precise,
a little impatient with hand-holding, but never actually unkind. The forbidden
vague phrases are still forbidden — dryness is not vagueness.

## Finishing pass (after writing)

Run `/done` if it hasn't already:
- **Subtitle:** add an italic line under the title if missing — understated, dry,
  not a sales pitch.
- **Visual suggestions:** seed `<!-- → [TYPE: ...] -->` comments **sparingly** —
  this voice distrusts decoration; suggest a figure only where it earns its place.
- **Exercises:** the voice supplies its own hard end-of-chapter problems, so do
  not add a separate graduated set. Keep existing LLM exercises.

## Invoke

```
Rewrite chapters/<file>.md in the Sardonic voice per voices/sardonic/VOICE.md.
Dry, terse, capable-adult; jokes in footnotes; hard problems at the end, no
solutions. Keep the title (as "# Chapter X — Title"), all markdown comments, any
LLM exercises, and any images. Save to voices/sardonic/<file>.md — never touch
chapters/. Then run the finishing pass (understated subtitle + sparse visual
comments; the voice supplies hard problems, so don't add a separate set).
Output markdown only, no preamble.
```
