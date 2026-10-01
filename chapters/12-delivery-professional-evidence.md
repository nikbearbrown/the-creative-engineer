# Chapter 12 — Conducting Delivery and Designing Professional Evidence
*Release an inspectable candidate and explain your contribution without inventing outcomes.*

Here is a portfolio claim that sounds strong and means nothing.

"The AI assistant transformed student learning through an intuitive interface."

The project record contains an implemented resource journey. It contains local failure checks for source-link behavior and no-source states. It contains a diff history and a design comparison. It does not contain a learning-outcome study. No students used the system in a controlled condition. No learning was measured before and after.

The claim isn't a lie about what was built. It's a claim about something the project never measured. The gap between "I built a resource-discovery interface" and "student learning was transformed" is not a matter of confident phrasing — it's an evidentiary gap that no amount of fluent writing closes.

This is the delivery problem in its professional form. The same principle that governs the design system, the approval gate, and the evaluation plan governs the case study: claims need evidence capable of reaching them, and evidence for one claim doesn't automatically support the next one.

---

## Defining the Release Candidate

Before anything else, identify exactly what is being released.

A release candidate is a specific version: a commit hash, a tagged package, a recorded date, a referenced design version. Not "the latest code" — the specific code that the review checks were run against. If a correction is made after review, the correction creates a new candidate. The earlier results stay associated with the version that was actually checked.

The release record contains:

```
Candidate: [commit hash or tag]
Package date:
Referenced design version: [Figma file and frame version]
Tested environment: [OS, runtime version, relevant tool versions]
Fixture version: [sample data file and date]
Check results: [link to executed check outputs]
Known issues: [remaining defects and accepted limits]
Review status: [reviewed, pending, or not reviewed]
```

A working link in the evidence index is not enough — the reviewer needs access. Check Figma links using the reviewer's access conditions, not the author's. A frame that's visible to you because you own the file may not be visible to someone reviewing from outside the project.

The candidate identifier is what makes the evidence index meaningful. Evidence associated with "the project" is ambiguous. Evidence associated with commit `4a7f3c2` is traceable.

---

## What "Reproduce" Means

The package's run instructions make three different claims that are often stated as one: someone else can inspect the materials, someone else can get the system running, and someone else can reproduce a specific result.

These are separate achievements requiring different evidence.

Inspectability means the reviewer can locate and open the relevant materials. Setup success means installation and startup actually succeed in a stated environment. Reproducibility means the documented procedure produces a specific observable result — not that the code produces identical binary artifacts, which is a stricter technical property the classroom prototype doesn't need to satisfy.

Define reproduction at the level the course requires. For the resource assistant, a reasonable definition: another person can execute the source-link and no-source scenarios following the run instructions, and the documented predicates hold when they check the results.

For AI-generated outputs, distinguish three different things that look similar. Replaying a saved transcript demonstrates what the saved record contains. Running a deterministic fixture tests the system's handling of a known input. Making a fresh model request demonstrates current behavior, which may differ from the behavior recorded during development. Each requires different evidence, and claiming all three from a single demonstration is overclaiming.

The package's run instructions should include four things that most instructions omit: prerequisites including account access and any network dependencies, configuration steps with placeholders instead of actual credentials, expected observable behavior after each essential command, and stop, reset, and cleanup instructions. A fresh directory on a developer's machine may inherit global dependencies or credentials that a genuine new reviewer won't have. Report the actual conditions the setup was tested in.

