# Research 11 — Designing operational constraints and conducting revision

*Research notes, not chapter prose. Reviewed sources: 2026-09-29. Human Gate 1 approval pending.*

## Sources and claim boundaries

Source IDs: S01, P01, P02, W07, W08. Full titles, publishers or local provenance, links, access dates, and source classifications are in [the source register](sources.md).

S01's exercise includes exhausted budgets and action-result logs. P01 warns that its path validator is not an operating-system sandbox. P02 uses regression checks plus scope review. Adapting these to latency, cost, privacy, and release constraints is a proposed design exercise.

## Playlist experiment evidence

V03 and V05: separate call accounting, estimated cost, actual billing, and account-specific access failures. See [playlist evidence](playlist-evidence.md) for primary local reports, dates, and limitations. The playlist tests the education account's capabilities; it is central course evidence, not merely supplemental viewing.

## Proposed hands-on adaptation

Set declared budgets for the assistant: elapsed time, maximum steps, retained data, authorized actions, and recovery responsibility. Use synthetic resource data. Conduct Claude through injected lookup timeout and retry scenarios. Capture actual timings if run; treat all sample limits as chosen classroom targets. Review logging for sensitive payloads, select a revision, and rehearse rollback to the previous local release.

### Candidate conducting prompt

> Investigate the supplied failure trace without changing code first. Distinguish observed facts from hypotheses. Propose the smallest revision and tests for timeout, retry, duplicate action, and privacy boundaries. Do not raise permissions or hide failing tests.

## Evidence and failure checks

Retest successful journeys after recovery changes. A retry must not duplicate the consequential action. Cost projections require identified units and rates; no live model pricing or unlimited quota claim is included. Inspect what logs retain.

## Milestone

A5: Evaluation and redesign dossier, including operating assumptions

## Unverified or intentionally excluded

[UNVERIFIED] No performance, reliability, cost-saving, or production-security measurements exist for the illustrative assistant. A classroom prototype is not certified deployment-ready.

## Drafting contract

Apply the author's Pragmatist voice: result first, conditions and failure cases, compact worked example, and approximately twelve graduated practice tasks without inline solutions. Cover all four approved content blocks. Label the running assistant as illustrative and any outputs as expected until actually executed. Each practice task should require a decision, inspectable artifact, or specific check; the weekly artifacts feed the existing six submissions. No copied source-course grading schemes.
