# Worked Exercises & Solutions

> **Covered by `build-exercises.py`.** The Practice Exercises tool produces an
> annotated worked example per concept plus complete annotated solutions for all
> Tier 1–4 problems, inline in each `editions/exercises/exercises-<stem>.md`.
> See `practice-exercises.md`. The stub below is the standalone fallback.

---


> **Edition stub.** Run only after the spine is complete (GATE 6 signed).
> Expand this into a full prompt when you decide to build it.

**What it is:** Fully worked solutions that model the reasoning, not just the answer.

**When to use:** You want readers to see expert problem-solving step by step.

**Inputs:** the finished spine chapters in `chapters/` (and `research/` where relevant).

**Outputs:** `editions/worked/<chapter-slug>.md` with worked solutions.

## Starter prompt

```
Take the practice exercises (or write new representative problems) and produce fully worked solutions. Show the reasoning at each step, name the principle being applied, and call out the common mistake at the point a reader would make it. End each with a one-line 'what this problem taught.'
```
