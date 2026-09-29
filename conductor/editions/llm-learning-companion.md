# LLM Learning Companion

> **Edition stub.** Run only after the spine is complete (GATE 6 signed).
> Expand this into a full prompt when you decide to build it.

**What it is:** A guide and prompt set for using an LLM to learn the book's material — strategically, not as an answer machine.

**When to use:** You want readers to study WITH an LLM and learn to prompt it well.

**Inputs:** the finished spine chapters in `chapters/` (and `research/` where relevant).

**Outputs:** `editions/llm-companion.md` — per-chapter study prompts and strategy.

## Starter prompt

```
For each chapter, write study prompts a reader can paste into an LLM: explain-it-back checks, Socratic 'quiz me' prompts, 'find my misconception' prompts, and compare-two-approaches prompts. Teach WHEN each is useful and when an LLM will mislead them. Frame the LLM as a study partner to argue with, not an oracle.
```