<!-- → [TABLE: Four-row table. Columns: Claim, Evidence needed, Common false substitute. Rows: Package is inspectable (reviewer can locate and open materials — reviewer confirmed access, links work from their account — links work from author's account), Setup works in stated environment (installation and startup succeed there — actual fresh-environment test — "it works on my machine"), Cited result can be reproduced (documented procedure produces specified result — another person follows instructions and reaches result — author demonstrates on their own machine), AI behavior is consistent (same inputs produce same outcomes across runs — multiple fresh-request results under stated conditions — single recorded successful run). Caption: Each claim requires different evidence. Evidence for the earlier rows does not establish the later rows.] -->

---

## Packaging the Experience

A repository of files does not tell a reviewer how to use the work. The package's job is to make the critical journey discoverable and runnable without a verbal explanation from the author.

The README is what the peer starts with, not a verbal briefing. Write it as instructions for someone who has never seen the project. State the purpose, the intended audience, and where to start. The first five lines should be enough to orient a new reviewer.

Beyond the README, the package needs: design references that connect to the Figma version that was current at release, run instructions with the tested environment named, sample data labeled as fixtures with no credentials embedded, check commands with their actual observed outputs, an evidence index linking case-study claims to artifacts, a contribution ledger distinguishing human decisions from AI assistance, and a known issues section that names remaining defects and accepted limits as separate categories.

Use real dependency versions, not ranges. Don't claim a clean installation works if the tested environment already had global packages installed. If the package has an offline fixture mode, state which checks it can exercise and which live integrations it cannot reach.

---

## Checking Design Fidelity at Release

Before releasing, compare the implemented journey against the Figma design version that was current when implementation began.

Record deviations in three categories. Intentional changes are improvements that emerged during implementation — the interface was better than the design specified, and the design should be updated to reflect the approved change. Defects are cases where the implementation diverged from the design without a design decision to authorize it. Unresolved differences are cases where it's unclear whether the deviation is intentional, and a decision is needed before the release can be accepted.

If the implementation improved the design, update the Figma record to reflect the approved change — but preserve the earlier frame and the reason for the change. Updating Figma to match the implementation without preserving the original frame erases the baseline the fidelity review was supposed to protect. Distinguish fidelity to the original approved design, acceptance of an intentional change, and agreement between the updated design and the final candidate. These are three different things and they require three different records.

Keep review notes connected to specific subjects: a named frame, a component, a state, or a file location. A review note that says "the source link behavior needs attention" is much less useful than one that says "Frame 4, no-source state: the message text reads 'Nothing found' rather than the approved 'No eligible source matched this question' — this collapses the no-source and failed-lookup conditions."

---

## The Peer Handoff

The peer handoff is the package's functional test. The peer starts with the README and a stated task — not a verbal explanation from the author.

Give the peer five things to accomplish: locate the candidate and starting instructions, start the prototype, complete one critical journey, exercise one documented failure path, and find the evidence supporting one specific case-study claim. Record what happened at each step, including where the peer needed help.

If you supply a missing command verbally during the handoff, that's a packaging failure. Fix the instruction and label the handoff as assisted. Don't report it as successful because the journey eventually completed with your help.

When the peer can't reproduce a result, distinguish among three situations. An unsupported operating system may be outside the package's stated scope. A missing dependency in an advertised supported environment is a packaging defect. An unspecified environment is a documentation gap — the instructions didn't say what they require, so you can't evaluate whether the peer's environment qualifies.

Review acceptance is not publication authorization. A peer confirming that the local package works does not authorize a public launch. Separate those decisions explicitly.

---

## Writing the Case Study from the Record

The case study is derived from the evidence index, not written to justify a predetermined conclusion. The structure:

*Problem:* what task and audience did you choose, and why was this the right problem for this project?

*Alternatives:* what materially different approaches did you consider, and what made the selected approach preferable given the available evidence and constraints?

*Design:* which decisions shaped the experience — the architecture, the state distinctions, the approval design, the information hierarchy?

*Conducting:* what did you ask Claude to do, and how did you review it? This section should name the specific decisions you made, not just the tools you used. "Used Claude and Figma" names the environment. "I specified the state transitions before asking Claude to implement, then reviewed the diff against the design spec and rejected a proposed simplification that would have collapsed the no-source and failed-lookup states" describes a contribution.

*Evidence:* what actually happened when you checked the candidate? Not what you expected — what the checks found.

*Limits:* what remains unknown or unfinished? Use precise labels: not evaluated, planned, observed, or inconclusive. "Pending" implies work that was planned; use it only when work is actually planned. "Not evaluated" is the honest label for something that wasn't measured.

When asking Claude to help draft the case study:

```
Draft a concise case study from this evidence index only.
Attach an artifact reference to each outcome claim.
Separate my decisions, your generated work, and joint revisions.
Leave missing outcomes labeled with their accurate status:
  not evaluated, planned, observed, or inconclusive.
Do not invent testimonials, users, metrics, or approvals.
```

Edit the result yourself. Remove claims whose evidence you cannot locate in the index. Preserve limitations even when deleting them would make the project sound more complete.

---

## The Contribution Ledger

Outcome claims need evidence references. Contribution claims need them too.

"I designed the approval flow" is a factual claim. "Claude implemented the approval validator" is a factual claim. Both require records. A case study that attributes outcomes to the project without specifying who made which decisions is the same kind of evidence gap as a case study that claims learning outcomes without a study.

A lightweight ledger:

| Work | Human contribution | AI assistance | Supporting record |
|---|---|---|---|
| Approval invalidation | Selected the rule: revision match plus content hash | Proposed the initial implementation | Decision record; inspected diff |
| Failure testing | Defined expected outcomes and holdout check | Drafted candidate test cases | Reviewed test suite; execution outputs |
| Timeout state | Specified distinct no-results vs. timeout messages | Proposed unified message; I rejected it | Finding ledger rejection record |
| Case study | Selected claims; verified evidence links; edited prose | Drafted initial text from evidence index | Evidence index; before/after draft |

"Joint revisions" should describe the interaction rather than becoming a category that absorbs everything uncertain. Where a teammate contributed, identify their work separately from your own and from AI assistance.

---

## The Claim Ladder

Evidence for one kind of claim doesn't carry to the next kind. Being explicit about this prevents the fluency of good writing from obscuring the gap.

An implemented candidate with working checks establishes that the system behaves as specified under tested conditions. It does not establish that participants understood the interface. Observations from a usability session establish what those specific participants did and said. They do not establish that all intended users would behave the same way. A defined comparison with measured results establishes a performance difference under stated conditions. It does not establish general impact.

The inflated claim — "transformed student learning" — skips from implemented interface to general impact in a single sentence. The honest version climbs the ladder one rung at a time, stopping where the evidence stops.

For the resource assistant case study, the honest version of that sentence: "I designed a resource-discovery journey and conducted Claude's implementation against a specified interaction design. The release record includes source-link and no-source checks with actual results; learning outcomes have not been evaluated."

Each rung of the ladder has a specific evidence type. An artifact and its check results occupy the first rung. A usability session with actual participants occupies the second. A learning-outcome study occupies a rung that this project has not reached. The case study should name the rung it's on.

<!-- → [TABLE: Five-row claim ladder. Columns: Claim, Appropriate evidence, What this evidence cannot establish. Rows: "Implemented source inspection" (working candidate, executed interaction check — whether participants understood the source status), "Participants understood source status" (actual participant observations under stated conditions — whether all intended users would behave similarly), "Reduced task completion time" (defined comparison with measured results — whether the reduction persists across contexts), "Improved student learning" (appropriate learning-outcome evaluation — whether impact generalizes), "Generated customer demand" (actual demand evidence with defined measure — causation or persistence). Caption: Evidence for an earlier row does not support a later row. Name the rung the case study is on.] -->

---

## What Would Change My Mind

The chapter requires that each claim in the case study have an artifact reference in the evidence index. This is the right rule for an assessed project in a course context, where the evidence index is a required artifact. For a professional portfolio published externally, the same standard applies to outcome claims but may be relaxed for contribution claims where the supporting record is confidential or proprietary. The principle — claims need evidence capable of reaching them — is constant. The form of the evidence and whether it's publicly visible may vary depending on what can be shared.

## Still Puzzling

The case study is written for two audiences simultaneously: the course assessment, which values inspectable evidence and accurate contribution attribution, and a professional audience that values concise narrative and insight into decision-making. These aren't always in tension, but they pull in different directions — the assessed version needs every claim linked to an artifact, while a professional audience may find a claim-saturated case study difficult to read. The chapter recommends two levels (concise narrative plus linked evidence), but doesn't specify which version constitutes the A6 submission and which is the external portfolio. That probably needs to be specified in the course requirements rather than in the chapter.

---

## Practice

1. Write the release record for your candidate: identifier, package date, design version, tested environment, fixture version, check results, known issues, and review status.
2. Check all Figma links in your evidence index from an account that is not your own. Record which links are accessible and which require additional permission.
3. Write the run instructions for your package: prerequisites, configuration steps with placeholders, expected behavior after each command, and cleanup instructions. Identify the specific environment the instructions were tested in.
4. Build the reproduction test: follow your own run instructions in a fresh directory that doesn't inherit your development environment's global packages. Record what fails.
5. Define "reproduction" for your project at the level the course requires. State what another person must be able to do, and what evidence would confirm they succeeded.
6. Record deviations between the implemented journey and the Figma design version in three categories: intentional change, defect, and unresolved difference. For each intentional change, preserve the original frame and the decision that authorized the change.
7. Conduct the peer handoff. Give the peer the README and five tasks. Record which tasks required assistance. Fix any instruction that required verbal clarification and label the handoff assisted if it did.
8. Write the contribution ledger for two work items: human contribution, AI assistance, and the supporting record for each. Avoid "joint revisions" as a category — describe the interaction instead.
9. Place one of your case-study claims on the claim ladder. Name the evidence that supports it and the rung it does not reach.
10. Rewrite one outcome claim that exceeds its evidence. Replace it with an honest account of the artifact and the checks that were actually run.
11. Ask Claude to draft the case study evidence section from the index only. Then edit the result: remove one claim whose evidence you can't locate, and add the accurate status label to one missing outcome.
12. Inspect the package for private information: synthetic secret markers, API keys or tokens in configuration, personal data in fixtures, and log output that retained prompt text. Document what was found and what was removed.
13. Write the case study's "Conducting" section. Name at least two specific decisions you made about what Claude would do, at least one proposal you rejected and the reason, and at least one thing you inspected before accepting a result.
14. Separate review acceptance from publication authorization for your project. Name what the peer handoff establishes, and name what decision would need to happen before a public release.
15. For the A6 submission: include the release record with candidate identifier, tested execution contract, version-specific evidence links, contribution ledger, and peer handoff result with assisted/unassisted labeled. Keep the actual review history — do not rewrite it into a frictionless story.
