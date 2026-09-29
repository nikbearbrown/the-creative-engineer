# Chapter 3 — Identity and information architecture with AI

[Contents](README.md) · [Previous](02-problem-design.md) · [Next](04-interaction-design.md)

*Make purpose, evidence, and the next action easy to locate.*

> Rough draft for author review. Worked examples are illustrative.

## The result

Design two information architectures for the same audience and task. Select one using stated criteria rather than preference for its visual finish.

Information architecture determines what belongs together, how it is named, and how a person moves between it. For this project, represent it as content objects, relationships, navigation labels, and task paths. Do not begin with a list of pages copied from a familiar website.

Identity enters through those choices. A professional portfolio that emphasizes tools communicates something different from one organized around problems and evidence. Neither arrangement proves professional competence. The work behind the labels must do that.

## Design the audience's decision

Write the decision at the top of the FigJam board:

~~~text
After this journey, the audience should be able to decide:
[specific decision]
using:
[evidence available in the experience]
without:
[unacceptable confusion or unsupported inference]
~~~

For the resource assistant, the decision is whether a resource is relevant enough to open. For a portfolio, it may be whether the engineer's contribution matches a prospective collaboration.

Use voice as an interface constraint. A source label should identify the material. A limitation should state what is missing. A call to action should identify the next step. Claude can draft concise alternatives, but you choose the language that reflects the actual work.

The portfolio lesson in Branding and AI links claims to artifacts, credits, and versions. Adapt that method here: every identity claim needs a route to supporting evidence. [Source B04](../research/sources.md).

## Inventory objects before drawing pages

For the assistant, begin with question, resource, relevance explanation, source location, and no-source response. For the portfolio, begin with project, contribution, decision, artifact, outcome, and limitation.

Give each object an identifier and required fields:

~~~text
Resource
  id
  title
  eligible source location
  relevance explanation
  limitations

Project
  id
  problem
  personal contribution
  evidence references
  version
  known limitations
~~~

These are proposed content contracts. A filled field is not proof that its contents are true.

Draw object relationships in FigJam. Mark which relationships imply navigation and which are merely associations. A project can cite several evidence artifacts without turning each artifact into a top-level navigation item.

## Build two genuinely competing architectures

Use the same content inventory in both alternatives.

| Architecture | Resource assistant | Portfolio |
|---|---|---|
| Task-first | Start with what the learner is trying to do | Start with the kind of problem the reviewer wants solved |
| Category-first | Browse resources by topic | Browse work by discipline or medium |

Trace one primary journey and one difficult journey through each. The difficult journey might involve an unfamiliar term, a missing resource, or evidence that requires special access.

In Figma, create an entry frame and detail frame for each alternative. Use comparable fidelity. A low-fidelity sketch is sufficient if the labels, grouping, and transitions can be inspected.

Ask Claude:

~~~text
Trace the supplied task through each architecture using only its labels.
List each selection and the information available at that point.
Mark ambiguous labels, missing destinations, and assumptions.
Compare against the audience decision; do not invent participant behavior.
Do not choose based on polish or add pages.
~~~

Claude's path is a generated interpretation. It is useful for finding questions, but it is not a usability observation.

## Worked example: an evidence-first portfolio

Consider a hypothetical student who designed the resource assistant. A first portfolio architecture has pages named Python, Figma, and AI. A reviewer who wants to understand the student's design judgment must assemble the story across all three.

The alternative starts with the project: Resource Discovery. Its detail view presents the problem, two considered designs, the chosen design, the student's decisions, Claude's contribution, and linked checks.

Choose the alternative if the declared audience task is inspecting contribution to a complete project. Preserve the tool inventory as supporting detail. Do not erase it; change its role.

Record the choice:

~~~text
Decision: project-first navigation.
Reason: keeps the contribution and its evidence in one journey.
Rejected alternative: tool-first top-level structure.
Remaining uncertainty: whether the project title is understandable to new readers.
Next test: ask a reader to locate the design decision without coaching.
~~~

This is a rationale, not a demonstrated improvement. The final line identifies the evidence still needed.

## Check structure and meaning separately

The Branding and AI architecture exercise checks missing parents, duplicate identifiers, and cycles. Those checks are useful for content structures. [Source B02](../research/sources.md).

Use a structural audit to find broken references. Use a task review to examine meaning. A navigation loop is not automatically a defect: returning to a project list may be intentional. Distinguish a valid return path from a parent hierarchy that accidentally contains a cycle.

[FIGURE: The same project content organized by tool versus by problem and evidence.]

## Practice

1. State the audience's next decision.
2. Inventory five content objects without naming pages.
3. Identify a claim with no evidence destination.
4. Write three labels for an unfamiliar concept.
5. Draw task-first navigation.
6. Draw category-first navigation using the same content.
7. Trace a missing-resource journey.
8. Find an intentional return path and an accidental dead end.
9. Ask Claude to identify assumptions in its own path.
10. Separate the student's contribution from the tools used.
11. Justify a navigation choice and name remaining uncertainty.
12. Transfer the method to an original product or AI tool.

## Submission checkpoint

Retain the FigJam journey map and two competing information architectures. Include a content inventory, comparable Figma frames, the critique record, and your choice with reasons. These support A2.

Next: design what happens at each step, including interaction states and accessibility.

Source basis: [Chapter 3 research](../research/03-identity-information-architecture.md).
