# Chapter 5 — Design systems as instructions for agents

[Contents](README.md) · [Previous](04-interaction-design.md) · [Next](06-design-context.md)

*Make reusable design decisions explicit, retrievable, and testable.*

> Rough draft for author review. Component rules below are proposed project rules, not universal design laws.

## The result

Build a small Figma design system that tells Claude what to reuse, what may vary, and when to ask. Test whether the relevant instructions reach the agent before judging whether it followed them.

A design system is more than a collection of attractive components. For this course it is a reusable specification: parts, states, variables, layout behavior, names, and usage constraints. The agent should not have to infer an important rule from appearance alone.

Figma recommends components, variables, semantic names, Auto Layout, and annotations for communicating design intent. Treat these as useful preparation, not a guarantee of faithful implementation. [Figma file-structure guidance](https://developers.figma.com/docs/figma-mcp-server/structure-figma-file/).

## Define the smallest useful component set

For the resource assistant, start with a resource card, source link, action button, status message, and question field. Add a component when repeated behavior or styling needs a shared rule, not merely because a drawing can be grouped.

For each part, distinguish content from state:

| Part | Content that varies | Behavior or state that varies |
|---|---|---|
| Resource card | Title, relevance explanation, source | Available or unavailable source |
| Action button | Label | Default, focus, disabled when justified |
| Status message | Explanation | Loading, partial evidence, no source, failure |

Do not use one generic “error” variant for every condition. The distinctions designed in Chapter 4 must remain visible in the system.

Create a specimen frame containing all intended variants. This becomes the reference for both human inspection and bounded agent work.

## Name variables by purpose

Use semantic names for design decisions: surface, main text, supporting text, primary action, spacing between card elements. Keep names intelligible to someone who did not create the file.

For this exercise, choose a small set and document its purpose. You do not need an exhaustive token architecture. You do need to explain which differences are intentional.

Apply Auto Layout where the content should determine sizing or alignment. Stress the specimen with long labels, missing optional text, and narrower frames. Write down what should wrap, grow, remain aligned, or change arrangement. Do not rely on a single screenshot to communicate all responsive behavior.

## Write preserve, infer, and ask rules

Use an explicit boundary table:

| Category | Example instruction |
|---|---|
| Preserve | Keep source links adjacent to their recommendation |
| Preserve | Use the defined status variants; do not hide no-source behavior |
| Infer within bounds | Allow text wrapping while preserving the content order |
| Ask first | Add a new state or replace an existing component |
| Ask first | Change an action's meaning or remove its confirmation |

Separate a visual rule from a product rule. “Use one primary action on this screen” is a project convention. “Do not send before approval” is a behavior requirement. Their checks will differ.

The local button experiment used a one-primary-action rule, but that alone did not distinguish builds with instructions from builds without them. A later unusual label rule provided a more informative test. The lesson is experimental: choose a test that can reveal whether the instruction mattered. [Playlist case V02](../research/playlist-evidence.md).

## Read the instruction back

Ask Claude through Figma MCP:

~~~text
Read the selected specimen and component context.
List the rules actually returned by the tools.
For each rule, identify its source in the returned context.
Compare with the supplied preserve/infer/ask table.
Report omissions. Do not edit or implement yet.
~~~

Inspect the returned material. If a rule exists visually but does not appear in the retrieved context, solve that communication problem before blaming the implementation.

The source project's review-note record found different retrieval behavior for different design objects. That historical observation motivates a read-back check; it does not establish a permanent limitation of all clients. [Source F04](../research/sources.md).

## Worked example: a rule the model cannot guess

Use a duplicate test component, not the production specimen. Add a harmless house rule: the primary label in the test must end with an arrow character. Prepare two equivalent tasks, one with that rule and one without it.

Keep the task and other context comparable. Ask Claude to propose a screen using the component, then inspect the output. Record whether the rule was retrieved and whether it was followed. Do not assume the instruction caused every difference between outputs.

If both outputs satisfy an ordinary convention, the experiment may tell you little. If the instructed output misses the unusual rule, inspect the retrieved context and the generated result separately. A failure to receive the rule and a failure to follow it are different problems.

This is a teaching adaptation of the playlist experiment, not a new reported result. The source's manually written rules file must not be described as an automatically generated Figma artifact.

## Accept the system, not just the screenshot

Review the specimen at several sizes of your choosing. Confirm the intended variants, variable use, names, and usage notes. Record which checks concern structure and which concern appearance.

For a portfolio, use the same method for project cards, evidence links, contribution labels, and limitation blocks. A truthful content pattern is as reusable as a button.

[FIGURE: Component intent moving from Figma description to retrieved context to implementation checks.]

## Practice

1. Inventory repeated parts in your selected flow.
2. Separate content properties from state variants.
3. Define five semantic variable names.
4. Stress a component with long text.
5. Document one responsive transition.
6. Write three preserve rules.
7. Identify a change that requires a question.
8. Read a rule back through MCP.
9. Diagnose a missing rule without editing unrelated components.
10. Design a test that avoids the one-primary-action ceiling effect.
11. Compare structural fidelity with visual fidelity.
12. Audit a portfolio component for unsupported claims.

## Submission checkpoint

Retain the inspectable design system and documented interaction states. Include the specimen, usage rules, read-back evidence, and unresolved gaps. These feed A3.

Next: conduct a bounded implementation and compare the result against the design.

Source basis: [Chapter 5 research](../research/05-design-systems.md).
