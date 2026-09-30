# Chapter 5 — Design Systems as Instructions for Agents
*The difference between a component an agent can see and a rule an agent will follow.*

Here is a failure that happens silently.

You build a design system. You define a resource card with a title, a relevance explanation, and a source link. You create variants for the available and unavailable states. You name your colors semantically — `color/text/primary`, `color/action/primary` — so the intent is legible. You write a usage note in the component description: "Keep the source link adjacent to the recommendation. Do not hide the no-source state." You connect the specimen to Figma MCP. You ask Claude to implement the resource card.

Claude produces something that looks like your resource card. The title is there. The explanation is there. The colors are approximately right. There is no source link.

Did Claude fail to follow the rule? Or did Claude never receive it?

Those are different problems with different fixes. If the rule was in the retrieved context and Claude ignored it, the problem is interpretation. If the rule was in the file but never appeared in the retrieved context, the problem is communication. If the rule was in the component description but that description wasn't exposed by the tool that ran, the problem is you haven't checked what the tools actually return. Blaming the implementation before answering those questions is debugging in the wrong place.

This chapter is about building a design system that functions as an instruction set — and about developing the discipline to verify whether your instructions are actually reaching the agent before judging whether it followed them.

---

## What a Design System Is For, in This Context

In standard practice, a design system is a library of reusable components that enforces visual and behavioral consistency across a product. Buttons look the same. Cards behave the same. Color tokens are shared rather than redeclared in every file.

In this course, it is all of that plus something more specific: a machine-readable specification. An agent reading your design system should be able to determine what to reuse, what may vary within bounds, and when a proposed change requires human review before proceeding. The system is not just a collection of attractive components. It is a set of decisions that have been made, documented, and made retrievable.

The distinction matters because agents don't infer important rules from appearance the way a human collaborator might. A human looking at your design might notice that source links are always adjacent to their resource cards and conclude this is intentional. An agent sees a layout. If the adjacency rule isn't written somewhere in the retrievable context, the agent has no particular reason to preserve it.

This creates a new kind of design work: making implicit decisions explicit. The rule that seemed obvious from the design — because it was consistent, because it made visual sense — needs to be stated. Not because the agent is unintelligent. Because explicitness is what separates a rule the agent can follow from a pattern the agent can accidentally break.

---

## Four Checkpoints

Tracking whether an instruction reaches an agent requires distinguishing four stages that the phrase "the agent has the rule" collapses together.

*Authored:* is the rule explicit in a designated source? This means a component description, an annotation, a variable definition, or a project rules file — not a visual pattern that expresses the rule implicitly. A consistently applied pattern is not the same as an authored rule.

*Retrieved:* does the relevant tool response actually contain the rule? Not "the rule is in the file" — "the rule appeared in the text of the tool response." These are different claims. Figma MCP exposes different tools that return different kinds of content: design context, variable definitions, screenshots, sparse metadata. A rule in a component description may not appear in a tool response that returns the frame's layout structure. Which tool ran, and what did it return?

*Interpreted:* does the agent's restatement of the rule preserve its meaning? When you ask the agent to list the rules it retrieved, does it restate "keep the source link adjacent to the recommendation" accurately — or does it paraphrase in a way that loses the specificity?

*Implemented:* does the resulting artifact satisfy the rule? This is the check most people perform first. The argument of this chapter is that it should be the last check, not the first, because a failure at implementation could be a failure at any of the three stages before it.

