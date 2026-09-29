# Chapter 13 — Final design and conducting reviews — Group 1

[Contents](README.md) · [Previous](12-delivery-professional-evidence.md) · [Next](14-final-reviews-synthesis.md)

*Demonstrate the experience, locate the critique, and justify the response.*

> Rough draft for author review. Sample review findings are hypothetical, not comments from actual students.

## The result

Complete a final design review that produces an inspectable response record. Show what the experience does, defend the decisions behind it, and identify what should change.

This chapter serves the first presentation group. The second group uses the same requirements, evidence standards, and final revision deadline. Presentation order does not create a different project or another implementation assignment.

## Prepare a claim-centered demonstration

Begin with the audience task and the bounded value of the experience. Identify the candidate version. Demonstrate the critical journey and a consequential failure path.

Use evidence on demand. If a reviewer asks why an interaction exists, open the relevant design alternative and decision record. If asked whether a behavior works, show the appropriate check or run the journey. Do not answer a behavior question with a screenshot of code.

For a portfolio, the demonstrated journey may itself be the evidence path. For a product or AI tool, show the chosen product behavior rather than a catalog of features.

Keep a short review packet:

~~~text
Demonstration claim
Candidate version and starting conditions
Critical journey and failure path
Design alternatives and selected rationale
Human/AI contribution record
Evaluation evidence
Known limitations
~~~

The source portfolio method supports this evidence-first presentation. [Source B04](../research/sources.md).

## Make critique specific enough to act on

A useful finding names the artifact, the observed issue, its consequence, and the evidence. “Make it more intuitive” is a concern to clarify, not an implementation instruction.

Use this ledger:

| Field | What belongs there |
|---|---|
| Finding ID | Stable reference for discussion |
| Location | Frame, state, file, or demonstrated step |
| Observation | What the reviewer actually saw |
| Interpretation | Why it may matter |
| Response | Revise, defend, or acknowledge with a limit |
| Revision evidence | What changed and how it was checked |

Keep the reviewer's words separate from your interpretation. Do not invent a precise complaint from a vague note. Ask a clarifying question or label the ambiguity.

Conducting AI's rehearsal lesson uses these dispositions and does not require every criticism to be accepted. The standard is justified response, not automatic agreement. [Source C03](../research/sources.md).

## Conduct Claude as an organizer, not a fictional reviewer

After collecting actual review notes, ask:

~~~text
Organize these notes into located findings.
Preserve the original statement and distinguish your interpretation.
Flag missing evidence or ambiguous locations.
Suggest a verification step and possible response for each.
Do not fabricate feedback or decide that every change is required.
~~~

Inspect the organized output against the original notes. A polished summary can change the meaning of a criticism. Correct it before using it to direct implementation.

Choose the response yourself. For a revision, create a bounded task contract. For a defended decision, provide the reason and evidence. For a limitation, state the consequence and why it remains.

## Worked example: a criticism with two possible causes

Suppose a reviewer says, “I could not tell what would happen when I pressed Continue.”

Locate the exact state. The problem might be the label, missing consequence information, or a transition inconsistent with the design. Do not immediately replace every button label in the application.

1. Ask what the reviewer expected at that step.
2. Inspect the selected frame and actual candidate.
3. Determine whether the action meaning was specified.
4. Revise the local label or surrounding explanation if the evidence supports it.
5. Check that the underlying action still matches the approved contract.
6. Revisit the same task and record the result.

If the action is approval for a consequential operation, a clearer label alone may be insufficient. The exact action and relevant consequences still need to be inspectable.

This scenario is illustrative. Your ledger must contain the review that actually occurred, including uncertainty when the note is incomplete.

## Evaluate the proposed correction

A criticism may be valid while its proposed remedy is poor. A reviewer can correctly notice a confusing source display and recommend removing the source. Preserve the problem, but test another remedy that keeps evidence visible.

Likewise, Claude may introduce a new defect while fixing the visible complaint. Re-run affected checks and inspect related states. Evaluating a critique and its correction extends the supervisory-check method. [Source H01](../research/sources.md).

Do not count revisions as a quality score. One well-supported correction may matter more than numerous cosmetic edits. Do not invent a struggle or a reversal to make the process appear reflective.

## Preserve unresolved trade-offs

State the alternatives, the selected priority, and the cost of that choice. An accepted trade-off has a reason. An unnoticed defect does not become a trade-off merely because it is inconvenient to fix.

If a required boundary remains broken, call it a defect and identify the plan. Do not hide it in an “opportunities” paragraph.

[FIGURE: Located review finding splitting into revise, defend, and acknowledge-with-limit responses, each linked to evidence.]

## Practice

1. Choose a claim for the final demonstration.
2. Identify the exact candidate version.
3. Prepare a consequential failure path.
4. Turn a vague critique into a clarifying question.
5. Separate observation from interpretation.
6. Record a revise disposition.
7. Record a defensible disagreement.
8. State a limitation with its consequence.
9. Audit Claude's summary against original notes.
10. Bound a review-driven implementation change.
11. Inspect a regression after a correction.
12. Distinguish an accepted trade-off from an unresolved defect.

## Submission checkpoint — A6, Group 1

Complete the presentation and critique participation. Retain the review ledger, supporting evidence, response decisions, and revision checks. Both groups share the same final requirements and final revision deadline supplied in Canvas.

Next: complete the second review round and audit the full evidence chain for final submission.

Source basis: [Chapter 13 research](../research/13-final-reviews-group-one.md).
