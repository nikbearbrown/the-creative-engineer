# Chapter 1 — The Creative Engineer: Designing and Conducting AI
*Why the person who chooses the problem and accepts the result is not the same as the system that does the work.*

Here is the mistake almost everyone makes on the first day.

Someone opens a new conversation with an AI system and types: "Build me an educational assistant." The system produces something — a React component, a Python script, a schema, a mockup description. It arrives quickly and looks complete. The person reads it, nods, and begins building on top of it.

What just happened? Not "build me an educational tool for students working on one course task, where the tool finds eligible resources from an instructor-approved catalog, explains why a resource was recommended, and stops rather than invents when the catalog can't support the request." Something closer to "produce output that resembles what an educational assistant might look like."

The difference between those two requests is not stylistic. It is the difference between a designed system and a generated artifact. The first has an audience, a purpose, a stop condition, and a human who has made decisions about what counts as eligible and what counts as sufficient. The second has none of those things. It has fluency.

Fluency is not design. This chapter is about learning to tell them apart — and about what it means to be the person responsible for the distinction.

---

## What Conducting Actually Means

A conductor does not play the instruments. The conductor decides what piece is being performed, sets the tempo and dynamics, shapes how sections relate to each other, and makes the real-time decisions about what is working and what isn't. The musicians execute with technical skill the conductor doesn't need to have. But the conductor is accountable for the performance.

That analogy is not exact — it never is — but it captures something important about the relationship between a Creative Engineer and the systems they use. Claude can implement a substantial part of the work in this course. It can write code, generate layout proposals, critique a design against stated criteria, draft explanations from evidence you supply, and find structural problems you missed. What it cannot do is decide which problem deserves attention, choose what counts as a good outcome for a specific audience, or accept responsibility for the result.

Conducting means five things in practice. Setting objectives: knowing what the system should accomplish before asking it to accomplish anything. Supplying context: giving the system the specific information it needs — the audience, the eligible sources, the stop conditions — rather than relying on it to infer from a vague prompt. Bounding actions: specifying what the system is and is not permitted to do, and understanding which of those bounds are enforced by the environment and which are merely requests. Reviewing changes: inspecting what the system actually produced against what you actually intended. And deciding what evidence is sufficient: determining, before the close, whether the output meets the standard you set.

The last one is the hardest, and it's the one most practitioners skip. Deciding that evidence is sufficient is not the same as deciding that the output looks good. It requires having defined, in advance, what sufficient looks like.

<!-- → [DIAGRAM: Conductor-and-orchestra structure. Left: "Creative Engineer" — makes decisions about objective, context, bounds, evidence standard. Center: "Bounded task" — specific objective, permitted tools, excluded actions, stopping conditions. Right: "Claude" — implements within bounds, reports on what was done, flags when stopping conditions are reached. Arrow from right back to left labeled "Evidence for review." Caption: The Creative Engineer sets the terms. Claude works within them. The review loop is what makes the work accountable.] -->

---

## Four Verbs, Four Kinds of Evidence

The work organizes around four recurring activities. They are not a sequence — a failed check may require returning to Ideate rather than attempting Build again — but they are distinct, and each one produces a different kind of evidence that the next activity depends on.

**Ideate** is the activity of choosing problems. The human question is: which problem deserves attention? The boundary here is between generating alternatives — which Claude can help with — and selecting among them, which requires judgment about what matters to an actual audience. Claude can stress-test an assumption, surface edge cases that human optimism tends to overlook, and propose journeys you hadn't considered. What Claude cannot do is tell you which problem is worth solving, because that judgment requires stakes the system doesn't have.

The evidence Ideate produces is not a shortlist of good ideas. It is a record of the reasoning behind the choice: why this journey rather than that one, what assumptions were made about the audience, what would need to be true for a different framing to be better.

Before you ask Claude to generate alternatives, write two of your own. Afterward, mark which of Claude's overlapped with yours. The overlap is information about what the obvious moves are in this space. The non-overlapping items are where the interesting pressure is.

**Build** is the activity of making behavior exist. The human question is: what behavior should exist, specified precisely enough that someone else could implement it and you could check whether they did? The boundary here is between the specification — which requires human decisions about what the system should do in each state — and the implementation, which Claude can handle once the specification is solid.

The evidence Build produces is not working code. It is a record of which behaviors were checked, against which expected results, in which cases. An implementation that passes three tests is not the same as an implementation that handles the critical journey reliably. The difference shows in what was tested.

