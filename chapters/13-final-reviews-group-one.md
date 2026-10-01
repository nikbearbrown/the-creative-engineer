# Chapter 13 — Final Design and Conducting Reviews — Group 1
*Demonstrate the experience, locate the critique, and justify the response.*

Here is the review that looks thorough and isn't.

A reviewer says: "The interface feels a little confusing in places." The presenter nods, goes back to Claude, and asks it to make the interface "clearer and more intuitive." Claude produces several revisions. The presenter accepts them. The review ledger shows twelve changes made.

Nothing in that sequence established what was confusing, why, or whether any of the changes addressed it. The number of revisions is not a quality score. A vague criticism accepted without investigation and addressed with a sweeping revision is not a thoughtful response — it's activity that looks like reflection.

The review's value is in what it forces you to find out. A specific criticism — "In Frame 4, after I submitted a question, I couldn't tell from the interface whether the system was searching or had finished" — establishes something you can investigate. You can open Frame 4. You can look at the loading state's design spec. You can check whether the implementation matches the spec. You can determine whether the loading indicator was in scope when the candidate was built.

That investigation is the skill the review is building. Not the number of changes. Not automatic agreement. Justified response to located critique.

---

## Preparing the Demonstration

The demonstration has the same structure as the midterm: a claim, a candidate version, and evidence on demand. The difference is that the final review includes external critique — feedback from reviewers who haven't been inside the project — and the response to that critique becomes part of the submission.

Start with the bounded claim. Not "here is my project" — "here is what this experience is designed to do, for whom, and what the evidence shows about whether it does that." Then demonstrate the critical journey and one consequential failure path. Show what happens when something goes wrong, not only the path that succeeds.

The review packet:

```
Demonstration claim
Candidate version and starting conditions
Critical journey and failure path
Design alternatives and selected rationale
Human/AI contribution record
Evaluation evidence
Known limitations
```

Identify the exact candidate version before the demonstration begins, for the same reason Chapter 12 required it at release: the evidence collected during the review must stay associated with the specific candidate being reviewed. A correction made after the review creates a different candidate.

When a reviewer asks why an interaction exists, open the relevant design alternative and decision record — don't reconstruct the rationale from memory. When a reviewer asks whether a behavior works, show the check result or run the journey. Answering a behavior question with a screenshot of code is not showing the behavior.

---

## What the Review Is Building

Before the critique begins, name what you're trying to develop.

A critique produces reviewer statements. A reviewer statement establishes what the reviewer said. It does not automatically establish why the confusion occurred, how common the problem is, or what the correct fix is. Each of those requires additional investigation.

The skill the review builds is the capacity to move through that chain: from a reviewer statement to an understanding of what the criticism actually establishes, to an investigation of the underlying condition, to a justified response decision. The quality measure is not whether you agreed with the criticism. It is whether you understood it specifically enough to respond to it with evidence.

A vague criticism — "more intuitive" — is not a usable finding. It's a concern to investigate. Ask what the reviewer expected at the specific step where they felt uncertain. Locate the frame and the state. Determine whether the expected behavior was specified, whether the specification was implemented, and whether the implementation communicates what it does. That investigation may lead to a revision, to a defense of the existing design, or to an acknowledgment that a known limit applies. Each of those is a justified response. Immediate revision without investigation is not.

---

## Separating What Was Said from What Was Found

The review ledger has more structure than a list of comments and responses. Each entry needs four distinct records that are easy to collapse into one:

*Original reviewer statement* — the reviewer's words, quoted accurately. What the reviewer said.

*Observed behavior* — what happened during the demonstration. What the system actually did.

*Interpretation* — a proposed explanation or consequence. What might account for the gap between what the reviewer expected and what they saw.

*Verification result* — what a subsequent check established. What actually changed after investigation.

These are distinct because the gap between them is where misdiagnosis happens. A reviewer who says "I couldn't tell what Continue would do" has told you they experienced uncertainty. They haven't told you whether the uncertainty came from an ambiguous label, missing consequence information, an inconsistency between the interface and the approved contract, or something in their mental model that the design can't address. Those possibilities call for different responses.

