# Chapter 10 — Conducting AI Evaluation and Human Usability Inquiry
*Match each claim to a check capable of challenging it — then check whether the checker works.*

Here is a test that passes and tells you nothing.

An automated check confirms that the source identifier field is populated. The source identifier exists. The field is not empty. The check passes.

The source is about a completely different topic.

This is not a contrived failure. It's the normal failure mode of a test that measures the wrong property. The check was designed to verify that a citation exists, and it verified that a citation exists. Whether the citation supports the claim the interface makes about it is a different question, and that question requires a different kind of evidence — someone needs to read the source and check whether it says what the interface says it says.

Evaluation fails the same way interfaces fail: by appearing to verify something it isn't actually checking. A test can pass while inspecting the wrong property. A person can complete a task while misunderstanding what the system was doing. A model can produce a plausible critique without observing either event. The discipline of evaluation is matching each claim to the kind of evidence that can actually challenge it — and then verifying that the evidence collection method works.

---

## Design the Evaluation Before Requesting Tests

The most common evaluation mistake is starting with the tool. "Let's ask Claude to generate tests." Tests for what? Checking which properties? Using which success criteria? Treating which failures as blocking?

Start with the question, not the tool.

For each claim the system makes or behavior it's supposed to produce, ask: what kind of evidence can actually challenge this? Then ask: what is the meaningful failure case that would show this check is doing something real?

Some claims can be verified by checking system state. "Did cancellation prevent the action from executing?" is answered by comparing the mock outbox state before and after — but with an important nuance: an unchanged outbox after a failed send is not the same as an unchanged outbox after a successful cancellation. To distinguish them, you need to confirm that the action successfully reaches the outbox when cancellation is absent, and that the same action does not reach it when cancellation takes effect before execution. Starting state and event order both belong in the record.

Some claims require judgment about content. "Does the source support the claim the interface makes about it?" requires someone to read the source and read the claim and evaluate whether one actually supports the other. A field check, a model-generated assessment, and a citation existence check are three different things that all look similar in a test report. Only the second one — actual content judgment — answers the question.

Some claims require observing people. "Can participants explain what will happen before approving an action?" requires asking actual participants, not generating simulated responses, and recording what they actually say rather than what you expected them to say.

<!-- → [TABLE: Four-row table. Columns: Claim, Suitable evidence, Meaningful failure case, Insufficient substitute. Rows: Cancellation prevented sending (outbox state, with baseline established — outbox unchanged because sender was broken, not because cancellation worked — agent says it canceled), Source supports the claim (inspector reads source and claim, evaluates support — source exists but covers different topic — source identifier field is non-empty), Person understands approval (actual participant response before acting — participant clicks approve while misunderstanding what it authorizes — generated persona response), Keyboard users can complete the flow (runtime keyboard inspection on actual implementation — focus trap at the approval modal — screenshot of the interface looks orderly). Caption: The meaningful failure case is what makes the check real. A check with no failure case is not checking anything.] -->

---

## Building the Evaluation Board

The evaluation board is a table whose rows are situations and whose columns are the expected status, the source or reason for that expectation, the allowed action, and the forbidden behavior.

Before asking Claude to generate tests from the board, read it back through MCP — the same two-stage read-back from Chapter 5. Confirm that the retrieved rows match the intended board. Missing tests could reflect missing context in what Claude received rather than poor test generation. Coverage runs in both directions: every consequential requirement should have a suitable check, and every proposed test should trace back to a specific requirement.

The coverage question is not "does every row have a test?" Some requirements span multiple rows. Some rows provide context that informs other tests. The question is whether every consequential failure mode — every case where the system could do something harmful or misleading — has a check capable of detecting it.

When asking Claude to convert the board to candidate tests:

```
Convert this evaluation board into candidate tests.
Map every test to a specific requirement or transition.
State what each test actually inspects.
Identify requirements that need human observation or content judgment
rather than automated checking.
Do not claim tests passed unless you executed them.
Do not invent participant findings.
```

Then inspect the result. A large test count doesn't establish meaningful coverage. Inspect whether the tests would catch the meaningful failures — not just whether they would pass on a well-behaved implementation.

---

## Evaluating the Evaluator

A checker that passes on bad output and rejects good output is worse than no checker, because it inverts the evidence. The false-acceptance fixture and the false-rejection fixture are how you find out which kind of checker you have.

Build a small reference set with five categories:

Clearly valid outputs — the check should accept these. Clearly invalid outputs — the check should reject them. Valid paraphrases and alternative structures that express the same requirement in different words — the check should accept these. Superficially compliant but substantively wrong outputs — outputs that satisfy the literal check but violate the underlying requirement. Ambiguous cases where the right answer is genuinely unclear.

