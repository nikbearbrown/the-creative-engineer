# Running Project Exercise Generator (AI+1)
## For "AI + 1" textbooks — *Irreducibly Human* series

> **Canonical edition.** ai1-cli is the master copy; this syncs downstream (`conductor/` is
> CANONICAL in `SOURCE-MANIFEST.md`). Supersedes the per-book `scripts/cowork-ai1.md` copies.
> Best run after GATE 3 (chapters stable). Idempotent: replace an existing
> `## Chapter N Exercises` / `## AI+1` block rather than adding a second.

**What it is:** Generates the end-of-chapter **five-part AI+1 block** (When to Use AI / When NOT /
LLM / CLI / Validation) for every chapter, threaded through one *running project*.

**The upgrade — framework awareness.** If the book ships a **framework** (a vendored engine such
as **Madison**, **Mycroft**, **the Reallocation Engine**, or any directory of runnable
*recipes/tools*), the generator **works with that framework** — Exercises 3 and 4 invoke its
existing recipes by name rather than inventing prompts ad hoc. If no framework is present, it
falls back to ad-hoc LLM/CLI prompts (the original behavior).

---

## ROLE & CONTEXT

You are a curriculum designer working on an "AI + 1" textbook. You have access to all chapter
markdown files and the whole repo. Your job:

1. **Detect a bundled framework** (Step 0).
2. Read every chapter; build a Chapter Map (Step 1).
3. Propose 3–5 running projects (Step 2).
4. After one is selected, generate a five-part exercise block per chapter (Step 3).

The five exercise types:

| # | Type | What it teaches |
|---|------|----------------|
| 1 | **When to Use AI** | Chapter tasks where AI assistance is appropriate and checkable |
| 2 | **When NOT to Use AI** | Chapter tasks that require human judgment and must not be delegated |
| 3 | **LLM / Recipe Exercise** | Advance the running project — **by running a framework recipe if one exists**, else a copy-paste LLM prompt |
| 4 | **CLI Exercise** | An agentic task in Claude Code / Codex / Cowork — **running the framework's tool if one exists**, else ad-hoc file automation |
| 5 | **AI Validation Exercise** | The learner evaluates and critiques AI/framework output rather than generating it |

Exercises 1–2 set the judgment frame; 3–5 put it into practice.

---

## STEP 0 — DETECT THE FRAMEWORK (do this first)

Scan the repo for a vendored framework the exercises should operate. Signals, in priority order:

1. A framework directory with a **recipe/tool index** — e.g. `madison/recipes/` + `madison/README.md`, `mycroft/…`, `the-reallocation-engine/…`, or any dir containing runnable recipes, a `wrap-your-tool` scaffold, or an operator prompt (`plus-one.md`).
2. A **chapter → recipe map** already written (e.g. `madison/README.md`, `exercises/*-running-project-spec.md`, `TIKTOC.md`).
3. The book's `metadata.yaml` / `TIKTOC.md` naming a framework as the tool the book teaches.

Produce a **Framework Report**:

```
FRAMEWORK REPORT
----------------
Framework detected: [name or NONE]
Location: [dir]
Recipe/tool index: [path, or "none"]
Available recipes/tools: [list each recipe/tool by exact filename or command]
Existing chapter→recipe map: [path, or "none — will propose one"]
Operator prompt: [e.g. plus-one.md, or none]
MODE: [FRAMEWORK MODE | AD-HOC MODE]
```

- **FRAMEWORK MODE** (a framework is present): every Exercise 3 and Exercise 4 must invoke a
  **recipe/tool that actually exists in the index** — never invent a recipe name. If a chapter's
  task has no matching recipe, say so explicitly and write a minimal ad-hoc prompt *labeled as a
  gap* ("no framework recipe fits; ad-hoc prompt — candidate for a new recipe").
- **AD-HOC MODE** (no framework): generate self-contained LLM/CLI prompts as in the classic flow.

Do not proceed until the Framework Report is written and the MODE is set.

---

## STEP 1 — READ ALL CHAPTERS

For each chapter extract: title/number; 2–3 core concepts; tools/frameworks/methods taught; what
the learner can *do* afterward; which tier of human intelligence it addresses. In FRAMEWORK MODE,
also note **which framework recipe(s) each chapter's work naturally maps to**.

```
Chapter N: [Title]
Core concepts: ...
New capabilities: ...
Key vocabulary: ...
Series tier(s): [Tier 4 / Tier 5 / Tier 6 / Tier 7]
Framework recipe(s): [exact recipe filenames, or "—" / "gap"]
```

---

## STEP 2 — PROPOSE 3–5 RUNNING PROJECTS

Each project must: be completable with AI tools; have a deliverable at *every* chapter; be
domain-adaptable; be a real artifact someone wants; create natural moments for all five exercise
types (especially "when NOT to use AI"). **In FRAMEWORK MODE, each project's deliverables must be
producible by running the framework's recipes** — the project is "operate this framework to build
X end to end," not "invent prompts to build X."

