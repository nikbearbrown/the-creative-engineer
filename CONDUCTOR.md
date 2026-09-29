# CONDUCTOR.md

**The orchestration spine for this book** — the procedure for taking this
repository from an empty starter to a finished, checked book. The source of
truth for the AI+1 system is `AI1.md`, which authorizes this spine; if this
file and `AI1.md` ever disagree, `AI1.md` governs and the conflict is a bug.

> **You are the conductor's agent.** Work **one phase at a time**, in order.
> Do **not** start a phase until the previous phase's **gate** is signed off in
> `STATUS.md`. If a gate is not signed, stop and tell the human what's missing.
>
> **Generation is the fallback, not the default.** Before producing any
> artifact, run `python scripts/verify.py check <artifact>`. If it's verified,
> use the existing file — don't regenerate. If not, generate it, write a stub
> with `verify.py stub`, and stop for human sign-off. See `conductor/VERIFICATION.md`.

---

## How this book gets made

This book is built by a human and a CLI agent (Cowork, Claude Code, or Codex)
working together through seven phases. Each phase has:

- a **prompt** in `conductor/<phase>/` you paste into your CLI,
- defined **inputs** and **outputs**,
- a **gate** — a check that must pass before the next phase begins.

The seven phases produce **the spine**: a complete, fact-checked, illustrated
book. After the spine, the human chooses **optional editions** (quizzes,
flashcards, alternate voices, simulations) from `conductor/editions/`.

```
0  BLUEPRINT        plan the book           → GATE 0  TOC approved
1  RESEARCH       gather + verify sources → GATE 1  sources solid
2  DRAFT          write chapters          → GATE 2  full draft exists
3  HUMAN REWRITE  make it yours           → GATE 3  author sign-off
4  FACT CHECK     verify every claim      → GATE 4  claims verified
5  IMAGES         generate figures        → GATE 5  figures exist
6  CHECK IMAGES   audit figures           → GATE 6  figure audit passes
   ─────────────────────────────────────────────────────────────
   = THE SPINE
   then → conductor/editions/  (optional, reader's choice)
```

**The rule that matters:** never skip a gate. A drafted-but-unresearched
chapter, or an image that was never audited, is worse than no chapter at all.
Gates are how a starter becomes *your* book instead of a pile of AI output.

---

## Verified Artifact System

Every artifact produced by this pipeline — scripts, data files, chapter drafts,
fact-check reports, figures, final output — has a corresponding sidecar metadata
file that records whether a human has reviewed and signed off on it. Any script,
prompt, or tool in this pipeline that produces or consumes artifacts MUST check
for and respect this metadata before generating new output.

### Sidecar File Format

For every artifact `foo.md` (or `foo.py`, `foo.csv`, `foo.json`, etc.), a sidecar
file `foo.md.verified.json` lives in the same directory (append `.verified.json`
to the full filename — collision-safe, so `foo.md` and `foo.py` get distinct
sidecars):

```json
{
  "artifact": "foo.md",
  "phase": "rough_draft",
  "verified": false,
  "verified_by": null,
  "verified_at": null,
  "note": null,
  "sha256": null
}
```

When a human signs off, they set `verified: true`, add their initials to
`verified_by`, add the date to `verified_at`, and optionally add a note.
The sha256 field is optional — if populated, it holds a hash of the artifact
at the time of sign-off so drift can be detected.

### Routing Logic

Before generating any artifact, check for its sidecar:

1. Sidecar exists AND `verified: true` → load and use the existing artifact.
   Do not regenerate. Report: "Using verified [artifact]."
2. Sidecar exists AND `verified: false` → stop. Report: "[artifact] exists but
   is not yet verified. Awaiting human sign-off before proceeding."
3. No sidecar exists → generate the artifact, write a stub sidecar with
   `verified: false`, and stop. Report: "[artifact] generated.
   Sidecar written. Awaiting human sign-off before proceeding to next phase."

Never proceed past an unverified gate. Never silently regenerate a verified artifact.

### facts.json — The Fact Dictionary

