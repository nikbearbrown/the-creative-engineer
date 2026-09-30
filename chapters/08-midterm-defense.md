# Chapter 8 — Midterm Defense: Design and Conducting Decisions
*The defense is an examination of a claim — and the claim has to be narrow enough that the evidence can actually reach it.*

Here is the defense that fails without lying.

A student opens the prototype. The source card appears, the title is correct, the explanation is present. They tap the source link. The source opens. "As you can see," they say, "the implementation is complete."

But complete against what standard? The implementation matches a screenshot from a favorable state of the prototype. The reviewer can't see whether the no-source condition produces a distinct message or silently fails. They can't see whether the source adjacency holds when the title is three lines long. They can't see whether the button width mismatch documented in the fidelity review is a known limit or an undisclosed defect. They can't see whether the implementation was demonstrated from the submitted candidate or from a development copy that was quietly switched before the room was entered.

A working journey is evidence about one path, once, from a starting state the student chose, with the system in a condition the student controls. That's meaningful. It's also much narrower than "the implementation is complete."

The defense is not a tour of what works. It's an examination of a claim — and the claim has to be narrow enough that the evidence can actually reach it.

---

## Two Things the Defense Assesses

Before the defense, distinguish the two claims it examines.

The first is about the prototype: whether it performs the stated journey under stated conditions. Evidence for this is behavioral — what the system actually does, recorded under specified starting conditions, checked against criteria declared in advance.

The second is about your judgment: whether you understand and can justify the design and implementation decisions, including the ones that didn't go well. Evidence for this is the decision chain — alternatives considered, proposals accepted or rejected, limits acknowledged, gaps named.

A working artifact does not by itself establish sound supervision. A fluent explanation does not establish working behavior. Both need to be present, and the evidence for each is different. Conflating them produces a defense where a convincing explanation of a broken behavior, or a working button that the student can't explain, both pass when neither should.

---

## Narrow the Claim

"The assistant helps students learn" is not a demonstrable claim. It's a hope that would require a learning study to substantiate. "The prototype shows an identified source and opens that source from a recommendation" is demonstrable. You can show it. A reviewer can inspect it.

Upper claims tend to be vague and not directly provable. Lower claims can be substantiated with specific evidence. The defense proceeds by decomposing the upper claim into lower ones and demonstrating the lower ones, while stating clearly which upper claims the lower evidence supports and which it doesn't reach.

For the resource assistant, a defensible lower claim: "The prototype returns a distinct message for a completed search with no results and a different distinct message for a failed lookup, and a reviewer can trigger both conditions using the supplied fixtures."

For a portfolio: "A reviewer can move from the contribution claim on the project page to the dated artifact that supports it, without encountering a broken link or a claim the artifact doesn't establish."

Both claims are specific. Both can fail. Both can be demonstrated by showing the path and running the fixture. That's what makes them defensible.

---

## The Demonstration Card

The demonstration has starting conditions, and those conditions should be declared before the demonstration begins.

```
Claim:
Candidate: tag [name], commit [hash], run from a fresh clone
Sample data: [file]
Input mode: typed live / pasted / pre-staged fixture
Timing: live / recorded (if recorded: edited? Y/N)
Path selection: chosen by reviewer / chosen by presenter (reason)
Rehearsal history: [n] attempts, [n] succeeded; failures: [describe]
Blocking criteria (declared before the defense):
Expected failure condition:
```

Each field closes a dimension along which a demonstration can misrepresent without producing false output. In December 2023, Google's "Hands-on with Gemini" video showed apparently real-time voice interaction with its new model. The outputs, as Google described them, were real. But the interaction mode was text prompts rather than live voice, the latency had been reduced, and the presented examples had been selected from available outputs. Each of those dimensions — mode, timing, selection — could, in a student defense, produce a demo that feels more complete than it is.

Name the commit hash and clone the repository fresh before the defense. "Not another development copy" is an instruction. A hash is a check.

Declare the blocking criteria before the demonstration, not after seeing what fails. If the button-width mismatch is a blocking defect, it needs to block before the demo, not because the demo exposed it. Pre-declared criteria are the difference between an evaluation and a negotiation.

Report rehearsal history, not just the live result. If the journey worked three times in five rehearsal runs, the live success doesn't tell you something different from the rehearsal history — it's a sample of what the prototype does, not evidence of reliable performance. "Succeeded in 4 of 5 rehearsal runs; the timeout on the catalog lookup accounted for the single failure" is a stronger defense than a smooth live demo with no history behind it.

---

## The Evidence Index

The evidence index is a small table that connects each claim to the specific artifacts that support it, the argument for why they support it, and the limits of what they establish.

