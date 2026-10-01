# Chapter 14 — Final Design and Conducting Reviews — Group 2 and Synthesis
*Close the evidence chain, preserve the full history, and identify what transfers.*

Here is the case study that sounds like the project went well and is impossible to check.

"Over the course of this project, I learned to conduct AI effectively, improved my design process, and delivered an experience that better serves students' needs."

Every word of that sentence may be true. None of it is traceable. There is no candidate version number, no check result, no decision record, no before-and-after comparison that would let a reviewer verify whether any of the claimed improvements actually occurred.

The final case study has the same evidentiary requirement as every other artifact in this course: claims need evidence capable of reaching them. "I improved the experience" is a claim. "The approval invalidation check, which was absent from the candidate demonstrated at the midterm, now passes consistently in the final candidate" is a claim that can be verified. One of those belongs in the A6 submission. The other is the kind of statement that looks like a conclusion without being one.

The audit question for the final submission is not "does this tell a coherent story?" It is "can a reviewer trace each material claim back to a specific artifact at a specific version, understand why that artifact supports the claim, and identify what the claim doesn't establish?"

---

## Applying the Same Standard

Group 2 uses the same review ledger, the same response dispositions, and the same submission requirements as Group 1. Presentation order is a scheduling constraint, not a separate assignment.

What differs structurally between the groups is not the requirements but the revision timeline: Group 1 has more calendar time after its review before the final deadline, and Group 2 has the advantage of having seen Group 1 demonstrate first. Neither is clearly superior, and the fairest assessment treats those structural differences by evaluating what was demonstrated during the review separately from subsequent revision quality — grading the demonstrated candidate against the pre-announced rubric, and grading the revision response on the quality of the investigation, not the volume of changes.

Don't create a new feature sprint because the semester is ending. Complete the required experience, repair consequential defects, and make the record accurate. A project whose final submission adds three new features to avoid fixing one broken approval boundary is not a strong final submission.

---

## Auditing the Evidence Chain

The audit moves through each material claim and asks, at each link: what supports this, at which version, under which conditions?

For each claim, the audit needs six answers.

*What artifact supports this claim?* Name the specific file, frame, check output, or observation. Not "the evaluation" — the specific file at the specific version that was checked.

*Why does that artifact support the claim?* State the reasoning that connects the artifact to the claim. A source-link check that passes establishes that the navigation behavior worked under tested conditions. It doesn't establish that participants found the source relevant. Those are different claims requiring different evidence.

*Under which assumptions does the reasoning hold?* Name the conditions. "The check passed" is shorthand for "the check passed in this environment, with this fixture, against this candidate version." The assumptions are part of the evidentiary record.

*What contrary evidence or untested condition limits the claim?* If the check passed but a similar check was not run on the failure path, name that. If the evaluation covered one type of participant but not another, name that.

*Which candidate contains the resulting artifact or check?* Version-specific evidence prevents the case study from describing a newer candidate than what was submitted or reviewed.

*Does the portfolio account match the evidence?* This is the last check: confirm that the narrative in the case study says what the evidence actually shows, not what would make the project sound more impressive.

<!-- → [TABLE: Claim register structure. Columns: Claim, Supporting artifact and version, Why this supports the claim, Limiting assumptions, Contrary evidence or untested conditions, Portfolio account matches evidence? Rows should be filled by student. Example partial row: "Approval invalidation prevents stale-approval execution — invalidation check output, candidate v2.3 — check tests the specific conditions the approval contract specifies — fixture tests only the local mock, not live service — live service behavior untested — [check against case study text]." Caption: Traceability alone does not establish support. The reasoning column is what connects the artifact to the claim.] -->

---

## What the Audit Is Not

The audit is not an exercise in constructing a positive narrative. A student who conducted a useful investigation that found a proposed revision ineffective has done exactly what the course is designed to develop. The final record should allow that result to remain visible.

The claim the final submission must support is not "I improved the experience." It is: you made consequential design decisions, conducted bounded AI work, inspected the result, and responded to the evidence — including when the evidence pointed toward a limit rather than a success.

"The approval invalidation check passes in the final candidate, which was absent in the midterm candidate" supports a specific claim. "The experience was improved" is a claim at a different level of abstraction, and reaching it requires more evidence than checking a single boundary.