<!-- → [DIAGRAM: Four-stage pipeline. Authored (rule explicit in designated source) → Retrieved (rule appears in tool response) → Interpreted (agent's restatement preserves meaning) → Implemented (artifact satisfies rule). Gap arrows between each stage labeled with the failure mode at that gap: "rule not in a designated source," "tool didn't expose the source," "paraphrase lost specificity," "implementation diverged." Caption: A failure at implementation could be a failure at any earlier stage. Identify where the discrepancy first becomes observable.] -->

---

## The Smallest Useful Component Set

For the resource assistant, the components that need to exist are: a resource card, a source link, an action button, a status message, and a question field. Add a component when repeated behavior or styling needs a shared rule — not because a drawing can be grouped, and not because the library looks more complete with more entries.

For each component, distinguish content from state. Content varies per instance: the resource title, the relevance explanation, the action label. State varies per condition: whether the source is available or unavailable, whether the action is in its default, focused, or disabled state, whether the status message is reporting a successful result, a partial result, a no-source condition, or a lookup failure.

This distinction maps to Figma's component mechanisms. Text properties carry editable strings. Boolean visibility properties expose or hide optional layers. Instance-swap properties allow approved alternatives for a nested element. Variant properties define the named states the component can be in.

What variant properties cannot do is implement runtime behavior. A button in its disabled-looking variant still needs implementation semantics — the rendered element needs to be genuinely non-activatable, not just styled gray. The variant communicates the intended appearance. The interaction specification from Chapter 4 communicates the intended behavior. The later implementation check confirms whether both were respected.

The status message component deserves specific attention. Do not use one generic "error" variant for every failure condition. The distinctions designed in Chapter 4 — no returned matches, failed lookup, partial results, resource inaccessible — are different conditions with different messages and different recovery paths. Collapsing them into a single error variant would undo the design work that made the interface honest. Each condition is its own named variant, with its own message and its own specified next action.

<!-- → [TABLE: Component inventory. Columns: Component, Content (varies per instance), State variants (defined conditions), What the variant cannot establish. Rows: Resource card (title, explanation — source available, source unavailable — whether source link is implemented as a real link), Action button (label — default, focus, disabled — whether disabled variant is genuinely non-activatable), Status message (explanation text — no matches, failed lookup, partial results, source inaccessible — which runtime condition triggered the state), Question field (placeholder, entered query — empty, populated, loading — whether query is preserved across state changes). Caption: Content and state are different design concerns and Figma's mechanisms for them differ. Variant properties define presentation; interaction specifications define behavior.] -->

---

## Naming Variables by Purpose

Semantic names communicate why a value exists, not what the value is. `#1A1A2E` is a hex code. `color/text/primary` is a design decision. The difference is that someone who didn't create the file can read the second one and understand the intent.

For this exercise, define a small set and document what each one is for. You don't need an exhaustive token architecture. You do need to explain which differences are intentional. A system where heading text and body text happen to share the same color value may be intentionally consistent or accidentally undifferentiated — the name tells you which.

A proposed starting set for the resource assistant:

`color/text/primary` — the main reading text across all components.
`color/text/supporting` — secondary explanatory text, including relevance explanations.
`color/action/primary` — the primary action treatment.
`color/focus/indicator` — the keyboard focus indicator, a design decision that exists for accessibility reasons and should be named explicitly.
`space/resource-card/content-gap` — the separation between designated content elements within the resource card.

Document the purpose of each. Then verify the name is actually bound in the Figma file — that the component referencing `color/text/primary` is using that variable, not a hardcoded value that happens to match. Two tokens can share a value while serving different purposes. Literal equality alone does not establish correct reuse.

Apply Auto Layout where content should determine sizing. Stress the specimen: long resource titles, missing optional descriptions, narrow frames. Write down what should wrap, what should grow, and what should remain aligned. A single screenshot cannot communicate all responsive behavior. An annotation that says "title wraps; explanation truncates at two lines; source link always visible" communicates the intent. A later check verifies whether it was respected.

---

## The Preserve / Infer / Ask Table

Every design system implicitly contains three categories of decision. Making them explicit is the work that converts a design file into a specification an agent can act on.

*Preserve* rules are inviolable. They encode product requirements, safety behaviors, or design decisions where deviation would break something. "Keep the source link adjacent to its recommendation" is a preserve rule. "Use the defined status variants — do not hide the no-source condition" is a preserve rule. An agent that proposes changing a preserve rule has proposed something that requires human review before it proceeds.

*Infer within bounds* rules allow variation within a specified range. "Text may wrap while preserving content order" is an infer rule. "Card height adjusts to content; minimum height is the title plus one line of explanation" is an infer rule. The agent can make these choices without asking, as long as the choice stays within the stated bound.

*Ask first* rules define the gate. "Adding a new state or replacing an existing component requires a question before implementation." "Changing an action's meaning or removing a confirmation requires a question before implementation." These are the places where the agent's judgment is most likely to diverge from the design's integrity constraints.

For each rule, name the scope (which components or interactions it applies to), the source (which file, component, annotation, or rules file is authoritative), and the acceptance check (how you would verify it in the implementation).

The difference between a visual rule and a product rule matters here. "Use one primary action on this screen" is a visual convention — it exists to reduce visual noise and guide attention. "Do not send before approval" is a behavior requirement — it exists to prevent an action with real consequences from happening without authorization. Their acceptance checks are different. The visual rule can be verified by inspecting the rendered screen. The behavior rule requires demonstrating that no send occurs before the approval condition is satisfied. Displaying a confirmation button does not demonstrate that.

<!-- → [TABLE: Preserve/Infer/Ask table with scope, source, and check. Three sections. PRESERVE: "Keep source link adjacent to recommendation" — Scope: resource card — Source: component description — Check: inspect rendered card for link position relative to explanation. "Use defined status variants; do not hide no-source condition" — Scope: status message component — Source: component description — Check: trigger each search condition; confirm distinct messages appear. INFER WITHIN BOUNDS: "Title text may wrap; card height adjusts to content" — Scope: resource card — Source: Auto Layout definition — Check: resize frame; confirm wrap without overflow or loss of source link. ASK FIRST: "Adding a new component state requires review before implementation" — Scope: all components — Source: project rules file — Check: any new variant must be preceded by a human-visible question in the implementation session transcript.] -->

---

## Reading the Instructions Back

Before asking the agent to implement anything, ask it to read the design system back to you. The read-back has two stages, and they should be separate.

In the first stage — extraction — give the agent the specimen location and ask it to list the rules present in the tool responses, with exact source locations. Do not supply the expected rule list. If you supply the list, the agent can repeat it even when retrieval omitted a rule, which makes the extraction test uninformative.

```
Read the selected specimen and component context through Figma MCP.
List the rules actually present in the returned tool responses.
For each rule, identify its source in the returned context:
  which tool, which node, which field.
Do not add rules you know from prior context.
Do not edit or implement yet.
```

In the second stage — comparison — compare the extracted rules against your authored list. Record what was retrieved, what was omitted, and whether any restatement changed meaning.

Preserve the actual tool responses. An agent's assertion that it retrieved a rule is weaker evidence than the corresponding response text. Know which tool ran and what it returned — not just whether "the MCP context" contained the rule. Figma MCP exposes different tools that return different content: design context, variable definitions, screenshots, and sparse metadata are distinct outputs. A rule in a component description may be absent from a tool response that returns frame layout. Identify the mismatch between where you authored the rule and what the tool exposed.

If a rule exists in the file but doesn't appear in the retrieved context, that is a communication problem to solve before implementation. Fix the channel — move the rule to an accessible annotation, a separately accessible rules file, or a variable description — then re-verify retrieval before asking the agent to implement.

---

## Designing a Test That Reveals Something

The worked example uses a rule the agent wouldn't reliably satisfy by following ordinary conventions — not because unusual rules matter in themselves, but because a rule an agent would follow anyway can't tell you whether the instruction mattered.

The diagnostic structure that reveals something uses three conditions:

*Baseline:* the rule appears nowhere in the available task context. Estimate how often the output satisfies it without instruction. If the baseline rate is already high, the rule isn't unusual enough to be diagnostic.

*Direct instruction:* the rule is stated explicitly in the task prompt. Check whether the agent follows it when it's clearly supplied. If the agent doesn't follow the rule when stated directly, the experiment is telling you something different than you intended.

*Retrieved instruction:* the rule appears only in the designated design-system source, not in the task prompt. This is the check on the combined retrieval-and-implementation workflow.

Keep the task, starting files, component content, and other instructions equivalent across conditions. Use fresh sessions to reduce carryover effects. Define in advance exactly what counts as satisfying the rule. Run a small, predetermined number of trials. Report all outputs, including failures.

One pair of outputs is a demonstration, not a reliable estimate of an instruction effect. Name it as a demonstration.

Note also: the read-back is itself an intervention. Asking the agent to restate a rule may increase its salience in what follows. That is appropriate when you're testing the read-back workflow. It must be disclosed when you claim to measure unaided retrieval and implementation. Keep those conditions separate.

---

## Accepting the System, Not Just the Screenshot

The review before submission distinguishes five things a screenshot cannot verify.

*Structure:* are component instances, properties, variable bindings, and code references actually present? A rendered button that looks like the design component might be a freshly created element with hardcoded values.

*Appearance:* does the rendered output match the specimen at specified conditions? Include narrow frames, long labels, and missing optional content — not just the clean, representative case.

*Behavior:* do the state changes, keyboard operation, and recovery paths work as the interaction specification requires? The design system defines the presentation. Chapter 4's state records defined the behavior. Both require checking.

*Instruction delivery:* what tool responses document the retrieved rules? Preserve the evidence with source locations — not just a statement that retrieval succeeded.

*Content integrity:* are source attributions, limitations, and contribution records preserved correctly? A portfolio project card that attributes a team achievement to one person, or that omits the limitation section, has failed a content requirement even if the visual design is accurate.

Document unresolved gaps separately from confirmed findings. For each gap, name an owner, a next check, and the checkpoint by which it must be resolved. An open gap with a bounded resolution plan is honest. An open gap carried forward silently is not.

---

## What Would Change My Mind

The premise of this chapter — that making rules explicit and verifiable improves an agent's ability to follow them — is reasonable but not established by controlled comparison in this course's specific workflow. The research support (IFEval on instruction-following, the context-position findings on presence versus effective use of information in context) addresses related questions in different settings. If a student conducted a clean three-condition experiment and found that retrieved instructions produced no reliable improvement over baseline, that would be a genuine finding worth reporting. The chapter's method produces evidence; it doesn't guarantee a particular result.

## Still Puzzling

The preserve/infer/ask framework assumes a clean hierarchy: some rules are inviolable, some allow bounded variation, some require questions. In practice, a rule that's a preserve requirement for one project may be an infer rule for another, depending on what the product actually needs. There's no principled way to assign a rule to a category without knowing the product's actual requirements — and those are stated in the brief and the interaction specification from Chapters 2 and 4, not derivable from the design system itself. The table is a teaching structure. Its real content has to come from decisions made earlier in the project.

---

## Practice

1. Inventory the repeated parts in your selected flow. For each, write one sentence explaining why it belongs in the component set rather than as a one-off frame element.
2. For one component, separate its content properties (vary per instance) from its state variants (vary per condition). Name the Figma mechanism you would use for each.
3. Define five semantic variable names for your project. For each, document the purpose — what decision it represents, not what value it holds.
4. Stress one component with a title that is three lines long and a missing optional description. Write down what should wrap, grow, remain aligned, or change arrangement.
5. Document one responsive transition in the specimen: what changes when the frame narrows below a specified width?
6. Write three preserve rules for your design. For each, name the source that makes it authoritative and the acceptance check that would verify it in the implementation.
7. Identify one proposed change from Claude that would require an "ask first" response. Write the question you would ask before authorizing it to proceed.
8. Run the two-stage read-back. First, ask the agent to extract rules with source locations, without supplying the expected list. Second, compare against your authored rules. Record what was retrieved, what was omitted, and whether any restatement changed meaning.
9. Identify one rule that exists in the file but did not appear in the retrieved context. Diagnose whether the gap is in authoring (the rule isn't in the right source), tool selection (the tool that ran doesn't expose that source), or retrieval (the tool ran but the rule was absent from the response). These are different problems with different fixes.
10. Design a test for one preserve rule that distinguishes "the agent followed the rule from the retrieved instruction" from "the agent produced output that happens to satisfy the rule by convention." Describe the baseline condition, the direct-instruction condition, and the retrieved-instruction condition.
11. Compare structural fidelity against visual fidelity for one component. Name one thing visual fidelity can establish and one thing it cannot.
12. Audit one component — from the resource assistant or your portfolio — for unsupported claims in its content. Identify any property or behavior the content implies that the component specification doesn't actually establish.
13. For one open gap in your design system, write a bounded resolution entry: what is unresolved, why it can't yet be confirmed, what check would resolve it, who owns the check, and by which submission checkpoint it must be complete.
14. Examine one status message variant. Confirm it is named for the specific condition it represents — not a generic label — and that the message text and recovery action are appropriate to that specific condition, distinct from all other status variants.
15. Write the distinction between a visual convention and a product requirement for one rule in your preserve table. Name the different acceptance check each requires.
