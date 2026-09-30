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

Three questions belong inside these fields that most students skip entirely.

*Transition conditions:* what must be true before an event produces a transition? A search can't move from Loading to Results unless the catalog responds with a parseable payload. If it responds with an error, the transition is to Failed-lookup, not to Results. The condition governs which branch fires.

*Preserved information:* which elements of context survive a state change? Does the query persist when the user opens a detail view and returns? Do the results? Does the scroll position? For the resource assistant, if a student opens a resource, reads it, and comes back, finding their query gone is an unexpected cost. That cost should be a design decision, not an implementation accident.

*Asynchronous behavior:* what happens when responses arrive out of order? A student submits a query, revises it, submits again. The second response arrives first. Then the first response arrives. Which results does the interface show? This scenario can't be depicted in any static screen. It can only be specified in a state record. If it isn't specified, the implementation will choose — and the implementation's choice may produce a result that's incorrect and invisible.

The failure and recovery field is where most designs are genuinely incomplete. Failure states are not edge cases to be handled later — they are requirements to be designed now, because the failure state is often the moment when the interface's honesty is most visible.

A search that returns nothing and says "No results" is making a claim. A search that couldn't complete because the catalog service timed out and says "No results" is making a different claim — a false one. The user concludes there is nothing relevant, when in fact nothing was checked.

And there is a third case worth understanding clearly: even a completed search that returns no matches does not establish that no eligible resource exists. The catalog may be incomplete. Indexing may lag. A ranking threshold may have excluded suitable resources. The honest interface describes the scope of what was checked and the result of that check. It does not imply exhaustive knowledge.

<!-- → [TABLE: Four-row table. Columns: Condition, What the system can establish, Illustrative message, Recovery action. Rows: Completed search, zero matches (this search returned no matches within its scope — "We didn't find matches for this query." — Edit query, adjust filters, browse catalog), Search failed (the requested search did not complete — "We couldn't complete the search. Your query is saved." — Retry or use another route), Partial search (only part of the intended collection was checked — "Results may be incomplete — one collection is unavailable." — Inspect available results or retry later), Resource cannot be opened (a catalog record exists but access failed — "This resource is listed, but we couldn't open it." — View citation or alternate access). Caption: Do not label a link "broken" or "restricted" unless the system can distinguish those causes. Describe what happened, not what you inferred.] -->

---

## States and Screens Are Not the Same Thing

A screen is a visual frame — a layout, a viewport, a rendered page. A state is a condition the interface is in. Several states can share a single screen. An expanded inline preview coexists with the results list; both are states on the same screen. Conversely, one state can render differently at different viewport sizes or in different accessibility contexts.

The state record specifies behavior. The screen depicts one visual instantiation of a state. You need both, and you need them in dialogue. A screen without a state record is a picture. A state record without a screen is an abstraction. The pair constitutes a specification.

This distinction lets you name all the states that need specifying without artificially inflating the screen count. Eight states — initial, loading, results, no-results, failed-lookup, source-detail, inaccessible-source, error — don't require eight elaborate frames. Some share a frame with different annotations. Some require only a transition annotation until a prototype can instantiate them. But every state needs to be named, because an unnamed state is a state the design has decided not to think about.

---

## Drawing Alternatives That Actually Differ

The chapter's core exercise is building two interaction concepts for the same journey. The requirement is that they actually differ in behavior, not just in visual treatment.

For the resource assistant, a meaningful behavioral difference: one concept shows search results as a list with an inline source preview expanded within the same view; the other shows results as a list that opens a separate detail view when tapped.

These are genuinely different behaviors with genuinely different consequences — and the consequences are hypotheses, not certainties. The inline preview keeps the query and other results visible while the user examines one resource, which may support comparison. But expanded content within a list view increases scrolling and may crowd the visible candidates. The separate detail view dedicates space to one resource, which may support deep inspection. But it requires navigation back to compare candidates.

