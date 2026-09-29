# Chapter 11 — Designing operational constraints and conducting revision

[Contents](README.md) · [Previous](10-evaluation-usability.md) · [Next](12-delivery-professional-evidence.md)

*Set operating limits, investigate failures, and revise without expanding authority.*

> Rough draft for author review. Budgets are project decisions; no current platform quota or measured performance is asserted.

## The result

Produce a redesign dossier that connects observed failures to justified revisions and explicit operating assumptions. Include latency, cost, reliability, privacy, security, and recovery.

Operational constraints are design inputs. They affect what the user sees when work is slow, when evidence is unavailable, and when the system must stop. Do not postpone those decisions until the interface appears complete.

## Define a budget the system can enforce

For the critical journey, write a budget table:

| Constraint | What you must choose | Evidence to collect |
|---|---|---|
| Elapsed time | When waiting becomes a visible failure | Actual start and finish observations |
| Agent actions | Maximum permitted steps | Action trace |
| Tool requests | Allowed calls and retry behavior | Tool log |
| Data retention | What persists and for how long in the prototype | Stored files and deletion behavior |
| Consequential actions | Who can authorize them | Approval and outcome records |

Choose limits appropriate to the exercise and label them as design targets. Do not present them as Figma or Claude account entitlements.

The playlist's cost record distinguishes logged tool calls, unmeasured credit consumption, and CLI-reported list-price estimates. Use that distinction. An estimated dollar figure is not necessarily a charge to a card; an unmeasured quantity is not zero. [Playlist case V03](../research/playlist-evidence.md).

## Design the waiting and failure experience

Specify what the interface says while work is underway. Give the person a meaningful route when the operation fails or exceeds the chosen budget.

For the resource assistant, a failed lookup should not become “no resource exists.” A timeout establishes that the operation did not finish within the limit, not that the catalog contains no relevant material.

Decide whether retry is appropriate. A repeated read may be acceptable in the exercise; repeating a consequential action requires a duplicate-prevention design. Preserve the approval rules from Chapter 9.

Draw the revised states in Figma before directing a repair. Otherwise Claude may solve the technical failure by inventing a user-facing behavior you never selected.

## Investigate before editing

Give Claude the failure evidence:

~~~text
Investigate this trace without changing code.
Separate observed facts, plausible causes, and missing evidence.
Identify the smallest test that could distinguish the causes.
Do not raise limits, add retries, change permissions,
or remove failing checks without an approved design decision.
~~~

Review its hypotheses. A proposed cause must explain the observed behavior and suggest a discriminating check. “The API is unreliable” is not a sufficient diagnosis if the evidence is one failed request.

After investigation, approve a bounded revision:

~~~text
Implement the selected recovery behavior in the named files.
Preserve the success path and approval contract.
Run the failure check and existing regression checks.
Report actual outputs and anything not exercised.
~~~

This follows the source diff-review method: reproduction, plan, patch, checks, and acceptance remain distinct. [Source P02](../research/sources.md).

## Worked example: a timeout repair

Use a local fixture that delays lookup beyond your chosen exercise limit. The expected design response is a failed-retrieval state with an explanation and permitted next action.

Suppose the first proposed repair converts every exception into an empty result. Reject it because it collapses two meanings: “search completed without a match” and “search did not complete.”

Choose a revision that preserves the distinction. Then test:

1. A successful resource lookup.
2. A completed lookup with no eligible resource.
3. The delayed fixture.
4. A malformed result.
5. A repeated request under your retry policy.

Record actual outcomes when run. Do not fill a dossier with expected passes and call it verification.

For a portfolio, the corresponding failure could be an evidence asset that cannot load. Design an explicit unavailable state rather than replacing it with a fabricated thumbnail or outcome.

## Review privacy, security, and observability

Collect enough information to investigate behavior without retaining unnecessary content. In the classroom prototype, prefer synthetic queries and sample records. Inspect logs for copied prompts, personal details, and accidental secrets.

Separate observability from surveillance: state transitions and error categories may answer the diagnostic question without recording everything a person typed.

Review permissions in the actual client and execution environment. A warning in a prompt is not an enforceable access boundary. A local path-checking exercise is not a complete sandbox. [Source P01](../research/sources.md); [Claude Code permissions](https://code.claude.com/docs/en/permissions).

## Rehearse release and rollback choices

Keep the previous candidate and identify the revision being tested. Define what would make you stop a release and return to the prior version. Test the recovery procedure on a disposable local candidate.

Rolling code back does not automatically undo messages, data changes, or disclosures. State which effects your rollback can reverse. This is an operating assumption to defend, not a generic promise of safety.

[FIGURE: Failure trace to competing causes, discriminating check, bounded revision, regression review, and release decision.]

## Practice

1. Define an elapsed-time target for your journey.
2. Specify an action budget and exhausted-budget state.
3. Separate a cost estimate from actual billing evidence.
4. Identify an unmeasured quantity.
5. Design a timeout state distinct from no results.
6. Compare two plausible causes of one failure.
7. Ask Claude for a discriminating check before a fix.
8. Reject a repair that hides errors.
9. Test duplicate behavior under retry.
10. Inspect a log for unnecessary information.
11. State a boundary your prompt cannot enforce.
12. Rehearse a local rollback and document what it cannot undo.

## Submission checkpoint — A5

Submit the evaluation and redesign dossier, including operating assumptions. Connect each material revision to evidence, a design decision, an inspected change, and a follow-up check. Retain unresolved limits.

Next: package a reproducible release and a truthful professional case study.

Source basis: [Chapter 11 research](../research/11-operational-constraints.md).
