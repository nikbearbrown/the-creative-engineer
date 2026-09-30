# Chapter 7 — Designing Agentic Systems and Conducting Workflows
*Every arrow in the architecture must have a meaning that can be inspected.*

Here is the architecture that isn't one.

A rectangle labeled "Interface." An arrow. A rectangle labeled "AI." Another arrow. A rectangle labeled "Database." The boxes are named, the arrows are drawn, and the diagram looks like a system. But it answers none of the questions that matter: which tools does the agent have access to? Under whose authority? Using what state? What happens when the lookup returns nothing? What happens when it fails? When does the system stop, and who decides?

A box labeled "AI" is a placeholder for a decision that hasn't been made yet. An arrow between "planner" and "tools" is a promise that hasn't been specified. Every unspecified piece in the architecture is a decision that someone will eventually make — either you, intentionally, or the implementation, by default. The difference between a diagram and an architecture is whether every arrow has a meaning that can be inspected.

This chapter is about earning the right to call it an architecture.

---

## Separate the Participants

The first move is to draw each participant separately in FigJam — and to name what each one is, not what it does.

The person using the interface. The interface itself. The agent operating within it. The resource store the agent can query. The review gate where a human makes a consequential decision. A notification sink, if your project includes an approval step — in this lab, a mock sink, not a real inbox.

These are not the same as the boxes in a system diagram. Each participant has a distinct set of permissions, a distinct kind of state, and a distinct relationship to accountability. The person makes decisions and bears consequences. The interface depicts state and accepts input. The agent takes bounded actions within its permitted scope. The resource store holds content that the agent can read. The review gate is where the agent's output becomes human-authorized output.

For every line connecting participants, name what crosses it. Not "data" — the specific payload, in both directions.

