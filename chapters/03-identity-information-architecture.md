# Chapter 3 — Identity and Information Architecture with AI
*What your navigation choices say about you before anyone reads a word.*

Here is a portfolio that looks professional. Three top-level sections: Python, Figma, AI. Clean labels, consistent typography, everything in its place.

A reviewer arrives. They want to know one thing: can this person design a system that solves a real problem, make defensible decisions under constraint, and separate their own judgment from what an AI produced? They open Python. They find code. They open Figma. They find screens. They open AI. They find a description of tools used.

The problem they're trying to solve — understanding your design judgment — is distributed across three sections with no connecting thread. They have to reconstruct your project from fragments, infer what you decided versus what Claude generated, and guess at the relationship between the screens and the code.

They close the tab.

Not because the work is bad. Because the architecture hid it.

Information architecture is not decoration. It is not the color scheme or the font. It is the set of decisions that determine what belongs together, how things are named, and how a person moves from where they are to what they need. Those decisions communicate something about you before anyone reads a word of your writing — and they determine whether a reviewer can actually inspect the evidence you've assembled.

---

## The Decision You Are Designing For

Before drawing a single frame, write this sentence at the top of your FigJam board:

*After this journey, the audience should be able to decide: [specific decision] — using: [evidence available in the experience] — without: [unacceptable confusion or unsupported inference].*

This is not a mission statement. It is an architectural constraint. Every navigation decision you make should be testable against it.

For the resource assistant: the decision is whether a specific resource is relevant enough to open for a specific task. The evidence needed is the source identity, the description, and whatever basis exists for the match. What you're preventing is the inference that "recommended" means "answers every part of your question."

For the portfolio: the decision is whether your contribution is relevant to a prospective collaboration. The evidence needed is the problem you worked on, what you specifically decided, what Claude contributed, and what result was produced. What you're preventing is the inference that a team achievement was entirely your work, or that a tool listed implies mastery of it.

Notice what this does. It forces you to specify who is making the decision, what information they need, and what they might wrongly conclude from an incomplete presentation. All three of those are architecture problems, not writing problems. You can't solve them by adding more descriptive text. You solve them by making the right objects visible, accessible, and connectable.

The reason this matters more now than it did five years ago is specific. When AI made fluent writing cheap, employers shifted toward verifiable work history. When persuasive cover letters cost nothing to produce, the signal value of well-written applications collapsed, and reviewers moved weight toward prior work samples and identifiable contributions. An architecture that routes every claim directly to its evidence is building for the signal that still carries information — because it's the only signal that can't be generated without the underlying work.

<!-- → [DIAGRAM: Two portfolio architectures side by side. Left: tool-first with three top-level nodes (Python, Figma, AI), project fragments scattered beneath each, dashed line showing reviewer's path hopping across branches to reconstruct one project story. Right: project-first with one node (Resource Discovery) containing problem, decision, contribution, AI disclosure, and evidence, with tools as a secondary facet. Annotation on each: "Steps from claim to nearest evidence: 4" and "Steps from claim to nearest evidence: 1." Caption: Same content. Different architecture. The reviewer's experience of the work is entirely different.] -->

---

## Objects Before Pages

The most common information architecture mistake is beginning with pages. "I'll have a Home page, a Projects page, an About page, a Contact page." This is copying the shape of familiar websites rather than thinking about what information exists and how it relates.

The correct starting point is objects: the distinct kinds of content that exist in the experience, each with its own identity and required fields.

For the resource assistant, the core objects are: a question (what the student asked), a resource (an approved catalog entry with source identity and description), a recommendation (the relationship between a specific question and a specific resource, with whatever matching basis exists), and a no-source response (the state when nothing in the catalog can support the request).

Notice that the recommendation is its own object, not a property of the resource. The same resource can be relevant to different questions for different reasons. A relevance explanation belongs to a specific question-resource pair, not to the resource permanently. Putting it permanently on the resource record would mean one question's explanation overwrites another's — or you'd have to show all of them, which may be misleading. Getting the object model right prevents a class of design errors before you've drawn anything.