`facts/facts.json` (in-repo, so the book stays self-contained) is a special
verified artifact that accumulates across all phases. Its sidecar is
`facts/facts.json.verified.json`. The `facts/` directory also holds the extractor
(`extract-facts.py`), the source-tier registry (`facts-sources.yaml`), and the
process docs (`README.md`, `EXTRACTING-FROM-OPENSTAX.md`, `FACTCHECKER-INTEGRATION.md`).
Any fact-checking script, prompt, or tool
in this pipeline that finds, verifies, or disputes a fact MUST:

1. Check facts.json before looking up a fact externally — if it exists and
   `verified: true`, use it directly.
2. Add any newly found fact to facts.json using the three-layer schema below.
3. Set `verified: false` on any new entry — facts require human sign-off
   before they are treated as authoritative.
4. Never overwrite a `verified: true` entry. Append a new evidence record
   to its `evidence` array instead.

#### facts.json Entry Schema

```json
{
  "fact_id": "domain-short-slug",
  "canonical": "One atomic, decontextualized, declarative statement. Present tense.",
  "domain": ["physics"],
  "stable": true,
  "verified": false,
  "verified_by": null,
  "verified_at": null,
  "human_note": null,
  "consensus": "unverified",
  "evidence": [
    {
      "source": "wikipedia",
      "url": "https://...",
      "verbatim": "Exact sentence from the source.",
      "retrieved": "YYYY-MM-DD",
      "verdict": "SUPPORTS"
    }
  ],
  "books": ["this-book-slug"],
  "category": "BASIC",
  "expires": null
}
```

Consensus values: "agreement" (all sources align) | "partial" (same substance,
different precision) | "conflict" (sources contradict — hard block, human must
resolve) | "unverified" (single source only).

Stable: true for physical constants, historical dates, definitions.
false for guidelines, approval status, statistics, rapidly evolving claims.

Expires: ISO date string for facts that have known expiry (e.g. guideline
version dates, FDA approval windows). null if no known expiry.

### Phase Gate Checklist Integration

STATUS.md tracks sign-offs. For every phase gate, the human must verify:
- [ ] Phase output artifact(s) have `verified: true` in their sidecar
- [ ] Any facts found during this phase have been reviewed in facts.json
- [ ] facts.json itself has `facts.json.verified.json` with `verified: true`
      before the next phase begins

---

## The phases

### Phase 0 — BLUEPRINT  ·  `conductor/00-blueprint/blueprint.md`
**Goal:** decide what the book *is* before writing a word.
**Inputs:** `book.md` (your pitch), your own intent.
**Outputs:** `vision.md`, `architecture.md`, `chapters-spec.md`, `risks.md`, `outline.md`.
**GATE 0 — TOC approved:** every `[NEEDS HUMAN INPUT]` is filled; the outline
reflects the thesis; a human has read it and agrees this is the right book.

### Phase 1 — RESEARCH  ·  `conductor/10-research/research.md`
**Goal:** gather and verify the facts each chapter needs *before* drafting.
**Inputs:** `chapters-spec.md`, `outline.md`.
**Outputs:** `research/<chapter-slug>.md` notes with sources and citations.
**GATE 1 — sources solid:** each chapter has research notes; key claims have a
real source (not "as is well known"); no source is a dead link or hallucination.

### Phase 2 — DRAFT  ·  `conductor/20-draft/draft.md`
**Goal:** write chapters *from the research*, not from the model's memory.
**Inputs:** research notes, `chapters-spec.md`.
**Outputs:** `chapters/NN-*.md` for every chapter in the outline.
**GATE 2 — full draft exists:** every outlined chapter has a draft that uses the
research notes and meets its spec (outcomes, worked example, exercises).

### Phase 3 — HUMAN REWRITE  ·  `conductor/30-human-rewrite/rewrite.md`
**Goal:** the human makes it theirs. This is the phase that can't be skipped or
automated — the agent assists, the human decides.
**Inputs:** the full draft.
**Outputs:** revised `chapters/NN-*.md` carrying the author's voice and judgment.
**GATE 3 — author sign-off:** the human has read every chapter, rewritten what
didn't sound like them, and signed `STATUS.md`. *No agent may sign this gate.*

