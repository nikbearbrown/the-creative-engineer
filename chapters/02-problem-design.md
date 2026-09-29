# Chapter 2 — Problem design and conducting AI inquiry

[Contents](README.md) · [Previous](01-creative-engineer.md) · [Next](03-identity-information-architecture.md)

*Write an opportunity brief whose assumptions can be challenged.*

> Rough draft for author review. Examples are hypothetical unless explicitly attributed.

## The result

Produce an opportunity brief that connects a person's task to evidence, constraints, and success criteria. Use Claude to expand and challenge the framing after making your own initial attempt.

A precise implementation of the wrong objective is still the wrong project. “Reduce the number of clicks” can conflict with “make the consequential choice understandable.” Before optimizing a measure, state whose outcome it represents and what it leaves out.

Use this problem statement:

~~~text
For [audience] attempting [task] in [situation],
the current experience creates [specific difficulty].
Evidence: [identified observations or sources].
We propose [bounded change].
We will judge it using [observable criteria].
We will not [explicit exclusions].
~~~

Empty evidence is a research gap. Do not fill it with plausible language.

## Separate observation, interpretation, and suggestion

An observation records what a person did or what a source contains. An interpretation explains why it may matter. A suggestion proposes what to do. Keep them in separate fields.

| Field | Hypothetical example |
|---|---|
| Observation | A participant opened three resource pages before selecting one |
| Interpretation | The labels may not distinguish the resources adequately |
| Alternative explanation | The participant may have been comparing useful options |
| Proposed intervention | Add a short statement of relevance |
| Needed evidence | Ask what information guided the selection |

This table is a teaching fixture, not an interview record. In your actual ledger, attach the source and date. If the only origin is Claude, label it a generated hypothesis.

The audience-evidence lesson in Branding and AI uses this separation and explicitly rejects fabricated interviews. Repeated synthetic personas do not become independent observations by appearing in several conversations. [Source B01](../research/sources.md).

## Frame alternatives that change the problem

Three differently worded chatbot prompts are not three different framings. Change the objective, the intervention, or who controls the decision.

For the resource assistant:

| Framing | Main intervention | New responsibility |
|---|---|---|
| Discovery | Recommend relevant resources | Explain relevance and preserve sources |
| Comparison | Help students compare candidate resources | Make differences inspectable |
| Navigation repair | Improve the course resource index | Maintain accurate categories and labels |

The third option may need little or no runtime AI. That does not make it an inferior Creative Engineer project. The course concerns design judgment and conducting AI during development, not adding an agent to every interface.

Draw the alternatives as three small FigJam journeys. Keep equivalent detail so a polished favorite does not win by presentation alone. Name a person affected by failure in each.

## Conduct the inquiry

Save your initial brief before asking Claude to critique it:

~~~text
Use only the attached brief and evidence ledger.
Offer three materially different problem framings.
For each, identify beneficiaries, excluded interests, constraints,
unsupported assumptions, and an observation that could disconfirm it.
Do not invent interviews, demand, quotations, or findings.
Do not start implementation.
~~~

Inspect whether the alternatives actually differ. If Claude replaces “resource assistant” with “learning copilot,” ask what changed in behavior. If nothing changed, reject the rebranding as a new framing.

Choose the framing yourself. Record the objective, rejected alternatives, reason, and remaining uncertainty. This follows the Conducting AI practice of writing the problem before requesting a solution. [Source C01](../research/sources.md).

## Worked example: choosing discovery over automatic answers

Assume, for this exercise, that you have a small authorized set of resource descriptions but no evidence about the accuracy of generated explanations.

1. Initial proposal: answer every course question.
2. Constraint: use only the supplied resources; do not fabricate citations.
3. Competing proposal: recommend resources and expose the matching explanation.
4. Human choice: begin with discovery because its first outcome can be inspected directly.
5. Remaining question: can students determine whether a recommendation is relevant?
6. Next inquiry: observe a voluntary participant attempting that judgment, following the instructor's procedures.

The choice is not “AI answers are always wrong.” It is “this project currently has evidence and capacity to evaluate a narrower function.” If later evidence supports answer generation, revise the brief explicitly.

For a portfolio, apply the same reasoning. “Make me look impressive” becomes “help a reviewer inspect my contribution to one project.” The first invites unsupported claims; the second identifies an audience decision and evidence path.

## Write acceptance criteria and exclusions

Use criteria that can fail:

~~~text
Given an eligible resource recommendation,
the reader can open the named source from the recommendation.

Given no eligible source,
the interface presents a no-source state rather than a fabricated citation.
~~~

These are design requirements, not claims of achieved behavior. Add how you will inspect them. A schema checker can detect missing fields; it cannot determine whether your chosen audience or objective is appropriate. That judgment remains yours. [Sources C01 and H02](../research/sources.md).

[FIGURE: Evidence ledger feeding three competing briefs and one justified scope choice.]

## Practice

1. Rewrite a solution-first brief as a task-first brief.
2. Identify an affected person omitted from your first version.
3. Separate an observation from two possible interpretations.
4. Label every generated hypothesis in your ledger.
5. Design a question that does not suggest its own answer.
6. Produce a non-agentic alternative.
7. State a constraint that changes your preferred framing.
8. Ask Claude for a falsifier and evaluate its relevance.
9. Write one positive and one failure acceptance criterion.
10. Identify a metric that could improve while the experience worsens.
11. Compare your original and revised briefs without deleting either.
12. Defend the selected scope to a peer using the evidence ledger.

## Submission checkpoint — A1

Submit the opportunity and experience brief: audience, task, evidence ledger, competing framings, constraints, exclusions, acceptance criteria, and scope decision. Include one accepted or rejected Claude contribution. Do not report planned inquiry as completed research.

Next: translate the chosen problem into identity, content, and navigation.

Source basis: [Chapter 2 research](../research/02-problem-design.md).