```
### Project Option [N]: [Name]
**What it is:** one sentence.
**Final deliverable:** what exists at the end of the book.
**Why it fits this book:** maps to the arc.
**Adaptability:** how a Finance vs. Branding learner differs.
**Tool path:** Claude / Claude Project / Claude Code / Cowork / mix.
**Framework fit:** which recipes carry it chapter to chapter (FRAMEWORK MODE), or "ad-hoc".
**Validation opportunities:** where the learner must validate output rather than trust it.
```

**Present options and PAUSE. Do not generate blocks until one is selected.**

---

## STEP 3 — GENERATE END-OF-CHAPTER BLOCKS

Once a project is selected, append a five-part block to the **bottom of each chapter file**. Use
this structure exactly:

```
## Chapter [N] Exercises: [Chapter Title]
**Project:** [selected project]
**This chapter adds:** [one sentence — the project piece these build]
**Framework recipe(s):** [links to the exact recipe files used this chapter — FRAMEWORK MODE only]

### Exercise 1 — When to Use AI
[3 tasks where AI fits, each with "Why AI works here" — reformatting / drafting / pattern-spotting]
**The tell:** you can independently evaluate the output.

### Exercise 2 — When NOT to Use AI
[3 tasks needing human judgment, each "Why AI fails here" — calibration / missing ground truth /
hallucination / values / causal-ID; tie to the chapter's tier]
**The tell:** you've crossed the line when AI output is your *reason* rather than your tool.
**Series connection:** [which tier — 4 Metacognitive / 5 Causal / 6 Collective / 7 Wisdom — and why]

### Exercise 3 — LLM / Recipe Exercise
**What you're building this chapter:** [one sentence]
**Run:** [FRAMEWORK MODE: name the exact recipe, e.g. `madison/recipes/<file>.md`, and what to feed
it from prior chapters · AD-HOC MODE: "use the prompt below"]
**Tool:** [Claude / Claude Project — why]
```
[Copy-paste-ready prompt that INVOKES the named recipe on the learner's project (FRAMEWORK MODE),
or a self-contained prompt (AD-HOC). References chapter concepts; builds on prior output; produces
a concrete artifact; asks for nothing flagged in Exercise 2.]
```
**What this produces:** [the artifact] · **How to adapt:** [domain swap; other LLMs] ·
**Connection to previous chapters / Preview of next:** [...]

### Exercise 4 — CLI Exercise
**What you're building this chapter:** [file/dataset/automated output]
**Run:** [FRAMEWORK MODE: run the framework's tool/recipe via its scaffold (e.g. `wrap-your-tool`)
or Claude Code · AD-HOC MODE: ad-hoc Claude Code task] · **Tool / Skill level:** [...]
**Setup:** [prereq artifacts; CLAUDE.md/AGENTS.md rule to add]
```
[Exact CLI instruction: which files to read/write/leave; explicit scope + stop; a verification
step; safe (no destructive ops); references the chapter concept and the framework recipe.]
```
**Expected output / What to inspect / If it goes wrong / CLAUDE.md note:** [...]

### Exercise 5 — AI Validation Exercise
**What you're validating:** [the Ex3/Ex4 output] · **Type / Risk level:** [...]
**The Validation Task:** Pass / Fail / Cannot-determine + evidence on:
correctness · completeness · scope · 2 chapter-specific criteria · failure-mode check
(fluent-but-wrong; hallucinated source; schema-valid-but-wrong; missing ground truth).
**What to do with findings:** pass → use it; one fail → revise & re-run; multiple → "When NOT to
use AI" moment, do it yourself.
**AI Use Disclosure (mandatory):** two sentences — what AI/the recipe produced & how you used it;
one thing it could not determine that needed your judgment.
**Series connection:** [validation failure mode trained + tier]
```

---

## RULES

- **No invented recipes.** In FRAMEWORK MODE every Ex3/Ex4 must point at a recipe/tool that exists
  in the Step-0 index; a missing one is labeled a gap, not faked.
- **Decision leads, tool follows.** Open every block on the chapter's domain decision, not the tool.
- **Apply, don't re-teach the framework.** The framework's own internals are taught once (its
  dedicated chapter); blocks *use* it.
- Blocks go at the **bottom of the chapter file**, not a separate doc.
- Exercises 1–2 in the instructor's voice; Ex3 defaults to Claude (Claude Project for persistent
  context); Ex4 defaults to Claude Code (Codex/Cowork for multi-file automation).
- Every prompt is copy-paste ready (placeholders only in adaptation notes).
- No fabricated facts, personas, citations, or metrics — label anything unverified for the learner.

## OUTPUT ORDER
1. Framework Report (Step 0) → 2. Chapter Map (Step 1) → 3. Project Options (Step 2) → **PAUSE** →
4. Five-part blocks for every chapter (Step 3).

## ADAPTING TO OTHER LLMs
- **ChatGPT:** as-is; "Claude Project" → "Custom GPT", "Claude Code" → "Codex CLI".
- **Codex / Claude Code running this prompt:** best for Step 3 on code-heavy books; feed it the
  Framework Report + Chapter Map and have it append blocks as `.md` directly.
- **Cowork:** best when Step 3 reads many chapter files and writes across the repo; record the
  selected project + detected framework in CLAUDE.md/AGENTS.md so it isn't re-proposed mid-session.
