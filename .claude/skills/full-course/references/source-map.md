# Source map — inspected 2026-09-12

Local examples were inspected under
`/Users/bear/Documents/CoWork/bear-textbooks/books/`. These paths document
provenance; downstream users do not need all five repositories installed.
Read actual sources again when adapting a specific course; this is not a live
certification of their correctness, publication status, or approval.

| Repository | Sources inspected | Distinct lesson for the skill |
| --- | --- | --- |
| `info-7375-prompt-engineering-for-generative-ai` | `course.json`, `SYLLABUS.md`, `LESSON_TEMPLATE.md`, lesson/assignment/prerequisite layout | `weeks[]` schema, lesson directories containing `docs/en.md`, code/tests/quizzes; symbolic reading references need explicit resolution |
| `info-7375-computational-skepticism-for-ai` | `course.json`, `SYLLABUS.md`, `NEU-COURSE-TEMPLATE.md`, `LESSON_TEMPLATE.md`, instructor decisions | 13 core chapters revisited in 15 lessons; historical Summer material and conflicting drafts must not become the active course by accident |
| `info-7375-conducting-ai` | `course.json`, `COURSE.md`, `SYLLABUS.md`, lesson template, shared rubric prerequisites, `NEU-COURSELOOP.md` | 15 chapter/lesson pairs; artifact handoffs and independent checks; instructor films distinct from optional student videos |
| `info-7375-irreducibly-human` | `course.json`, `SYLLABUS.md`, lesson template, reading map | Introduction/seven tiers/conclusion expand into 15 lessons; explicit AI/human responsibilities; research rubric ratification is not classroom grading approval |
| `info-7375-branding-and-ai` | `course.json`, `SYLLABUS.md`, lesson template, reading map | 19 core chapters grouped into 15 lessons with `readings[]`; creative artifact plus testable mechanism, not Python replacing human creative judgment |

All five support the five-stage spine, ungraded Assessments, ten-day Assignments,
and 60/10/10/20 grading. Their current Fall 2026 paths are examples, not a timeless
default. Preserve existing course-specific artifact names and official policies.

## AI+1 integration findings

- Canonical framework instructions live in `instructions/`; `AGENTS.md` and
  `CLAUDE.md` are generated adapters. Edit the source and review rebuilt diffs.
- `AI1.md` requires human signatures on every gate. Weaker wording elsewhere
  does not authorize agent signatures. This skill does not change existing gates.
- `build-imscc-standard.py` currently reads `chapters/*.md` and creates webcontent
  pages and organization entries. It does not create this full course's graded
  assignment structure or rubric integration. A successful ZIP build is not proof
  of full LMS readiness.
- The skill's explicit file entries in `SOURCE-MANIFEST.md` allow canonical
  distribution without recursively copying skill-local verification sidecars.
  No downstream sync or global skill installation is performed by this task.
