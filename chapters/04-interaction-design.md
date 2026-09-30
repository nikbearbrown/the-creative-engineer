# Chapter 4 — Interaction Design and Conducting AI Critique
*Why a static screen is always a lie, and what to do about it.*

A screen is a photograph of one moment in a journey that has a before and an after. The photograph doesn't show how you got there. It doesn't show what happens when you tap the button, what appears when the search fails, or where you land when you close the detail view and need to try again. A screen shows what the interface looks like when everything is going according to plan and the data is clean and the user knows exactly what they're doing.

None of those conditions are reliably true.

The gap between a screen and an interaction is the difference between depicting a state and specifying a behavior. A static mockup of a search results view looks complete. It has a list, titles, descriptions, a back button. But it doesn't specify what the list looks like when the search takes three seconds. It doesn't specify what happens when the query returns nothing. It doesn't specify what the user sees if the source exists in the catalog but the link is broken. It doesn't specify whether the query is preserved when the user navigates to a detail view and comes back.

Each of those unspecified states is a design decision that someone will eventually make — either you, intentionally, or the implementation, by default. The interaction specification is how you make it intentionally.

---

## The State Record

The practical tool that makes interaction design explicit is the state record. For every distinct condition the interface can be in, you write:

*State* — what the interface looks like and what information is present.
*Entry event* — what caused the interface to arrive in this state.
*Information shown* — what the user can see and read.
*Available actions* — what the user can do from here.
*Feedback* — what the interface communicates about actions in progress.
*Exit conditions* — what causes the interface to leave this state.
*Failure and recovery* — what happens when something goes wrong, and what path leads back.

That last field is where most designs are incomplete. Failure states are not edge cases to be handled later — they are requirements to be designed now, because the failure state is often the moment when the interface's honesty is most visible. A search that returns nothing and says "No results" is making a claim. A search that couldn't complete because the catalog service timed out and says "No results" is making a different claim — a false one. The user concludes there is nothing relevant, when in fact nothing was checked.

This distinction is not cosmetic. For the resource assistant, it matters whether a student believes no eligible resource exists versus believing the search didn't complete. Those lead to different next actions: in the first case, revise the question; in the second, try again or use a different route. An interface that collapses both into the same message is making a design decision that produces incorrect behavior by omitting the information the user needs to act.

<!-- → [TABLE: Three-row table. Columns: Condition, What it means, Proposed message purpose, Next action available. Rows: Search completed, no eligible match (the catalog was checked and found nothing matching this query — explain the search result — revise the question or browse the catalog), Search did not complete (the catalog service failed or timed out — explain the operational failure — retry or use an alternative route), Source exists but cannot be opened (the resource is in the catalog but the link is broken or access restricted — explain the access limit — show the reference and an alternative path). Caption: Collapsing these three into "No results" makes a false claim in two of the three cases. Each requires a different message and a different next action.] -->

---

## Drawing Alternatives That Actually Differ

The chapter's core exercise is building two interaction concepts for the same journey. The requirement is that they actually differ in behavior, not just in visual treatment.

For the resource assistant, a meaningful behavioral difference is this: one concept shows search results as a list with an inline source preview expanded within the same view; the other shows results as a list that opens a separate detail view when tapped. These are genuinely different behaviors with genuinely different consequences.

The inline preview keeps the user in context — the query and the other results remain visible while they examine one resource. But the available space for the preview is constrained by the list, so the preview is necessarily compressed. The separate detail view gives the resource room to be presented fully, but the user loses sight of the other candidates and has to navigate back to compare.

Both are reasonable choices. Neither is obviously correct without knowing more about the audience and the task — whether users typically compare several resources before selecting one, or whether they tend to identify one candidate and inspect it deeply. That's an empirical question. The interaction design exercise is to make the behavioral trade-off explicit, not to guess the answer.

Changing the corner radius of a button does not produce a competing interaction concept. It produces the same interaction concept in two different visual styles. The exercise is behavioral.

The states you need for the resource assistant flow: initial (before any query), loading (query submitted, waiting), results (candidates returned), no-results (catalog checked, no match), failed-lookup (catalog not reached), source-detail (one resource being examined), inaccessible-source (resource in catalog, link broken), and error (something unexpected went wrong). Not every state needs an elaborate separate screen. A clear annotation defining a transition is sufficient until the prototype supports it. But every state needs to be named and accounted for — because an unnamed state is a state the design has decided not to think about.

<!-- → [DIAGRAM: Branching flow diagram for resource assistant. Start: Initial state. Arrow to Loading on query submit. Arrow from Loading to Results, No-results, and Failed-lookup. From Results, arrow to Source-detail and back. From Source-detail, arrow to Inaccessible-source on broken link. Each terminal state (No-results, Failed-lookup, Inaccessible-source) shows a distinct message and a distinct next action. No two terminal states share the same message. Caption: Every branch that terminates needs a message and a next action. If two branches show the same message, one of them is wrong.] -->

---

## Visual Hierarchy as a Design Decision

Visual hierarchy is not decoration. It is the specification of what must be understood first.