For the portfolio, the core objects are: a project (a bounded piece of work with a problem and a status), a contribution (what you specifically did within that project, described in terms of decisions made, not tools used), an evidence artifact (a document, file, or record that supports a claim about the project), and a limitation (what the project doesn't establish, or what evidence is unavailable).

The limitation object is the one most portfolios omit. Its presence is what makes the rest of it credible.

Give each object a stable identifier that doesn't change when you update the display label. "Resource Discovery" can become "Finding Course Resources" without breaking every evidence reference — if the internal identifier stays fixed and the display label is what changes. This seems like a technical detail but it governs whether your architecture is maintainable.

<!-- → [TABLE: Content object inventory structure. Columns: Object, Stable ID, Required fields, What it supports, What a filled field doesn't establish. Rows: Resource (resource-001 — title, source location, approved description, eligibility status, limitations — audience's decision about whether to open it — that the description is accurate or the resource answers the question), Recommendation (rec-001 — question reference, resource ID, matching basis, explanation status — showing why a match was surfaced — that the match is correct or the explanation is reliable), Project (project-001 — problem, contribution IDs, decision IDs, evidence IDs, version, limitations — reviewer's assessment of contribution — that achievements were solely the individual's or that a prototype is deployed), EvidenceArtifact (artifact-001 — title, type, location or access status, credited contributors, supported claim IDs — inspecting a specific claim — that the artifact proves the claim, or that a private link is public evidence). Caption: A filled field is not proof that its contents are true. The object model determines what can be verified; it doesn't verify it.] -->

---

## Three Graphs, Not One

When you draw your FigJam diagram with boxes and lines, you need to know which kind of relationship each line represents. There are three, and they have different rules.

The first is containment: "is part of." A project contains contributions. A project contains evidence artifacts. In a strict containment hierarchy, cycles are never valid — a project cannot be part of itself, and two projects cannot each be part of the other. If you find a cycle in your containment graph, it is an error.

The second is reference: "cites" or "is evidence for." A project cites several evidence artifacts. A decision cites the brief that preceded it. Reference graphs allow cycles — two documents can cite each other — and they normally allow an artifact to be cited by multiple claims. A reference relationship doesn't imply navigation; you can cite an artifact without making it a separate navigable destination.

The third is navigation: "links to." A project detail view links to the project list. The project list links to each project. Navigation graphs allow return paths and often require them — returning to the list is the intended behavior, not an architectural error.

The structural audit that matters is running the right rule on the right graph. "No cycles" is appropriate for containment. It is not appropriate for navigation. A navigation loop — project detail links back to project list, which links back to project detail — is not a defect. It is a correctly functioning return path.

Two checks matter above the others. First, claim coverage: every claim in the experience has at least one outgoing reference edge to an evidence object. A claim with no evidence destination is exactly the kind of gap that turns a portfolio into a list of assertions. Second, evidence distance: how many navigation steps separate each claim from its nearest supporting artifact. You can count this for both architectures and compare the number. It directly measures the chapter's core argument.

<!-- → [TABLE: Three-row table. Columns: Relationship type, What an edge means, Cycles valid, Multiple parents valid, The defect to check for. Rows: Containment (is part of / is filed under — no — only in declared polyhierarchy — orphans, accidental loops, duplicate IDs), Reference (cites / is evidence for — allowed but worth reviewing — normal, one artifact supports many claims — dangling references, claims with no evidence edge), Navigation (links to — often intended (return to list) — normal — dead ends, destinations reachable only one way). Caption: Run the correct rule on each graph type. A navigation cycle is not a containment error.] -->

---

## What Claude Can and Can't Reveal About an Architecture

The standard instruction — ask Claude to trace a task through each architecture — has a problem that makes it systematically misleading for this purpose.

When you give Claude both architectures at once and ask it to trace a task through each, Claude sees every destination before it chooses. A person sees one level of labels, makes a prediction, clicks, and discovers whether they were right. Claude skips the prediction step. Research on AI navigation agents confirms this: compared with human participants on multi-step tasks, agents take direct, low-branching paths while humans explore and backtrack. The agent reaches the destination with fewer steps and fewer wrong turns.

This matters because information architecture problems show up as wrong first clicks, backtracking, and abandonment when the scent is weak. An architecture that passes Claude's trace has demonstrated only that the correct route exists — not that a person following the labels would find it.

A better protocol runs the trace one level at a time, in a fresh message, supplying only what would be visible at that step:

```
You are testing a navigation structure one level at a time.
Task: [task]
You can see only these labels: [labels at this level]
Choose one label and explain what you expect to find behind it.
State how confident you are and what would make you go back.
Do not guess at labels you have not been shown.
```

Reveal the chosen label's children and repeat. Record every choice, including the moments Claude expresses uncertainty or proposes going back. Those moments are the architectural findings.

There is a second problem. If Claude drafted some of the labels in one architecture, asking Claude to compare the two architectures is asking it to judge its own work. Research on this is specific: language models consistently favor text written by language models over text written by humans, and the preference is stronger than human evaluators show for human-written text. Keep label drafting and label evaluation in separate conversations, and don't disclose to the evaluating conversation which labels came from which source.

What Claude's trace is genuinely useful for: generating questions to investigate, identifying ambiguous labels, and surfacing missing destinations — provided you remember that the trace is a best-case path through the architecture, not evidence of how a person would navigate it.

---

## Building Two Architectures That Are Actually Different

The comparison exercise only works if the two architectures genuinely differ. "Task-first" and "category-first" are starting points, not formulas.

For the portfolio, the two architectures that are actually different are tool-first and project-first.

In the tool-first architecture, the top-level navigation reflects what you know: Python, Figma, AI. Each section contains the work done with that tool. The taxonomy is your skill set.

In the project-first architecture, the top-level navigation reflects what you did: Resource Discovery, or whatever the project is called. The detail view contains the problem, the competing designs you considered, the one you chose, why, what Claude produced, and the evidence for the outcome. Tools appear as supporting metadata within the project, not as the organizing principle.

The worked example in this chapter shows a hypothetical student choosing project-first. The reasoning is specific: the declared audience task is inspecting a complete project contribution, and the project-first architecture keeps the contribution and its evidence in one journey. The tool inventory doesn't disappear — it becomes a secondary facet, accessible to a reviewer who wants it, but not the primary organizing logic.

That choice should be recorded before anything is built:

```
Decision: project-first primary navigation.
Audience task: inspect a complete project contribution and its support.
Reason: keeps the contribution and associated evidence within one journey.
Alternative retained: tool-based secondary access.
Known trade-off: a reviewer searching only for a particular tool may prefer
the tool-based route.
Evidence status: content mapping and design review; no participant result.
Remaining uncertainty: whether the project title is understandable to new readers.
Next inquiry: observe a reader locating the design reasoning without coaching.
Reopen the choice if: readers cannot locate the relevant project or evidence,
or the prioritized audience task changes.
```

The last line matters. This is a provisional choice based on reasoning, not a demonstrated improvement. The next line of the inquiry is actually running the first-click test.

Compare the two architectures on criteria that have nothing to do with visual finish:

Does the primary journey require a single click, or does the audience have to reassemble the story from fragments? How many steps separate each claim from its nearest evidence? Is each key destination reachable by more than one route? Can the missing-resource or no-evidence state be found and understood? When you trace the difficult journey — arriving through a direct link into a detail view, with no home page context — does the view supply enough local information to orient the reader?

These are answerable questions. "Which one looks more professional" is not.

<!-- → [DIAGRAM: Portfolio comparison. Left panel: tool-first entry showing three top-level nodes, each containing project fragments, with a path indicator showing 4 steps from "I selected the project scope" to the dated brief that supports it. Right panel: project-first entry showing one project node, with problem, decision, contribution, AI disclosure, and evidence linked within two steps. Both panels labeled with evidence distance. Caption: The comparison criterion is how many steps separate a claim from its nearest evidence, not visual finish.] -->

---

## Attribution: The Object the Chapter Gets Wrong

The portfolio's contribution object has one field that almost every student fills incorrectly: the distinction between what you did and what Claude produced.

There is an established taxonomy for this. The Contributor Roles Taxonomy, standardized as ANSI/NISO Z39.104-2022, defines fourteen roles for attributing specific contributions to named, accountable people: conceptualization, methodology, software, validation, investigation, data curation, writing, visualization, supervision, and others. Publisher policy, following the International Committee of Medical Journal Editors, is consistent: AI tools are not authors and cannot be listed in a contributor role, because they cannot take responsibility for the work. AI use is disclosed separately.

For a portfolio, this translates directly. The contribution field describes what you did, in role terms: which problems you framed, which design decisions you made, which implementations you reviewed and accepted, which you rejected. The AI disclosure is separate: Claude drafted X, implemented Y, proposed Z. I reviewed and accepted A. I rejected B. The design reasoning behind B is the most interesting part of the record.

The distinction between "I used Claude" and "Claude implemented this, which I reviewed and modified" is the difference between a tool list and evidence of judgment. The second formulation is what the project-first architecture is designed to make visible.

```
My roles: problem framing, information architecture selection,
          criteria definition, implementation review, evaluation design
Claude's contribution: label alternatives for the topic hierarchy (drafted);
                       navigation critique for both architectures (generated);
                       content contract for resource objects (drafted).
I accepted: the progressive-disclosure trace protocol with modifications.
I rejected: the suggestion to add a testimonials page — no testimonials exist
            and the brief asks reviewers to inspect project evidence, not
            social proof.
```

The rejection note is where the judgment becomes visible. Anyone can accept a reasonable suggestion. Rejecting one with a specific reason demonstrates that the decision was yours.

---

## Structure Is Honest Until the Facts Change

An architecture can become misleading when the work behind it changes. A prototype becomes deployed. An approved source is withdrawn. A result is corrected. A contribution that was individual becomes collaborative.

The labels and routes that were accurate in October can imply something false in March if they're not updated. This is not just a maintenance problem — it is an integrity problem. A portfolio that says "deployed" when the system was decommissioned is not out of date; it is inaccurate.

Attach an owner and a review trigger to each consequential claim. The trigger might be a project status change, a new version, or a changed access condition. When a claim's supporting evidence changes, inspect the routes that lead to it. When a label changes, inspect the paths that depend on it.

For the resource assistant, if the approved catalog changes — sources added, sources withdrawn, eligibility criteria revised — every route that implies a current catalog needs to be checked. A resource that was eligible last semester may not be eligible this semester. The interface doesn't know. The architecture's job is to make that kind of mismatch findable before it misleads someone.

---

## What Would Change My Mind

The argument that project-first portfolio architecture is better than tool-first for design-judgment reviewers rests on the claim that reviewers are trying to understand contribution. If the primary audience were recruiters doing keyword searches rather than collaborators evaluating judgment, the tool-first architecture might perform better for that task — because it surfaces the vocabulary they're searching for. The worked example should be understood as a choice made for a specific declared audience task, not a universal claim about portfolio structure. If your audience task is different, re-run the comparison against that task's criteria.

## Still Puzzling

The progressive-disclosure trace protocol is more honest than giving Claude the full architecture at once. But it's still a model path, and the finding about AI navigation agents — that they take direct, low-branching routes where humans explore — suggests the protocol underestimates how often a real person would backtrack or skip a level. The right calibration between "Claude's trace caught a real ambiguity" and "Claude's trace missed the problem because it navigated differently than a person would" is something I don't have a clean answer to. The protocol's output should probably be treated as a lower bound on the problems your architecture has, not an estimate of the full set.

---

## Practice

1. Write the audience decision statement for your project using the three-part structure: specific decision, evidence available, unacceptable inference to prevent.
2. Inventory five content objects for your project without naming any pages. Give each a stable ID and its required fields.
3. Identify one claim in your current design that has no accessible evidence destination. Name what evidence would close the gap.
4. Write three candidate labels for a concept your audience might not immediately recognize. For each, state what prediction it creates about what lies behind it.
5. Draw task-first navigation for your project.
6. Draw category-first navigation for the same content at the same level of detail. If one has more detail than the other, the comparison is about completeness, not architecture.
7. Trace the missing-resource or no-evidence journey through both architectures. Write down exactly where each one stops and what the audience sees there.
8. Find one intentional return path and one accidental dead end in your architecture diagram. Label both.
9. Run the progressive-disclosure trace protocol on one architecture. Record every label chosen, every moment of expressed uncertainty, and any point where the trace went back.
10. Write the contribution record for one project: your roles, Claude's contribution, one thing you accepted and why, one thing you rejected and why.
11. Compute the evidence distance for your three most important claims in each architecture. Record the numbers.
12. Identify which WCAG 2.2 navigation criteria — Multiple Ways, Consistent Navigation, Link Purpose — your chosen architecture already satisfies, and which ones remain to be addressed.
13. Run a card sort of your content inventory with Claude, then sort it yourself. Mark every item where you disagree with Claude's grouping, and decide which grouping serves your audience.
14. Attach a maintenance trigger to one consequential claim: what event would make you check whether the claim is still accurate?
15. State the condition under which you would reopen the architecture decision. Not a general condition — the specific evidence that would make you switch from your current choice to the alternative.
