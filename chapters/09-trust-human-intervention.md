# Chapter 9 — Designing Trust and Human Intervention in Agentic AI
*How to make uncertainty inspectable, bind approval to the action actually reviewed, and keep recovery honest when reversal isn't possible.*

Here is a trust problem disguised as a design question.

A student asks the resource assistant a question. The assistant finds something in the catalog that could be relevant. It generates an explanation of why the resource matches. The explanation is fluent. It sounds authoritative. The student reads it and opens the source.

The source doesn't support the relevance claim.

The citation exists. The link works. The source is in the approved catalog. The explanation was generated from the question and the resource's description — it was not derived from the source's actual content. The mismatch between the explanation and the source is invisible unless the student reads far enough into the source to discover it, and most students will stop earlier, confident that the confident explanation has already done the verification work.

This is the trust problem: the interface has the form of transparency — it shows a source, it provides an explanation — without the substance. The student cannot tell, from looking at the interface, whether the explanation was derived from the source or generated around it.

Trust in an agentic system is not a visual style. It is not a confidence bar or a certainty score or a design that feels reassuring. The practical question is whether the person can inspect the actual basis of a response, understand what action is actually being proposed, and intervene before an unacceptable consequence occurs.

---

## Four Response Types, Three Dimensions

The chapter's four response types — supported recommendation, partial evidence, no supported answer, approval required — are the right starting point. But they mix two dimensions that need to stay separate, because they can coexist in combinations the original list doesn't capture.

The first dimension is evidential: what does the system actually know about this question and this resource? Supported means a source passage can be directly linked to the claim the response makes. Partial means some part of the claim is supported and some part is not. No supported answer means the catalog was checked and no match was found.

The second dimension is permission: what action is proposed, and who has authorized it? Not required means the response can be shown without further approval. Pending means an action is awaiting authorization. Approved means authorization has been granted for a specific revision. Invalidated means a change has occurred since authorization was granted and the authorization no longer applies.

And the third dimension, which most approval designs omit entirely, is execution: did the proposed action happen? Not started. In progress. Completed. Failed. Outcome unknown — which is different from failed, and matters more than it looks.

A supported recommendation might still require permission to act on. An unsupported answer might still legitimately lead to an approved request for human help. Approval might be granted for revision 1 of a draft and invalidated by a change to revision 2, even when both revisions seem similar. Keep the dimensions visible rather than collapsing them into a single status label.

<!-- → [TABLE: Three-section table. Section 1 Evidence: Supported (source passage directly linked to the claim), Partial (some claims supported, others unresolved), No supported answer (catalog checked, no match found). Section 2 Permission: Not required, Pending, Approved for revision [n], Invalidated (revision changed since approval). Section 3 Execution: Not started, In progress, Completed, Failed, Outcome unknown (acknowledgment not received). Caption: These three dimensions can coexist in combinations. A supported recommendation requiring permission that was granted for an earlier revision is a real state the interface must handle. Collapsing them into one label hides which dimension changed.] -->

---

## Making Uncertainty Specific

The editorial reform this chapter asks for is not replacing vague confidence labels with more precise vague confidence labels. It is identifying exactly which claim is unsupported and exactly what would resolve it.

A resource can be confirmed to exist in the catalog while its suitability for a specific question remains entirely unresolved. Those are different conclusions, and the interface should say which one it's making.

A useful display for a partial-evidence state doesn't say "Confidence: 72%" or "Possibly relevant." It says: "This source addresses the general topic of [X]. Whether it covers [the specific aspect of the question] is not established — the description does not address that part. You can inspect the source directly to check."

For each recommendation, the system should be able to distinguish: what is the claim being made? What source or passage supports it? What part of the claim has no support? What action could resolve the uncertainty?

The irrelevant-citation fixture is worth expanding into three cases. First: a source that exists and is in the approved catalog, but whose content is not relevant to the claim the explanation makes. Second: a source that supports part of the claim but not all of it. Third: a source whose content contradicts the claim. Each of these looks like a citation. Each produces a different diagnosis and a different next action. Building all three reveals whether your evidence-checking logic distinguishes them — or whether it stops after confirming the source exists.

---

## Binding Approval to the Reviewed Action

The approval problem is an ordering problem. If a draft is approved in one state and executed in a different state, the executed action is not the one that was authorized.

This is not a subtle edge case. It's the normal failure mode of any approval system that compares revision numbers instead of content, or that stores approval status in a field the agent can write to, or that executes without verifying that the action matches the authorization.

A secure approval record contains at minimum: the action identifier, the revision number, the destination, the content as approved, and the approval status — and crucially, the approved content must be an immutable snapshot, not a reference to the current draft that could have changed since approval was granted.

```json
{
  "action_id": "contact-instructor-01",
  "revision": 2,
  "destination": "local-mock-outbox",
  "recipient": "course-instructor",
  "content": "I am looking for a resource that covers X in the context of Y. Could you recommend something from the approved catalog?",
  "content_hash": "sha256:...",
  "approved_at": "2026-10-14T11:32:00Z",
  "approved_revision": 2,
  "approval": "pending"
}
```

