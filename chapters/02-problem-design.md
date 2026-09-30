# Chapter 2 — Problem Design and Conducting AI Inquiry
*Why a precise implementation of the wrong objective is still the wrong project.*

Before you write a single line of code, before you open Figma, before you prompt Claude to generate anything at all, there is a question that will determine whether the work you're about to do is worth doing.

Not "can we build this?" That one is almost always yes. The interesting question is "is this the problem?"

Here is a concrete example. A team observes that students open several course-resource pages before selecting one. This is a real observation about real behavior. But it doesn't tell you what the problem is. One interpretation: the labels aren't distinctive enough, so students are hunting. Another interpretation: students are comparing options, which is exactly the behavior you'd want to see. A third: the index is fine, but the descriptions are too thin to assess relevance without opening the page.

Three different problems. Three different interventions. One of them might call for an AI recommendation engine. One might call for a comparison interface. One might call for a better copywriter and an afternoon of editing. None of that is determinable from the observation alone.

The mistake is treating "students open multiple pages" as a problem statement rather than a signal that needs interpretation. The work of this chapter is learning to hold the observation separate from the interpretation — and to hold both separate from the proposed intervention — until there is enough evidence to justify moving from one to the next.

---

## The Three Questions You Are Actually Answering

Problem design isn't one question. It's three, and they require different kinds of evidence.

The first is: is there a consequential difficulty? Not "could someone have trouble with this?" but "does this specific audience encounter a problem worth addressing, and do you have evidence for that?" An invented persona doesn't answer this question. A polished pain-point paragraph doesn't answer it. What answers it is an account of recent experience — observed behavior, documented workarounds, recorded failures — from people who actually encounter the situation.

The second is: could this intervention help? Even if the difficulty is real, a proposed solution is a hypothesis. The fact that students struggle to find resources doesn't establish that an AI recommendation engine will help them find better ones. It might. It might make things worse by adding a relevance-framing layer that sounds authoritative and misleads. This question requires comparing the proposed change against the current experience and against alternative approaches, including the non-AI alternatives most teams never seriously consider.

The third is: does the implementation meet the specification? This is the question acceptance criteria answer. It's entirely different from the first two, and conflating it with them is how teams end up with software that passes all its tests and doesn't solve anything.

A passing link test establishes that a source opens under tested conditions. It does not establish that students needed the recommendation, or that the resource selected was actually useful for the task. These are separate findings. Keeping the three questions separate isn't bureaucratic overhead — it's how you avoid spending six weeks building something that answers the third question while leaving the first two open.

