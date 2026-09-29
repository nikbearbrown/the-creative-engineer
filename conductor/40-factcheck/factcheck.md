# Phase 4 — FACT CHECK

**Verify every checkable claim — through `facts.json` first, the web second.**
The human rewrite may have sharpened claims or changed numbers, so re-verify after
the voice is settled.

## When to run
After GATE 3 (human sign-off) is signed.

## Inputs
Rewritten `chapters/`, `research/` notes, and the fact dictionary `facts/facts.json`.

## Outputs
- `factchecks/<chapter>-assertions.md` — per chapter, every flagged claim + verdict + source.
- `factchecks/MASTER_REPORT.md` — book-wide rollup.
- Inline `<!-- FACT-CHECK FLAG -->` notes + a References section in each chapter.
- **`facts/facts.json` enriched** with every finding (the dictionary grows each run).

---

## The rule: every fact routes through `facts.json`

Before any web search, **look the claim up in the dictionary**. After any web
check, **record the finding back**. Never overwrite a verified fact — append
evidence. The deterministic bookkeeping is `facts/facts.py` (built on
`facts_store`); you supply the judgment. See `facts/FACTCHECKER-INTEGRATION.md`.

```bash
python facts/facts.py lookup "<the claim>"     # exit 0 = trusted (agreement/verified) · 2 = candidate/conflict · 1 = no match
python facts/facts.py record --claim "<claim>" --source <id> --url <url> \
       --verbatim "<exact sentence>" --verdict SUPPORTS|REFUTES|PARTIAL [--domain d --category C]
```

---

## STEP 1 — Scan
Read every content file in `chapters/` in order (skip index/TOC/nav). Track which
chapter and file each sentence came from. Create `factchecks/` if absent.

## STEP 2 — Classify assertions
For each sentence, skip non-assertions (questions, transitions, headings, first-time
definitions). For real assertions, note the **type** (basic / emphatic / I-language /
positive; *emphatic + positive = COMBINATION*, highest priority) and whether it needs
verification by **content category**: STAT, GUIDELINE, APPROVAL, EVIDENCE, SPECIALIST,
CURRENT. Pure definitions, standard mechanisms, and unquantified comparisons are
AI-only (no web).

## STEP 3 — Check `facts.json` FIRST
For each flagged claim, `facts.py lookup`:
- **exit 0** (`agreement` or `verified`) → use it as the verdict. **Skip the web.**
  Cite the fact's evidence.
- **exit 2, `consensus: conflict`** → flag for expert review now; don't pick a side.
- **exit 2, single-source candidate** → treat as a hint, but still web-verify to add
  an independent vote.
- **exit 1** (no match) → proceed to STEP 4.

## STEP 4 — Web-verify (only what STEP 3 didn't resolve)
Visit the authoritative sites for the claim's category; stop at the first clear
answer. Default sites are field-specific — substitute for this book's field
(e.g. GUIDELINE/APPROVAL → standards bodies/regulators; STAT → official statistics;
EVIDENCE/SPECIALIST/CURRENT → PubMed / scholarly search / field databases, recent first).
Record URL, what you found, and a verdict: CONFIRMED / OUTDATED / UNVERIFIED / CONTRADICTED.

## STEP 5 — Record findings back to `facts.json`
For each web-verified claim, `facts.py record` so the dictionary learns:

| web verdict | `--verdict` | effect |
|---|---|---|
| CONFIRMED | `SUPPORTS` | +1 vote (may reach `agreement`) |
| CONTRADICTED | `REFUTES` | → `conflict` (review) |
| OUTDATED | `REFUTES` (+ note expiry) | superseded → review |
| UNVERIFIED | — (don't record) | stays a candidate |

The source's tier is auto-filled from `facts-sources.yaml` (regulators/standards =
trusted, journals/PubMed = solid, general web = low).

## STEP 6 — Write reports + annotate
One `factchecks/<chapter>-assertions.md` per chapter (flagged sentences, verdicts,
sites, suggested references; "Critical" section for OUTDATED/CONTRADICTED/COMBINATION).
In each chapter, add an inline `<!-- FACT-CHECK FLAG: [VERDICT] -->` after any
OUTDATED/CONTRADICTED/UNVERIFIED sentence, and a `## References` section for CONFIRMED
claims. Do not change prose.

## STEP 7 — Master report
`factchecks/MASTER_REPORT.md`: totals by category and assertion type, all critical
findings (GUIDELINE/APPROVAL first), a chapter-by-chapter table, and recommended
next steps.

---

## GATE 4 — Claims verified
- [ ] Every flagged claim resolved via `facts.json` or the web (Verified / Corrected / removed).
- [ ] No citation is broken; numbers and quotes confirmed.
- [ ] Findings recorded back to `facts/facts.json`; conflicts triaged.
- [ ] `factchecks/` reports committed.

Record sign-off in `STATUS.md` (GATE 4), then move to `conductor/50-images/`.