<!-- → [TABLE: Five-row table. Columns: Relationship, Payload, Design question, What the arrow does not establish. Rows: Person → Interface (question and chosen context — what is necessary to collect? — that the agent can use context it wasn't given), Agent → lookup tool (bounded query — which materials may be searched? — that the tool's results are accurate or complete), Tool → Agent (results and source identifiers — what does an empty result mean? — that a result answers the question), Agent → Interface (recommendation or stated limitation — what must remain uncertain? — that the recommendation is correct), Person → Review gate (approval or rejection — what exact action is authorized? — that the downstream system enforces approval). Caption: A read relationship does not imply write permission. A displayed approval button does not establish that the backend enforces approval. Name both what the arrow carries and what it doesn't grant.] -->

---

## Specify States and Transitions

The state table is where the diagram becomes a specification. For every condition the system can be in, you write the current state, the event that triggers a transition, the next state, and the evidence required before the transition is valid.

For the resource assistant:

*Received → Retrieving:* the person submits a query. Evidence required: the query is non-empty, the allowed source set is defined and accessible.

*Retrieving → Source found:* the lookup returns at least one eligible result. Evidence required: a source identifier traceable to the authorized catalog.

*Retrieving → No source:* the lookup completes with zero results and all queried catalogs responded. Evidence required: a completed lookup record with the list of sources checked and a result of none from each.

*Retrieving → Partial results:* the lookup returns results from some catalogs, but at least one catalog failed to respond. This is a distinct state from No source — one means the catalog was checked and found nothing; the other means some part of the catalog wasn't checked. Collapsing them produces the same false claim the chapter on interaction design warned about: "No results" when in fact "Nothing was checked" is the more accurate statement for some of what was searched.

*Retrieving → Failed:* the lookup fails before returning any results. Evidence required: an error outcome, not a generated explanation of what might be there.

*Source found → Completed journey:* the person opens a source. Evidence required: the actual destination, not a predicted one.

*No source → Review required:* the person requests to escalate or contact someone. Evidence required: the exact proposed draft, not a summary of intent.

Two things the state table makes visible that the diagram doesn't. First, the distinction between No source and Partial results — they look the same to a user who receives no useful recommendation, but they require different messages and different next actions. Second, termination: the table needs a maximum action budget, chosen explicitly, and a state for what happens when it's exhausted. That number is a design parameter. It is not a platform default.

<!-- → [DIAGRAM: State transition diagram for the resource assistant. States: Received, Retrieving, Source found, No source, Partial results, Failed, Completed journey, Review required. Transitions labeled with event and evidence required. Partial results has its own branch with a distinct message and a Retry transition. Failed has its own branch with an error record, not a generated explanation. No two terminal states share the same message or the same next action. Caption: The state table enforces the same rule as the interaction design chapter: every branch that terminates needs a distinct message and a distinct next action.] -->

---

## Make Handoffs Explicit

When one component passes output to the next, the handoff should carry three things: the payload, the provenance, and the unresolved claims.

The payload is the data. The provenance is the record of where it came from — which catalog, which version, what timestamp. The unresolved claims are the things that the payload doesn't establish but that a later stage might accidentally treat as if it does.

An illustrative handoff record:

```json
{
  "source": "resource_lookup",
  "destination": "recommendation_builder",
  "payload": { "resource_id": "course-catalog-entry-047" },
  "provenance": {
    "catalog": "authorized-course-catalog",
    "version": "2026-Q3",
    "queried_at": "2026-10-14T09:23:11Z"
  },
  "acceptance_condition": "resource_id exists in the supplied catalog at the stated version",
  "unresolved_claims": [
    "relevance to this specific question has not been judged",
    "the student has not confirmed the resource matches their task"
  ]
}
```

The acceptance condition is what the next stage can check mechanically. An identifier check can confirm the resource exists in the catalog. It cannot confirm the resource answers the question. The unresolved claims field is the explicit record of what the identifier check doesn't establish.

This structure matters because a later stage that receives only the payload — without the unresolved claims — is likely to treat the handoff as more authoritative than it is. A recommendation builder that receives a resource ID may generate a recommendation that sounds confident about relevance it has no basis to claim. The unresolved claims field is how you prevent preparation from becoming judgment through the handoff.

---

## Conduct Implementation from the Board

Give Claude the FigJam architecture and the handoff contracts before asking it to write any code. The prompt structure matters.

```
Review the board and contracts before writing code.
List missing state transitions, permissions, termination rules,
and assumptions that would change behavior if left unresolved.
Then propose a local simulator with read-only fixture lookup.
No network calls or real messages.
Do not fill unresolved product decisions silently — flag them.
```

Resolve the consequential questions. Then permit the bounded implementation. After the implementation runs, ask for a trace that separates four things: the proposed action, the attempted action, the tool result, and the final state. These are different records, and conflating them is where narrated success diverges from actual state change.

Use code as a way to test the design, not as a replacement for it. When implementation exposes an ambiguous transition — the fixture returns a result the state table doesn't have a branch for, or the simulator reaches a state that wasn't named — revise the board and the handoff contract, not just the code. Implementation discrepancies are design findings.

---

## The False-Success Test

The most important test in agentic system design is the one that separates what the agent says happened from what actually happened.

Construct a fixture in which the agent's final message reports success — "I saved the recommendation to your resource list" — but the local saved-resource list remains unchanged. Now you have two records: the transcript, which says the action occurred, and the state, which says it didn't. These are different kinds of evidence, and neither one automatically overrides the other.

The transcript establishes that the agent narrated success. The state establishes whether the expected state change occurred. Keep both. Define acceptance as a concrete predicate: the expected resource identifier appears exactly once in the saved list. Then test a missing entry (the agent said it saved but didn't) and a duplicate entry (the agent saved twice when once was intended). Do not let the same success sentence serve as both the action and its proof.

The portfolio version of this failure is announcing that an evidence link was added while the published page still points nowhere. The link was narrated. The destination doesn't exist. These are different problems with different fixes, and the only way to find the second one is to check the actual destination, not the description of what was done.

This distinction — narrated state versus actual state — is the chapter's central test. An agent that describes its own actions accurately when those actions failed is not a reliable narrator. Verification requires checking the state independently of what the agent reports.

---

## Review the Boundaries

After the simulator runs, check whether the boundaries held.

Missing provenance: does the output carry the source identifiers and catalog version it needs for the handoff to be trustworthy? An identifier without provenance is a claim that can't be verified.

Invalid source identifiers: does the acceptance condition actually reject a resource ID that isn't in the catalog? Test it with a fabricated ID.

Exhausted action budget: what happens when the simulator reaches the maximum step count? Does it halt cleanly, or does it continue past the limit?

Unauthorized writes: did the simulator attempt to write to anything outside the authorized scope? Review the diff, not the agent's description of the diff.

Tool failure: what happens when the catalog lookup throws an exception? Does the system reach the Failed state as designed, or does it silently route to No source, collapsing two distinct conditions into one?

A path validator or a prompt instruction does not create an operating-system sandbox. The permissions of the actual environment need to match the task. If the simulator is running in an environment where it has write access to the notification sink, the instruction "do not send real messages" is a request, not a boundary. Know which category each constraint falls into.

---

## What Would Change My Mind

The state machine approach to agentic system design assumes that the system's behavior can be fully described by a finite set of states and transitions. For the resource assistant, this is approximately true. For a system that takes open-ended actions in a less-bounded environment — an agent that can browse the web, send messages, and modify files — the state space becomes large enough that specifying it in a table is not practical. The design discipline this chapter teaches scales down gracefully to more bounded systems; it scales up in spirit but not in form to more open-ended ones. If you're building a more open-ended agent, the relevant adaptation is to specify the classes of states and the acceptance conditions for each class, rather than enumerating every possible state.

## Still Puzzling

The handoff contract's unresolved-claims field is designed to prevent preparation from becoming judgment through the boundary between components. But the field is only useful if the next component reads it. If the recommendation builder ignores the unresolved claims and generates a confident recommendation anyway, the field's presence in the handoff doesn't protect against the problem it was designed to prevent. The honest answer is that the unresolved-claims field is a design instrument, not an enforcement mechanism — and the acceptance condition is what actually enforces the boundary. Whether the acceptance condition is expressive enough to catch all the cases the unresolved claims name is the question that can't be answered by looking at the handoff contract alone.

---

## Practice

1. Draw your architecture with each participant as a separate named box. Replace any box labeled "AI" or "System" with a description of that participant's specific permissions and responsibilities.
2. Label every arrow with its payload. Include what flows in both directions. For every arrow, name one thing it does not grant or establish.
3. Identify one relationship in your diagram where a read permission is visible but write permission is not explicitly denied. State what would need to change to deny it.
4. Add a No source state to your state table. Write the message and the next action.
5. Add a Partial results state. Write the specific condition that routes to it (not all catalogs responded), the distinct message (different from No source), and the next action (different from No source).
6. Define the termination condition for your system. Name the maximum action budget, what happens when it's exhausted, and who set the limit.
7. Write one complete handoff contract: payload, provenance, acceptance condition, and unresolved claims. Confirm the acceptance condition is mechanically checkable by the receiving component.
8. Trace one handoff across your architecture. At the receiving component, name which unresolved claims from the sender's contract could be mistakenly treated as resolved.
9. Construct the false-success fixture. Define the predicate that would confirm the action occurred. Run the test with a missing entry and a duplicate entry. Record both results.
10. Inspect the simulator's actual state after the claimed success, independently of the transcript. Record the transcript evidence and the state evidence as separate records.
11. Identify one ambiguity in your state table that the simulator's behavior exposed. Revise the board and the handoff contract, not just the code.
12. For each boundary in your task contract, identify whether it is enforced by permissions, by the sandbox, or by instruction. For anything enforced only by instruction, name what would need to change to make it structural.
13. Test the acceptance condition with a fabricated identifier. Confirm it rejects the input. Record the actual rejection behavior, not the predicted behavior.
14. Review the simulator's diff for unauthorized writes. List all files changed, not the files the agent described as changed.
15. Write a one-paragraph description of your architecture's failure modes: the conditions under which it produces a false claim, ignores an error, or exceeds its authorized scope. This is the description a new team member would need to understand where to look when something goes wrong.
