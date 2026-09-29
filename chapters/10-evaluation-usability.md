# Chapter 10 — Conducting AI evaluation and human usability inquiry

[Contents](README.md) · [Previous](09-trust-human-intervention.md) · [Next](11-operational-constraints.md)

*Match each claim to a check capable of challenging it.*

> Rough draft for author review. Sample tasks and observations are illustrative; no participant results are supplied.

## The result

Create an evaluation plan that separates automated behavior checks, Claude's critiques, and observed human experience. Use each for questions it can address.

A test can pass while inspecting the wrong property. A person can complete a task while misunderstanding the system's authority. A model can produce a plausible critique without observing either event. Keep those evidence types separate.

Anthropic distinguishes agent transcripts from environmental outcomes and discusses several grader types. Use the distinction to choose evidence, not to assume that one grading method establishes everything. [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

## Design the evaluation before requesting tests

Start with the question, not the tool:

| Question | Suitable evidence | Insufficient substitute |
|---|---|---|
| Did cancel prevent sending? | Final mock-outbox state | Agent says it canceled |
| Does the source support the claim? | Inspection of source and claim | Source identifier exists |
| Can a person explain the approval? | Actual participant response | Generated persona response |
| Can keyboard users complete the flow? | Runtime keyboard inspection | Screenshot looks orderly |

Write a success criterion and a meaningful failure case for each question. Keep expected outcomes in the plan separate from observations made later.

For a new product or AI tool, evaluate the core value proposition and its consequential failure. Do not spend the entire session assessing cosmetic preferences while leaving the main task unexamined.

## Turn a FigJam evaluation board into candidate tests

Create a table whose rows are situations and whose columns are expected status, source or reason, allowed action, and forbidden behavior. Read it through MCP and ask Claude to propose tests:

~~~text
Convert this evaluation board into candidate tests.
Map every test to a cell and state what it actually inspects.
Identify cells requiring human observation or source judgment.
Do not claim the tests passed unless you executed them.
Do not invent participant findings.
~~~

Inspect coverage in both directions: every required cell should have a suitable check, and every proposed test should have a reason to exist. A large test count does not establish meaningful coverage.

The playlist's Eval Board to Tests record found tests that missed a guess embedded in a label and a citation to an irrelevant but existing source. The tests inspected fields rather than the intended meaning. [Playlist case V04](../research/playlist-evidence.md).

## Evaluate the evaluator

Create two kinds of challenge fixture:

- A bad output that looks compliant to a superficial check.
- A valid output that differs from the checker's expected wording.

The first tests false acceptance. The second tests false rejection. Inspect both before trusting a generated evaluator. This follows the supervisory-check exercise in Irreducibly Human. [Source H01](../research/sources.md).

If a test only checks that a field is empty, put the forbidden claim somewhere else. If it checks one exact sentence, provide a valid paraphrase. Then determine whether the check measures the requirement or merely the implementation's current shape.

## Conduct human usability inquiry

Use voluntary participation and the instructor's approved procedures. Explain the task, what you will record, and the person's ability to stop. Avoid collecting unnecessary personal information. A classroom script does not replace institutional requirements.

Ask neutral task questions:

~~~text
Find a resource you would inspect for this question.
Show what you would open next.
Explain what the system is telling you here.
Before selecting an approval action, describe what would happen.
~~~

Do not coach the desired interpretation into the prompt. Ask for the participant's reading before explaining the designer's intention.

The Figma project's four-state protocol is useful preparation, but its inspected version explicitly reports no completed sessions. Keep planned study procedures distinct from findings. [Source F03](../research/sources.md).

## Worked example: separate three findings

Consider this hypothetical evaluation packet:

1. An automated check confirms that a source identifier exists.
2. Manual inspection finds that the source concerns a different topic.
3. A future participant session is planned to examine how relevance is interpreted.

Only the first two are observations in this fixture. The third is a plan. A correct report does not turn it into “users found the source confusing.”

The design response may include improving the relevance explanation, revising retrieval, or refusing the recommendation. Choose based on the actual failure. Moving the source link lower on the screen would hide evidence rather than repair it.

## Prioritize justified revisions

For each finding, record affected task, consequence, evidence strength, proposed change, and a check for the revision. Fix a failed approval boundary before polishing incidental spacing.

Use specific accessibility criteria and runtime checks. A generated accessibility review is a list of hypotheses to inspect, not a certification. [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

When findings disagree, retain the disagreement. A participant's preference, a behavior failure, and a model's aesthetic critique need not receive equal weight.

[FIGURE: Evaluation board branching to deterministic tests, source inspection, and human sessions, then a shared finding ledger.]

## Practice

1. Match a claim to an appropriate check.
2. Identify an insufficient proxy for your main outcome.
3. Build a four-column evaluation board.
4. Map generated tests back to requirements.
5. Create a false-acceptance fixture.
6. Create a false-rejection fixture.
7. Rewrite a leading usability question.
8. Design a minimal observation record.
9. Separate a prediction from a finding.
10. Inspect a source for relevance, not existence alone.
11. Prioritize three conflicting findings with reasons.
12. State what your evaluation cannot establish.

## Submission checkpoint

Retain the evaluation plan, actual observations, and prioritized design changes. Label pending sessions and unexecuted checks explicitly. These artifacts feed A5.

Next: revise under operating constraints and verify that repairs do not introduce new failures.

Source basis: [Chapter 10 research](../research/10-evaluation-usability.md).