Keep the reviewer's words separate from your interpretation. Do not invent a precise complaint from a vague note. When the note is incomplete, ask a clarifying question or label the ambiguity explicitly in the ledger.

<!-- → [TABLE: Five-row table. Columns: Record, What it establishes, Common error. Rows: Original reviewer statement (what the reviewer said — attributing precision to an ambiguous comment), Observed behavior (what happened during the demonstration — describing intended behavior instead of actual behavior), Interpretation (a proposed explanation — treating the first explanation as the only explanation), Verification result (what a subsequent check established — accepting a passing check as proof the concern was addressed), Unresolved question (what remains uncertain after investigation — omitting this field when uncertainty remains). Caption: Collapsing these into a single "finding" field loses the information needed to choose the right response.] -->

---

## The Worked Example: Several Possible Causes

A reviewer says: "I could not tell what would happen when I pressed Continue."

This comment contains at least three possible explanations. The action meaning was never specified — it wasn't in the design at all. The design specified it, but the implementation diverged from the spec. The implementation matches the design, but the interface doesn't communicate it adequately. Each implies a different repair, and applying the wrong repair is likely to leave the underlying problem unaddressed.

The investigation sequence:

Ask what the reviewer expected at that step. Not what they would prefer — what they expected based on the surrounding context. Locate the exact state in Figma and in the candidate. Determine whether the action meaning was specified in the design, and if so, whether the implementation matches. Review the approval contract from Chapter 9 to confirm whether Continue triggers a consequential action that requires specific communication before the user acts.

If the action is an approval for a consequential operation, a clearer label alone may be insufficient. The exact action and its consequences need to be inspectable — visible enough that the reviewer can evaluate whether they're authorizing what they intended to authorize. A label change without that context doesn't resolve the underlying trust problem.

After revision, check that the label changed. Then check that the behavior contract is intact. Then — where possible — revisit the same task with someone who hasn't seen the explanation. Label the evidence accurately: a repeat with the same reviewer who now knows your intentions is different from an unfamiliar participant encountering the revised interface for the first time.

---

## Response Decisions and Verification Status

Revise, defend, and acknowledge-with-limit are response decisions. They describe what you chose to do. They are not evidence that anything was resolved.

A fourth response — investigate or clarify — is also necessary. Sometimes you don't have enough information to decide. A criticism that points at a problem without enough specificity to diagnose it warrants investigation before a response is possible. Forcing every criticism into one of the three available buckets before the investigation is complete produces responses that look decisive and aren't.

Track response decisions and verification status as separate fields:

| Response decision | Verification status |
|---|---|
| Revise | Planned, implemented, check run, check passed, check failed |
| Retain with justification | Rationale documented, counterevidence noted or absent |
| Acknowledge limitation | Consequence documented, follow-up identified |
| Investigate or clarify | Evidence collected, decision pending |

A revision without a check run is a change without evidence. A retained decision without a rationale is a position without support. A limitation without a documented consequence is a gap without an explanation.

If a required boundary remains broken — a failed approval gate, a collapsed state distinction — that is a defect. Acknowledging it as a limitation documents its status. It does not waive the requirement. A defect and an accepted trade-off are different things. An unnoticed problem does not become a trade-off by being inconvenient to fix.

---

## Conducting Claude as an Organizer

After collecting actual review notes, ask Claude to organize them — not to evaluate them or decide which require action.

```
Organize these notes into located findings.
Preserve each original statement and its source identifier.
Distinguish the reviewer's words from any interpretation you add.
Flag notes with missing evidence, ambiguous locations, or uncertain meaning.
Suggest a verification step and a possible response for each.
Do not fabricate feedback, add critics' names, or decide that every change is required.
```

Inspect the organized output against the original notes. Check whether Claude preserved qualifications — "might," "in this state," "seemed like." Check whether it changed a question into an assertion. Check whether it combined two incompatible comments. Check whether it omitted a minority observation that didn't fit the pattern of the others.

