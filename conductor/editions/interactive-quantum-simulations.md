# Interactive Quantum Simulations

> **Edition stub.** Run only after the spine is complete (GATE 6 signed).
> Expand this into a full prompt when you decide to build it.

**What it is:** Standalone interactive simulations of the book's core phenomena (domain-specific; named for this template's quantum lineage — rename for your subject).

**When to use:** Your subject has dynamics or systems a reader learns better by manipulating than reading.

**Inputs:** the finished spine chapters in `chapters/` (and `research/` where relevant).

**Outputs:** `editions/sims/<concept-slug>.html` — standalone, browser-runnable simulations.

## Starter prompt

```
For each simulatable concept in the book, build a standalone HTML simulation (no build step, no external storage). Expose the parameters that matter pedagogically as sliders/controls, show the system responding live, and add a one-paragraph 'what to notice.' Keep each file self-contained. Rename 'quantum' to your subject.
```
