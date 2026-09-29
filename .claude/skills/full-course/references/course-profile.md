# Course profile: Professor Bear / NEU

These are defaults observed in the five INFO 7375 courses, not universal rules
for every institution. Record deviations explicitly in the course blueprint.

## Course layers

| Layer | Purpose and required contents |
| --- | --- |
| `chapters/` | Narrative readings, sources, figures; book voice and human gates |
| `COURSE.md`, `course-plan.json` | Outcomes, scope, reading/lesson/assignment crosswalk |
| `SYLLABUS.md`, original syllabus document | Description, outcomes, tools, schedule, grading, unchanged official boilerplate |
| `lessons/` | Five-stage practice, real mechanism, examples, checks, ungraded Assessments |
| `assignments/` | Graded briefs every ten days, rubric and precise evidence/delivery |
| `prerequisites/` | NEU Claude access, setup, AI policy, GitHub/Canvas, Frictional, quartile; optional Brutalist tutorial |
| `templates/` | README, predictions, evidence, contributions, Frictional, handoff examples |
| `docs/` | Reading map, instructor decisions, source provenance, verification report |
| `canvas/`, `output/` | Requested paste-ready pages or tested LMS/book exports |
| `<term>/first-name-last-initial/assignment-XX/` | Student submission convention; do not seed actual student work |
| `youtube/` | Film source inventory, beats, sources, render/QC/publication receipts |

Do not create empty folders as a substitute for useful artifacts. Reference
existing equivalent paths rather than renaming a working course unnecessarily.

## Access and AI policy

