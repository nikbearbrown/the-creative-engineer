# Wiring the Fact-Checker to facts.json

The book fact-checker (the STEP 1–7 prompt) and `facts.json` are currently two
separate systems. They should be one loop: the checker **reads** `facts.json`
before hitting the web, and **writes** its findings back. That coupling *is* the
update — and it's the payoff of having a shared dictionary.

```
        ┌─────────────── facts.json (shared memory) ───────────────┐
        │  OpenStax-extracted facts  +  fact-checker web findings   │
        └───────────────▲───────────────────────────┬──────────────┘
        read (skip web) │                            │ write (new evidence)
                        │                            ▼
   book assertion ──► STEP 3.5 check ──► hit? use it / miss? STEP 4 web verify ──► STEP 4.5 record
```

---

## The two edits to the prompt

### New STEP 3.5 — Check `facts.json` before any web lookup

Insert **before STEP 4 (Site Verification)**:

> Before visiting any site, search `facts.json` for a fact matching this
> assertion (by `canonical` / wording similarity).
> - **Match with `consensus: agreement` or `verified: true`** → use it as the
>   verdict. Do **not** web-search. Cite the fact's evidence as the source.
>   (`SUPPORTS` evidence → CONFIRMED; a `REFUTES`/expired fact → CONTRADICTED/OUTDATED.)
> - **Match with `consensus: unverified` (single-source candidate)** → treat as a
>   strong hint, but still web-verify to add a second, independent vote.
> - **`consensus: conflict`** → flag for expert review immediately; do not pick a side.
> - **No match** → proceed to STEP 4 as normal.

This is exactly the routing rule already stated in `CONDUCTOR.md` ("check
facts.json before looking up a fact externally").

### New STEP 4.5 — Write every web finding back to `facts.json`

Insert **after STEP 4**, before writing the report:

> For every assertion you web-verified, append an evidence record to the matching
> `facts.json` fact (or create a new `source-attested` fact if none exists), then
> let consensus recompute. The source is the site you used; its tier comes from
> `facts-sources.yaml`.

A second independent source (PubMed, FDA, NIST…) agreeing turns an OpenStax
candidate into `agreement`; a contradicting source creates a `conflict` for the
human queue. The checker thus *feeds* the dictionary it reads from.

---

## Verdict ↔ evidence mapping (reconcile the two vocabularies)

The checker speaks CONFIRMED/OUTDATED/UNVERIFIED/CONTRADICTED; `facts.json`
stores `verdict` + derives `consensus`. Map them:

| Checker verdict | evidence `verdict` | effect on the fact |
|---|---|---|
| CONFIRMED | `SUPPORTS` | +1 vote; may reach `agreement` |
| CONTRADICTED | `REFUTES` | → `conflict` (human review) |
| OUTDATED | `REFUTES` + set `expires` / `stable:false` | → `conflict` / superseded |
| UNVERIFIED | (no evidence written) | unchanged; stays a candidate |

Each evidence record still carries `source`, `tier`, `url`, `retrieved`,
`verbatim` — so the checker's audit trail and the extractor's are the same shape.

---

## Source tiers for the checker's sites

The checker's authoritative sites slot into `facts-sources.yaml` tiers:

- **trusted**: standards/regulators — NCCN, FDA, EMA, WHO, NIST, IPCC
- **solid**: PubMed, journals (Nature), SEER/GLOBOCAN, IEEE/ACM
- **low**: general web / Scholar snippets without a primary source

A GUIDELINE/APPROVAL confirmation (FDA, NCCN) is a *trusted, non-OpenStax* vote —
the strongest kind of corroboration (`same_publisher: false`).

---

## Where the prompt lives and how it stays in sync

- The fact-checker is the **Phase 4 (Fact Check)** step — it belongs in
  `conductor/40-factcheck/` as the runnable prompt, with the STEP 3.5 / STEP 4.5
  additions above.
- **Single source of truth, referenced not restated.** The fact schema, the
  consensus/voting rules, and the source tiers live in `CONDUCTOR.md` +
  `facts/README.md` + `facts-sources.yaml`. The checker prompt should *point at*
  them ("append evidence per the facts.json schema; consensus is derived") rather
  than re-describe them — so when the facts model changes, you edit it in one
  place and the checker inherits it. That's the answer to "how does it get
  updated": you update the facts model/registry, and the checker references it.
- Deterministic plumbing (search facts.json, append evidence, recompute) can be a
  `scripts/` helper the prompt calls, exactly like the extractor uses
  `make_fact` / `merge_fact` — keeping the LLM doing judgment and code doing
  bookkeeping.

---

## Two tensions worth deciding

1. **Domain genericness.** The pasted prompt hardcodes biomedical sites (NCCN,
   FDA, SEER). The header says "works for any field," but the site lists are
   oncology-specific. Move the site→tier mapping into a small per-field config
   (like `facts-sources.yaml`) so the checker is truly field-agnostic.
2. **One dictionary, mixed provenance.** `facts.json` will hold OpenStax-extracted
   facts *and* fact-checker web findings together. That's correct — it's how
   multi-source consensus works — but it means the checker must dedup against
   existing facts (it already does, via `merge_fact`) so a re-check appends a vote
   instead of duplicating the fact.