On a resource recommendation, the question of what comes first is a design decision with real consequences. If the resource title is visually dominant and the match explanation is subordinate, the user learns what the resource is before they understand why it was suggested. If the match explanation is dominant, the user encounters the reasoning before the label. These produce different cognitive sequences and different decision behaviors. Neither is inherently correct — but the choice should be deliberate.

Define text roles before selecting visual treatments: page heading, resource title, explanation, source reference, status, action, and supporting detail. Assign each role a typographic position in the hierarchy. Keep the same roles consistent across both interaction concepts — otherwise you're not comparing the behavioral difference between inline preview and separate detail view; you're comparing a well-organized design against a poorly organized one, which doesn't tell you anything useful about the behavioral question.

Stress test the hierarchy before you commit to it. Replace the resource title with a title that is three lines long. Remove the description entirely. Resize the frame to a narrow mobile viewport. Now look at what the hierarchy shows. Is the source reference still visible? Is the action — open source, revise query, retry — still within the useful reading sequence, or has it been pushed below the fold by the long title?

A hierarchy that works with clean, well-proportioned content and fails with real content has not been designed. It has been illustrated. The stress test is where you find out which one you built.

---

## Accessibility as Specified Behavior

Accessibility is not a post-hoc audit step. It is a set of behaviors that are designed or not designed.

The behaviors at stake in an interaction design are specific. Keyboard order: can a user navigate the entire journey using only a keyboard, in a sequence that makes sense? Focus visibility: when a user is navigating by keyboard, is the current location visible on screen? Control labels: does each interactive element have a label that describes what it does, not just what it looks like? Status announcements: when something changes — a search completes, an error occurs, new content loads — is that change communicated to users who aren't watching the screen?

WCAG 2.2 names these precisely: 2.1.1 Keyboard, 2.4.7 Focus Visible, 2.4.6 Headings and Labels, 4.1.3 Status Messages. The chapter doesn't ask you to memorize criterion numbers. It asks you to annotate your Figma frames with the intended behavior for each — and then, critically, to name the later check that would verify the annotation.

A Figma annotation records intent. It does not establish that the implemented interface supports that behavior. An annotation that says "focus moves to the first result after search completes" is a requirement. Verifying it requires loading the interface in a browser and tabbing through it. Those are different activities and they happen at different times. The annotation tells the implementer what to build; the later check tells you whether they built it.

Do not ask Claude whether a screen "is accessible." That question produces a general answer about what accessibility usually requires. What you need is a specific answer about what your specific design requires. Ask for it in terms of specific criteria and specific annotated behaviors — and then treat the answer as a hypothesis that requires implementation testing, not a finding.

<!-- → [TABLE: Accessibility behavior annotation structure. Columns: WCAG Criterion, What it requires, How to annotate in Figma, Later check required. Rows: 2.1.1 Keyboard (all functionality available via keyboard — annotate tab order with numbered sequence on each interactive element — load in browser, navigate with Tab only, verify sequence and completeness), 2.4.7 Focus Visible (focus indicator visible on all focused elements — annotate intended focus ring color/weight on each interactive element — load in browser, check focus ring visibility at each stop), 2.4.6 Headings and Labels (headings and labels describe topic or purpose — annotate semantic role for each text element — inspect rendered HTML for correct heading levels and label associations), 4.1.3 Status Messages (status changes announced without focus moving — annotate which messages are live regions — load with screen reader, verify announcements on search complete and error states). Caption: Each annotation is a requirement. Each check is evidence. They are not the same thing and they do not happen at the same time.] -->

---

## Conducting the Critique

The critique exercise runs in two directions. First you ask Claude to evaluate the design. Then you evaluate the evaluation.

The prompt structure matters. Ask for located findings — findings that name a specific frame or state — rather than general observations. Ask for the likely consequence of each issue, not just a description of it. Ask for what evidence would confirm the finding, which separates observations about the visible design from inferences about runtime behavior.

```
Review concepts A and B against the stated journey.
For each finding provide:
  frame or state,
  observable issue,
  likely consequence,
  evidence needed to confirm,
  and a possible revision.
Separate what is visible in the frames from inferred runtime behavior.
Do not change the design.
```

A finding that says "the no-source state looks confusing" is not a located finding. A finding that says "in Frame 4 (no-source state), the message 'Nothing found' does not distinguish between a completed search and a failed lookup — a user who receives this after a timeout may incorrectly conclude there is no relevant material" is located, consequenced, and specific about what evidence would confirm it.

Now evaluate the evaluation. Several failure modes appear reliably in AI design critique.

The simplification proposal is the most common. In the worked example for this chapter: Claude recommends removing the no-source state because it makes the flow longer. The no-source state is a requirement — it is the boundary that distinguishes "nothing eligible exists" from "something failed." Removing it would allow a failed lookup to appear as a false conclusion about the catalog's contents.

The correct response is not to reject the concern. The correct response is to separate the concern — the state might be unnecessarily verbose — from the proposed solution — remove it entirely. Investigate whether the message can be shorter. Revise it to state what is missing and what the user can do next. Preserve the state.