One practical test: can you explain what a proposed change does without reading Claude's description of it? If not, reduce the scope of the change, ask for an explanation, and check the explanation against the artifact before accepting anything.

**Brand** is the activity of communicating honestly about the work. The human question is: what should this audience understand about what was built, and can you say it without outrunning the evidence? The characteristic failure of Brand is persuasion that precedes the work. A case study written before the evaluation is complete is speculation formatted as achievement.

The evidence Brand produces is claims traceable to records: not "an intelligent learning platform" but "a resource-discovery tool that found an eligible match in X of Y tested queries on an instructor-approved catalog, with Z failure cases documented." The specificity is not modesty — it is precision about what was actually built and what wasn't.

**Ship** is the activity of handing something to someone else. The human question is: is this ready for someone else to use, and have I told them truthfully what it does, what it doesn't do, and where to report a problem? At this stage in the course, shipping can mean giving another person an inspectable candidate. It does not mean public deployment.

The evidence Ship produces is a repeatable journey — the critical path, the no-result branch, the error state — verified by someone who wasn't the person who built it, with limitations documented and a recovery path specified.

<!-- → [TABLE: Four-column table. Columns: Verb, Human design question, Bounded Claude contribution, Evidence to inspect. Rows: Ideate (Which problem deserves attention — Generate alternatives and challenge assumptions — Observation, uncertainty, and the reason for choosing this journey over alternatives), Build (What behavior should exist — Implement a reviewed specification — Changed artifacts and checks tied to intended behavior, not appearance), Brand (What should this audience understand — Draft from actual evidence you supply — Claims traceable to records, dates, and tested results), Ship (What is ready for someone else — Package, test, and document a candidate — A repeatable journey including the no-result branch, limitations stated, and a recovery path). Caption: Each verb produces a different kind of evidence. The evidence from one becomes the context for the next.] -->

---

## Choose One Critical Journey

A critical journey is the smallest connected sequence that delivers the project's central value. "Use AI for education" is a domain. "Find a relevant course resource and inspect why it was recommended" is a journey. The difference is that the second one can be observed: you either found the resource and understood why, or you didn't.

Write your journey using this structure before you draw a single screen:

*When [person] encounters [situation], they can [connected actions] so that they can [meaningful decision or outcome]. The system stops or hands control back when [specific condition].*

For the running example in this chapter:

*When a student needs help with one course task, they can enter a question, inspect an eligible resource and its matching evidence, and open the source, so that they can decide what to study next. If no eligible resource supports the request, the system reports that limit and offers a way to revise the question or browse the approved collection.*

Two things are doing real work in that sentence. First, "eligible resource" is doing design work — it means something has to decide, before the system runs, what counts as eligible, and that decision belongs to a human. Second, the stop condition is not "the system fails" but "the system reports a limit" — the failure mode is designed, not undefined.

Select a journey using three questions. Who can tell you whether its outcome matters — not in theory, but for a specific person doing a specific task? Can you observe completion without relying on a satisfaction rating? And can you test it without first building the entire product? If the answer to any of those is "not yet," you're not ready to build. You're still in Ideate.

There is a baseline exercise worth doing before any AI is involved: write the desired outcome without naming the technology. "A student finds an eligible resource and understands its relevance." Now sketch how that could happen using an annotated list, topic filters, keyword search, or a curated index. This baseline gives the project a comparison surface. When you add AI assistance later, you'll have a concrete question: compared to the baseline, what did the AI contribution actually improve? An attractive generated response is not itself evidence of improvement.