### Phase 4 — FACT CHECK  ·  `conductor/40-factcheck/factcheck.md`
**Goal:** verify every checkable claim in the rewritten text.
**Inputs:** rewritten chapters, research notes.
**Outputs:** a fact-check report; corrections applied; citations resolved.
**GATE 4 — claims verified:** every factual claim is sourced or removed; no
citation is broken; numbers and quotes are confirmed against primary sources.

### Phase 5 — IMAGES  ·  `conductor/50-images/images.md`
**Goal:** generate the book's figures — static SVG (for the EPUB) and
interactive D3 (for the web).
**Inputs:** finished chapter text; `brutalist/` design prompts (in `conductor/design/`).
**Outputs:** `images/*-fig-NN.svg`, `d3/*-fig-NN.html`, and PNGs via
`node scripts/svg-to-png.mjs`.
**GATE 5 — figures exist:** every figure called for in the text exists as SVG +
PNG (and D3 where interactive), and renders.

### Phase 6 — CHECK IMAGES  ·  `conductor/60-check-images/check-images.md`
**Goal:** audit the figures for visual + notation defects.
**Inputs:** the generated SVGs.
**Outputs:** a clean run of `node scripts/svg-visual-audit.mjs` (subscripts,
superscripts, math notation, overflow), fixes applied, PNGs re-rendered.
**GATE 6 — figure audit passes:** `DRY_RUN=1 node scripts/svg-visual-audit.mjs`
reports `0 flagged`, or every residual is a reviewed, accepted exception.

> Phases 5–6 mirror the figure pipeline already proven on the other books in
> this repo: generate → render to PNG → audit → fix → re-render.

---

## After the spine: optional editions

Once GATE 6 is signed, the spine is done. The human now chooses any of the
add-ons in `conductor/editions/` — see `conductor/editions/README.md` for the
menu. Each edition is independent; pick none, some, or all. Examples: Chapter
Quizzes, Practice Exercises, Worked Solutions, Key Terms, Flashcards/Anki,
Further Reading, Interactive Simulations, CLI companions, and alternate-voice
editions (Socratic, Pragmatist, Wonder, Griffiths-style, Narrative).

**Voices.** The alternate-voice editions are produced in `voices/`: choosing a
voice writes a rewritten copy of `chapters/` into `voices/<voice>/`, leaving the
originals untouched. The **Wonder** voice is built — see `voices/wonder/VOICE.md`.

---

## Advisory tool: Editorial Review

Any time a draft exists — and especially before GATE 3 and before calling the
book done — run `conductor/editorial-review/editorial-review.md`: a
developmental + line editor's read of the full manuscript against its own
stated intent, returned as a constructive reader's report
(`editorial-report.md`, sidecar-stubbed, advisory only). It is distinct from
Fact Check (claim accuracy) and from voices (register rewrite); it never
rewrites the book. The author acts on it in the Human-Rewrite pass.

---

## Working agreement (for the agent)

1. **One phase at a time, in order.** Check `STATUS.md` before acting.
2. **Don't sign gates you can't honestly sign.** GATE 3 is human-only.
3. **Prefer the repo's own tools.** Scripts live in `scripts/`; prompts in `conductor/`.
4. **Leave a trail.** Research notes, fact-check reports, and audit output are
   artifacts — commit them, don't discard them.
5. **When unsure, stop and ask the human.** A wrong autonomous phase is
   expensive to unwind.
6. **Canonical files are read-only downstream.** The scripts and recipes
   (`conductor/`, `scripts/`, the `build-*` tools, voice `VOICE.md` specs, the
   facts tooling) are owned by the ai1-cli source repo and propagated via
   `scripts/sync-to-book.sh` per `SOURCE-MANIFEST.md`. To change one, edit it in
   ai1-cli and re-sync — never patch it in a single book, or the next sync
   overwrites your change.