The executor contract: execute only when the revision of the action matches the approved revision, the content matches the approved content hash, the action has not been cancelled, and the action has not already been completed.

An agent-written `"approval": "approved"` field must not grant permission. The permission check is performed by the executor against the authorization record, not by trusting the agent's description of its own approval status.

Now test the subtle defect: change the content of the draft without incrementing the revision number. An executor that compares only revision numbers will miss this. The content hash catches it. Build the test explicitly.

The stale-approval scenario: start with revision 1, approve it, change the content and produce revision 2, attempt execution with the revision 1 approval. Five things should happen: the action is not executed, the interface identifies that the draft changed, the new exact draft is available for review, the mock outbox remains unchanged, and new approval is required for revision 2. These are expectations to verify, not results already obtained. If the outbox changes, a reassuring "content changed" warning screen doesn't rescue the failed boundary.

<!-- → [TABLE: Stale approval test scenarios. Columns: Scenario, Expected result, How to verify. Rows: Content changes without revision increment (action not executed — content hash mismatch detected, executor logs mismatch), Revision changes (action not executed — revision mismatch detected, new approval required), Cancellation before execution (no outbox change — outbox queried before and after, entry absent), Cancellation after execution (completion remains recorded — outbox entry present, cancellation logged as received-too-late), Duplicate request for same action (one outbox entry — outbox queried after both requests), Lost acknowledgment retry (existing result recognized, no second entry — request ID checked before executing). Caption: Each row is a specific test with a verifiable expected result. "Reassuring screen" is not a verification method.] -->

---

## Outcome Unknown Is a Real State

Tool failure is too broad a category for recovery design. A request can succeed — the action can take effect — even when the acknowledgment never reaches the caller.