| Claim | Evidence (frame, file, check) | Argument: why this supports the claim | Status | Remaining limit |
|---|---|---|---|---|
| Source stays adjacent to recommendation | Frame `[id]`; render at `[commit]` | Adjacency lets the reader verify the source before acting — the audience decision from Ch. 3 | Demonstrated in candidate | Reader comprehension not yet observed |
| No source is not a tool error | Distinct states and rationale; fixtures `[file]` with actual outputs | Separate state means a reader never mistakes a missing source for a broken system | Executed, actual outputs preserved | Live service behavior untested |
| New dependency rejected | Disposition record `[id]`; retained proposal | Scope boundary from task contract, Ch. 6; scope creep would expand what the Chapter 7 review would need to cover | Documented decision | Other alternatives remain open |

The argument column is the one most evidence indexes omit. Without it, the index is a list of artifacts. With it, each row is a small argument: here is the claim, here is the evidence, here is the reason the evidence reaches the claim, here is where it stops. That's the structure the defense is built from.

The status vocabulary distinguishes different kinds of epistemic standing. Demonstrated in candidate means shown working in the tagged submission. Inspected in code or design means verified by reading the artifact, not by running it. Executed fixture means the check was run and actual outputs were preserved. Observed with people means seen in a participant session following course procedures. Documented decision means a recorded choice with reasons — not a behavior claim. Not yet established means no evidence yet, with a named next step.

"Not yet established" is appropriate for untested claims. It is not appropriate when a check has already produced a result that contradicts the claim. In that case, the evidence column contains the result, the remaining limit column names the implication, and the claim may need to be narrowed.

