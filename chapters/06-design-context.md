# Chapter 6 — Conducting AI Through Design Context
*Connect Figma to Claude, bound the implementation, and review fidelity — including what the agent received, what it used, and what you had to correct.*

Here is what the comparison exercise is actually testing.

You give Claude a screenshot of your resource card frame. You ask it to implement the component. The output is close — the title is there, the spacing is approximately right, the colors are plausible. You compare it to a second implementation that received the same screenshot plus structured design context retrieved through Figma MCP. The second output matches more precisely.

You conclude that structured context produced the better result.

This conclusion may be right. But it conflates several things that are worth keeping separate. The structured context included layout metadata, token values, and a code starting point that Figma's server produces alongside the design information. The second agent also had Code Connect mappings telling it which code component corresponds to which Figma component. If the second implementation is better, is it because of the structured representation, the additional information, the reference implementation, or something else entirely? One pair of outputs doesn't answer that question. The experiment can show what happened. It can't isolate what caused it.

What the experiment can reliably teach is something more modest and more useful: the discipline of specifying exactly what each run received, enforcing the isolation you claim, and reviewing the outputs against criteria defined before either run began. That discipline is the point. The measurement is evidence for your specific project, not a finding about structured context in general.

---

## Connecting Through the Course Environment

Use the Northeastern Claude account and the course's supported client. Confirm with the instructor which client is provisioned and whether Claude Code is available in your account — institutional deployments vary, and the lab's enforcement mechanisms require Claude Code specifically. If Claude Code is not available, the chapter describes a labeled offline fallback.

Figma documents two installation routes for Claude Code. The plugin install is preferred:

```bash
claude plugin install figma@claude-plugins-official
```

The manual alternative configures the server without additional skills:

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

These are not equivalent for this experiment. The plugin bundles MCP configuration with Agent Skills for common Figma workflows — implementing designs, connecting components through Code Connect, and creating design-system rules. Those skills shape how the agent approaches implementation and belong in condition B's description, not left as background noise. The manual install configures only the server. For a controlled comparison, use the manual install, or record the plugin's skills as part of what condition B received.

After installation, use `/mcp` to authenticate through Figma's OAuth flow and confirm the connection. Record the actual server name — permission rules in Claude Code key off the name as registered, and a plugin install may register under a different name than `figma`. Read the name from `/mcp` before writing any rule.

Once connected, perform a read-only check on your sample frame. Give Claude the frame link and ask it to report what the tool returned — specifically, the frame name, each text string exactly as returned, and any component names — without editing the file. Compare the returned content with the actual frame. Record a failed connection as a failure, not a successful run with missing evidence.

---

## Bounding the Action Surface

A task contract specifies what the agent may do. An enforcement layer makes those specifications effective. The chapter's key principle: a prompt is a task instruction, not a substitute for actual permissions. The two need to match.

Claude Code has two enforcement layers. Permission rules are evaluated before any tool runs and apply to every tool including Bash, Read, Edit, WebFetch, and MCP tools. Sandboxing is OS-level enforcement that restricts filesystem and network access, but only for Bash commands and their child processes. For network isolation to be reliable rather than instruction-dependent, it belongs in the sandbox, not in a deny rule on `curl` or `fetch` commands alone.

The task contract for this lab:

```
Goal: implement the resource-card journey.
Design reference: selected frame and specimen.
Allowed changes: the named prototype files.
Preserve: source placement, state distinctions, component rules.
Ask first: new dependencies, new states, revised product behavior.
Forbidden in this exercise: deployment, account changes, external messages.
Evidence required: plan, diff, rendered outputs, actual check results, unresolved limits.
```

Map each line of the contract to an enforcement mechanism. Allowed changes become Edit rules scoped to the prototype path. Forbidden deployment becomes a deny rule on push and deploy commands plus sandbox network isolation. Ask first on new dependencies becomes an Ask rule on package manifest edits and install commands.

The things the enforcement layer cannot handle — preserve source placement, preserve state distinctions, ask first on new states — are the things your review is for. The review is more valuable when it's focused on what can't be enforced rather than also checking whether the agent ran `git push`.

For the Figma server itself: condition A (screenshot only) should have the Figma server denied in its project settings, with `/mcp` confirming it's unavailable. If the server is installed at user scope, it reaches condition A regardless of what the task contract says. Install at local scope only, and verify the denial actively.