Suppose the mock outbox appends the message and then returns an error to the caller instead of a success confirmation. From the caller's perspective, the action failed. From the outbox's perspective, the action completed. The interface now has a choice: report failure (which is false), report success (which it didn't confirm), or report that the outcome is not yet established.

The honest behavior is outcome unknown, pending a state check. Not "something went wrong, please try again" — which may produce a duplicate. Not "your message was sent" — which the caller cannot confirm. The interface shows what it knows: the request was submitted, no confirmation was received, the outbox has not been verified. It offers a state check, not a retry.

This distinction becomes critical when the action has side effects that can't be undone. Telling a student to try again when the message may have already been sent is not recovery design — it's a prompt to create a duplicate with no mechanism to prevent it.

To test this: extend the local mock with a scenario where it appends the message and then returns an error. Verify that the interface reports outcome unknown rather than success or failure. Then query the outbox directly and verify that the entry is present. Both records — the caller's uncertainty and the outbox's state — belong in the test report.

---

## Correction, Cancellation, and the Limits of Undo

Three recovery actions that are frequently conflated:

Correction changes a draft before execution. It's available while the action is in the preparation and approval states. Correcting a draft after it's been sent is not correction — it's a different kind of action entirely.

Cancellation prevents an action that has not yet occurred. It's only available before execution begins. If execution is already in progress or completed, cancellation cannot undo it. The interface must say so rather than offering a cancellation button that will silently fail.

Undo reverses a completed action — but only when reversal is actually possible. Removing an entry from a local mock outbox reverses local state. It does not reverse a real delivered message, and the interface must not present it that way. If a message has already left the system, the interface should say what happened and offer an honest next step — not promise reversal because that's reassuring.

For a portfolio, the equivalent: editing an unpublished case study before it's been shared is correction. Issuing a correction to a claim after someone has received the published version is a different action, with a different record. The interface should preserve an accurate account of the change, not just replace the original.

For the simulator, test both orderings of cancellation and execution: cancellation arrives first, execution arrives first. The interface must report the resulting state accurately in both cases. "Your cancellation was received after the action completed" is an honest message. Displaying a success screen for a cancellation that arrived too late is not.

---

## Keeping Uncertainty Through Handoffs

The approval workflow has a version of the fluency trap from Chapter 1: if the lookup finds a partial result, and the recommendation builder receives only the resource identifier without the unresolved claims, the builder may generate a confident explanation that silently promotes partial evidence to certain support.

The handoff contract from Chapter 7 is the mechanism: include the unresolved claims alongside the payload, and the acceptance condition must check that the receiving component doesn't promote the evidence beyond what was established.

A polished explanation is not additional evidence. If the lookup says "relevance to the specific question is unresolved," the recommendation that arrives at the interface must say the same thing in its evidence status. The generation of a fluent sentence does not resolve the underlying uncertainty.

---

## Conducting the Failure Scenarios

Ask Claude to work only against the local mock:

```
Inspect the state and approval contracts.
Generate tests for: cancel-before-execution, cancel-after-execution,
changed draft after approval with content hash mismatch,
changed revision number, duplicate request for the same action,
missing source in catalog, tool failure with no acknowledgment,
and outcome-unknown state.
Implement only the approved local simulator behavior.
Do not connect external services.
For each test, report: starting state, event sequence,
expected result, actual result, and final outbox state.
Preserve these records separately from your narration.
```

Review the actual outbox state after each test, independently of the agent's narration. The agent can say the outbox is unchanged while the outbox has changed. The test report is the outbox query result, not the agent's description of it. Preserve both — the narration and the actual state — as separate records.

---

## What the Approval Gate Cannot Establish

A technically functioning approval gate establishes that the permission boundary works under tested conditions. It does not establish that the person understood what they were approving.

Research on AI-assisted decision-making is consistent on this point: reducing over-reliance on AI recommendations requires more than showing a confirmation screen. The design difference that matters is whether the interface supports deliberation — whether it gives the person enough specific information about what changed, what is proposed, and what the consequences are to make an actual decision rather than a habitual confirmation.

For the human evaluation in Chapter 10, the questions worth asking participants are: Can they identify the recipient and the information that would leave the system? Can they identify what changed since they last reviewed the draft? Do they know what cancellation can still prevent? Do they understand that an "outcome unknown" state requires a state check rather than a retry?

Measuring whether participants notice a change to the draft before re-approving is a more useful indicator of deliberation than measuring approval completion time.

---

## What Would Change My Mind

The chapter treats the approval invalidation problem as primarily a technical enforcement problem — the executor must check content hashes, not just revision numbers. This is correct given the threat model of an agent that can write to the approval record. But in a system where the approval record is managed by a trustworthy server that the agent cannot write to, and where all changes go through a controlled API, the enforcement model can be simpler. The content hash approach is the right default for a system where the trust boundary is uncertain; it may be overengineered for a system where the trust boundary is well-controlled. Knowing which you have is the prerequisite for knowing how much enforcement the approval gate needs.

## Still Puzzling

The "outcome unknown" state is honest but frustrating for the person experiencing it. "We don't know if your message was sent" is accurate and also a bad user experience. The honest recovery from outcome unknown — check the outbox directly and report what you find — requires the interface to have read access to the outbox to provide that report. Whether that access should exist, and who should be able to initiate the state check, is a design decision the chapter doesn't make for you. It probably depends on the sensitivity of what the outbox contains, who is authorized to see it, and how quickly the uncertainty can be resolved. The chapter names the state but doesn't specify the recovery workflow, which remains open.

---

## Practice

1. Write the three-part evidence display for a partial-evidence recommendation: what is supported, what is unresolved, and what would resolve the unresolved part.
2. Build the three irrelevant-citation fixtures: source exists but is irrelevant, source supports part of the claim, source contradicts the claim. Write the distinct diagnosis each should produce.
3. Replace one vague confidence label in your current design with a specific statement of what is supported and what isn't. The statement must identify a specific claim, not just a confidence level.
4. Separate the evidential status and permission status for one response in your design. Name a case where they differ from what a single combined status label would show.
5. Write the approval record for one action using the structure from this chapter: action identifier, revision, destination, recipient, content, content hash, approved revision, and approval status. Keep the approved content as an immutable snapshot.
6. Define the executor contract: under what conditions exactly will the action execute? Name each condition. Confirm that agent-written approval status is not one of them.
7. Test the content-without-revision-change scenario: change the draft content without incrementing the revision number. What does the executor do? What should it do?
8. Build the outcome-unknown scenario in your mock: the outbox appends the entry and returns an error. Verify that the interface reports outcome unknown rather than success or failure. Then query the outbox directly and verify the entry is present. Preserve both records.
9. Test cancellation in both orderings: cancellation before execution, and cancellation after execution has completed. What does the interface report in each case? What is the actual outbox state in each case?
10. Test duplicate request behavior: submit the same action request twice. How many outbox entries result? Is the second request recognized as a repeat or executed independently?
11. Identify one handoff in your architecture where unresolved claims from an earlier stage could be silently promoted to certain claims by the receiving component. Name the specific claim and the specific promotion that would occur without the unresolved-claims field.
12. Write the honest recovery message for each of three failure states: action cancelled before execution, action completed before cancellation arrived, outcome unknown pending state check. Confirm each message says what actually happened, not what would be reassuring.
13. Separate the technical verification questions (does the approval gate enforce the boundary?) from the human evaluation questions (does the person understand what they're approving?). For each, identify what evidence would answer it.
14. For one accessibility annotation in your approval flow, identify the WCAG criterion it addresses and the later check that would verify it in the implemented interface. Distinguish annotation (intent) from verification (evidence).
15. For the A4 submission: document each executed scenario with its starting state, event sequence, expected result, actual result, and final outbox state. Mark unexecuted scenarios as pending. Keep technical boundary results and human comprehension findings as separate records.
