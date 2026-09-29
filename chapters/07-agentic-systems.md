# Chapter 7 — Designing agentic systems and conducting workflows

[Contents](README.md) · [Previous](06-design-context.md) · [Next](08-midterm-defense.md)

*Turn a diagram into explicit states, tool contracts, and reviewable actions.*

> Rough draft for author review. The example system and contracts are teaching designs, not a deployed service.

## The result

Design and conduct one bounded workflow connecting the interface, an agent, a tool, and a human decision. Every arrow in the architecture must have a meaning that can be inspected.

A box labeled “AI” is not an architecture. A loop between “planner” and “tools” leaves important questions unanswered: which tools, with whose authority, using what state, stopping under which conditions?

The source project's Whiteboard to Code questions expose precisely these gaps. Its scaffold made assumptions where the board was silent and retained placeholder behavior. Use that record as a warning against mistaking generated structure for resolved design. [Source F02](../research/sources.md).

## Separate the participants

In FigJam, draw the person, interface, agent, resource store, and review point separately. Add a mock notification sink if your project includes an approval exercise. Do not connect a real inbox or gradebook for this lab.

For every relationship, name what crosses it:

| Relationship | Payload | Design question |
|---|---|---|
| Person → interface | Question and chosen context | What is necessary to collect? |
| Agent → lookup tool | Bounded query | Which materials may be searched? |
| Tool → agent | Results and source identifiers | What does an empty result mean? |
| Agent → interface | Recommendation or limitation | What must remain uncertain? |
| Person → review gate | Approval or rejection | What exact action is authorized? |

A read relationship does not imply write permission. A displayed approval button does not establish that the backend enforces approval.

## Specify states and transitions

For the running assistant, use a small state table:

| Current state | Event | Next state | Required evidence |
|---|---|---|---|
| Received | Lookup begins | Retrieving | Accepted query and allowed source set |
| Retrieving | Eligible result returned | Source found | Source identifier and result |
| Retrieving | Lookup completes empty | No source | Completed lookup with no eligible result |
| Retrieving | Tool fails | Failed | Error outcome, not a guessed answer |
| Source found | User opens source | Completed journey | Actual destination |
| No source | User requests contact | Review required | Exact proposed draft |

These states are a proposed model. Change them if your project requires another behavior, but preserve the distinction between no evidence and failed retrieval.

Add termination conditions. Name the maximum action budget you choose for the exercise and what happens when it is exhausted. The number is a design parameter, not a platform limit.

## Make handoffs explicit

Use a contract like this illustrative record:

~~~json
{
  "source": "resource_lookup",
  "destination": "recommendation_builder",
  "payload": {"resource_id": "example-resource-01"},
  "provenance": {"fixture": "authorized-course-catalog"},
  "acceptance_condition": "resource_id exists in the supplied catalog",
  "unresolved_claims": ["relevance has not been judged by a student"]
}
~~~

The record is synthetic. Its value is the structure: a later stage receives both the result and its limitations. The Conducting AI handoff lesson requires provenance and unresolved claims so processing does not turn an unsupported statement into apparent authority. [Source C02](../research/sources.md).

An identifier check can reject a nonexistent resource. It cannot establish that a real resource answers the question. Design a separate relevance check.

## Conduct implementation from the board

Give Claude the FigJam context and task contracts:

~~~text
Review the board and contracts before writing code.
List missing state transitions, permissions, termination rules,
and assumptions that would change behavior.
Then propose a local simulator with read-only fixture lookup.
No network calls or real messages.
Do not fill unresolved product decisions silently.
~~~

Resolve the consequential questions. Then permit the bounded implementation. Ask for a trace that separates proposed action, attempted action, tool result, and final state.

Use code as a way to test the design, not as a replacement for it. If implementation exposes an ambiguous transition, revise the board and contract as well as the code.

## Worked example: the agent says “done”

Construct a fixture in which the agent's final message says that a recommendation was saved, but the local saved-resource list remains unchanged.

The transcript establishes that the agent said it saved the recommendation. The list establishes whether the expected state change occurred. Keep both records. The Computational Skepticism exercise uses this distinction to test narrated success against actual state. [Source S01](../research/sources.md).

For the simulator, define acceptance as a concrete predicate: the expected resource identifier appears once in the saved list. Then test a missing entry and a duplicate entry. Do not let the same success sentence serve as both the action and its proof.

In a portfolio project, the analogous failure is announcing that an evidence link was added while the released page still points nowhere.

## Review the boundaries

Check missing provenance, invalid source identifiers, exhausted steps, unauthorized writes, and tool failure. A path validator or prompt does not by itself create an operating-system sandbox. Match the permissions of the actual environment to the task. [Source P01](../research/sources.md).

[FIGURE: Interface, agent, lookup, state store, and human review with named payloads and failure transitions.]

## Practice

1. Replace a generic AI box with named responsibilities.
2. Label every arrow with its payload.
3. Separate a read relationship from write authority.
4. Add a no-source state.
5. Add a failed-retrieval state.
6. Define a stopping condition.
7. Write one complete handoff contract.
8. Preserve uncertainty across a handoff.
9. Create a false-success fixture.
10. Inspect an outcome independently of narration.
11. Find a decision Claude would otherwise infer.
12. Update the board after an implementation discrepancy.

## Submission checkpoint

Retain the FigJam architecture, agent task contracts, and working critical journey. Include one successful and one failed path with actual evidence when run. These feed A3.

Next: defend the design and the way you conducted its implementation.

Source basis: [Chapter 7 research](../research/07-agentic-systems.md).