Both are reasonable designs. Neither is obviously correct without knowing whether your audience is primarily comparing candidates or primarily inspecting one at a time. The design exercise is to make the behavioral trade-off explicit, and to name the evidence that would distinguish them.

Changing the corner radius of a button does not produce a competing interaction concept. It produces the same interaction concept in two visual styles. The exercise is behavioral.

<!-- → [TABLE: Three-row table. Columns: Design question, Inline preview hypothesis, Separate detail hypothesis, Evidence to collect. Rows: Comparing candidates (visible context may support comparison across results — repeated navigation may interrupt comparison — selection errors, backtracking, task completion on a comparison task), Inspecting one resource (expansion may increase scrolling or crowd list — dedicated space may support detailed reading — ability to locate and interpret required information in the allotted space), Returning to search (context remains available throughout session — depends on how well return navigation restores state — query, filters, scroll position, and focus after returning). Caption: These are hypotheses to investigate, not predictions. Name them before testing so you know what you're looking for.] -->

---

## Visual Hierarchy as a Design Decision

Visual hierarchy is not decoration. It is the specification of what must be understood first.

On a resource recommendation, what comes first is a design decision with real consequences. If the resource title is visually dominant and the match explanation is subordinate, the user learns what the resource is before they understand why it was suggested. If the match explanation is dominant, the user encounters the reasoning before the label. These produce different reading sequences and different decision behaviors. Neither is inherently correct — but the choice should be deliberate, and it should be consistent across both alternatives you're comparing. Otherwise you're not comparing inline preview versus separate detail view — you're comparing a well-organized design against a disorganized one.

Define text roles before selecting visual treatments: page heading, resource title, explanation, source reference, status, action, supporting detail. Assign each role a typographic position in the hierarchy.

Stress test the hierarchy before you commit to it. Replace the resource title with a title that is three lines long. Remove the description entirely. Resize the frame to a narrow mobile viewport. Now look at what remains visible and in what order. Is the source reference still in the reading sequence? Is the action — open source, revise query, retry — accessible without scrolling?

A hierarchy that works with clean, well-proportioned content and fails with real content has not been designed. It has been illustrated. The stress test is where you find out which one you built.

One accessibility dimension connects directly here: WCAG 1.4.10 Reflow requires that content can be presented without horizontal scrolling at 400% zoom or 320 CSS pixels wide. Being below the fold is not itself a failure — losing information or functionality is. Design the hierarchy so the critical content reflows, not just renders in the ideal case.

---

## Accessibility as Specified Behavior

Accessibility is not a post-hoc audit step. It is a set of behaviors that are designed or not designed at the interaction layer.

Before listing criteria: WCAG 2.2 criteria address different levels of the implementation stack, and conflating them produces annotations that don't match the check they're supposed to enable. Descriptive wording (2.4.6 Headings and Labels) is different from programmatic structure (1.3.1 Info and Relationships) and accessible names (4.1.2 Name, Role, Value). A label can be descriptively clear and semantically wrong. A heading can be programmatically correct and meaningless. These require different annotations and different checks.

For an interaction design in Figma, the work at this stage is annotation — recording intent — not verification. Verification requires the rendered implementation. Every annotation implies a later check.

*2.1.1 Keyboard:* all functionality operable without a mouse. This means more than reaching controls with Tab — it means activating them with the correct keys, and operating composite widgets (like an expanded inline preview) with the keys convention expects. Tab moves between controls; Enter and Space activate them; arrow keys navigate within widgets. Annotate which keys operate which elements.

*2.4.3 Focus Order:* focus must move in a sequence that preserves meaning and operability. For a dynamic interface where results appear after a search or a preview expands, the focus destination after a state change is a design decision. Where does focus land when results load? When a preview expands? When the user returns from a detail view? These belong in the state record's exit conditions, not to be decided at implementation time.

*2.4.7 Focus Visible and 2.4.11 Focus Not Obscured:* when a user navigates by keyboard, the focused element must have a visible indicator, and that indicator must not be completely hidden by author-created content — sticky headers, overlays, banners.

*2.4.6 Headings and Labels:* wording describes topic or purpose. This is about semantic accuracy: a heading that says "Results" is acceptable. A heading that says nothing about what the results are, or that has the wrong heading level, fails even if it's styled correctly.

*4.1.3 Status Messages:* when something changes — a search completes, an error occurs, new content loads — that change must be communicated to users who aren't watching the screen, without moving focus. Status messages are not focus moves. For a search that returns results, a reasonable implementation announces a concise summary ("3 results found") while leaving focus in place. The results list is not itself a status message; navigation to the list is a separate interaction.

Do not default to moving focus to the first result after a search. For an in-place update, retaining focus and announcing a summary is often the better behavior. Document the decision and the reasoning in the state record.

<!-- → [TABLE: Accessibility annotation structure. Columns: WCAG Criterion, What it requires, Annotation in Figma, Later check required. Rows: 2.1.1 Keyboard (all functionality via keyboard, including activation and widget interaction — annotate keys for each element: Tab to reach, Enter/Space to activate, arrows within widgets — complete all tasks using only keyboard, including widget interaction), 2.4.3 Focus Order (focus sequence preserves meaning — annotate focus destination after each state change: results load, preview expands, return from detail — check forward and reverse, including conditional content and transitions), 2.4.6 Headings and Labels (wording describes topic or purpose — annotate semantic role and heading level for each text element — inspect rendered HTML heading levels and label associations), 2.4.7 + 2.4.11 Focus Visible and Not Obscured (indicator visible and not hidden by overlays — annotate indicator appearance; flag sticky elements that might obscure it — check visibility at each focus stop, including under sticky elements), 4.1.3 Status Messages (status announced without focus moving — annotate which messages are live regions and what they announce — test with screen reader on search complete, error, and partial results). Caption: Each annotation is a requirement. Each check is evidence. They happen at different times and one does not substitute for the other.] -->

---

## Conducting the Critique

The critique exercise runs in two directions. First you ask Claude to evaluate the design. Then you evaluate the evaluation.

The research on AI design critique is specific enough to inform expectations. A study by Duan and colleagues evaluated GPT-4 feedback on 51 interfaces and found it useful for identifying subtle errors, improving text, and considering interface semantics. Importantly, the system evaluated one static mobile screen at a time — it could not evaluate interactivity, cross-screen consistency, or task flows. Feedback became less useful across repeated iterations. A companion dataset (UICrit) shows that structured prompting and targeted examples improve automated critique quality. The practical implication: AI critique is useful for what it can see — layout, visible text, static structure — and structurally limited for what it cannot — runtime behavior, timing, state transitions, focus movement.

Your prompt should ask for findings about the visible design and explicitly request that inferences about runtime behavior be labeled as such:

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

Now evaluate the evaluation.

The simplification proposal is the most common AI critique failure for interaction design: recommend removing a state or condition because it makes the flow longer. In the worked example: Claude recommends removing the no-source state because it makes the flow longer. The no-source state is a requirement — it is the boundary that distinguishes "nothing eligible exists" from "something failed." Removing it would allow a failed lookup to appear as a false conclusion about the catalog's contents.

The correct response is not to reject the concern. The correct response is to separate the concern — the state might be unnecessarily verbose — from the proposed solution — remove it entirely. Investigate whether the message can be shorter. Revise it to state what is missing and what the user can do next. Preserve the state.

There is a subtler failure worth naming: the persuasive rationale. Research by Bansal and colleagues found that AI explanations increased acceptance of AI recommendations whether or not the recommendation was correct. A fluent argument for removing the no-source state is not evidence that removing it is right. The argument's quality and the conclusion's correctness are independent. Evaluate the substance, not the confidence.

Extracting a useful concern from a proposed change while rejecting the change itself is the specific skill this chapter builds. Claude can observe that a state feels heavy or a message is long. It cannot observe whether the state is required by the design's integrity constraints. That determination belongs to the person who holds the requirements.

---

## The Finding Ledger

Critique output without a decision record is noise. For every finding Claude produces, record two things separately: your assessment of the finding, and your decision about the revision. These are different judgments and they should not be collapsed.

*Finding assessment* — three values: Supported (the finding identifies a real issue visible in the supplied design), Unsupported (the finding claims something the design files don't demonstrate), Unresolved (the finding may be real but requires runtime or participant evidence to confirm).

*Revision decision* — four values: Adopt (the proposed direction is appropriate), Modify (the concern is valid but the proposed revision is wrong — accept the concern, reject the solution), Decline (the finding is unsupported or the revision violates a requirement), Defer (the finding is real and the revision may be right, but can't be evaluated without information not yet available).

The worked example in this chapter — the no-source state — is a case where the finding is Supported and the revision decision is Modify. The concern (verbosity) is valid. The solution (delete the state) is not. Collapsing both into a single accept/reject field makes that distinction invisible and prevents students from demonstrating the most important judgment this chapter teaches.

A ledger full of Adopt entries is a flag: it suggests the critique was treated as instruction. But the opposite error is equally real — manufacturing disagreement regardless of merit. The goal is not a particular distribution of dispositions. It is to demonstrate that each finding was evaluated against a specific requirement, annotation, or constraint, and that the decision was yours.

<!-- → [TABLE: Finding ledger with two example entries. Columns: ID, Frame/State, Observable Issue, Consequence, Evidence Needed, Proposed Revision, Finding Assessment, Revision Decision, Reason/Next Step. Row 1: F-01 — Frame 4 No-source state — "Nothing found" doesn't distinguish completed search from failed lookup — User after timeout may conclude no resource exists — Runtime: observe message after simulated timeout — Add distinct messages per condition — Supported — Adopt — Message revised to specify condition; required state boundary preserved. Row 2: F-02 — Frame 4 No-source state — State adds length to flow — Users may feel lost — Observation of participant behavior — Remove no-source state — Supported — Modify — Concern valid (message may be verbose); revision not (state required for no-match/failed-lookup distinction); message shortened instead. Caption: Row 1 accepts both the finding and the remedy. Row 2 accepts the finding and rejects the remedy. The two-field structure makes that distinction explicit.] -->

---

## The Coverage Check

The finding ledger evaluates what Claude mentioned. It doesn't reveal what Claude missed.

After recording dispositions on every finding, run an independent coverage check against the journey. Work through the complete flow — failed search, partial results, late responses, return navigation, keyboard operation, recovery from each terminal state — and for each element, ask: did the critique address this? If not, is it because the element is fine, or because the static-screen evaluation couldn't reach it?

Mark uncovered elements. Some will be genuinely fine — note why. Some will be genuinely problematic — add them to the ledger as your own findings. Some will be uncertain — they become investigations.

This step exists because the most dangerous critique result is a clean ledger with a large gap. A ledger that doesn't cover asynchronous behavior, return navigation, or keyboard operation has told you nothing about those things. The coverage check makes the gap visible.

---

## Resolving Unresolved Investigations

A Defer or Unresolved entry in the ledger does real work — it names something that can't yet be evaluated. But it creates a grading problem: how do you evaluate an open investigation at submission?

The answer is not whether the investigation is resolved. It is how precisely it is bounded.

A passing open investigation names a specific testable mechanism. "Runtime test required: monitor screen reader output via VoiceOver when focus returns from the detail view after a keyboard-triggered expansion. Acceptable outcome: focus returns to the trigger element or the next logical position; screen reader announces the collapsed state." This proves the student understands what information is missing and how to acquire it, even if the runtime environment isn't available yet.

A failing open investigation defers design responsibility without establishing an evidentiary standard. "Need to check if users like this." That is not an investigation — it is an undecided opinion.

The structure for a complete investigation entry:

*Specific question:* what exactly remains unknown.
*Missing evidence:* why it can't yet be resolved.
*Test and expected observation:* what you would do, and what outcome would confirm or disconfirm.
*Consequence if wrong:* what matters if the finding turns out to be real.
*Interim decision:* whether work can proceed, and under what assumption.

That last field prevents indefinite deferral. "Work can proceed on the assumption that keyboard navigation is handled conventionally; this assumption must be verified before A3 submission" is a bounded, time-limited choice. "TBD" is not.

---

## What Would Change My Mind

The argument that behavioral specification should precede visual direction assumes that design and implementation are separable concerns. In workflows where they're tightly coupled — rapid prototyping with a live environment, or systems where visual choices directly constrain what behaviors are feasible — the sequencing may need to be different. This chapter assumes more separation than some workflows have. When the separation is real, specify behavior first. When it isn't, specify it simultaneously and document the coupling.

## Still Puzzling

The coverage check depends on the student knowing what the journey's states are — which is exactly what the state record exercise is supposed to establish. A student who missed a state in the state record will also miss it in the coverage check, since they're working from the same mental model. An external journey checklist would make the coverage check more robust, but it also does some of the student's analytical work for them. The right level of scaffolding here is genuinely unclear, and probably depends on how far into the course this chapter appears.

---

## Practice

1. Write the complete state record for the first user action in your critical journey. All seven fields, including transition conditions, preserved information, and asynchronous behavior.
2. Identify one transition in your current prototype that is visible in the design but not specified — where the behavior on arrival or departure is implicit rather than stated.
3. Name a scenario where two responses to two successive queries could arrive out of order. Write the transition condition that determines which results the interface shows.
4. Produce an alternative interaction concept that differs from your current one in behavior, not visual treatment. Name the behavioral difference in one sentence.
5. Write distinct messages for all four search conditions from this chapter: completed with no match, did not complete, partial results available, source exists but cannot be opened. Confirm each implies the correct next action without overclaiming what the system established.
6. Define the return path from source detail to the results list. Specify whether query, results, and scroll position are preserved or lost — and why each was a deliberate choice.
7. Stress your primary results frame with a resource title that is three lines long and a missing description. Then resize to 320px wide. Note what reflows acceptably and what breaks or disappears.
8. Assign text roles across both interaction concepts — heading, title, explanation, status, action, supporting detail — and confirm they are consistent between alternatives.
9. Annotate the keyboard order for your primary flow. For each interactive element, name the key that activates it (not just that Tab reaches it). Then name the later check that would verify the annotation against the rendered implementation.
10. Annotate the focus destination after three state changes: search results load, inline preview expands, user returns from detail view. For each, explain why that destination preserves meaning and operability.
11. Ask Claude for a located critique of one specific state using the prompt structure from this chapter. Confirm each finding names a frame, an observable issue, a consequence, and required evidence. Flag any finding that makes runtime inferences without labeling them as such.
12. Select one finding and complete the full two-field ledger entry: finding assessment and revision decision, separately. If the finding is Supported and the revision decision is Modify, write out the distinction between the accepted concern and the rejected remedy.
13. Run the coverage check on your critique session. List the journey states Claude addressed and those it didn't. For one uncovered state, assess whether the gap is because the state is fine, because the static-screen evaluation couldn't reach it, or because you missed it in the state record.
14. Select one Defer or Unresolved entry from your ledger. Write the complete investigation entry: specific question, missing evidence, test and expected observation, consequence if wrong, and interim decision. Confirm the interim decision is time-limited.
15. Defend your selected interaction concept in writing. Address hierarchy decisions, behavioral trade-offs, and accessibility intent. Your defense may not use the phrase "I prefer."
