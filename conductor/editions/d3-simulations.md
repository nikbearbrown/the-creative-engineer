# Browser-Based D3 Simulations

> **Edition stub.** Run only after the spine is complete (GATE 6 signed).
> Expand this into a full prompt when you decide to build it.

**What it is:** Interactive D3 v7 versions of the book's figures and data, runnable in a browser.

**When to use:** You want the static figures to become explorable, or want a living-figure web companion.

**Inputs:** the finished spine chapters in `chapters/` (and `research/` where relevant).

**Outputs:** `d3/<chapter-slug>-fig-NN.html` — standalone D3 v7 files (pairs with images/ PNGs).

## Starter prompt

```
For figures that carry data or change over a parameter, build standalone D3 v7 HTML versions in d3/. Match the static figure's content and the design system in conductor/design/. Add interactivity that teaches (hover detail, a parameter slider, animated transition). No external storage; embed data inline. Name to match the static figure.
```
