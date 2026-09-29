# Full-course artifact templates

Fill these from the actual subject. Bracketed prose is authoring guidance, not
student-facing final text. The JSON example is a **one-module partial release**,
not an approved or complete course. Add every planned module and Assignment to
the inventory; mark only the current release `released: true`.

## `course-plan.json` contract (schema version 1)

Paths are relative to the course root. Files must stay inside that root; use
source provenance links in prose for external readings, and a local reading-guide
file in `readings` when needed. Each rubric is tailored to the assignment.

```json
{
  "schema_version": 1,
  "profile": "neu",
  "title": "Course title",
  "term": "Instructor-selected term",
  "release": "partial",
  "assignment_cadence_days": 10,
  "outcomes": ["O1"],
  "artifacts": {
    "syllabus": "SYLLABUS.md",
    "course_guide": "COURSE.md",
    "prerequisites": "prerequisites/README.md",
    "ai_policy": "prerequisites/ai-policy.md",
    "submission_template": "templates/submission.md",
    "reading_map": "docs/reading-map.md"
  },
  "modules": [{
    "id": "M01", "title": "First mechanism", "released": true,
    "outcomes": ["O1"], "readings": ["chapters/01-first-mechanism.md"],
    "lesson": "lessons/01-first-mechanism/README.md",
    "assessments": [{"id": "A01", "graded": false,
      "path": "lessons/01-first-mechanism/assessment.md"}]
  }],
  "assignments": [{
    "id": "AS01", "released": true, "modules": ["M01"],
    "outcomes": ["O1"], "path": "assignments/01-first-mechanism.md",
    "points": 100,
    "rubric": {"implementation": 60, "frictional": 10,
      "github": 10, "relative_quartile": 20},
    "implementation_criteria": {"contract_and_prediction": 8,
      "working_mechanism": 22, "applied_evidence": 12,
      "independent_verification": 12, "handoff_and_explanation": 6}
  }]
}
```

Use `release: "full"` only when every planned module and assignment is released.
This flag says what the author intends to deliver, not that a human approved it.
The companion `COURSE.md` defines O1 etc in measurable language, audience,
prerequisites, tools, workload, term/cadence and publication scope. An explicit
`custom` profile may use other positive point totals and cadence; retain a rubric
and explain the differences. Add video/LMS export plans in separate documents.

## Lesson

```markdown
# Lesson NN — [Title]

Reading: [exact file and section]. Prior skills: [named skills].
Outcome: [observable capability and artifact]. Tools: [required, optional].

## Predict
[Record expectation, confidence, assumptions and falsifier before running.]

## Build It
[Contract, smallest mechanism, manual example, boundaries. Initial attempt first.]

## Use It
[Concrete domain task, explicit Claude interaction, retained inputs and outputs.]

## Ship It
[Exact candidate files, README and reproduction commands.]

## Verify
[Independent expected result, failure case, test the candidate, record revisions.]

### Assessments — ungraded
[Misconception-revealing task; explanation/reference after learner attempt.]

[Only relevant, sourced companion notes; no automatic four-note boilerplate.]
```

## Assignment (separate from the lesson)

```markdown
# Assignment NN — [Deliverable title]

100 points. Due: [actual date or course's Canvas deadline reference].
Uses Lessons [IDs] and outcomes [IDs].

## What you will deliver
[A concrete artifact; exact files, inputs, output and acceptance conditions.]

## Predict → Build It → Use It → Ship It → Verify
[Task-specific instructions for each step; independently checkable evidence.]

## Rubric — 100 points
[Task-specific implementation rows totaling 60.]
Frictional: 10. GitHub posting: 10. Relative Quartile: 20.
[Link full criteria and explain the cohort-relative portion.]

## Submission
[Designated repo/folder convention; reviewer access; README/reproduction;
matching Canvas files and pushed commit SHA; approved large-media links.]

## AI use and responsibility
You may use AI and must identify what it contributed. You must be able to explain
your submission and distinguish verified results from simulations and assumptions.
[AI Policy for Professor Bear's Courses](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz)
[State whether an explainer is optional or explicitly required for this course.]
```

## Submission records

README: identity; assignment; file inventory; setup/run/test commands; known
limitations; sources; media links; AI contributions; matching Canvas instructions.

Prediction: timestamp; claim; confidence; assumptions; falsifier; original result
retained alongside the eventual observation.

Frictional entry: date/checkpoint; attempt and expectation; what actually happened;
evidence path or commit; human work; AI work; response/change; learning; unresolved
question/next test. Label retrospective entries. No fabricated struggle or hours.

Evidence: command + environment/input + observed output + independent comparison
+ pass/fail + limitation. Distinguish real, synthetic and simulated evidence.

Contributions: component → AI contribution → human decision/edit → verification
performed → unresolved issue. Include sources, attribution and relevant rights.

## Syllabus and course release checklist

Preserve the original official description/boilerplate unless changes are
authorized. Update approved course description, measurable learning outcomes,
tools/access, pedagogy, readings/module schedule, assignment cadence and grading,
submission rules, AI policy, and required/optional video work. Keep official
late-work/accommodation/integrity/contact policies and original document styling.
Track unknown instructor decisions outside the student-facing syllabus.

For each released module: reading links resolve; examples execute; independent
checks discriminate; Assessments are ungraded; graded evidence aligns to outcomes;
rubric totals are correct; AI policy linked; submission instructions match Canvas;
math and figures are legible/accessibly described; no hidden paid dependencies.

Release report: requested scope; released and deferred IDs; artifact paths;
mechanical tests; execution evidence; human gate status; document/Canvas visual
checks; sandbox import evidence or explicit untested status; film state; remaining
decisions. Do not equate a passing checker with approval or publication.