<!-- → [TABLE: Two-column table showing project settings differences between conditions A and B. Column headers: Condition A (screenshot only), Condition B (screenshot plus context). Rows showing key permission differences: Figma server (mcp__figma denied entirely — get_design_context, get_metadata, get_screenshot, get_variable_defs allowed; use_figma and generate_figma_design denied), Test files (Edit(./tests/**) denied — same), Deployment (WebFetch denied, sandbox on — same), Plan mode (defaultMode: plan for first prompt — same). Caption: The two conditions differ only in Figma server permissions. Everything else is identical. That's the comparison.] -->

---

## Running the Comparison

Prepare two equivalent starting copies — the same starting folder, the same dependencies, the same assets, the same test files, the same project instruction file. Use fresh Claude Code sessions. Keep each run from reading the other's output.

Several leakage paths undermine the comparison if not closed. A shared git history between the two folders. A shared project instruction file with different content. A user-scope Figma server that reaches condition A. Files written by an earlier B run — a design-system-rules output file, for example — present in A's working tree. A session that carries context from a previous run. Close each one before beginning.

Freeze condition B's design context before either implementation begins. Retrieve the content from the Figma frame, save the complete tool response, and give it to B as a file. This separates the retrieval step from the implementation comparison and means you know exactly what B received. It also closely matches the historical playlist observation referenced later in this chapter, where saved context rather than live retrieval was used.

Plan mode enforces read-only behavior for the first prompt. Before either implementation begins, ask each agent to report what it received and produce a file-level plan:

```
Read the supplied design and contract.
Report received context, missing behavior, and a file-level plan.
Do not edit until the plan is reviewed.
```

Review the plan before authorizing anything. If the plan identifies missing information, correct it at the plan stage — not by letting the agent make assumptions during implementation. Record any correction as part of the run log, because a plan stage where you corrected A's missing layout decisions but merely approved B's plan is measuring context plus different human intervention.

After reviewing the plan, authorize the implementation:

```
Implement the approved plan only in the allowed files.
Preserve the specified design rules.
Run the agreed checks and report their actual outputs.
Separate observed passes from checks you could not perform.
Do not publish or expand scope.
```

Capture everything that matters for comparison: the prompt, the full returned context for B, the file changes, the test results, and the rendered output. Inspect the actual output — don't accept the agent's description of it.

Run each condition at least three times from clean starting copies. LLM code generation is nondeterministic even with identical prompts, and agent runs add more sources of variance — tool order, file exploration, retries. A single A-versus-B comparison shows what can happen. Three runs each lets you report how often each condition passes each check.

---

## What the Agent Actually Received

Before comparing outputs, examine what B received. Figma's documentation is specific about this: the MCP server extracts structured context from the selected frame — layout, component structure, token values, variable definitions — and passes that context alongside a code starting point to the agent. B is not receiving design context in place of reference implementation material. It may be receiving both.

Mark which parts of B's final code were already present in the tool response. This doesn't invalidate the comparison, but it changes what you've measured. "B produced better code because it had structured context" and "B produced better code because it received a reference implementation alongside structured context" are different conclusions, and only one of them tells you something about the value of Figma MCP for this kind of task.

The research on design-to-code generation makes a specific prediction worth writing down before either run. Figma2Code's evaluation found that combining the design image with layout and style metadata reduced visual fidelity errors, but responsiveness was most sensitive to geometry and hierarchy information — and in some cases, exact geometry from Figma metadata led implementations to use absolute positioning where flexible layout would have been more maintainable. A visually faithful implementation that hard-codes exact pixel positions may fail at narrower viewports in ways that a more generalized implementation handles correctly.

Write the prediction before running: B will match the frame more closely at the design width; it may perform worse than its visual fidelity suggests at narrow widths, because exact geometry invites absolute positioning. Report whether the prediction held.

---

## Reviewing the Diff

After implementation, read the changed-file list and the important code differences. For each changed file, ask why the change exists. Look for removed states, invented dependencies, unrelated cleanup, and tests weakened to pass.

Test modification is the specific failure worth checking explicitly. Keep one check — the narrow-width behavior is a natural holdout — that you run yourself after the build and never show the agent during implementation. Deny edits to test files during implementation via an Edit rule on the test path; review that rule's effectiveness by looking for test-file changes in the diff. An empty diff for the test path is evidence the boundary held. A changed test file is a finding even if the permission rule should have prevented it.

Separate the diff review into three categories that require different responses. State removals — the no-source state is gone, the failed-lookup message is missing — are design integrity failures. Scope expansions — new dependencies added, files outside the authorized path modified — are permission failures. Test modifications — assertions weakened, test inputs special-cased, baseline values replaced — are evidence quality failures. Each category requires a different next action.

The fidelity review uses six checks, defined before either run begins:

*Spacing and text hierarchy:* does the rendered output match the specified spacing and typographic relationships?

*Source placement:* is the source link adjacent to the recommendation as the design specifies?

*State distinctions:* are the no-match, failed-lookup, partial-results, and inaccessible-source states present and distinct? This is behavioral, not visual — the visual check sees whether the variants exist; the behavior check would require loading the interface and triggering each condition.

*Narrow-screen behavior (holdout):* this check runs after the build, is run by you not the agent, and is not shared with the agent before implementation.

*Absolute-positioning count:* how many absolute position rules appear in the implementation? This is a maintainability indicator, checkable with a text search.

*Hard-coded values that should be tokens:* how many specific pixel or color values appear in the implementation that the design system defines as tokens? Also checkable with a text search.

Do not combine these into a single score unless you explain the weighting. A visually accurate result can still fail a behavioral requirement. Fidelity checks whether the implementation matches the frame. The acceptance criteria from Chapter 2 check whether the frame solves the problem. A faithful implementation of a poor design satisfies the first and fails the second. These are different questions.

<!-- → [TABLE: Review sheet for six conditions (A1, A2, A3, B1, B2, B3). Columns: Check, Type, A1, A2, A3, B1, B2, B3. Rows: Spacing and text hierarchy (Visual), Source placement (Visual/Behavioral), State distinctions (Behavioral), Narrow-screen behavior — holdout, run by student (Responsiveness), Absolute-positioning count (Maintainability), Hard-coded values instead of tokens (Maintainability), Out-of-scope changes (Scope). Caption: Report counts across runs, not a single winner. The holdout row is filled by the student after each build, not by the agent.] -->

---

## Offline Fallback

If the live connection fails, use exported Figma context for a labeled offline comparison. The learning exercise remains valid. The submission carries two independent status fields: the connection exercise (succeeded, failed, or not attempted) and the implementation comparison (completed with live retrieval, completed with saved context, partial, or not completed). These are different things and should be reported separately. A student who clearly documents a failed connector setup and completes a rigorous offline comparison has produced more honest evidence than one who describes an unverifiable live run.

---

## What Would Change My Mind

The chapter treats a single-pair comparison as a demonstration, not a finding — because LLM code generation is nondeterministic enough that one pair of outputs could go either way. If Anthropic or Figma published a controlled evaluation with repeated trials, predefined criteria, and isolated variables showing that structured Figma context reliably improves implementation on specific task types, that would change the evidentiary claim from "here is what happened in your project" to "here is what tends to happen in this class of task." The research exists for screenshot-to-code generation generally; it doesn't yet exist for the Figma MCP workflow specifically.

## Still Puzzling

The plan-review step is designed to catch misunderstandings before implementation. But if you correct A's plan and approve B's plan without correction, the comparison now measures context plus different human intervention. The clean version would be to define acceptance criteria for a valid plan and approve or reject each plan against those criteria mechanically — but that requires knowing in advance what a good plan looks like for this task, which requires having solved the task enough to know. There's a circularity here that the lab design doesn't resolve cleanly, and the honest answer is probably to record every correction as a variable rather than claiming it was held constant.

---

## Practice

1. Confirm your actual client and whether Claude Code with the Figma connector is available in your institutional account. If not, document the fallback you'll use.
2. Perform a read-only frame check using the extraction prompt from this chapter. Record the actual returned text and compare it to the frame at the character level for one text string.
3. Read the Figma server name from `/mcp` and write the deny rule for condition A using the actual name.
4. Write an allowed-files boundary for condition A as an Edit rule. Confirm the syntax against Anthropic's current Permissions documentation.
5. State one change that would require separate approval under the task contract. Identify which enforcement mechanism (permission rule or sandbox) would prevent it if the agent attempted it without asking.
6. Prepare two equivalent starting copies. List each leakage path from the checklist in this chapter and confirm each is closed.
7. Define all six fidelity checks before running either build. Write the acceptance criterion for each — what exactly would pass, and what would fail.
8. Save the complete `get_design_context` response from condition B. Mark which parts of B's final code were already present in the retrieved content.
9. Write the Figma2Code prediction before either build: what specifically do you expect B to do better, and where do you expect it to perform worse or differently than visual fidelity would suggest?
10. Run the holdout check yourself after the build. Record the result before showing the agent any failure. Do not ask the agent to diagnose a failure before you've recorded what you observed.
11. Review the diff for one run and classify each changed file as a state removal, scope expansion, or test modification. Identify the correct next action for each category.
12. Compare absolute-positioning count and hard-coded token values between your best A run and your best B run. Report the counts before commenting on what they mean.
13. Record the plan-stage corrections you made for each run. If you corrected A more than B, note that the comparison now measures context plus different human intervention.
14. Report the connection exercise status and the implementation comparison status as separate fields. If the connection failed, document the offline fallback you used.
15. Write one sentence stating what the experiment established and one sentence stating what it did not establish. These should be specific to your runs and your checks, not general claims about structured context.