<!-- → [DIAGRAM: One claim box at top. Four evidence boxes beneath it, each connected to the claim through a small labeled argument node (the "because" statement). One evidence box drawn in outline only, labeled "evidence without argument — artifact present, evidentiary role unstated." Separate reviewer box connected to the claim by a dashed arrow labeled "defeater: reviewer selects failure path." Limitation box hanging from the claim. Caption: Evidence supports a claim only through a stated argument. The reviewer's job is to find the defeater — the condition under which the claim fails.] -->

---

## The Consequential Decision Record

Show one consequential proposal and its disposition. Not a minor stylistic choice — a decision where a different choice would have changed the architecture, the behavior, or the honesty of a claim.

The disposition record borrows its structure from architecture decision records:

```
Title:
Date:
Status: proposed / accepted / changed / rejected / deferred
Context: what was proposed and why it came up
Decision:
Reason: (cite ledger IDs, criteria, or contract lines)
What I inspected before deciding:
Consequences: what this makes easier, harder, or impossible
Evidence that would reopen it:
```

The requirement is one consequential decision, fully documented. The disposition is whatever it actually was — accepted, changed, rejected, deferred. All four are equally valid answers. The quality being assessed is the reasoning and the inspection that preceded the decision, not the direction of the decision itself.

If you accepted a proposal, state what you inspected before accepting it. If you rejected one, state the requirement or constraint the rejection cited. If the same proposal came back five times in slightly different forms and you rejected it each time, that's a supervision finding worth recording: either the proposal had merit you weren't engaging with, or you had a constraint you weren't articulating clearly enough for the model to work within.

Rejecting every suggestion is no better than accepting every suggestion. Both are calibration failures. Over the course of a project, the accept/reject pattern should track the quality of what was proposed.

Note separately whether the rationale was recorded during the work or reconstructed for the defense. Both are legitimate. They're different kinds of evidence.

---

## Rehearsal

Use Claude to generate rehearsal questions. Give it the demonstration claim and the evidence index — an index with thin entries will produce thin questions. Ask it to cover alternatives, boundaries, failure behavior, accepted proposals, rejected proposals, and conclusions the evidence doesn't support. Ask it to rank the questions from hardest to easiest to answer from the evidence.

```
Below are a demonstration claim and evidence index for a student prototype.
Write ten questions a skeptical reviewer would ask, covering alternatives,
boundaries, failure behavior, accepted changes, rejected changes,
and conclusions the evidence doesn't support.
For each, name the index row or artifact that could answer it,
or say that none can.
Rank the questions from hardest to easiest to answer from the evidence.
Do not answer them, invent reviewer feedback, or mark the work approved.
```

Answer each question yourself before asking for a suggested answer. Answer from the evidence index, not from memory of what the prototype does. The discipline of formulating an answer before seeing one matters: it's the practice that builds the judgment that the oral defense is assessing.

After you've written an answer, ask Claude to find which parts lack evidence — but present your answer as a draft someone else wrote, not as your own. The sycophancy finding from Chapter 2 applies here: Claude will give more critical feedback on work it doesn't know you produced.

```
Below is a question and a draft answer written by a student,
followed by their evidence index.
For each claim in the answer, name the index row that supports it.
List any claim that no row supports.
Do not rewrite the answer.
```

Then rehearse with a peer. Let the peer choose which path or evidence item to inspect — this is the defeater search. A reviewer who picks the path you chose to show finds a demonstration. A reviewer who picks the path you didn't demonstrate is the actual test of whether the evidence packet can answer questions the student didn't stage for.

If no peer is available, label the session self-review and retain peer review as pending. Claude is not a substitute participant whose feedback can be reported as a human review.

Both participants in a peer rehearsal are learning. The reviewer practicing applying criteria to someone else's work is doing the same judgment-building that the oral defense is designed to verify.

---

## Partial Success and the Limits of "Not Yet Established"

Suppose the card implementation preserves the source and text hierarchy but stretches the action button beyond its design specification. The button-width mismatch is real, documented in the fidelity review, and visible in a direct comparison against the specimen.

An inadequate response says "mostly correct except for a small detail." That hides the standard, the magnitude, and the decision.

A complete response identifies the mismatch specifically, shows the reference and the render, names the applicable criterion, states the consequence for the journey (does it block the task?), and identifies whether the milestone rules permit deferral or require repair.

You can recommend accepting the limitation. The blocking criteria declared before the defense determine whether that's permissible — which is why they had to be declared before the defense.

"Not yet established" is appropriate for untested claims. It is not appropriate for defects, which are a different category. When a check has produced a result that contradicts the claim, the honest label is "contradicted" or "failed" — and the response is to preserve the result, narrow the claim to what the evidence supports, or fix the defect before the defense.

Four gap categories, distinguished:

Missing evidence means run or obtain the check. Missing design decision means make and document the decision. Known defect or contradictory evidence means preserve the result, repair or narrow the claim. Accepted scope limit means explain the boundary and its consequence for the journey.

If the no-source path fails during the live demonstration, preserve the failure. Do not switch to a version where it works and report the original run as successful. A labeled backup recording can provide evidence of an earlier run alongside the live failure. Both belong in the evidence packet, attributed to their respective candidates and conditions.

---

## What Would Change My Mind

The chapter treats the oral defense as a Lane 1 secure assessment: Claude helps you prepare, but you answer for yourself. The research supports oral assessment as a valid format for verifying student understanding, with appropriate design. What the research doesn't establish is that this specific format — Claude-assisted preparation followed by peer rehearsal followed by a live demonstration — improves learning outcomes over alternatives. If a controlled study compared this format against a traditional written portfolio defense and found no difference in what students could demonstrate, that would be worth knowing. The chapter's claim is about validity of the format, not efficacy compared with alternatives.

## Still Puzzling

The demonstration card requires reporting how the demonstrated path was chosen — reviewer-selected or presenter-selected. Reviewer-selected is clearly the stronger evidentiary standard, because it tests whether the system works on paths the student didn't stage. But a reviewer who selects a path that wasn't implemented yet isn't testing the submitted candidate — they're exposing a scope gap. The right rule is probably that the reviewer selects among the states the task contract specifies should exist, but not outside them. Working out where that boundary falls in practice is something the course rubric needs to specify, and this chapter doesn't quite do it.

---

## Practice

1. Take a broad claim about your prototype ("the assistant helps students find better resources") and decompose it into three lower claims, each specific enough to demonstrate with an observable outcome.
2. Write the demonstration card for your midterm. Fill in all eight fields. If any field reveals something you don't yet know (the rehearsal history, the commit hash), name what you need to establish it.
3. For one claim in your evidence index, add the argument column: the specific reason this evidence supports this claim. Then identify the limit — what the evidence doesn't establish about the claim.
4. Identify the evidence status for each row in your index using the status vocabulary: demonstrated in candidate, inspected in code, executed fixture, documented decision, or not yet established.
5. Write the disposition record for one consequential proposal. Fill all eight fields. Note whether the rationale was recorded during the work or reconstructed for the defense.
6. Distinguish the inspection you performed before deciding from the reasons you gave. If you can't articulate what you inspected, that's the gap.
7. Generate ten rehearsal questions using the prompt from this chapter. Rank them by difficulty. Answer the three hardest in writing, from the evidence index, before looking at suggested answers.
8. Present one answer to a peer as a draft someone else wrote. Ask the peer where the answer's claims aren't supported by the index.
9. Record one demonstration run that fails. Preserve the failure — the candidate, the starting state, the observed result, the expected result. Do not switch versions.
10. For the button-width mismatch or an equivalent defect in your project: identify the applicable criterion, the observed deviation, the consequence for the journey, and whether your blocking criteria permit deferral.
11. Distinguish missing evidence, a missing design decision, a known defect, and an accepted scope limit for four gaps in your current submission. Each requires a different next action.
12. Ask a peer to choose which path or evidence item to inspect during rehearsal. Record what they chose and what the inspection found.
13. Add the argument column to one row of your evidence index and read it aloud to the peer. Ask whether the argument actually connects the evidence to the claim, or whether it restates the claim.
14. Identify one dimension in which your demonstration could misrepresent the system — mode, timing, or path selection — and state it explicitly on the demonstration card.
15. Write the A3 evidence packet summary: candidate identifier, bounded claim, acceptance criteria, evidence index (with argument column), consequential decision record, actual run results including failures, and unresolved gaps with named next steps.