A polished summary can change the meaning of a criticism. The original notes and the organized findings both belong in the ledger. Choose your responses from the organized findings only after confirming they accurately represent the original.

---

## Receiving Critique

The chapter has focused on how presenters respond. Reviewers also need guidance on how to give critique that's useful.

A useful review comment names the location and what was observed, asks a clarifying question before prescribing a remedy, explains the possible consequence, and distinguishes a possible defect from a personal preference.

A comment that says "I think a different color scheme would improve this" is a preference. A comment that says "In the failure state, the message text and the background color are both red, and I initially read them as part of the same error rather than the system's description of the error and the recovery option" is a located observation with an interpretation. The second is useful to the presenter regardless of whether they agree with it.

Evaluate critique participation through the quality of the observations, not the volume of comments. A well-located concern with a clear consequence is more useful than several broad observations, even if it takes fewer words to state.

---

## What Would Change My Mind

The chapter treats the review as primarily a formative exercise — its value is in the investigation it requires, not in the changes it produces. If a controlled study compared this investigation-focused review against a simpler compliance-focused review (accept criticisms, make changes, check) and found no difference in what students could demonstrate afterward, that would challenge the premise. The chapter's claim is about what the investigation builds, which is a learning claim that the chapter doesn't directly test.

## Still Puzzling

The chapter gives Group 1 and Group 2 the same requirements and the same final deadline, and notes that presentation order doesn't change the requirements. What it doesn't fully resolve is that Group 1 has more time after its review to revise, and Group 2 has the advantage of having seen Group 1 present first. Those are structural asymmetries that a common rubric doesn't eliminate. The fairest approach is probably to assess the demonstrated candidate separately from subsequent revisions — grading what was shown during the review against the requirements known in advance, and grading the revision response against the quality of the investigation, not the amount of change. Whether the course implements it that way is a course-design decision rather than a chapter-design decision.

---

## Practice

1. Write the demonstration claim for your final review. Name the bounded value of the experience, the audience, and the candidate version.
2. Prepare the consequential failure path you'll demonstrate. Name the state, the trigger, and the expected system behavior.
3. For one actual criticism you've received, write the original reviewer statement in their words. Then write your interpretation separately. Confirm the interpretation doesn't add precision the statement didn't contain.
4. Take a vague criticism ("feels a little unclear") and write three possible explanations. Identify the smallest investigation that would distinguish between the first two.
5. Record one criticism in the full ledger format: original statement, observed behavior, interpretation, verification result, and unresolved question.
6. Choose a response disposition for one criticism: revise, retain with justification, acknowledge limitation, or investigate or clarify. Identify the verification status that would close it.
7. Write a retained-with-justification response for one design decision that received criticism. Name the evidence that supports the decision and any counterevidence you considered.
8. Acknowledge one limitation with its consequence and a follow-up step. Confirm the consequence description is specific enough to explain why the limitation matters.
9. Ask Claude to organize your review notes using the prompt from this chapter. Then audit the organized output against the original notes. Find at least one place where Claude changed the meaning — a qualification removed, a question turned into an assertion, or notes combined that shouldn't have been.
10. For one revision decision: write the bounded task contract before implementing anything. After implementation, run the affected checks and at least one adjacent check. Record the results.
11. Identify one case in your review where a criticism was valid but the proposed remedy would have created a different problem. Name the concern that survived the rejected remedy and the revision you chose instead.
12. Inspect one corrected state for regressions. Name the adjacent state or transition you checked, and what you found.
13. Distinguish one accepted trade-off from one unresolved defect in your project. For the trade-off, name the reason and the cost. For the defect, name the plan.
14. Write the reviewer protocol you would give to someone reviewing your project: what to name, what to ask before prescribing a fix, and how to distinguish a possible defect from a preference.
15. For the A6 submission: retain the original review notes, located findings, response decisions with verification status, revision evidence linked to the revised candidate, and the demonstrated candidate as a separate version. Do not rewrite the review history into a frictionless narrative.
