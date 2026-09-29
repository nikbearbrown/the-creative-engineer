# Socratic Voice

Tells you almost nothing directly. Asks questions, surfaces confusion, and makes
the reader do the reasoning. The chapter advances by inquiry: a question exposes
a gap, the reader predicts, the prediction is tested, the idea is built by the
reader rather than handed over. Excellent for conceptual understanding —
maddening as a reference.

---

## Conversion contract

**Input:** one chapter file from `chapters/`.
**Output:** a rewrite saved to `voices/socratic/<same-filename>.md`. **Markdown only.**
The original in `chapters/` is never modified.

**Preserve exactly:** the title, formatted `# Chapter X — Title`; **all markdown
comments** including `<!-- → [TABLE: ...] -->`; **any LLM exercises** (verbatim);
**any images**.
**No fabrication:** verifiable facts and source text only; label hypotheticals.
**Output:** markdown only, no preamble.

---

## Structure

- **Open with a question** that exposes the gap in what the reader currently knows.
- **Escalate by questioning.** Each step is a question or a "before you read on,
  predict…" — advance the reader's reasoning, don't lecture.
- **Surface the common wrong answer.** Name the intuition most readers reach for,
  then ask the question that makes them feel why it fails.
- **Converge.** Do not withhold forever — by the end the reader has constructed
  the idea and can state it. Arrive at the same understanding the source teaches.

## Style

Interrogative and restrained. Minimal direct assertion; the work happens in the
reader's head. "What do you think happens if…", "Why might that be wrong?",
"Check your answer against this." Patient, never smug. Resist the urge to answer
your own question too early. The reader should finish having done the thinking.

## Finishing pass (after writing)

Run `/done` if it hasn't already:
- **Subtitle:** add an italic line under the title if missing — a question or
  tension, fitting the voice.
- **Visual suggestions:** seed `<!-- → [TYPE: ...] -->` comments where a figure
  would let the reader test a prediction.
- **Exercises:** the voice's question sequences already are the active-learning
  layer, so do not add a separate graduated exercise set. Keep existing LLM exercises.

## Invoke

```
Rewrite chapters/<file>.md in the Socratic voice per voices/socratic/VOICE.md.
Lead by questions, surface the common misconception, make the reader reason and
converge to the idea. Keep the title (as "# Chapter X — Title"), all markdown
comments, any LLM exercises, and any images. Save to voices/socratic/<file>.md —
never touch chapters/. Then run the finishing pass (subtitle + visual comments;
the question sequences are the exercises, so don't add a separate set).
Output markdown only, no preamble.
```
