# Chapter 11 — Designing Operational Constraints and Conducting Revision
*Set operating limits, investigate before editing, and revise without expanding authority.*

Here is a repair that hides the original failure.

The lookup times out. The simulator catches the exception. The catch block returns an empty result. The interface displays the no-results message. The test passes.

The test measured whether the interface displays the no-results message when the result is empty. That property is now verified. But the system just conflated two completely different conditions: "the catalog was searched and nothing matched" and "the search never completed." A student who sees the no-results message after a timeout concludes that nothing relevant exists in the catalog. That conclusion is false. The catalog was not successfully queried.

The repair solved the wrong problem. It made an exception disappear by converting it into a plausible-looking result. The test passed because the test was checking for the presence of the no-results state, not for whether the no-results state was being shown under the right condition.

This is the operational constraint problem: the failure modes that matter most in a running system are precisely the ones that are easiest to conceal. A timeout becomes a no-results message. An empty field becomes evidence. A retry silently doubles the effect. The discipline of this chapter is making those distinctions visible — in the constraints you define, in the failure states you design, in the hypotheses you form, and in the repairs you approve.

---

## Defining the Budget

Every constraint that affects what a user experiences needs to be designed before the interface appears complete, not patched in afterward when the interface fails in production.

The budget table has more structure than a single column of limits. For each constraint, name what you've decided, how the limit is verified or enforced, and what evidence would tell you whether the limit was met.

Constraints fall into three enforcement categories. An enforced limit is controlled by a mechanism that actually stops or prevents the behavior — a counter checked before dispatch, a deadline that cancels inflight work. A monitored limit is measured and reported but doesn't automatically stop anything. An assumed limit is documented but neither measured nor enforced.

A documented number is not a control. Listing "maximum 5 agent steps" in a table is not the same as a counter that refuses to dispatch step 6. The distinction matters because the gap between assumed and enforced is where failures occur.

<!-- → [TABLE: Six-row table. Columns: Constraint, What you decide, Enforcement category (enforced / monitored / assumed), Evidence to collect. Rows: Waiting threshold (when progress or delay becomes visible — interface check with timing — elapsed time from request to first visible state change), Journey deadline (maximum elapsed time before failure state — orchestrator deadline and cancellation behavior — start and finish timestamps, including whether inflight work was stopped), Action budget (what counts as an action; maximum steps — counter checked before dispatch — action trace with step count and budget remaining), Request budget (attempts, retries, concurrent calls — dispatch limit and retry policy — request log with counts at the observed layer), Cost target (measured usage, estimate basis, exclusions — accounting; hard cap only if implemented — tool call log, estimate basis, date, missing quantities), Data retention (what persists, how long, deletion scope — expiry mechanism and deletion check — storage locations, retention period, verified deletion). Caption: Label each constraint as enforced, monitored, or assumed. A monitored limit without enforcement relies on observation to detect violations — it does not prevent them.] -->

For costs specifically, preserve the playlist's distinction: a logged tool call count, an estimate based on current list pricing, and an actual billing event are three different things. An estimate requires its model, rate basis, date, and a list of what's excluded. An unmeasured quantity is not zero — it's unknown.

---

## What a Timeout Actually Establishes

A timeout is a decision by the waiting party to stop waiting. It establishes that the caller did not receive the required result before its deadline. It does not establish that the operation failed.

The operation may have completed after the caller stopped waiting. The operation may be still running. In both cases, a caller that reports a timeout as failure and a caller that reports a timeout as no-results are both misrepresenting what happened.

The defensible description is: the caller stopped waiting at the deadline without receiving a result. The result may or may not have arrived or may arrive later.

This matters for the interface design in two specific ways.

First, a late result must be handled explicitly. If the lookup completes after the interface has already entered its timeout state, what happens? Does the late result silently replace the current state? Does it appear as a new result with a status indicating it arrived late? Is it discarded? All three are design decisions. None of them should happen by default.

Second, stopping the wait does not stop the underlying work. If the simulator is still executing after the interface displays the timeout message, any consequential action the agent takes during that execution is happening without the user's knowledge. Define whether inflight work is cancelled when the deadline fires, and test that the cancellation actually reaches the work.

For the worked example's fixtures, add these two alongside the basic delay fixture: the lookup completes after the interface has entered the timeout state, and a newer lookup completes before an older delayed lookup returns. Both require explicit handling.

---

## Designing the Waiting and Failure Experience

The waiting state and the failure state are design outputs, not defaults. Before asking Claude to fix a timeout failure, draw the states in Figma. If you don't have a design for what the interface shows during a slow lookup and after a timeout, you don't have enough specification to review a repair. Claude will invent a user-facing behavior, and the behavior it invents may not be the one you would have chosen.