Use precise conclusion language throughout. What changed: the specific artifact or behavior that is different. What the checks established: the specific conditions under which the behavior was verified. What remains uncertain: the specific conditions that weren't tested.

---

## Gaps, Defects, and Trade-offs

The final submission will have gaps. The question is whether they're named correctly.

A defect is a case where the candidate violates an accepted requirement. The approval gate failing when the content hash doesn't match, but the revision number is the same — that's a defect. It has a plan: repair and reverify.

An accepted trade-off is a case where the design deliberately favors one objective with a documented cost. The inline preview was chosen over a separate detail view because it keeps the query visible during comparison, at the cost of constrained display space for individual resources. That's a trade-off. It has a rationale and an acknowledgment of the cost.

Missing evidence is a case where a claim hasn't been established. Learning outcomes haven't been evaluated. Long-term retention of discovered resources hasn't been measured. Those are missing evidence, not defects and not trade-offs.

Each category implies a different response. Repair the defect. Defend or revise the trade-off. Obtain evidence or narrow the claim. "Future work" applied to all three conceals which response is actually appropriate.

<!-- → [TABLE: Three-column table. Columns: Category, Definition, Required response. Rows: Defect (candidate violates an accepted requirement — repair and reverify), Accepted trade-off (design deliberately favors one objective with a documented cost — rationale on record; cost acknowledged), Missing evidence (claim has not been established — obtain evidence or narrow the claim). Caption: Do not apply a single "future work" label to all three. Each requires a different response, and collapsing them hides which response is appropriate.] -->

---

## When Objectives Changed

Projects change. A project that began as an automatic-answer tool and ended as resource discovery with an explicit no-source state is a project whose scope changed — and that change has a record.

The honest case study preserves both the original objective and the revised one, with the evidence or constraints that motivated the revision and the name of whoever accepted the change.

```
Original objective: generate automatic answers to student questions
Evidence motivating reconsideration: no evaluation framework existed
  for answer correctness; available catalog was structured around
  sources, not answers
Selected revision: narrow the journey to resource discovery and
  source inspection
Requirements retained: eligible-source constraint, no-source state,
  source link verification
Requirements changed: removed automatic answer generation
Who accepted the change: [student, per project scope; instructor
  notified at X checkpoint]
```

A narrower objective can be a justified design decision. It can also become a way to redefine failure after the fact. The audit distinguishes them by requiring that both original and revised evaluation criteria remain in the record, and that the final submission identifies which objective the candidate actually satisfies.

Students can propose a scope change. They cannot independently remove required capabilities by rewriting their brief after the fact.

---

## Conducting the Final Gap Audit with Claude

Provide the evidence index and ask Claude to identify what's missing — not to fill it in.

```
Audit this evidence chain.
For each material claim, identify its supporting artifacts and version.
Report missing links, contradictions, unsupported outcomes,
and unclear human/AI contributions.
Classify each gap as: missing reference, check never performed,
contradictory evidence, unresolved requirement, candidate defect,
or condition outside supported scope.
Do not fill gaps with a plausible story.
Do not mark a claim as supported based on what you infer the student intended.
```

Inspect the output against the actual index. A missing link might be a genuinely absent check or a badly named file that exists under a different reference. Resolve the distinction before requesting another implementation. A gap Claude identifies as "missing evidence" might be evidence that exists under a different name, or it might be evidence that genuinely doesn't exist. Those require different responses.

Don't let the final case study describe a newer candidate than the submitted artifact. Freeze the submission reference, then make the narrative point to it.

---

## Transferring the Method

Choose a new domain without implementing a second project. Write a one-page transfer brief that demonstrates reasoned adaptation.

```
New audience and task:
What remains useful from this project's method:
What assumptions no longer hold:
New authority or data boundaries:
One familiar technique that would be unsuitable here (and why):
First bounded experiment:
Evidence that would change the design:
```

The last two fields are the hardest and the most revealing. Naming the first bounded experiment forces specificity about where the uncertainty is. Naming the evidence that would change the design forces explicit acknowledgment that the design could be wrong.

Transfer requires naming what no longer applies, not just what can be reused. If the resource assistant used a fixed synthetic catalog, a new domain where information changes over time requires freshness checks and source-version tracking. If the approval boundary was tested only against a local mock, a domain where actions affect other people requires reassessing authority, consequences, and recovery. If the reviewed participants understood the course context, an audience without that context requires testing terminology and evidence navigation separately.

