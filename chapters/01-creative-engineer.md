# Chapter 1 — The Creative Engineer: designing and conducting AI

[Contents](README.md) · [Next](02-problem-design.md)

*Choose the experience, assign the work, and inspect what the agent actually produces.*

> Rough draft for author review. The running project is illustrative; its proposed results are not completed experiments.

## The result

Finish this chapter with a one-journey project, a division of responsibility, and a working design-context connection. Do not begin with “build me an app.” Begin with a person, a task, and a decision the experience must support.

A Creative Engineer designs the experience and conducts the systems that realize it. In this course, conducting means setting objectives, supplying context, bounding actions, reviewing changes, and deciding what evidence is sufficient. Claude can implement a substantial part of the work. It does not inherit responsibility for choosing the right problem or accepting the result.

Use four verbs to organize the project:

| Verb | Human design question | Bounded contribution from Claude |
|---|---|---|
| Ideate | Which problem deserves attention? | Generate alternatives and challenge assumptions |
| Build | What behavior should exist? | Implement a reviewed specification |
| Brand | What should this audience understand about the work? | Draft explanations from actual evidence |
| Ship | What is ready for someone else to use? | Package, test, and document a candidate |

These are recurring activities, not a waterfall. A failed check may require a new design, not another attempt at the same implementation.

## Choose one critical journey

A critical journey is the smallest connected sequence that delivers the project's central value. “Use AI for education” is a domain. “Find a relevant course resource and inspect why it was recommended” is a journey.

Students may design their own product or AI tool. They may also develop a professional portfolio, learning environment, public-interest service, workplace tool, or creative experience. An original product does not have to be a chatbot. A comparison interface with one carefully bounded AI action may be a better project.

For a portfolio, the journey might be: arrive from a project link → inspect one contribution → examine its evidence → decide whether to contact the engineer. Personal branding belongs here as the design of a truthful professional experience, not as a promise of employment.

Write the journey in a sentence before drawing screens. Name the start, the meaningful outcome, and one situation in which the system should stop.

## Establish the tool relationship

Figma Design and FigJam are the primary design environment. Claude, using the Northeastern account, is the primary conducting and implementation environment. Bear identifies this as his working setup. The [Figma for Educational AI playlist](https://www.youtube.com/playlist?list=PLW3r2g0eZ8lA) investigates what the Education account can and cannot do; treat its experiments as evidence to examine, not marketing to repeat.

Figma MCP supplies a connection through which a supported client can obtain design context. Keep the roles separate: a Figma file holds the design; the MCP server exposes supported operations; Claude uses that context while acting within the task's permissions. [Figma documents this relationship](https://developers.figma.com/docs/figma-mcp-server/).

Start with the [NEU Claude portal](https://claude.northeastern.edu/) and your Figma Education account. Check education status using [Figma's application guidance](https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education). In the course's Claude environment, inspect the Figma connection already configured before adding anything. Chapter 6 gives the dated Claude Code setup procedure.

Create a sample frame with a title, body, and button. Give Claude its frame link and ask:

~~~text
Read this authorized sample frame through Figma MCP.
Report the frame name, text, components, and missing context.
Do not edit the file or implement anything.
Tell me which observations came from a tool result.
~~~

Compare the returned content with the actual frame. A login establishes account access; a correct read establishes that this task's connection worked. Record the date, client, displayed model, operation, and outcome. Keep credentials out of the record.

## Worked example: an educational resource assistant

Use this hypothetical brief:

~~~text
Audience: students working on one course task.
Journey: enter a question, inspect a recommended resource, open its source.
Boundary: do not invent a source or submit coursework.
Stop condition: no supported resource can be identified.
Human decision: which materials count as eligible sources.
Claude contribution: implement the selected interface and lookup behavior.
~~~

Draw three FigJam nodes: question, resource, source inspection. Add a fourth branch for no supported resource. In Figma, sketch the resource and no-result states.

Now ask Claude to challenge the design:

~~~text
Review this journey and its boundary.
Propose two alternatives and identify missing human decisions.
Keep generated suggestions separate from evidence.
Do not implement, publish, or modify the design.
~~~

Suppose Claude proposes answering the question directly. Do not accept merely because it sounds more capable. Compare that proposal with the chosen purpose: resource discovery. A defensible response is to retain source discovery and defer answer generation until it has its own requirements and checks. That is a worked design decision, not an observed student result.

## Inspect capability, not appearance

For each playlist experiment, write four lines: question, observed result, limitation, next test. An account-linking failure may be a useful result. A polished frame may still omit a required state. The [playlist evidence ledger](../research/playlist-evidence.md) distinguishes the inspected records from experiments still pending.

[FIGURE: Human design decisions, Claude actions, Figma context, and evidence returning to review.]

## Practice

1. Reduce a broad product idea to one critical journey.
2. State an outcome that would not require AI.
3. Identify a decision Claude may propose but not finalize.
4. Draw a no-result branch.
5. Write a four-verb self-audit of your current skills.
6. Create a sample frame and verify its returned text.
7. Record a connection failure without guessing its cause.
8. Compare a product journey with a portfolio journey.
9. Reject one proposed feature with a reason.
10. Distinguish a playlist observation from a general claim.
11. Define what must remain private in your project record.
12. Explain the division of responsibility without reading Claude's response.

## Submission checkpoint

Produce the initial experience critique, four-verb self-audit, and setup record. Show one journey, one stop condition, and one actual tool observation. These artifacts feed later submissions; they are not a separate implementation assignment.

Next: turn the journey into an opportunity brief grounded in evidence.

Source basis: [Chapter 1 research](../research/01-creative-engineer.md), especially C01 and H02 in the [source register](../research/sources.md).
