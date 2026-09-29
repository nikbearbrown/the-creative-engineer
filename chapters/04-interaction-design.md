# Chapter 4 — Interaction design and conducting AI critique

[Contents](README.md) · [Previous](03-identity-information-architecture.md) · [Next](05-design-systems.md)

*Specify actions, feedback, and failure states before selecting the visual direction.*

> Rough draft for author review. Proposed behaviors are requirements, not tested outcomes.

## The result

Produce two interaction concepts for the critical journey and defend one. Your rationale must address hierarchy, typography, accessibility, and the limits of Claude's critique.

An interaction specification connects an event to a visible response and a next possible action. A static screen is incomplete when it does not explain how the person arrived there or what happens next.

Use a state record:

~~~text
State:
Entry event:
Information shown:
Available actions:
Feedback:
Exit conditions:
Failure and recovery:
~~~

Start with the journey selected in Chapter 3. Do not introduce another main project.

## Draw alternatives with different behavior

For resource discovery, compare a list with an inline source preview against a list that opens a separate detail view. The difference changes context retention, available space, and the return path. Changing only the corner radius does not produce a competing interaction concept.

In Figma, create the initial, loading, results, no-results, source-detail, and error states needed by your flow. Not every state requires a separate elaborate screen. A clear annotation may define a transition until the prototype supports it.

Connect the states and specify what is preserved when the user returns. If a query disappears unexpectedly, the journey may require repeated work. If a failed lookup is presented as no matching resource, the interface communicates a conclusion that the system has not established.

Use this distinction in the design:

| Condition | Proposed message purpose | Next action |
|---|---|---|
| Search completed with no eligible match | Explain the search result | Revise the question |
| Search did not complete | Explain the operational failure | Retry or use another route |
| Source exists but cannot be opened | Explain the access limit | Show the reference and an alternative |

## Assign visual hierarchy

Decide what must be understood first. On a recommendation, that might be the resource title and why it was selected. On an approval screen, it is the proposed action and consequence.

Define text roles before selecting decorative treatments: page heading, resource title, explanation, status, source, action, and supporting detail. Keep the same role consistent across alternatives so the comparison concerns behavior.

Stress the design with a long title and a missing description. Resize the frames. Inspect whether the source or recovery action is pushed out of the useful reading sequence. The visual-system exercise in Branding and AI combines token checks with rendered inspection because valid data alone does not establish a usable composition. [Source B03](../research/sources.md).

## Design accessibility as behavior

Annotate intended keyboard order, focus visibility, control labels, and status announcements. Refer to specific criteria rather than asking Claude whether the screen “is accessible.” WCAG 2.2 includes keyboard operation, focus visibility, and status-message criteria. [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/).

A Figma annotation records intent. It does not establish that the implemented page supports that behavior. For each annotation, name the later check: keyboard traversal, focus inspection, or appropriate assistive-technology inspection. Avoid claiming complete conformance from a screenshot review.

## Conduct critique, then critique the critique

Provide Claude with the task, both flows, and the criteria:

~~~text
Review concepts A and B against the stated journey.
For each finding provide:
frame or state, observable issue, likely consequence,
evidence needed, and a possible revision.
Separate visible facts from inferred runtime behavior.
Do not change the design.
~~~

Create a finding ledger with accept, reject, and investigate dispositions. “Looks confusing” needs a located example. “The focus order is wrong” needs runtime evidence unless the finding concerns an explicitly annotated order.

The supervisory-check exercise requires evaluating the checker, including false acceptance and false rejection. Use that discipline on Claude's design critique. [Source H01](../research/sources.md).

## Worked example: reject a premature simplification

In this hypothetical review, Claude recommends removing the no-source state because it makes the flow longer. The selected design requires a visible boundary when no eligible resource exists.

1. Locate the proposed deletion.
2. Identify the requirement it would remove.
3. Reject deletion, but investigate whether the state is unnecessarily verbose.
4. Revise the message to state what is missing and what the user can do next.
5. Preserve the separate operational-error state.

The result is a smaller message, not a hidden limitation. Conducting AI includes extracting a useful concern from a proposed change without accepting its solution.

For a portfolio, the equivalent issue is removing limitations to make the case study appear stronger. Keep the limitation; improve its wording and placement.

[FIGURE: Search flow with distinct no-match, failed-lookup, and inaccessible-source branches.]

## Practice

1. Write a state record for the first user action.
2. Identify a hidden transition in your current prototype.
3. Produce an alternative that changes behavior.
4. Separate no results from operational failure.
5. Define the return path from source detail.
6. Stress a frame with a long title.
7. Assign text roles across both concepts.
8. Annotate keyboard order and expected focus.
9. Ask Claude for a located critique.
10. Reject one unsupported finding with evidence.
11. Turn an accepted finding into a testable revision.
12. Defend the selected concept without relying on visual preference alone.

## Submission checkpoint — A2

Submit experience concepts and design rationale: two alternatives, interaction states, hierarchy decisions, accessibility intent, critique dispositions, and the reason for your choice. Include what still requires implementation or human testing.

Next: turn the selected design into reusable components and instructions that an agent can inspect.

Source basis: [Chapter 4 research](../research/04-interaction-design.md).
