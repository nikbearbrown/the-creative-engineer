# Chapter 9 — Designing trust and human intervention in agentic AI

[Contents](README.md) · [Previous](08-midterm-defense.md) · [Next](10-evaluation-usability.md)

*Expose uncertainty, bind approval to an action, and make recovery honest.*

> Rough draft for author review. The messaging example uses a local mock sender, not real email.

## The result

Design and test four kinds of response: supported answer or recommendation, partial evidence, no supported answer, and action requiring approval. Make the transitions and consequences visible.

Trust is not a visual style. In this project, the practical question is whether the person can inspect the basis of a response, understand the proposed action, and intervene before an unacceptable consequence.

The source Figma project designed tutor states for this purpose, but its human-usability protocol had not been run in the inspected record. Use the states as design material, not as proof that students understand them. [Source F03](../research/sources.md).

## Design uncertainty as information

Avoid replacing missing evidence with a vague confidence label. State what is supported, what is missing, and what the person can do.

| State | Information to show | Action to support |
|---|---|---|
| Supported recommendation | Resource, relevance explanation, source | Inspect the source |
| Partial evidence | Supported part and unresolved part | Inspect or refine the question |
| No supported answer | What was searched and what is missing | Revise or seek human help |
| Approval required | Exact proposed action and consequence | Approve, revise, or cancel |

A source link is not sufficient by itself. A citation can exist and still be irrelevant. The playlist's evaluation-board case demonstrates why field checks can miss that problem. [Playlist case V04](../research/playlist-evidence.md).

In Figma, give each state a name and clear text. Do not depend exclusively on color or an icon to distinguish important meanings. Keep the source inspection route available when it matters.

## Bind approval to the reviewed action

For the teaching example, the assistant proposes contacting an instructor. Show the recipient, exact draft, disclosed information, purpose, and what cancellation means.

Use a proposed approval record:

~~~json
{
  "action_id": "example-contact-01",
  "revision": 2,
  "destination": "local-mock-outbox",
  "content": "Illustrative request for a resource recommendation.",
  "approval": "pending"
}
~~~

Approval should apply to the reviewed revision. If the recipient or content changes, the previous approval must not silently authorize the new action. Design the invalidation behavior and ask Claude to implement it in the simulator.

The interface is only one part. The action executor must enforce the boundary too. A disabled button does not protect an unguarded tool call. The permissions exercise distinguishes task requests from enforceable action boundaries. [Source P01](../research/sources.md).

## Separate correction, cancellation, and undo

Correction changes a draft before execution. Cancellation prevents an action that has not yet occurred. Undo reverses a change when reversal is actually possible.

Do not label every recovery button “Undo.” If a message has already left the system and cannot be recalled, the interface should say what happened and offer an honest next step. It must not promise reversal merely because that is reassuring.

For a portfolio, the equivalent distinction is editing an unpublished case study versus correcting a claim after someone has received a published version. The design should preserve an accurate account of the change.

## Conduct failure scenarios

Ask Claude to work only against the local mock:

~~~text
Inspect the state and approval contracts.
Generate tests for cancel, changed draft after approval,
changed recipient, duplicate request, missing source, and tool failure.
Implement only the approved local simulator behavior.
Do not send messages or connect external services.
Report the final mock-outbox state for each executed test.
~~~

Preserve separate records for prompt, attempted action, returned result, and final state. The Computational Skepticism state-check exercise provides the underlying method: inspect the outcome independently of the agent's narration. [Source S01](../research/sources.md).

## Worked example: approval becomes stale

Start with a synthetic draft addressed to the mock destination. Approve revision 1. Change its content and mark the draft revision 2. Attempt execution using the earlier approval.

Expected behavior under this project's contract:

1. The action is not executed.
2. The interface identifies that the draft changed.
3. The new exact draft is available for review.
4. The mock outbox remains unchanged.
5. New approval is required for revision 2.

These are expectations to test, not results already obtained. When you run the exercise, record what actually happened. If the outbox changes, a reassuring warning screen does not rescue the failed boundary.

Next, test cancellation and repeated submission. Define whether repeating an already completed action should be rejected or recognized as the same completed request. Do not add an automatic retry without deciding how duplicate effects are prevented.

## Keep uncertainty through handoffs

If the lookup says relevance is unresolved, the final response must not silently promote it to certainty. Include unresolved claims in the handoff contract. A polished explanation is not additional evidence. [Source C02](../research/sources.md).

[FIGURE: Draft revision, approval, changed-content invalidation, cancellation, and execution into a mock outbox.]

## Practice

1. Write a supported recommendation state.
2. Separate partial evidence from no evidence.
3. Replace a vague confidence claim with an inspectable limitation.
4. Show the exact action on an approval screen.
5. Identify information that would leave the system.
6. Define what invalidates approval.
7. Test cancellation against actual state.
8. Test a repeated action.
9. Distinguish undo from mitigation.
10. Preserve uncertainty in a handoff.
11. Construct an irrelevant-but-existing citation fixture.
12. Explain a failed boundary without blaming the user.

## Submission checkpoint — A4

Submit agent orchestration and recovery design: Figma states, permission and approval contracts, failure scenarios, actual results where run, and unresolved risks. Human usability findings remain pending until people actually participate.

Next: evaluate both the experience and the checks used to judge it.

Source basis: [Chapter 9 research](../research/09-trust-human-intervention.md).