Mention early that NEU students use Claude Code through the university. Public
readers need their own Claude Code account/access. Link the
[NEU Claude page](https://claude.northeastern.edu/) and verify its current details
when writing a live syllabus. University Claude access does not imply paid API
credits. Core INFO exercises use Python and subscription-backed Claude Code;
optional API calls must be explicit and explain requests, responses, and costs.
Label offline fixtures, simulations, and actual model runs accurately.

Include the [course AI policy video](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz)
in prerequisites and **each Assignment**. Students may use AI throughout but must
identify its contributions and explain/defend the work they submit. Distinguish
what was observed from what was assumed, simulated, or not verified. Apply the
course's actual integrity process; do not infer misconduct from low performance.

NEU-only logistics belong in prerequisites, not numbered book chapters. Student
explainer films are optional in these INFO examples, considered only as relevant
professional communication. A different course may explicitly require them
(e.g. CSYE 7270's Brutalist Godot explainers); record that choice, do not inherit
it silently. No separate video points in the 60/10/10/20 profile.

## Teaching unit

- **Predict:** record expectation, confidence, assumptions, and a possible
  falsifier before execution. Retain it after learning otherwise.
- **Build It:** smallest understandable mechanism, input/output contract, manual
  worked example, and boundary cases. Initial learner attempt precedes reference.
- **Use It:** apply to a concrete domain task with real prompts, inputs, outputs;
  no invented client feedback or evidence. Synthetic examples are labeled.
- **Ship It:** package an inspectable candidate with code/artifacts, README,
  evidence, predictions, contributions, and Frictional. Not public deployment.
- **Verify:** run independent checks on the shipped candidate. Use discriminating
  counterexamples, manual results, proof or external measurement appropriate to
  the subject. Record failure, revision, and what is still unknown.

Assessments are ungraded self-checks with useful explanations, not disguised
graded Assignments. Quizzes must teach misconceptions; keep answer keys from
being accidentally exposed in a graded LMS activity. Python test counts and quiz
counts in one source course are not mandatory for every discipline.

## Grading: 100 points every ten days

| Component | Points | Evidence |
| --- | ---: | --- |
| Implementation | 60 | Task-specific artifact, demonstrated understanding, independent checks |
| Frictional | 10 | Honest, traceable account of effort and learning |
| GitHub version posting | 10 | Accessible, complete revision matching Canvas |
| Relative Quartile | 20 | Whole-cohort comparison after review |

Give implementation its own task-specific criteria summing to 60; do not reuse
the same generic rows for a proof, a brand system, and a game.

Frictional: five criteria worth 2 each: attempts/expectations; friction/response;
human versus AI contributions; learning/remaining uncertainty; dated traceable
evidence. Award 2 for specific sufficient evidence, 1 partial, 0 absent. This is
not a timesheet or a suffering contest. Honest failed work can earn full log
credit. If the work went smoothly, log the checks rather than inventing struggle.
Retrospective notes must say so. Do not grade number of hours or commits.

GitHub: five criteria worth 2 each: correct location/reviewer access; complete
artifact and evidence; usable README and attribution; committed **and pushed**
revision with folder URL/SHA in Canvas; matching Canvas package and appropriate
sharing. A private designated repo with reviewer access is acceptable. Use
`<term>/first-name-last-initial/assignment-XX/`; resolve name collisions with an
instructor-approved suffix. Record a commit SHA in Canvas; do not try to place a
commit's own SHA inside itself. A later change needs a new matching submission.

Relative Quartile: top 25% = 16–20; second = 10–15; third = 5–9; bottom = 0–4.
Review the whole comparison group first. The instructor defines ties, uneven
cohorts, late work and resubmission treatment before grading. Compare specificity,
substantive improvement, understanding, evidence, honest limits, usability and
professional communication. Requirements alone do not guarantee these points.
Polish never substitutes for correctness; plain precise work outranks beautiful
nonsense. Do not automatically rank students or expose peer grades.

## Versioning and sharing

Useful commit subject: `fix: preserve unmatched rows in join audit`. A useful
body names prediction, observed result, change, test evidence, and contributions.
Use meaningful learning checkpoints, not an essay on every commit.

GitHub holds source/text and appropriately sized documents; videos/audio and
large media belong in approved storage linked from the README. Ignore MP3/MP4,
build caches and secrets. `.gitignore` cannot enforce size: inspect staged files
or use a validator/hook to reject files over the course's 25 MB limit. Never
delete local media or rewrite history merely to enforce this. Do not include
credentials, private prompts, personal student data, or restricted datasets.

## Companion reading notes

Read the relevant chapter/section before adding a note, and cite it precisely.
Use portable links or approved local sources, not mandatory sibling checkouts.
Skip a note that adds no concrete action.

- **Anthropics:** official Anthropic guidance or repository tied to the mechanism;
  verify current behavior, cite URL and date checked.
- **Computational Skepticism:** specific falsifier, evidence boundary or calibration.
- **Conducting AI:** concrete delegation, handoff, authority or re-engagement decision.
- **Irreducibly Human:** explicitly state **AI should** and **Human should**, naming
  actual work and accountable decisions. Human judgment is not automatically correct.

Do not import another book's grades, research approvals, or historical tooling
requirements. Separate empirical claims from normative arguments.

## Instructor film workflow

Plan one AI deep-explainer per selected chapter, one AI explainer per current
Assignment, and one AI CLI explainer per lesson Assessment; Liam persona for this
profile. Map actual Assessment IDs, not every archived exercise or source variant.
Read the installed Brutalist skill and render instructions before production.
Resolve its real path; example docs disagree between `brutalist.art` and
`brutalist-art`. Do not vendor a guessed copy or invent commands.

Use real executed code/data, code-native diagrams and correctly typeset math.
Show code **and its visible effect**, not page after page of source. Pantry/image
generation is for visuals genuinely requiring it, not fake screenshots of Python
or fabricated evidence. Preserve ordinary persona intro/outro conventions.
Verify final 4K dimensions, audio, duration and sampled frames. Every 9:16 Short
must be **under 180 seconds**; create a focused short rather than blindly cropping.
Track planned → source-ready → rendered → QC → review-ready → approved → published
separately, with receipts; a slate draft is not a publishable final.

If continuous production is requested, adapt the existing per-repo
`neu-courseloop.sh`/config after reading its implementation. Require dry-run
inventory, source fingerprints, locks, bounded retries/timeouts, disk/quota
backoff, observable status, and stop instructions. Authoring the loop is not
permission to start a 24/7 service or publish its films. Preserve human gates.
