# Key Terms & Definitions

> **Edition stub.** Run only after the spine is complete (GATE 6 signed).
> Expand this into a full prompt when you decide to build it.

**What it is:** A per-chapter and consolidated glossary of the book's load-bearing terms.

**When to use:** You want a reference glossary and bolded first-use terms.

**Inputs:** the finished spine chapters in `chapters/` (and `research/` where relevant).

**Outputs:** `editions/glossary.md` (consolidated) and per-chapter term lists.

## Starter prompt

```
Extract every load-bearing term the book defines or relies on. For each: a one-to-two sentence definition in the book's own voice, the chapter where it's introduced, and a cross-reference to related terms. Produce both a per-chapter list and a single alphabetized glossary. Flag terms used before they're defined.
```