<!-- → [DIAGRAM: Journey map with three states connected by arrows. State 1: "Student enters question." Arrow to State 2: "System finds eligible resource, shows source and matching evidence." Arrow to State 3: "Student opens source and decides next step." Branch from State 1 to "No eligible resource" state: "System reports limit, offers revision or browsing." Branch from State 2 to "Retrieval failure" state: "System reports technical failure — distinct from no match." Caption: Draw the no-result branch before you design the happy path. The failure states are where the design's honesty lives.] -->

---

## The Three Layers of a Boundary

The chapter uses "bounding actions" as if it were a single idea. It isn't. There are three distinct layers, and only two of them are boundaries in any engineering sense.

The first layer is source-system permission: what the account is allowed to do at all. In this course, that means what your Figma seat type permits, what file edit permissions you have, and what the Northeastern Claude account's organizational policy allows. These limits are enforced by the systems themselves. You cannot override them with a prompt.

The second layer is host approval: whether a tool call runs, and whether it runs with or without your confirmation. In Claude's connector settings, this is the difference between a tool set to Always allow, Needs approval, or Blocked. A tool set to Blocked will not run, regardless of what the prompt says. A tool set to Needs approval will pause and ask before acting. These limits are enforced by the host application.

The third layer is instruction: what Claude has been asked to do. "Do not edit the file" is an instruction. It is not a boundary. An instruction is enforced only by Claude's compliance — and compliance is not the same as inability.

This matters specifically because Figma's MCP server can now write to the canvas. The `use_figma` tool can execute JavaScript in a Figma file through the Plugin API, creating frames, components, and variables. Write operations are, notably, exempt from Figma's rate limits: the operation that can change your file is the one that doesn't slow down. The practical implication is direct: before running the setup exercise in this chapter, set `use_figma` and `generate_figma_design` to Blocked in the connector's tool permissions. Then confirm, on a duplicate file, that a write request is stopped by the host — not by Claude's discretion.

"Do not edit the file" is useful as a clarifying instruction once the boundary is set. It is not useful as the boundary itself.

<!-- → [TABLE: Three-row table. Columns: Layer, What it controls, Who sets it, What enforces it, Chapter 1 example. Rows: Source-system permission (what the account can do at all — Figma plan and team owner, Northeastern org policy — the systems themselves — Figma seat type; file edit permission), Host approval (whether a tool call runs, and with or without confirmation — student, within the org ceiling — Claude's host application — use_figma set to Blocked), Instruction (what Claude is asked to do — student's prompt — Claude's compliance — "Do not edit the file"). Caption: Only the first two layers are boundaries in the engineering sense. Instructions shape behavior inside the bounds the other two layers set.] -->

---

## Establishing the Tool Relationship

Figma Design and FigJam are the primary design environment for this course. Claude, using the Northeastern account, is the primary conducting and implementation environment. Understanding why requires separating the parts of that setup clearly, because each part does something different and the presence of one does not establish the others.

The Figma file holds design content and structure. Its presence does not mean all required behavior has been specified — it means the visual artifact exists.

The Figma MCP server exposes supported operations and design context. Its presence does not mean every operation is available in this session. Figma offers a remote server (hosted at `https://mcp.figma.com/mcp`, the preferred option for this course's setup) and a desktop server that runs through the Figma application and is aimed at specific organizational cases. The remote server is link-based: it needs a link to a frame or layer. Selection-based prompting works only with the desktop server. The chapter's instruction to give Claude a frame link is correct for the remote server — and knowing why means you can diagnose what went wrong when it doesn't work.

The Claude application and MCP client connect to tools and use returned context. Their presence does not mean the returned context is complete or correctly interpreted.

The human reviewer selects scope and evaluates evidence. Their presence does not mean that merely viewing the output constitutes a sufficient review.

A note on the Figma Education account, because several details matter for course operation: Education plans receive the same MCP limits as Dev and Full seats on the Professional plan — up to 200 tool calls per day and 10 per minute. Write operations are exempt from these limits. However, the limits may attach to the team that owns the file rather than to the user's seat type, which means a frame stored in Drafts might operate under different limits than one in the course's Education team. Test this; don't assume. Additionally, the Education plan is tied to a verified school email and must be renewed annually for students, biannually for educators. If the team owner's status lapses, the entire team downgrades, and files become inaccessible to all members. The team owner's reverification date belongs on the course calendar.

---

## Verify One Small Read

Create a sample frame with a recognizable name, title, body text, and a button. Use invented content that contains no private information. Include a distinctive phrase you can check specifically — something unusual enough that you would notice if it came back wrong or garbled.

Before running anything, set write tools to Blocked in the connector settings.

Give Claude the frame link and ask:

```
Read this authorized sample frame through Figma MCP: [frame link]
Use read-only tools only.
Report the frame name, each text string exactly as returned,
component names, and anything the result did not include.
For each item, name the tool call that returned it.
If any call fails or is rate-limited, quote the error and stop.
```

Then compare the response with three things: the actual frame, the tool calls the interface shows, and the distinctive phrase you embedded. A login establishes account access. A successfully and accurately checked read establishes that this specific operation worked for this specific frame in this session. Neither of those establishes that later write operations, exports, or large-file operations will work. Record what you observed — not what you inferred.

The exercise is graded on the discrepancies you find, not on whether Claude's report was clean. A clean report with an unnoticed mismatch is a worse outcome than a messy report with every discrepancy identified.

One provenance check worth building into every Claude report:

For each factual claim in the response, ask: did this come from a tool call in the log, from Claude's inference, or from something you supplied in the prompt? Fill this in from the interface's tool-call display, not from Claude's own labeling. Claude's account of its own evidence is itself model output.

<!-- → [TABLE: Setup record structure. Fields: Date (UTC), Client and surface (web / desktop / Claude Code) and visible version, Model displayed, Figma plan and seat reported by whoami, Team that owns the test file (not Drafts), Write-tool permissions (Blocked / Needs approval / Always allow), Operation requested, Tool calls shown in the interface, Returned content vs. actual frame (match or mismatch with specific detail), Failures with verbatim error text, What I did not infer, Education status expiry (mine and team owner's). Caption: The setup record captures what was observed, not what was assumed. A blocker record is as valid an outcome as a successful connection.] -->

---

## The Worked Example: An Educational Resource Assistant

Use this brief as a hypothetical throughout the chapter:

*Audience: students working on one course task. Journey: enter a question, inspect a recommended resource, open its source. Boundary: do not invent a source or submit coursework. Stop condition: no supported resource can be identified. Human decision: which materials count as eligible sources. Claude contribution: implement the selected interface and lookup behavior.*

Before Claude touches any of it, make the source rule concrete. A proposed first version uses a small instructor-approved catalog where each record contains an identifier, title, source location, topic description, and approval status. The project owner selects those fields and approves the records. Their existence does not guarantee a good recommendation — it guarantees that any recommendation will be drawn from known, approved material rather than from the model's general knowledge.

The interface needs states that can change a decision. A student needs to see what collection is being searched. During a search, they need status information. When a result exists, they need the source identity and the matching evidence — not just the recommendation, but the basis for it. When a request is ambiguous, the interface should ask a specific clarifying question rather than guessing. When no resource exists, the interface reports that limit clearly, distinguished from a technical failure. These two states — no supported match and retrieval error — must be visually distinct. The first is a claim about the catalog; the second is a claim about the system. Collapsing them is the beginning of a dishonest interface.

Now ask Claude to challenge the journey:

```
Review this journey and its boundary.
Propose two alternatives and identify missing human decisions.
Keep generated suggestions separate from evidence.
For each alternative, explain what new behavior would need evaluation.
Do not implement, publish, or modify the design.
```

Suppose Claude proposes answering questions directly — skipping source lookup and generating answers from its training. The question to ask is not "would this be more capable?" It almost certainly would be. The question is: what new requirements does that introduce? What counts as an adequately supported answer? How are errors detected before they reach a student making a decision? How does this change what the instructor needs to approve? A defensible decision is to defer answer generation until those requirements are addressed — not because the capability doesn't exist, but because the design work hasn't been done.

That is the worked design decision. The choice to retain source discovery is not a limitation on Claude's capability. It is a deliberate scope decision made by someone who understands what the system is for.

---

## Inspect Capability, Not Appearance

There is a consistent finding in research on AI-assisted work that practitioners should understand before building anything: capable-looking output and capable output are not the same thing, and the difference between them tends to be invisible to the person who produced it.

In a preregistered study with 758 consultants, AI assistance substantially improved performance on tasks within the model's tested capability but reduced correctness on a task selected to fall outside it — in one condition, AI users were 19 percentage points less likely to reach the correct answer. The researchers called this a "jagged technological frontier": the boundary between what the model handles well and what it handles poorly is uneven and non-obvious, and fluent output appears equally fluent on both sides of it.

For this project: successful layout generation does not establish source accuracy. Correct source retrieval does not establish navigable interface structure. A well-formatted explanation does not establish that the explanation matches the source it cites. Each of these is a separate capability, and each needs its own test.

A separate result is worth holding onto for its specific implications. In a small randomized study with junior software engineers learning an unfamiliar library, participants who used AI assistance scored measurably lower on an immediate comprehension test than those who didn't — with the largest gap on debugging questions. The gap appeared specifically in tasks where participants had delegated understanding rather than implementation. The practical lesson is not "don't use AI while learning." It is "use AI in a mode that requires you to understand what was produced." Ask for explanations and check them against documentation. Ask Claude to explain a proposed change before you accept it. After the session, close Claude's response and explain the journey, one boundary, one failure, and the evidence that would change your decision in your own words. If you can't do that, the skill isn't there yet — and the next implementation is going to be harder to inspect.

---

## Brand and Ship from the Same Evidence

The portfolio is itself an experience. A visitor should be able to understand what you contributed and what supports the claim.

"Built an intelligent learning platform" is not a claim about what you did. It is a claim about a category you'd like to belong to. Replace it with a precise account of the audience, the journey, your contribution, and the evaluated scope. Use actual values when reporting results. If evaluation hasn't happened, say "planned evaluation" or "prototype." Writing a proposed result in the past tense is not branding — it is fabrication.

Distinguish where AI assistance was involved from where your own decisions were: source selection, interface design, implementation review, evaluation criteria. The distinction matters not because you should minimize AI involvement, but because the person reading your portfolio is trying to understand what you can do and what you learned to delegate.

At this stage, shipping means giving another person an inspectable candidate: what it does, how to try the critical journey, what is incomplete, and where to report a problem. Public deployment comes later, with the authorization and checks appropriate to that release.

---

## What Would Change My Mind

The three-layer boundary model — source-system permission, host approval, instruction — assumes that the host application correctly enforces its approval settings. There is evidence that "Always allow" settings don't always hold in practice; the failure runs in the safe direction (prompting unnecessarily rather than acting without confirmation), but the general lesson applies: test the boundary rather than trusting the settings screen. If a future version of the host application provided cryptographically verifiable audit logs of tool calls and their dispositions, the current gap between "I set it to Blocked" and "I confirmed it was Blocked" would close. Until then, the setup record's confirmation step — checking on a duplicate file — is not optional.

## Still Puzzling

The four verbs are presented here as distinct because their characteristic failures are distinct. But in practice, the line between Build and Brand becomes difficult when the implementation is generating explanations: is a relevance explanation part of the interface (Build) or a claim about the system (Brand)? If the explanation is generated by the model rather than derived from explicit record-matching, it belongs under Brand's standard — it needs to be traceable to evidence, not just fluent. I don't have a clean structural answer for where exactly that line should be drawn in the interface design, which means students will need to make that judgment case by case. That's probably the right answer, but it's worth naming as an open design question rather than pretending it resolves automatically.

---

## Practice

1. Reduce a broad product idea to one critical journey using the sentence structure in this chapter.
2. State the desired outcome without naming AI, and sketch a baseline approach using a curated list, search, or filters.
3. Identify a decision Claude may propose but not finalize — and explain specifically why that decision requires a human.
4. Draw both a no-result branch and a retrieval-failure branch, and confirm they are visually distinct in your design.
5. Write a four-verb self-audit using evidence — not confidence. For each verb, name current evidence and one next practice.
6. Create a sample frame with a distinctive phrase and verify its returned text against the actual frame and the tool-call log.
7. Record a connection failure without guessing its cause. "The tool returned an authorization error" is an observation. "My Education account is unsupported" is a diagnosis that requires additional evidence.
8. Compare a product journey with a portfolio journey. What is the meaningful decision each is designed to support?
9. Reject or defer one proposed feature — Claude's or your own — with a reason tied to what the design is actually for.
10. Before asking Claude for alternatives, write two of your own. Afterward, mark which of Claude's overlapped with yours.
11. For one claim in Claude's report, identify whether it came from a tool call in the log, from inference, or from something you supplied. Fill this in from the tool-call display.
12. After using Claude to help with a design decision, close the response and explain the journey, one boundary, one failure, and the evidence that would change your decision — in your own words, without reading Claude's account.
13. Set the write tools to Blocked, then confirm on a duplicate file that a write request is stopped by the host, not by Claude's discretion.
14. Run `whoami` and one read call. Record whether the reported seat type and the observed rate behavior agree.
15. Check one text string in Claude's report against the frame at the character level, including whitespace and capitalization.

---

## Submission Checkpoint

The submission for this chapter is not an implementation. It is a set of working artifacts that will feed later submissions.

The experience critique names an audience, one critical journey in the sentence structure from this chapter, a meaningful outcome, a baseline, and at least one unresolved assumption — an assumption you are making about the audience or the problem that you haven't yet confirmed with someone who actually experiences it.

The four-verb self-audit uses evidence, not confidence. For each verb: what evidence do you currently have for your capability, what is the specific gap, and what is the next practice that would close it.

The responsibility agreement specifies one bounded delegation in terms of objective, inputs, allowed actions, excluded actions, output, evidence, and stopping conditions — and names the decisions that remain with you.

The journey sketch shows the supported result state, the stop condition, and a technically distinct failure state. If the no-result state and the retrieval-failure state look the same in your sketch, that is the design problem to solve before Chapter 2.

The setup record captures one actual tool observation and comparison, or an accurate blocker record. A blocker that is honestly documented is a complete submission. A successful connection that wasn't actually verified is not.

Do not invent a successful connection to complete the checklist. The chapter's argument is that the difference between "looks complete" and "is complete" is the thing worth learning to see.
