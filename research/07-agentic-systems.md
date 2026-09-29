# Research 7 — Designing agentic systems and conducting workflows

*Research notes, not chapter prose. Reviewed sources: 2026-09-29. Human Gate 1 approval pending.*

## Sources and claim boundaries

Source IDs: F02, C02, S01, P01. Full titles, publishers or local provenance, links, access dates, and source classifications are in [the source register](sources.md).

F02 lists unresolved intake, policy, tool, termination, source, and human-review decisions in a small diagram; its scaffold assumes defaults and contains placeholder behavior. C02 requires provenance and unresolved claims at handoffs. S01 separates final state from narration. These establish the source exercises, not production reliability.

## Playlist experiment evidence

V04: trace a FigJam evaluation table into tests without treating a stub as the real tutor. See [playlist evidence](playlist-evidence.md) for primary local reports, dates, and limitations. The playlist tests the education account's capabilities; it is central course evidence, not merely supplemental viewing.

## Proposed hands-on adaptation

Replace a vague FigJam planner–tools loop with explicit states: received, retrieving, source found, no source, review required, completed, failed. Specify each tool's input, output, permission, and timeout behavior. Give the assistant read-only resource lookup and a mock notification sink. Conduct one successful journey and one missing-source journey. Do not add real email or gradebook access.

### Candidate conducting prompt

> Review this architecture for missing transitions and authority. Produce task contracts with source, destination, payload, provenance, acceptance condition, and unresolved claims. Do not infer permission from an arrow. Ask about ambiguous transitions before implementing the bounded simulator.

## Evidence and failure checks

Reject missing provenance and unknown source IDs. Test exhausted steps, unauthorized writes, and a success message with unchanged state. Inspect the mock sink to determine whether an action occurred.

## Milestone

FigJam architecture, agent task contracts, and a working critical journey

## Unverified or intentionally excluded

[UNVERIFIED] A diagram is not an executable policy. The source scaffold's placeholder lookup and absent escalation are limitations to expose, not functionality to claim.

## Drafting contract

Apply the author's Pragmatist voice: result first, conditions and failure cases, compact worked example, and approximately twelve graduated practice tasks without inline solutions. Cover all four approved content blocks. Label the running assistant as illustrative and any outputs as expected until actually executed. Each practice task should require a decision, inspectable artifact, or specific check; the weekly artifacts feed the existing six submissions. No copied source-course grading schemes.
