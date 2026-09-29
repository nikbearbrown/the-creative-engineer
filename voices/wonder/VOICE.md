# Wonder Voice

The Wonder voice rewrites a chapter as a single, flowing explanation in the
register of the great physics lectures — wonder first, first principles,
playful clarity, intellectual honesty. This is the **purer cut**: one hook, no
embedded exercises, ~3,000 words. Less workshop-chapter, more a lecture you
can't stop reading.

---

## Conversion contract

**Input:** one chapter file from `chapters/`.
**Output:** a rewrite saved to `voices/wonder/<same-filename>.md`. **Markdown only.**
The original in `chapters/` is never modified.

### Preserve exactly
- **The title.** Keep the title text as-is, formatted `# Chapter X — Title`
  (fold the chapter number into the title line; don't invent or change the words).
- **All markdown comments**, including visual-suggestion comments such as
  `<!-- → [TABLE: ...] -->`, `<!-- → [FIGURE: ...] -->`, `<!-- → [CHART: ...] -->`.
  They are invisible when rendered — carry them through verbatim.
- **Any LLM exercises** (e.g. a `## LLM Exercises` / prompt-practice section) —
  keep verbatim. Do not rewrite, expand, or remove them.
- **Any images** — image embeds (`![...](...)`), figure markers, and their
  captions stay.

### Change
- **Register** → Wonder (see below).
- **Structure** → a single hook then continuous explanation. Strip the workshop
  scaffolding: no learning-objective block, no prerequisites block, no graduated
  exercise set, no per-section cold opens.
- **Length** → ~3,000 words (not 5,000–8,000).

### Do not
- **Do not add embedded/graduated exercises.** The Wonder cut has none. (Existing
  LLM exercises stay; new pedagogical exercises are not introduced.)
- **No fabrication.** Do not invent people, quotes, conversations, data, or
  scenarios. Use only verifiable facts and the source text. Label any
  hypothetical plainly ("Suppose…", "Imagine if…").
- **No output but markdown.** No preamble, no notes on what changed.

---

## Structure — the purer cut

- **One hook.** Open in a single puzzle, scene, or question the reader can grasp
  with what they already know but cannot yet solve. Do not re-hook every section.
- **Unfold from first principles** in continuous prose. Let it breathe like a
  lecture, one animating thread rather than a checklist of concepts.
- **~3,000 words.** If a second or third idea is needed, weave it into the thread,
  don't bolt on a new section with its own opening.
- **Let significance arrive.** Reach understanding and let the weight land —
  don't announce it. End on the idea, not on "in this chapter we covered…".

---

## Style (descriptions, not names)

**Intellectual honesty.** Explain only what is actually understood. If something
is genuinely puzzling, say so plainly: "I don't fully understand why this works —
but here is what we can see." Admitting a limit is part of the voice.

**Know the thing, not its name.** Naming a concept is not explaining it. Show how
it works and why it is built that way. Strip every technical term down to plain
words the first time it appears.

**Wonder and curiosity.** Follow the genuinely interesting question. "What if we
changed this?" Use scale-shifts and analogy where they truly illuminate, not for
decoration. It is allowed to be delighted by the idea.

**Direct address.** A "you" that invites thinking ("you might wonder why…"); a
"we" in the act of figuring it out ("we need to see what happens if…"). Preserve
the author's first-person voice wherever the source uses it.

**Rhythm.** Short sentences create clarity. Longer sentences build understanding
by showing how things connect. Alternate them on purpose.

**Forbidden phrases.** Never: "One could argue…" (make the argument); "It seems
as though…" (say what's actually happening); "obviously" / "clearly" (if it were,
you wouldn't need to say it); "innovative" / "revolutionary" without saying what
actually changed; specs or numbers with no meaning attached.
Instead: "Here's what's actually happening…"; "The interesting part is…"; "Here's
where I had to stop and think the first time."

---

## Finishing pass (after writing)

When the rewrite is done, check whether a finishing pass has already run — is
there an italic subtitle directly under the title, and are there
`<!-- → [TYPE: ...] -->` visual comments? If **not**, run it:

1. **Subtitle (if missing).** Add a single italic line under `# Chapter X — Title`
   — a hook that compresses the chapter's animating tension, not a description.
2. **Visual suggestions.** Seed inline HTML comments where a visual would
   genuinely aid comprehension:
   `<!-- → [IMAGE|TABLE|INFOGRAPHIC|CHART: specific content + why it belongs here] -->`
   Name specific content, not the generic type. Invisible when rendered.
3. **Exercises — skip.** The Wonder cut omits embedded exercises, so the
   finishing pass does **not** add them here. Keep any existing LLM exercises.

The finishing pass adds only what's missing. It does not rewrite prose.

---

## Invoke

Paste this, naming the chapter:

```
Rewrite chapters/<file>.md in the Wonder voice per voices/wonder/VOICE.md.
Single hook, ~3,000 words, lecture register, no added exercises. Keep the title
(format as "# Chapter X — Title"), all markdown comments, any LLM exercises, and
any images. Save to voices/wonder/<file>.md — never touch chapters/. Then run the
finishing pass (subtitle + visual comments only; do NOT add exercises).
Output markdown only, no preamble.
```