For the resource assistant, three failure states need to remain distinct: search completed with no eligible result, search did not complete within the deadline, and search could not be attempted because a tool failed. Each has a different message and a different next action. A repair that routes all three to the same no-results message is not a repair — it's a concealment.

Retry is a design decision, not a default. For read operations, retry may be acceptable — the cost is time and resource consumption. For consequential operations — anything that sends a message, records an approval, or takes an action outside the simulator — retry requires duplicate prevention. A second attempt to contact the instructor is not the same as a second attempt to retrieve a source. The approval rules from Chapter 9 still apply during a retry.

Write the retry policy explicitly: which failures are eligible for retry, the maximum number of attempts including the initial one, the delay between attempts, whether the retry count consumes the journey's deadline, and who owns the retry decision. If client libraries retry automatically, identify the layer you're observing — a single visible tool call may conceal several underlying attempts, and your trace count is not the total request count.

---

## Investigate Before Editing

The investigation step has a specific purpose: prevent a repair from solving the wrong problem.

Give Claude the failure evidence without giving it permission to change anything:

```
Investigate this trace without changing code.
Separate observed facts from plausible causes from missing evidence.
Identify the smallest test that could distinguish among the causes.
Do not raise limits, add retries, change permissions,
or remove failing checks without an approved design decision.
```

A plausible cause must do two things: explain the observed behavior, and predict what a discriminating check would find. "The API is unreliable" is not a sufficient hypothesis if the evidence is one failed request. "The lookup timeout fires before the fixture's delay expires, causing the exception path to run before any result is returned" is a hypothesis — it predicts that shortening the fixture delay below the timeout limit will result in a successful return.

Keep rejected hypotheses and inconclusive checks in the dossier. An investigation that only shows the hypotheses that turned out to be correct is not an investigation — it's a retrospective narrative.

For each hypothesis, write the prediction before the check runs. Record what actually happened. If the check doesn't distinguish the hypotheses, the check was the wrong one, and that's a finding too.

<!-- → [TABLE: Six-row table. Columns: Record type, Question it answers, What belongs in it. Rows: Observation (what happened — timestamps, error text, state at failure, tool trace), Hypothesis (what could explain it — predicted mechanism, predicted discriminating check result), Discriminating check (what result favors which hypothesis — check design, actual result, which hypotheses it rules in or out), Mitigation (what limits the immediate consequence — applied action, scope, does not require a causal explanation), Repair (what changes the defective behavior — specific change, files, connection to the hypothesis), Verification (what evidence shows the change worked — regression results, failure fixture results, unexpected behavior). Caption: Keep rejected hypotheses and inconclusive checks. An investigation that only shows the winning hypothesis is a retrospective narrative, not evidence.] -->

---

## Approving a Bounded Revision

After the investigation, approve a specific repair. The approval prompt has the same structure as the task contract from Chapter 6:

```
Implement the selected recovery behavior in the named files.
Preserve the success path and approval contract from Chapter 9.
Do not raise action budgets or change permissions without a separate decision.
Run the failure check and the existing regression checks.
Report actual outputs and any checks not executed.
```

For the timeout example, five scenarios require actual test results:

A successful resource lookup under normal conditions. A completed lookup with no eligible resource in the catalog. The delayed fixture that exceeds the chosen deadline. A malformed result from a tool. A repeated request under your stated retry policy.

Record actual outcomes. Do not populate a dossier with expected passes and label it verification.

If the repair changes visible behavior — a new state, a revised message, a different transition — update the Figma states to match. If the repair restores already-specified behavior without changing what the user sees, the implementation evidence is sufficient without a new drawing.

---

## Privacy, Security, and Observability

The tension in logging is between having enough information to investigate failures and retaining more than you need. Prefer a minimal event record that can answer diagnostic questions without copying whole prompts or responses.

A useful minimal record for the resource assistant: journey identifier, candidate version, event type (query submitted, lookup started, result returned, timeout fired, state entered), attempt number, elapsed time, and outcome category. This connects events within a journey, supports timing analysis, and answers which branch executed — without retaining the text of what the student typed or what the catalog returned.

Test the logging explicitly. Verify that a synthetic secret marker (a distinctive string that should never appear in logs) is absent from retained records. Verify that an event trace for one journey doesn't bleed into the records of another. Verify that expired records are actually removed from the storage locations within the prototype's scope — and separately document other copies you don't control, including exports, client conversation histories, and remote service logs.

