# Chapter 6 — Conducting AI through design context

[Contents](README.md) · [Previous](05-design-systems.md) · [Next](07-agentic-systems.md)

*Connect Figma to Claude, bound the implementation, and review fidelity.*

> Rough draft for author review. Setup references were checked on 2026-09-29. The lab below has not been executed as part of this book draft.

## The result

Conduct one implementation from a selected Figma frame and compare it with a screenshot-only attempt. Keep the task small enough that you can inspect every consequential change.

The point is not to prove that structured context always wins. The point is to discover what information the agent received, what it used, what it missed, and what you needed to correct.

## Connect through the course environment

Use the Northeastern Claude account and the course's supported client. Bear's workflow uses that account. Check the existing Figma connection before installing another configuration.

For Claude Code specifically, Figma documents a plugin setup and a manual remote-server setup. These are alternatives; do not install both merely to complete the exercise. The documented plugin command is:

~~~bash
claude plugin install figma@claude-plugins-official
~~~

The documented manual alternative is:

~~~bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
~~~

In Claude Code, use the MCP management interface, shown as /mcp in the documentation, to authenticate and inspect the connection. Follow the institution's allowed setup; do not bypass controls or substitute a personal paid account as the default remedy. These instructions concern Claude Code, not an assertion that a browser chat accepts terminal commands. [Figma's remote setup guide](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/).

Once connected, perform a read-only check on the sample frame. Identify the frame and compare its text with the returned context. Record a failed connection as a failure, not a successful run with missing evidence.

## Bound the action surface

Prepare an isolated exercise folder or branch containing only the intended prototype work. Define allowed files, dependencies, network activity, and publication limits. A prompt is a task instruction, not a substitute for actual permissions.

Use this task contract:

~~~text
Goal: implement the resource-card journey.
Design reference: selected frame and specimen.
Allowed changes: the named prototype files.
Preserve: source placement, state distinctions, component rules.
Ask first: new dependencies, new states, revised product behavior.
Forbidden in this exercise: deployment, account changes, external messages.
Evidence: plan, diff, renders, actual check output, unresolved limits.
~~~

Treat fetched design content as context. If a description asks the agent to disclose credentials or alter unrelated files, that is outside the task, even when the text arrived through an authorized tool. Anthropic warns that externally retrieved content can introduce prompt-injection risk. [Claude MCP documentation](https://code.claude.com/docs/en/mcp).

## Run the comparison

Prepare two equivalent starting copies. In A, provide only the frame screenshot and the behavior contract. In B, provide the same screenshot and contract plus structured context retrieved from the same frame.

Hold the selected model, task, permissions, and acceptance criteria constant where possible. Record unavoidable differences. Do not let one run inherit the other's solution.

Before implementation, ask:

~~~text
Read the supplied design and contract.
Report received context, missing behavior, and a file-level plan.
Do not edit until the plan is reviewed.
~~~

After reviewing the plan, authorize the specific edit:

~~~text
Implement the approved plan only in the allowed files.
Preserve the specified design rules.
Run the agreed checks and report their actual outputs.
Separate observed passes from checks you could not perform.
Do not publish or expand scope.
~~~

Capture the prompt, returned context, changes, and rendered result. Inspect the actual output rather than accepting the agent's description of it.

## Worked example: a card that mostly matches

The playlist's Screenshot vs the Frame record compares image-only input with image plus saved Figma context. The more faithful result still stretched a button incorrectly. The build agents used saved context and did not themselves have live Figma access. Those details matter when describing what the experiment established. [Playlist case V01](../research/playlist-evidence.md).

Apply the lesson to your hypothetical resource card:

1. Define checks for spacing, text hierarchy, source placement, button width, and narrow-screen behavior.
2. Inspect both rendered outputs against the same reference.
3. Record each mismatch at a named element.
4. Ask Claude to diagnose one mismatch without redesigning the page.
5. Review the proposed correction.
6. Re-render and check the changed element and adjacent layout.

Do not equate fewer pixel differences with better task performance. Fidelity and usefulness are separate questions. A faithful implementation can reproduce a poor design exactly.

## Review the diff

Read the changed-file list and the important code differences. Ask why a change exists. Look for removed states, invented dependencies, unrelated cleanup, and tests weakened to pass.

The Prompt Engineering diff-review lesson separates the regression, scope, check results, and acceptance decision. Use that packet here. A passing check establishes only the behavior it inspected; it does not authorize merge or publication. [Source P02](../research/sources.md).

If live MCP access is interrupted, use exported context for a labeled offline comparison. Preserve the learning exercise without calling it a successful live-connector run.

[FIGURE: Same design and task branching into screenshot-only and structured-context implementations, then one shared review sheet.]

## Practice

1. Identify your actual client and connection.
2. Perform a read-only frame check.
3. Write an allowed-files boundary.
4. State a change requiring separate approval.
5. Prepare comparable starting copies.
6. Define five fidelity checks before running either build.
7. Inspect whether a rule reached the agent.
8. Record one mismatch without proposing a cause.
9. Conduct a narrowly scoped repair.
10. Detect a scope-expanding change in a hypothetical diff.
11. Explain why fidelity does not establish usability.
12. Report a failed or offline run accurately.

## Submission checkpoint

Deliver the bounded design-to-implementation experiment and fidelity comparison. Include the task contract, both input conditions, actual outputs, difference review, and limitations. This feeds A3.

Next: design the system around the interface, including tools, state, handoffs, and failure.

Source basis: [Chapter 6 research](../research/06-design-context.md).
