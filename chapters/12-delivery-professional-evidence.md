# Chapter 12 — Conducting delivery and designing professional evidence

[Contents](README.md) · [Previous](11-operational-constraints.md) · [Next](13-final-reviews-group-one.md)

*Release an inspectable candidate and explain your contribution without inventing outcomes.*

> Rough draft for author review. Release and case-study examples are illustrative.

## The result

Prepare a release candidate another person can inspect and a portfolio case study whose claims lead to evidence. Delivery includes design fidelity, reproduction, limitations, and human/AI contribution.

A public launch is not required to demonstrate these capabilities. A reviewed local package may be the appropriate release for a classroom prototype. Publishing is a separate decision with its own data, rights, and permission review.

## Package the experience, not only its source

A repository full of files does not tell a new reviewer how to use the work. Include the minimum entry path:

~~~text
README: purpose, audience, starting point
Design references: relevant Figma frames and FigJam architecture
Run instructions: tested setup and execution procedure
Sample data: labeled fixtures with no credentials
Checks: commands, observed results, and limitations
Evidence index: claim-to-artifact references
Contributions: human decisions and AI assistance
Known issues: remaining defects and accepted limits
~~~

These are proposed package roles, not mandatory filenames. Use names that fit the project, but make the roles discoverable.

State dependencies and versions actually used. Do not claim a clean installation works merely because the development machine already has everything installed.

## Conduct a release review

Ask Claude to inspect the candidate:

~~~text
Review this release candidate against the supplied checklist.
Identify missing setup steps, broken local references,
undocumented dependencies, unsupported claims, and out-of-scope files.
Do not publish, push, change permissions, or remove evidence.
Propose corrections before editing.
~~~

Review the findings and authorize only the changes you want. Run the actual reproduction checks on the candidate. Capture failures as part of the handoff record.

The source portfolio lesson requires checking evidence paths and reproducing a cited output. It also warns against fabricated career or customer outcomes. Apply both requirements here. [Source B04](../research/sources.md).

## Check design fidelity at the release boundary

Compare the released journey with the selected Figma version. Inspect content, state distinctions, source placement, action meaning, responsive behavior, and the approved recovery path.

Record deviations as intentional changes, defects, or unresolved differences. If implementation improved the design, update the design record rather than pretending that the old frame still describes the release.

Keep review notes associated with their subject: a named frame, component, issue, or file location. The source Figma review-note work emphasizes preserving that connection. Its historical tool limitations are not a substitute for checking the current client. [Source F04](../research/sources.md).

## Write the case study from the record

Use this structure:

| Section | Question to answer |
|---|---|
| Problem | What task and audience did you choose? |
| Alternatives | What materially different approaches did you consider? |
| Design | Which experience decisions shaped the result? |
| Conducting | What did you ask Claude to do, and how did you review it? |
| Evidence | What actually happened when you checked the candidate? |
| Limits | What remains unknown or unfinished? |

Do not make the tool list the whole story. “Used Claude and Figma” names the environment; it does not identify your contribution.

Ask Claude:

~~~text
Draft a concise case study from this evidence index only.
Attach an artifact reference to each outcome claim.
Separate my decisions, your generated work, and joint revisions.
Leave missing outcomes marked pending.
Do not invent testimonials, users, metrics, or approvals.
~~~

Edit the result yourself. Remove claims whose evidence you cannot locate. Preserve a limitation even when deleting it would make the project sound more impressive.

## Worked example: replace an inflated outcome claim

Consider this hypothetical draft sentence:

“The AI assistant transformed student learning through an intuitive interface.”

The project record contains an implemented resource journey and local failure checks, but no learning-outcome study. Replace the claim with an account of the artifact and observed scope:

“I designed a resource-discovery journey and conducted Claude's implementation. The release record includes source-link and no-source checks; learning outcomes have not been evaluated.”

In an actual case study, state which checks passed or failed and link their records. The sample sentence above describes a possible evidence scope, not a result established by this book.

For an original product, the same rule applies to claims about demand, time saved, or customer satisfaction. A prototype and a persuasive pitch do not establish those outcomes.

## Design the peer handoff

Ask a peer to begin with the README, not a verbal explanation. Observe where they need information that is absent from the package. Fix the missing instruction or record the dependency.

If the peer cannot reproduce a result, distinguish an environmental problem from a defect in the instructions or artifact. Do not retrospectively report the handoff as successful because you demonstrated it on your own machine.

Use critique dispositions from Conducting AI: revise, defend, or acknowledge with a limit. Each response should point to evidence. [Source C03](../research/sources.md).

[FIGURE: Release candidate linked to design version, check record, contribution ledger, and portfolio claim.]

## Practice

1. Write the first five lines a new reviewer needs.
2. Identify an undocumented dependency.
3. Separate a fixture from real user data.
4. Reproduce one cited output from the candidate.
5. Find a broken evidence reference.
6. Record an intentional design deviation.
7. Explain your contribution without naming tools.
8. Rewrite an unsupported outcome claim.
9. Ask Claude to draft from evidence only.
10. Inspect the package for private information.
11. Conduct a peer handoff or label it pending.
12. Explain why a release candidate need not be public.

## Submission checkpoint

Retain the release candidate, case-study draft, and peer handoff record. These feed A6. Keep the actual review history; do not rewrite it into a frictionless story.

Next: demonstrate the experience and respond to located critique.

Source basis: [Chapter 12 research](../research/12-delivery-professional-evidence.md).