Review permissions in the actual execution environment. The two permission boundaries are different: what Claude may do while investigating and editing the code, and what the resulting application may do when someone uses it. Restricting the development agent doesn't automatically enforce approval inside the application. Claude Code's permission rules and sandboxing are different mechanisms with different scopes. A path-checking function inside application code is not a sandbox.

---

## Release and Rollback

Keep the previous candidate. Name the revision being tested. Define, before testing, what would make you stop and return to the prior version.

The rollback exercise has more steps than just restoring the previous files. If the new version changes stored data, configuration, or record formats, the old version may not be able to read the state the new version created. Test the full sequence: run the previous candidate, apply the revision, create representative state using the revised version, restore the previous candidate, then verify the critical journey against the resulting state.

For an agentic prototype, restore prompts, model configuration, tool contracts, and fixture versions alongside the code. Source files alone may not restore the tested behavior.

Rolling code back does not undo messages, approvals, or disclosures that occurred while the revision was running. State which effects your rollback can reverse and which it cannot. This is an operating assumption to defend specifically, not a generic claim that rollback restores everything.

Define when rollback is unsuitable and a forward repair is required. Sometimes the state the revision created cannot be read by the previous version, or the external effects cannot be reversed, and the only path forward is a repair rather than a restoration.

---

## What Would Change My Mind

The chapter's investigation-before-editing rule is the right default for a classroom project where the cost of an investigation is low and the cost of a misdiagnosed repair is learning a bad habit. In an active incident affecting real users, the priority ordering reverses: mitigate first, investigate after. The chapter's rule is not wrong for its context — it's specific to a context where the urgency of a production incident is absent and the learning value of disciplined diagnosis is high. Understanding that distinction is part of knowing when to apply the rule.

## Still Puzzling

The chapter recommends defining whether inflight work is cancelled when a deadline fires. Implementing this correctly — propagating a cancellation signal to every downstream component that was spawned by the original request — is non-trivial even in simple systems. In a classroom simulator with a local mock catalog, the propagation path is short and testable. In a more complex system with multiple chained tool calls, the cancellation semantics become a design problem in their own right. The chapter names the requirement without providing the mechanism, which is probably the right scope for this course, but students should understand that "the deadline fired" and "all spawned work was stopped" are two separate claims, each requiring separate verification.

---

## Practice

1. Write the budget table for your critical journey. Label each constraint as enforced, monitored, or assumed. For any assumed constraint, name what would need to change to make it monitored.
2. Identify one constraint in your budget where the limit is documented but not enforced. Name the specific mechanism that would enforce it.
3. Define the journey deadline for your resource lookup. Specify whether inflight work is cancelled when the deadline fires, and name the test that would verify cancellation actually reaches the underlying work.
4. Write the distinct interface message and next action for each of the three failure conditions: search completed with no eligible result, search did not complete within the deadline, search could not be attempted.
5. Write the retry policy for your lookup: eligible failures, maximum attempts, delay, whether retry consumes the deadline budget, and who owns the retry decision.
6. Build the late-result fixture: the lookup completes after the interface has entered the timeout state. Define whether the late result is discarded, surfaced with a status, or silently applied, and test your chosen behavior.
7. Build the out-of-order result fixture: a newer lookup completes before an older delayed lookup returns. Verify that the old result does not silently replace the current state.
8. Investigate one failure from your evaluation using the structure from this chapter: observe without changing, form two competing hypotheses, identify the discriminating check, record the actual check result.
9. Write the prediction for one hypothesis before the discriminating check runs. Record whether the actual result matched the prediction. If it didn't, record that as a finding.
10. Design the verification suite for the timeout repair: five scenarios with expected behavior, then actual outcomes recorded. Do not populate the table with expected passes and call it verification.
11. Write the minimal logging record for your critical journey: the fields that can answer diagnostic questions without retaining prompt text or response content. Test that a synthetic secret marker is absent from the retained log.
12. Identify the two permission boundaries in your project: what the development agent may do, and what the application may do when a user uses it. Name one thing that is restricted in one boundary but not the other.
13. Conduct the rollback sequence: run the previous candidate, apply the revision, create state with the revision, restore the previous candidate, verify the critical journey. Record the step at which verification succeeds or fails.
14. List the effects of the revision that rollback cannot reverse. For each, name whether a forward repair or a separate mitigation is available.
15. For the A5 dossier: connect each material revision to its failure evidence, its approved design decision, the inspected change, and its follow-up verification. Add an enforcement-status column to the operating assumptions. Mark late-result and out-of-order fixtures, retry accounting, and rollback compatibility results as executed, failed, inconclusive, or pending.