The transfer brief doesn't establish that the method will work in the new domain. It demonstrates that you can identify which assumptions are load-bearing and which can be adapted.

---

## The Four-Verb Closing

Return to Ideate, Build, Brand, Ship. For each verb, the reflection has a specific form:

Earlier approach → current decision → artifact → observed consequence → next check

Not "I became more careful about problem framing." Earlier approach: "I began by asking Claude to generate journeys for an undefined audience." Current decision: "I write the audience decision statement before generating anything, using the sentence structure from Chapter 3." Artifact: "The Chapter 2 brief and the Chapter 3 FigJam board." Observed consequence: "The alternative architectures in Chapter 3 were genuinely different because they started from the same audience decision, not from different visual styles." Next check: "I don't yet have evidence about whether this produces better outcomes for the audience, because no participant evaluation covered that."

That is the Feynman test applied to method: can you explain your practice specifically enough that someone else could replicate it, and can you identify what you don't yet know?

---

## Final Packaging

Confirm the following before submitting: the entry point opens correctly from the reviewer's access conditions; the submitted candidate is identifiable by version; all evidence links resolve for the intended reviewer; limitations are visible rather than buried; private material is absent from public artifacts; and the package and case study identify the same candidate.

If a local submission and a public portfolio require different evidence packaging, name both and explain what differs and why.

A reviewer confirming that the package opens is not a completion certificate. The review establishes inspectability. Whether the experience is adequate is the criterion question, and the answer comes from the evidence, not from the package opening cleanly.

---

## What Would Change My Mind

The audit's reasoning column — "why does this artifact support this claim?" — requires students to make their inference explicit. In a mature research context, this reasoning is often formally structured (as in assurance cases or systematic review methods). For a course project, the informal version is sufficient. If evidence emerged that students who wrote out the reasoning produced no better-calibrated claims than those who didn't, I'd reconsider whether the column adds value or just adds length. The prediction is that making the reasoning explicit catches cases where the artifact doesn't actually reach the claim — but that prediction is itself untested by this course.

## Still Puzzling

The transfer brief is assessed as part of A6, but it describes a project that doesn't exist. How much credit it carries, and what standard governs whether the reasoning is adequate, isn't fully specified here. The course rubric probably needs to distinguish: did the student identify which assumptions are load-bearing (demonstrable from the brief), and did the student name a plausible first experiment (demonstrable from the brief)? Those are assessable. Whether the proposed experiment would actually work in the new domain is not assessable without doing it.

---

## Practice

1. Write the claim register for three material claims in your final submission. For each, complete all six columns: claim, supporting artifact and version, reasoning, limiting assumptions, contrary or untested evidence, and portfolio match.
2. Find one place in your current case study where the reasoning column would reveal that the artifact doesn't actually reach the claim. Name the correct conclusion.
3. Conduct the final gap audit using the Claude prompt from this chapter. Audit the output against your actual index. Identify one gap Claude misclassified and explain the correct classification.
4. Separate one defect, one accepted trade-off, and one instance of missing evidence in your project. Write the correct response for each.
5. If your project's objective changed during the semester, write the objective-change record: original, motivating evidence, revised objective, retained and removed requirements, and who accepted the change. If it didn't change, write why the original framing held.
6. Freeze the submission reference for your candidate. Confirm that the case study and the package identify the same version. Record any mismatch.
7. Write the transfer brief for a domain you haven't worked in. Complete all seven fields. Name at least one familiar technique that wouldn't apply and explain specifically why.
8. Write the four-verb self-audit in the specific form: earlier approach → current decision → artifact → observed consequence → next check. For each verb, confirm the artifact actually exists.
9. Identify one claim in your case study where the limiting assumptions column would reveal an untested condition that matters for the claim's scope.
10. Confirm all evidence links in your submission resolve under the reviewer's access conditions, not your own. Record any link that requires permissions the reviewer doesn't have.
11. Separate the three assessable dimensions of the final submission: whether the artifact meets requirements, whether you can defend consequential decisions, and whether you can adapt the method. Identify which artifact provides evidence for each.
12. For the A6 submission: include the reviewed candidate with its version identifier, the claim register with all six columns completed, the gap audit with gap classifications and resolution status, the objective-change record if applicable, the transfer brief, and the four-verb self-audit. Keep the demonstrated candidate as a preserved version separate from subsequent revisions.
