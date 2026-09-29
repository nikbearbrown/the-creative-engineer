# Research 9 — Designing trust and human intervention in agentic AI

*Research notes, not chapter prose. Reviewed sources: 2026-09-29. Human Gate 1 approval pending.*

## Sources and claim boundaries

Source IDs: F03, C02, S01, P01, W07. Full titles, publishers or local provenance, links, access dates, and source classifications are in [the source register](sources.md).

F03 designs four tutor states and explicitly reports no completed human test. It can supply a design exercise, not evidence that students understand those states. C02 supports carrying uncertainty across handoffs. P01 supplies an exercise separating read/write scope and approval.

## Playlist experiment evidence

V04: use a passed test with the wrong rationale to challenge a claim of trustworthy behavior. See [playlist evidence](playlist-evidence.md) for primary local reports, dates, and limitations. The playlist tests the education account's capabilities; it is central course evidence, not merely supplemental viewing.

## Proposed hands-on adaptation

Design answer-with-source, partial-evidence, no-answer, and approval-needed states in Figma. For an instructor-contact action, show recipient, exact draft, disclosed data, cancellation, and consequence. Use a local mock sender. Test approval then changed content, cancellation, duplicate requests, missing sources, and tool failure. State which actions can be undone and which can only be mitigated.

### Candidate conducting prompt

> Inspect these recovery states and tool contracts. Generate failure cases without sending anything. In the local simulator, deny a send unless approval matches the current recipient and content. Show the resulting state and remaining uncertainty.

## Evidence and failure checks

Check actual mock outbox state, not only confirmation text. A cancellation after an irreversible action must not promise to unsend. Approval for one draft must not authorize a later changed draft.

## Milestone

A4: Agent orchestration and recovery design

## Unverified or intentionally excluded

[UNVERIFIED] The source's human usability work is pending. Class consent and research procedures require instructor review; the protocol is not institutional research approval.

## Drafting contract

Apply the author's Pragmatist voice: result first, conditions and failure cases, compact worked example, and approximately twelve graduated practice tasks without inline solutions. Cover all four approved content blocks. Label the running assistant as illustrative and any outputs as expected until actually executed. Each practice task should require a decision, inspectable artifact, or specific check; the weekly artifacts feed the existing six submissions. No copied source-course grading schemes.
