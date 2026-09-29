# Chapter 8 — Midterm defense: design and conducting decisions

[Contents](README.md) · [Previous](07-agentic-systems.md) · [Next](09-trust-human-intervention.md)

*Demonstrate one journey and make its design history inspectable.*

> Rough draft for author review. The sample defense is hypothetical.

## The result

Deliver a working critical journey with an evidence packet that explains why it has this form and how you supervised its implementation.

A midterm defense is not a tour of every screen. It is an examination of a claim: this experience serves the stated task, within stated limits, and the submitted evidence supports that assertion.

Use this sequence:

~~~text
Task → selected design → observed behavior → supporting evidence → limitation
~~~

Do not substitute a fluent explanation for any missing link.

## Select the demonstration claim

Choose a claim narrow enough to demonstrate. “The assistant helps students learn” is broader than this prototype's evidence. “The prototype shows an identified source and opens that source from a recommendation” can be inspected.

State the starting conditions. Identify the version, sample data, expected behavior, and failure condition. Demonstrate from the candidate you are submitting, not another development copy.

For a portfolio project, the claim could concern the evidence journey: a reviewer can move from a contribution claim to the artifact that supports it. Do not claim that this journey produced interviews, clients, or employment unless you have actual evidence.

## Assemble the decision chain

Build a small index:

| Claim or decision | Design evidence | Implementation evidence | Remaining limit |
|---|---|---|---|
| Source stays adjacent to recommendation | Named frame and annotation | Rendered candidate and inspected change | Human comprehension not yet observed |
| No source is not a tool error | Separate states and rationale | Distinct failure fixtures | Live service behavior not tested |
| New dependency was rejected | Scope decision | Diff or retained proposal | Other implementation alternatives remain |

Use actual file and frame references in your submission. The table above illustrates the structure, not completed findings.

The Prompt Engineering review packet preserves reproduction, plan, diff, and checks. The Branding and AI portfolio method adds contribution and source evidence. Together they support a defense that can be inspected rather than merely believed. [Sources P02 and B04](../research/sources.md).

## Explain alternatives and rejected changes

Show at least one consequential alternative. Explain why you did not choose it using the audience task, constraints, and available evidence.

Also show a Claude proposal you changed or rejected. Rejection is not inherently evidence of good supervision. The reason matters. Rejecting every suggestion reflexively is no better than accepting every suggestion automatically.

Use a short disposition record:

~~~text
Proposal:
Intended benefit:
Conflict or uncertainty:
Decision: accept / change / reject / defer
Reason:
Evidence to revisit the decision:
~~~

If you accepted the proposal, be equally precise. State what you inspected before accepting it.

## Rehearse with Claude, then with a person

Use Claude to prepare questions:

~~~text
Read this evidence index and demonstration claim.
Ask questions about alternatives, boundaries, failure behavior,
accepted changes, rejected changes, and unsupported conclusions.
Identify the artifact that could answer each question.
Do not invent reviewer feedback or mark the work approved.
~~~

Answer a question yourself before asking for a suggested answer. Then ask Claude to identify which parts of your answer lack evidence.

Conduct a real peer rehearsal when available. Let the peer choose a path or evidence item to inspect. If no peer is available, label the session self-review and retain peer review as pending. Claude is not a substitute participant whose feedback can be reported as a human review. [Source C03](../research/sources.md).

## Worked example: defend a partial success

Suppose your card implementation preserves the source and text hierarchy but stretches the action button beyond its design specification.

An inadequate defense says, “Claude built it correctly except for a small detail.” That hides both the standard and the evidence.

A stronger defense identifies the specific mismatch, shows the reference and render, explains the intended behavior, and states the next check. You may decide that the mismatch blocks acceptance or that it is a documented limitation for this milestone. The decision must follow your criteria.

The playlist's screenshot/context case is useful because the more faithful output still contained a width error. Its conclusion was limited, not perfect fidelity. [Playlist case V01](../research/playlist-evidence.md).

Now ask the reviewer to select the no-source path. If it fails, preserve the failure. Do not quietly switch to another version and report the original demonstration as successful.

## Handle questions you cannot answer

Use “not yet established” with a specific next step. For example: “The source link opens in this candidate; whether readers judge relevance correctly requires the planned usability session.”

Distinguish three gaps:

- Missing evidence: run or obtain the needed check.
- Missing design decision: make and document the decision.
- Accepted limit: state the boundary and its consequence.

An honest limit is not a replacement for completing required work. It tells the reviewer what the current claim can support.

[FIGURE: One demonstration claim linked to a frame, decision record, diff, check, and limitation.]

## Practice

1. Narrow an overbroad demonstration claim.
2. State the candidate's starting conditions.
3. Link one claim to three distinct evidence types.
4. Show a rejected design alternative.
5. Explain one accepted Claude change.
6. Explain one rejected Claude change.
7. Generate rehearsal questions without generated answers.
8. Answer a question without relying on Claude's wording.
9. Record an unsuccessful demonstration accurately.
10. Separate missing evidence from an accepted limit.
11. Ask a peer to choose the failure path.
12. Revise a claim whose confidence exceeds its support.

## Submission checkpoint — A3

Submit the Figma system, agentic prototype, and midterm defense. Include the critical journey, alternatives, architecture, task contracts, implementation review, evidence index, and limitations. Canvas supplies presentation logistics.

Next: design what the system does when it lacks evidence, needs permission, or must recover.

Source basis: [Chapter 8 research](../research/08-midterm-defense.md).