For a checker that returns accept or reject, the calibration matrix has four cells: correct acceptance (valid accepted), false rejection (valid rejected), false acceptance (invalid accepted), correct rejection (invalid rejected). Keep ambiguous cases separate rather than forcing a judgment where none is defensible.

The source-exists check that passes on an irrelevant source is a false acceptance. A paraphrase check that rejects a valid response phrased differently from the expected wording is a false rejection. Both are calibration failures. The difference between them is which direction the error runs.

For Claude-based grading, document the rubric, the supplied evidence, the model version, and the prompt. Research on LLM judges has identified position bias (the judge favors responses presented first), verbosity bias (the judge favors longer responses), and self-enhancement bias (a model tends to favor its own outputs). Run the critique twice in opposite presentation orders for any comparison. A preference that flips with the order is an artifact of the judge, not a finding about the outputs.

Keep some challenge cases out of evaluator development, then check them after revisions. Passing the examples used to fix a checker is weak evidence. Handling additional cases is stronger.

<!-- → [TABLE: Calibration matrix with reference set categories. Columns: Reference judgment, Checker accepts, Checker rejects. Rows: Clearly valid (correct acceptance — false rejection), Clearly invalid (false acceptance — correct rejection), Valid paraphrase (correct acceptance — false rejection: checker measures exact wording, not the requirement), Superficially compliant but wrong (false acceptance: biggest risk — correct rejection), Ambiguous (record separately; do not force a label). Caption: Build the reference set before testing the checker. False acceptances and false rejections are both calibration failures; they just run in opposite directions.] -->

---

## Repeated Trials for Variable Behavior

An automated check on a deterministic system tells you what the system does in the tested condition. An automated check on a system with AI-generated components tells you what the system did that time.

For checks involving generated answers or agent decisions, repeat selected consequential cases under recorded conditions. The cases worth repeating are the ones where the agent makes a judgment — classifying evidence, generating an explanation, deciding whether to proceed. Preserve all attempts. Do not rerun until a favorable result appears and report only the favorable result.

A single successful run and consistent success across ten runs are different claims. They answer different questions, particularly for a system that will operate on behalf of people who can't re-run the experiment when it fails.

Distinguish three evaluation outcomes: a failed check means the observed behavior violated the criterion; an unexecuted check means no result exists; an inconclusive check means the available evidence can't determine whether the criterion is met. Don't average a failed approval boundary into an overall score dominated by cosmetic passes. Mandatory criteria require separate handling from graded quality dimensions.

---

## Conducting Human Usability Inquiry

Use voluntary participation and the instructor's approved procedures. Explain the task, what you will record, and the participant's ability to stop. Avoid collecting unnecessary personal information. A classroom script doesn't replace institutional requirements.

The sample questions in the draft do different jobs, and naming the distinction helps:

*Task observation* watches what participants do with minimal intervention: "Find a resource you would use for this question. Show me what you would do next." The moderator observes without coaching. This establishes what participants actually do, not what they can explain when asked.

*Comprehension inquiry* asks what participants understood and expected: "Before you select an option here, tell me what you think will happen." This establishes how participants understand the interface at specific moments. The interruption itself may encourage deliberation that wouldn't otherwise occur.

Both types are useful. The distinction matters because "participants successfully completed the approval step" means something different depending on whether they did it spontaneously or after being prompted to think aloud about it. Record when the moderator intervened. Completion after assistance should remain distinguishable from unassisted completion.

Task questions should be goal-oriented without revealing the solution: "Find something that would help you understand how to approach this assignment" not "Use the recommendation feature to find a relevant source." The first tests whether the system supports the task; the second tests whether participants can follow an instruction.

Also record who participated and why they're relevant to the target audience. Classmates who helped design the system may provide useful feedback while being poor substitutes for unfamiliar intended users. Finding a problem in a small session justifies investigation. Not observing it in a small session doesn't establish its absence.

---

## Separating Observations, Interpretations, and Proposed Repairs

The finding ledger should record observations and interpretations as distinct entries, because the same observation can support more than one interpretation, and the right repair depends on which interpretation is correct.

An illustrative record structure (this is a format, not reported findings):

```
Observation: participant selects the approval button, then immediately asks
             whether anything was sent
Interpretation: execution status after approval may be unclear
Alternative explanation: participant may understand approval but expect
                         visible confirmation before execution completes
Proposed revision: add a distinct "approved, executing" state between
                   "approved" and "completed"
Follow-up check: observe behavior after seeing the new state;
                 ask participant what they expect the current status to be
```