<!-- → [TABLE: Three-row table. Columns: Question, What answers it, What doesn't answer it. Rows: Is there a consequential difficulty? (Observed behavior, documented workarounds, recorded failures — invented personas, plausible pain-point paragraphs), Could this intervention help? (Comparison with current experience and alternatives, prototype inquiry — the fact that difficulty exists, software passing its tests), Does the implementation meet the specification? (Schema checks, reproducible examples, link tests, controlled cases — positive participant comments, outputs that look right). Caption: The three questions require different evidence. Acceptance tests answer only the third one.] -->

---

## Separation of Observation, Interpretation, and Suggestion

There is a discipline that makes the difference between evidence and wishful thinking visible: keeping observations, interpretations, and suggestions in separate fields, so each can be evaluated on its own terms.

An observation records what someone did, what they reported, or what an inspected source contains. Not what you think it means, not what you think should change — what was seen or said or found.

An interpretation proposes why that observation might matter. It is explicitly a hypothesis, not a finding. And because interpretations are hypotheses, the honest move is to generate at least two competing ones before committing to either.

A suggestion proposes what to do about it. It follows from an interpretation, but it is one possible response to it — not the inevitable conclusion.

Here is why the separation matters. Suppose you observe that a participant opened three resource pages before selecting one. Without discipline, this becomes: "Users are confused by the navigation — we should add AI recommendations." That sentence collapsed an observation into an interpretation into a solution in a single move, and the interpretation selected was the one that justifies the solution you were already planning to build.

With separation:

The *observation* is: a participant opened three resource pages before selecting one.

One *interpretation*: the labels may not adequately distinguish the resources.

A *competing interpretation*: the participant may have been comparing useful options deliberately.

The *needed evidence*: ask the participant what information guided the selection, and inspect the three pages they opened.

The *suggestion*, held in reserve: if the first interpretation holds, add a relevance statement; if the second, build a comparison view; if neither, look at the descriptions themselves.

The evidence ledger is where this discipline lives. One entry per meaningful claim. Every entry has a type — observed behavior, self-report, document, tool result, or generated hypothesis — a source and date, a locator, what was observed, an interpretation, at least one alternative explanation, and what the entry does and doesn't establish. If the origin is Claude, the type is "generated hypothesis." That label is not a dismissal; it is an accurate description of what the entry is and how much weight it can carry.

<!-- → [TABLE: Evidence ledger entry structure. Fields and example content: ID (EV-001), Type (observed behavior), Source and date (voluntary participant session, 2026-09-15), Locator (session notes, timestamp 14:32), What was observed (participant opened three resource pages before selecting the second one), Interpretation (labels may not distinguish resources adequately), Alternative explanation (participant may have been comparing options), What this supports (at least one participant engaged in multi-page exploration), What this does not establish (how common this is, whether it represents difficulty or deliberate comparison), Next check (ask participant what information guided the final selection). Caption: One entry per claim. Generated hypotheses are labeled as such. The "what this does not establish" field is not optional.] -->

---

## Why Synthetic Participants Aren't Evidence

Here is a move that feels like research but isn't: opening a conversation with Claude, describing your audience, and asking it to simulate what that audience would say.

The outputs are fluent. They're structured. They use the right vocabulary. They sound like user research. They are not user research.

Research by Wang, Morgenstern, and Dickerson compared identity-prompted language model outputs with human responses across sixteen demographic identities and three thousand participants. They found the models both misrepresented groups — producing responses closer to what outsiders imagine than to what members actually say — and flattened them, showing less within-group variation than real people exhibit. The same underlying finding appears in information-retrieval evaluation: multiple language model assessors agreeing with each other looks like consensus but functions more like one estimate repeated, because the correlated errors compound rather than cancel.

Five Claude conversations agreeing that your resource tool sounds useful is not five pieces of evidence. It is approximately one piece of evidence, with whatever bias that particular system brings to that type of question — and a consistent tendency to tell you things sound good when you wrote them yourself and signal that you'd like feedback.

There is a legitimate use for synthetic participants: piloting your interview questions. Ask Claude to play a respondent and notice where your questions lead the witness, where they are ambiguous, where the framing supplies the answer. Then revise the questions. That is using the model as a diagnostic instrument, not as a data source. The resulting outputs still go in the ledger as "generated hypothesis." They do not become findings because they arrived through a persona.

If you don't have access to actual participants before this submission, the honest move is to document the gap. State what inquiry would be needed, what it would test, and what it can't be replaced by. An honest gap with a relevant inquiry plan is more informative than a fabricated finding dressed as evidence.

---

## Three Framings That Are Actually Different

The chapter on the Creative Engineer introduced the four-verb loop: Ideate, Build, Brand, Ship. The work of Ideate is choosing which problem deserves attention — and to do that honestly, you need alternatives that are genuinely different, not the same idea wearing different clothes.

Here is the test for whether two framings are actually different. They need to change at least two of three things: the objective (what outcome you're trying to produce), the intervention (what you would actually build or change), and who controls the decision.

For the resource assistant running example, three distinct framings:

The *discovery* framing proposes a recommendation system. The objective is helping students identify relevant resources. The intervention is an interface that accepts a query, matches against an approved catalog, and surfaces candidates with explanations. The student selects. The system proposes. The people who maintain the catalog and approve what counts as eligible control what the system can recommend.

The *comparison* framing proposes a different interface. The objective is helping students evaluate candidates side by side. The intervention exposes meaningful differences between resources so the student can judge. The student compares and decides. Nothing is ranked; everything is displayed. The intervention changed, and so did what the student does with it.

The *navigation repair* framing doesn't build an AI system at all. The objective is making the existing course resource index findable. The intervention is editing the descriptions, labels, and category structure so students can locate what they need without a recommendation engine. A maintainer keeps it accurate. The runtime AI involvement is zero.

The third option is not a lesser version of the project. For some difficulties, it is the superior one. A curated index with accurate descriptions has no hallucination failure mode, no relevance-leniency problem, and no ongoing maintenance cost from a model layer. If the actual difficulty is "the descriptions are too thin," the third framing is the better engineering choice, not a fallback.

Draw all three as FigJam journeys at identical levels of detail. If one is three nodes and two are labels, you're not comparing framings — you're comparing polish. The polished one will win by presentation, and you'll have learned nothing about which framing is better for the problem.

<!-- → [TABLE: Three-row table. Columns: Framing, Objective, Intervention, Decision control, New responsibility created, A question that could weaken it. Rows: Discovery (identify relevant resources — recommendation system — system proposes, student selects — explain relevance accurately — What if students need to compare, not find?), Comparison (evaluate candidates — side-by-side interface — student compares and decides — keep comparison dimensions meaningful — What if no two resources are close enough to compare?), Navigation repair (make index findable — edit descriptions and labels — student browses, maintainer updates — sustain accurate descriptions — What if the descriptions are fine and students just don't know to look?). Caption: All three change the objective, intervention, and decision control. All three are genuine alternatives. None of them is obviously right before inquiry.] -->

---

## Conducting the Inquiry Without Creating an Echo Chamber

The standard move is to write a brief and ask Claude to critique it. The problem is that asking a system you built a brief in front of — in the same session, using the same framing — to challenge your assumptions tends to produce what research calls sycophantic feedback: agreement dressed as analysis.

In a study by Cheng and colleagues, language models affirmed users' actions roughly 49 percent more often than human respondents did, including in cases involving deception or harm. A single affirming exchange measurably increased participants' conviction that they had been right. The mechanism is not that the model is lying — it is that the model optimizes for responses that feel helpful and agreeable, and challenge that arrives wrapped in validation is barely a challenge at all.

There are two structural moves that reduce this. First, present the brief in the third person. Not "here is my opportunity brief" but "here is an opportunity brief written by a student." The research on sycophancy shows that signaling ownership of an idea reliably shifts feedback toward the positive. Removing that signal doesn't eliminate the tendency, but it disrupts the most obvious trigger.

Second, require the critique to be evidenced. Every factual claim in Claude's response must cite a ledger ID. Claims without a ledger ID are labeled generated hypotheses by default — not necessarily wrong, but not evidence. The prompt:

```
Below is an opportunity brief and evidence ledger written by a student.
Use only these documents.
Offer three materially different problem framings.
For each, identify beneficiaries, excluded interests, constraints,
unsupported assumptions, and one observation that could weaken it.
Cite the ledger entry ID for every factual claim.
Label claims without supporting entries as GENERATED HYPOTHESIS.
Include an option without runtime AI.
Do not invent interviews, demand, quotations, or findings.
Do not select the final framing or start implementation.
```

Then inspect the result. Watch for renames — "resource assistant" becomes "learning copilot" without anything changing about the objective, intervention, or decision control. If the name changed but the behavior is identical, reject the rename. Watch for claims without ledger IDs. A confident-sounding diagnosis of user behavior that has no entry in your ledger is a generated hypothesis, regardless of how plausible it sounds.

The critique itself is not a finding. It is a set of hypotheses and reframings that are worth evaluating. Evaluate them against the evidence, not against how well they were argued.

---

## Turning Assumptions Into Inquiry

Every framing rests on assumptions. The question is whether those assumptions are visible — and whether you've specified what would make you reconsider them.

This is not a philosophical exercise. It is a practical one. If you cannot state what evidence would change your framing, you cannot design inquiry that would actually challenge it. And if your inquiry cannot challenge your framing, it is not research — it is confirmation.

For each key assumption in your brief, work through three steps. First, state the assumption explicitly: "We assume students cannot distinguish resource descriptions adequately from the current labels." Second, name the observation that could weaken it: "If a participant, asked to select a resource for a specific task, correctly identifies the relevant one and explains why using the label information alone, the assumption is weakened." Third, decide what that would mean for the framing: "If the assumption fails, navigation repair becomes the candidate intervention, not recommendation."

This structure — assumption, disconfirming observation, decision implication — converts an untested belief into a testable hypothesis. It also makes the inquiry useful: you're not just gathering feedback, you're running a test with a known decision at the other end.

One specific assumption worth testing for the discovery framing: that AI relevance explanations help students make better selections. Research on AI explanations in recommendation contexts found that explanations increased users' acceptance of recommendations whether or not the recommendation was correct. An explanation that sounds authoritative makes a wrong recommendation more persuasive, not less. If you plan to generate relevance explanations, "explanations present" is not an acceptance criterion — "explanations that improve appropriate selection" is the criterion, and it requires an evaluation design that can distinguish the two outcomes.

<!-- → [TABLE: Four-row table. Columns: Candidate assumption, Observation that could weaken it, Decision if assumption fails. Rows: Students can't distinguish resource labels (participant identifies correct resource using label alone and explains why — shift to comparison or navigation repair), Relevance explanations improve selection (reader becomes more confident while selecting a less appropriate resource — revise or remove explanations), Recommendations outperform the current index (index supports the task equally with less maintenance — prefer index repair or narrow use case), Source availability is the obstacle (relevant resources available but students can't assess their content — reframe around comprehension or prerequisites). Caption: An assumption without a specified disconfirming observation is an untested belief, not a hypothesis.] -->

---

## Metrics That Improve While the Experience Gets Worse

Before you write acceptance criteria, there is a question worth asking about each metric you're considering: how could this number go up while the actual experience gets worse?

This is not a rhetorical question. It has specific answers for the resource assistant.

Recommendation click-through could rise because the explanations became more persuasive — not because the recommendations became more relevant. A more confident-sounding explanation makes people more likely to click, whether or not the resource is a good match.

The no-source rate could fall because the system became more willing to call things relevant — not because coverage improved. AI relevance judges tend toward leniency; a system that almost always finds something plausible-sounding will have a low no-source rate and a high rate of irrelevant recommendations.

Time-to-first-resource could fall because students stopped comparing options — which the observation table identified as possibly the useful behavior you're trying to support.

For each metric you plan to use, identify the failure mode: the condition under which the metric improves without the underlying outcome improving. Then design a companion check that would catch that failure. The companion check for click-through is inspecting which resources were selected and whether they were appropriate for the task. The companion check for the no-source rate is a negative test set — a list of questions you've determined in advance have no eligible match — and running the system against it to see what it produces.

Write exclusions with a reason and a reconsideration condition. "No generated relevance explanations in this version because we don't yet have an evaluation design that can distinguish helpful from persuasive" is an actionable exclusion. It names the gap, explains why it isn't yet filled, and identifies what would change the decision. "No AI mistakes" is not an exclusion — it's an aspiration, and you can't establish it with a small test suite.

---

## The Opportunity Brief

The brief is a provisional argument for investigation. It is not proof of demand. It should not sound more certain than the evidence supports.

```
For [audience] attempting [task] in [situation],
the current experience creates [specific difficulty].
Evidence: [ledger IDs]
Status: [observed / documented / generated hypothesis / none]
Affected by failure: [person or role, and how]
Decision owner: [who decides what counts as success]
We propose: [bounded change]
Alternatives considered: [other framings and why not]
Constraints: [limits that change the choice]
Exclusions: [what we will not attempt, and why]
Acceptance criteria: [observable behavior and inspection method]
We would reconsider this framing if: [specific disconfirming evidence]
Next inquiry: [what would be done, by whom, under what procedures]
```

If the difficulty hasn't been observed, write "We hypothesize that…" and specify the inquiry that could establish whether it occurs. If the evidence field has no entries, write "none — research gap." Do not fill gaps with plausible language.

The worked example for this chapter builds the discovery framing with those constraints applied honestly: it states what evidence exists (an authorized resource catalog, inspectable), what evidence is missing (participant observation, evaluation of generated explanations), and what would change the scope decision (if index repair resolves the difficulty, or if inquiry shows the difficulty doesn't exist). The alternative framings are documented. The exclusions explain why generated relevance explanations are deferred rather than included.

That combination — a bounded proposal, visible gaps, documented alternatives, explicit conditions for reconsideration — is more useful than a confident brief built on invisible assumptions. A brief that knows what it doesn't know is a brief that can be tested.

---

## What Would Change My Mind

The chapter's approach to synthetic participants — label them as generated hypotheses, never report them as evidence — is correct given current research. It would become less restrictive if we had reliable methods for specifying the exact conditions under which simulated outputs match real-participant behavior for a particular kind of question. Argyle and colleagues' "silicon sampling" work suggests this is sometimes possible for population-level survey distributions. The problem is that "sometimes possible under controlled conditions for specific question types" is not the same as "safe to use in a student project about a local audience's navigation behavior." Until the scope conditions are better understood, the conservative rule holds.

## Still Puzzling

The sycophancy mitigation — present the brief in the third person — is supported by the mechanism identified in the research. What's less clear is how much it actually moves the needle in practice versus simply feeling like it should help. The study by Sharma and colleagues demonstrates the problem exists. It doesn't give a validated intervention for removing it from a single student session. The structural check — require ledger IDs for every factual claim — is probably doing more work than the framing change, and it's worth being honest that neither of these makes the problem go away. They make it more visible.

---

## Practice

1. Rewrite a solution-first brief as a task-first brief using the template in this chapter.
2. Identify an affected person omitted from your first version — specifically, someone who bears the cost of your proposed success metric.
3. Separate one observation from two competing interpretations. Do not resolve the competition until you've named what evidence would settle it.
4. Label every generated hypothesis in your ledger. If anything from a Claude conversation is in your ledger without that label, add it.
5. Design a question for a participant that doesn't suggest its own answer. Pilot it through Claude playing a respondent and note where the question led the witness, then revise.
6. Produce the non-agentic alternative to your proposed framing at the same level of detail as your preferred option.
7. State a constraint that changes your preferred framing. Not a feature limit — a constraint that would make a different framing the better choice.
8. Present your brief to Claude in the third person. Run the inquiry prompt from this chapter and inspect the response for renames versus reframings and for claims without ledger IDs.
9. Write one positive and one failure acceptance criterion, each with a specific inspection method. Confirm the failure criterion would catch the failure mode you're most worried about.
10. Identify one metric in your evaluation plan that could improve while the experience gets worse. Name the companion check that would catch it.
11. Preserve your original brief alongside the revised one. Note what changed and what didn't, and whether any Claude contribution survived contact with the evidence.
12. Defend your scope decision to a peer using only the evidence ledger. If you can't, identify which assumptions need inquiry before the scope is defensible.
13. Build a negative test set: five questions for which no eligible resource exists. Use it as a quality check on whatever matching approach you plan.
14. For one claim in Claude's critique, check whether it has a ledger ID. If it doesn't, label it generated hypothesis and evaluate whether it's worth testing.
15. Write the condition under which you would abandon the AI component of your proposal entirely. State what specific evidence would make the non-agentic alternative the better choice.
