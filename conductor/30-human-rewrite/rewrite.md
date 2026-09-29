# Phase 3 — HUMAN REWRITE

**Make it yours.** This is the phase that cannot be automated. The agent
assists — suggests, tightens, flags — but the human decides what the book
sounds like and what it claims. This is what turns a cloned starter into *your*
book.

## When to run
After GATE 2 is signed.

## Inputs
- The full draft in `chapters/`.

## Outputs
- Revised `chapters/NN-*.md` carrying the author's voice and judgment.

## How to work (human + agent)
Read every chapter yourself. Rewrite anything that doesn't sound like you. Use
the agent as an editor, not an author:

```
Act as my editor, not my author. For the chapter I paste (or open), do NOT
rewrite it wholesale. Instead:
- point out passages that sound generic, hedged, or AI-flavored,
- flag claims that feel too strong or too weak for my argument,
- suggest tighter phrasings I can accept or reject,
- ask me questions where my intent or opinion should show but doesn't.

I will make the final edits. Keep my voice; surface choices, don't make them.
```

## GATE 3 — Author sign-off  (HUMAN ONLY)
- [ ] The human has read every chapter.
- [ ] The human has rewritten what didn't sound like them.
- [ ] The book now carries the author's voice and judgment.

**No agent may sign this gate.** A human initials `STATUS.md` (GATE 3), then the
build moves to `conductor/40-factcheck/`.