Extracting a useful concern from a proposed change while rejecting the change itself is the specific skill this chapter is building. Claude can observe that a state feels heavy or that the message is long. It cannot observe whether the state is required by the design's integrity constraints. That determination belongs to the person who holds the requirements.

The same pattern appears in portfolio contexts. Claude may suggest removing the limitations section of a case study to make the work appear stronger. The correct response is to improve the wording and placement of the limitation, not to remove it. A case study without limitations is not a stronger case study — it is a less credible one.

---

## The Finding Ledger

Critique output without a decision record is noise. For every finding Claude produces, record the disposition: accept, reject, or investigate.

Accept means the finding identifies a real problem and the proposed revision or direction is appropriate. Document what was changed.

Reject means the finding identifies either a non-problem or a real problem with an unacceptable proposed solution. The rejection must cite a specific requirement, a specific annotation, or a specific constraint — not a general preference. "I prefer this layout" is not a rejection. "The proposed revision would remove the required operational-error state, which violates the separation between no-match and failed-lookup" is a rejection.

Investigate means the finding may be real but the evidence isn't in the design files — it would require runtime testing, participant observation, or implementation inspection to confirm. Note what the test would be.

The finding ledger is part of the submission. It is evidence that the critique was conducted, that the output was evaluated, and that the decisions were yours. A ledger full of "accept" entries is a flag: it suggests the critique was treated as instruction rather than as a set of hypotheses to evaluate.

<!-- → [TABLE: Finding ledger structure with example entries. Columns: Finding ID, Frame/State, Observable Issue, Consequence, Evidence Needed, Proposed Revision, Disposition, Reason or Next Step. Example row 1: (F-01 — Frame 4 No-source state — Message "Nothing found" doesn't distinguish search complete from failed lookup — User may conclude no resource exists after a timeout — Runtime: observe message after simulated timeout — Add distinct messages for each condition — Accept — Preserves required state boundary, message revised to specify condition). Example row 2: (F-02 — Frame 4 No-source state — State adds length to flow — Users may feel lost — Observation of participant behavior — Remove no-source state — Reject — State is required by design; no-match and failed-lookup must be distinguishable; message revised to be more concise instead). Caption: Every disposition requires a reason. A ledger full of "accept" entries suggests the critique was treated as instruction.] -->

---

## What Would Change My Mind

The argument that behavioral interaction specification should precede visual direction is strong when the development environment supports separation of those concerns. In a context where design and implementation are highly coupled — rapid prototyping with a live environment, or a system where visual choices directly constrain behavioral possibilities — the sequencing may need to be different. If the visual system imposes hard constraints on what behaviors are feasible, you may need to understand those constraints before you can specify behaviors. This chapter assumes more separation than some workflows have. When the separation is real, specify behavior first. When it isn't, specify it simultaneously and document the coupling.

## Still Puzzling

The finding ledger's "investigate" category is doing real work, but the chapter doesn't specify what happens to investigate entries at submission. If they remain open at A2, the submission contains findings the student hasn't resolved. That might be the honest answer — some things require implementation testing that hasn't happened yet — but the rubric should specify how unresolved investigations are evaluated. An open investigation is not a failure if it names the test. It is a failure if it names nothing and leaves the finding dangling.

---

## Practice

1. Write the complete state record for the first user action in your critical journey. All seven fields.
2. Identify one transition in your current prototype that is visible in the design but not specified — where the behavior on arrival or departure is implicit rather than stated.
3. Produce an alternative interaction concept that differs from your current one in behavior, not just visual treatment. Name the behavioral difference in one sentence.
4. Write distinct messages for the three conditions: search completed with no match, search did not complete, and source exists but cannot be opened. Confirm each message implies the correct next action.
5. Define the return path from source detail to the results list. Specify whether the query and results are preserved or lost, and why.
6. Stress your primary results frame with a resource title that is three lines long and a missing description. Note what breaks.
7. Assign text roles across both interaction concepts — heading, title, explanation, status, action, supporting detail — and confirm they are consistent between alternatives.
8. Annotate the keyboard order for your primary flow in Figma. Number each interactive element in tab sequence. Then name the later check that would verify the annotation.
9. Ask Claude for a located critique of one specific state using the prompt structure from this chapter. Confirm each finding names a frame, an observable issue, a consequence, and required evidence.
10. Select one finding from the critique and reject it. Write the rejection with a specific requirement, annotation, or constraint as the basis. Not a preference — a constraint.
11. Select one finding from the critique and mark it "investigate." Name the specific test — runtime, participant observation, or implementation inspection — that would resolve it.
12. Build the finding ledger for your critique session. Count the accept, reject, and investigate dispositions. If all are accept, identify one finding that should have been challenged.
13. Apply the simplification proposal test: identify one state in your design that Claude could plausibly suggest removing to shorten the flow. Write the argument for why it must be preserved, or the criteria under which you would accept its removal.
14. Defend your selected interaction concept in writing, addressing hierarchy, behavioral trade-offs, and accessibility intent. Your argument may not use the phrase "I prefer."
15. Name two things about your interaction design that still require implementation testing to verify, and write the specific test for each.