Recording the alternative explanation is what keeps the repair specific. If the problem is unclear execution status, the fix is a status indicator. If the problem is expected confirmation before execution, the fix is different — the interface should confirm receipt of approval separately from reporting completion. Jumping from observation to repair without naming the alternative interpretations risks solving the wrong problem.

---

## Prioritizing Findings

When findings disagree — a behavior failure, a participant's preference, and a model's aesthetic critique pointing in different directions — they don't need to receive equal weight. The evaluation record should support a prioritization that explains why one finding warrants immediate repair and another warrants monitoring.

Factors worth recording for each finding: the affected task (which part of the critical journey does this impact?), the consequence (what happens when this failure occurs?), the evidence strength (was this observed once, observed repeatedly, inferred from an automated check, or produced by a model critique?), and the uncertainty about frequency (did you observe it in one of five participants or in all five?).

One verified failed approval boundary — the action executed when it shouldn't have — justifies immediate repair regardless of how rare it appeared in testing. A model's suggestion to move a button 8 pixels to the right needs a different justification. The prioritization decision belongs to the designer, based on the consequence and the evidence — not to whichever finding happened to appear first in the ledger.

For accessibility findings, name the specific criterion from WCAG 2.2, the tested environment, and the method used. A screenshot, an automated scan, and a generated critique each cover different portions of the accessibility requirements. A runtime keyboard traversal covers things none of the other three can detect. No single method is sufficient.

---

## What Would Change My Mind

The chapter treats source-support verification as requiring human judgment — someone needs to read the source and evaluate whether it actually supports the claim. This is currently correct for the resource assistant's domain. If the system were redesigned to display specific passages from sources rather than model-generated relevance explanations, a smaller portion of the verification would require human judgment and a larger portion could be verified by checking whether the displayed passage appears in the source. That would change the evaluation design without changing the underlying principle: match the check to the property being evaluated.

## Still Puzzling

The calibration exercise for a checker is itself subject to the same problem: the reference set that decides whether the checker is well-calibrated is built by someone, and that person's judgment about what counts as clearly valid, clearly invalid, and genuinely ambiguous is itself a judgment call. For clear cases, this isn't a problem. For the cases that matter most — the superficially compliant but substantively wrong outputs — reasonable people sometimes disagree about whether an output satisfies a requirement. The chapter recommends having a second reviewer inspect consequential or disputed labels, but doesn't specify when disagreement between reviewers should be resolved by discussion versus treated as evidence that the requirement itself is ambiguous. That question probably requires the instructor to specify the arbitration process.

---

## Practice

1. Take one claim about your system and identify: what kind of evidence can challenge it, what the meaningful failure case is, and what would be an insufficient substitute.
2. Build the causal test for cancellation: establish that valid actions reach the outbox when cancellation is absent, then confirm the same action does not reach it when cancellation fires first. Record starting state and event order.
3. Build the irrelevant-citation check using the three cases from Chapter 9: source exists but is irrelevant, source supports part of the claim, source contradicts the claim. Write the specific diagnostic each should produce.
4. Write the evaluation board for your critical journey. Four columns: expected status, source or reason, allowed action, forbidden behavior.
5. Ask Claude to convert the board to candidate tests using the prompt from this chapter. Before reviewing the tests, complete the two-stage read-back to confirm Claude received the intended board.
6. Build the false-acceptance fixture: an output that satisfies the literal check but violates the underlying requirement. Confirm the checker accepts it. Document what property the check is actually measuring.
7. Build the false-rejection fixture: a valid output that the checker rejects because it differs from the expected wording or format. Confirm the checker rejects it. Document the gap between the check and the requirement.
8. For one AI-generated evaluation in your project, run the critique twice with the concepts in opposite order. Record whether the critique changes. If it does, note the finding as a potential order artifact.
9. Select two consequential scenarios in your agent system and run each three times under recorded conditions. Report all outcomes — not just the favorable ones.
10. Write task-observation instructions for one part of your critical journey: goal-oriented, neutral, not revealing the expected solution.
11. Write comprehension-inquiry prompts for the approval step: asking participants to describe what will happen before they take action.
12. Record one observation from your evaluation using the four-layer structure: observation, interpretation, alternative explanation, proposed revision. Confirm the proposed revision addresses the interpretation, not just the observation.
13. Prioritize three findings from your evaluation by consequence and evidence strength. Name the factor that places each one in its priority position.
14. For one accessibility check, name the specific WCAG 2.2 criterion, the testing method (screenshot, automated scan, generated critique, or runtime inspection), and what the method cannot detect.
15. For the A5 submission: document the evaluation plan, evaluator challenge cases with calibration matrix, run results with all attempts preserved, participant and session context, observation ledger with interpretations separated, and prioritized revisions with follow-up checks. Mark unexecuted checks and pending sessions as explicitly pending.
