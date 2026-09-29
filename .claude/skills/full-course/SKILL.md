---
name: full-course
description: Design or adapt a complete AI+1 course from books or existing teaching materials, including syllabus, reading-to-lesson mapping, practical lessons, ungraded assessments, graded assignments, rubrics, prerequisites, submission templates, Canvas delivery, and instructor video plans. Use for course conversion or a staged course release, not merely chapter drafting or exporting a book to EPUB.
---

# Full course — AI+1

A book explains; a course also gives learners something to attempt, evidence to
produce, feedback to use, and a fair way to be evaluated. Build both layers.

Invoke with `/full-course` where repository skills are supported, or ask:
“Use full-course to turn this book into an NEU course.” Scope can be a complete
course or “plan the whole course; release the syllabus, Module 1, and Assignment 1.”

## Read first

1. Read the target repository's instructions, `AI1.md`, `CONDUCTOR.md`, and
   `STATUS.md`. The AI+1 constitution takes precedence over weaker gate wording.
2. Read [the course profile](references/course-profile.md) and
   [the source map](references/source-map.md). Inspect the actual target content;
   the examples are design evidence, not content to blindly copy.
3. Use [the templates](assets/course-templates.md) for the planning contract and
   artifacts. Read the applicable template before generating that artifact.

## Authority and gates

Inventory and course planning do not authorize rewriting the book, student data,
official policies, or existing assessments. Preserve originals and dirty edits.
Check artifact verification before generation using the target's `verify.py`.
Reuse verified artifacts; stop for review on unverified or stale gated artifacts.
Create unsigned sidecars for new artifacts. Never sign gates, perform the human
rewrite, fabricate a student's Frictional log, or infer approval from tests.

For an AI+1 book edition, respect the seven-phase spine and Gate 6 before edition
production. Pre-gate work may inventory sources and draft the course blueprint;
identify unavailable/unapproved readings and stop at the human review boundary.
For an independently supplied course, record its own source approvals and course
review gates rather than declaring the unrelated AI+1 example book approved.
At each gate, report the exact artifact awaiting review and stop before the next
phase. Partial releases still need approval for their released material.

Do not push repositories, publish films, import into a live LMS, install services,
spend API/media credits, or launch continuous workers merely because a course is
being created. These require authorization for the corresponding action.

## Workflow

### 1. Inventory the whole course

Read the existing syllabus and its original format; chapters and selected sections;
lessons; exercises/Assessments; assignments; rubrics; prerequisites; templates;
course metadata; tests; Canvas exports; and video/loop records. Exclude archives,
student submissions, draft duplicates, generated media, and vendored dependencies
from the teaching inventory unless explicitly selected. Do not silently delete them.

Run the read-only inventory helper when `course.json` exists:

```sh
python3 <skill-directory>/scripts/course_check.py inventory <course-root>
```

It reports `weeks` or `lessons` metadata, not approval or content completeness.
The bundled helper requires Python 3.9 or newer and no third-party packages.
Inspect actual files to resolve symbolic readings and conflicting chapter variants.
Build a provenance crosswalk: outcome → source file/section → lesson → Assessment
→ graded Assignment → evidence/test → optional film. Many-to-one and one-to-many
chapter mappings are valid; never force fifteen chapters from fifteen lessons.

### 2. Draft the course blueprint; obtain human review

Write `course-plan.json` using the template contract plus a readable `COURSE.md`.
Record audience, prior knowledge, measurable outcomes, tools/access, term,
assignment cadence, grading, reading map, release scope, and deliverable paths.
Select `neu` only for the Professor Bear/NEU format; otherwise use `custom` and
record explicit grading and policy choices. Ten assignments and fifteen lessons
are example counts, not requirements. Derive counts from the actual course span.

Keep unresolved official dates, policy decisions, cohort tie rules, and missing
permissions in `docs/instructor-decisions.md`. Ask only blocking questions.
Do not invent dates, use stale semester dates, or insert “not supplied” warnings
into student-facing boilerplate. Preserve official policies unless asked to change
them. Course approval is human; the checker cannot provide it.

### 3. Build one complete teaching unit

After the relevant approval, create a representative vertical slice:
reading + lesson + ungraded Assessment + reference/example + independent test
+ Assignment brief + rubric + submission example + Canvas page when requested.
Use **Predict → Build It → Use It → Ship It → Verify** in that order. “Ship” is an
inspectable candidate; verify that version and revise it if the checks fail.

Keep narrative chapters separate from actionable lessons. If chapters need new
writing, use AI+1's existing blueprint/research/drafting/voice/figure workflows
under their gates. Do not substitute a lesson outline for a narrative chapter.
Use the selected book voice; do not default every book to a teardown voice.

Run the mechanism and reference tests. Review a beginner's route through the
unit, access needs, expected time, answer visibility, and a genuinely diagnostic
failure case. An AI's agreement with itself is not independent verification.
Get instructor review of this slice before replicating the structure.

### 4. Expand the approved structure

Build the planned lessons and assignments with distinct outcomes and appropriate
scaffolding; avoid repeated generic prompts with changed titles. Every assessed
outcome needs observable evidence and a rubric criterion. Every assignment needs
exact files, reproducible commands, submission instructions, AI policy, and a
clear connection to its source lessons. Keep Assessments ungraded.

Add relevant companion notes only after reading the cited passage. Create a
video inventory separately from student deliverables. See the profile for Liam,
Brutalist, real-output visuals, and optional loop requirements. Do not render or
publish merely to fill a directory tree.

### 5. Validate and deliver the requested formats

```sh
python3 <skill-directory>/scripts/course_check.py validate <course-root>
python3 <skill-directory>/scripts/course_check.py validate <course-root> --files
```

First checks plan structure, mappings, and rubric totals. `--files` additionally
checks released artifact paths and lesson headings. These are narrow mechanical
checks, NOT a substitute for running code, checking claims, reviewing pedagogy,
verifying signatures, inspecting visuals, or testing LMS behavior.

For DOCX, use the documents skill and render/inspect the result; preserve the
original typography, headers, tables, boilerplate, and policies. For Canvas,
support separate paste-ready module and assignment pages when requested.
AI+1's current `build-canvas.sh` / `build-imscc-standard.py` exports chapter reading
pages, not a complete graded course. Do not call that output a full course.
If an IMSCC is requested, inspect its builder and extend/use a suitable course
exporter: include syllabus, prerequisites, ordered modules, assignment content,
points/rubrics, and accessible linked assets. Check ZIP/manifest/resource links,
then test import in a sandbox course with permission. Distinguish imported pages
from native graded assignments; report any manual LMS setup, never claim an
untested import preserves due dates, gradebook groups, or rubrics.

### 6. Handoff and maintenance

Report released vs planned modules, paths to syllabus/assignments/Canvas outputs,
test evidence, unresolved decisions, human review state, and optional film status.
Do not say “full course complete” for a Module 1 release. Keep course content and
source metadata synchronized through the crosswalk, not by overwriting originals.
Changes to a source invalidate dependent checks/films; preserve version history.
No Git commit/push, live publishing, or 24/7 service startup without authorization.
