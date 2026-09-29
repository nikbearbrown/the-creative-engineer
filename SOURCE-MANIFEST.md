# SOURCE-MANIFEST.md

**ai1-cli is the source of truth for scripts and recipes.** This manifest declares
exactly which files propagate to other book repos, which are seeded once, and
which are never touched. `scripts/sync-to-book.sh` reads the lists below.

Three categories:

- **CANONICAL** — overwritten on every sync. The shared tooling and prompt-sets.
  Never edit these in a downstream book; edit them here and re-sync.
- **SEED** — copied only if missing in the target. Per-book templates you fill in
  (planning docs, configs, status, an empty fact dictionary).
- **PROTECTED** — never copied or overwritten. The book's own content, generated
  outputs, data, secrets, and audit trail.

> The blocks below (between the `sync:` markers) are the machine-readable lists
> the sync script parses. Keep edits inside the markers. Paths are relative to a
> book root; a trailing `/` means the whole directory.

---

## CANONICAL — overwrite on every sync

<!-- sync:canonical -->
AI1.md
CONDUCTOR.md
CLAUDE.md
AGENTS.md
HELP.md
HOW-TO-USE.md
MODES.md
KEYS.md
SOURCE-MANIFEST.md
.gitignore
.env.example
build.sh
graphs.sh
build-canvas.sh
build-site.sh
build-imscc-standard.py
build-react-site.py
build-anki.py
build-quizzes.py
build-exercises.py
scripts/verify.py
scripts/svg-to-png.mjs
scripts/svg-visual-audit.mjs
scripts/extract-cards.py
scripts/gen-audio.py
scripts/build-apkg.py
scripts/sync-to-book.sh
scripts/README.md
.claude/skills/full-course/SKILL.md
.claude/skills/full-course/references/course-profile.md
.claude/skills/full-course/references/source-map.md
.claude/skills/full-course/assets/course-templates.md
.claude/skills/full-course/scripts/course_check.py
.claude/skills/full-course/scripts/test_course_check.py
conductor/
voices/README.md
voices/wonder/VOICE.md
voices/generic/VOICE.md
voices/socratic/VOICE.md
voices/sardonic/VOICE.md
voices/narrative/VOICE.md
voices/pragmatist/VOICE.md
facts/facts_store.py
facts/facts.py
facts/extract-facts.py
facts/facts-sources.yaml
facts/README.md
facts/CONTRIBUTING.md
facts/EXTRACTING-FROM-OPENSTAX.md
facts/FACTCHECKER-INTEGRATION.md
<!-- /sync:canonical -->

`conductor/` is copied whole — it holds only recipes (phase prompts, the editions
menu, design, VERIFICATION.md); no generated data lives there. `voices/` copies
only the README and the `VOICE.md` specs — never the rewritten chapter outputs.

The full-course skill is listed file by file so its local verification sidecars
are not recursively copied over downstream human sign-offs.

---

## SEED — copy only if missing (per-book templates)

<!-- sync:seed -->
README.md
STATUS.md
metadata.yaml
package.json
anki-config.yaml
quiz-config.yaml
exercises-config.yaml
book.md
outline.md
vision.md
architecture.md
chapters-spec.md
risks.md
styles/kindle.css
styles/kindle-book.css
facts/facts.json
facts/facts.json.verified.json
<!-- /sync:seed -->

These carry per-book values (title, gate state, configs, filled planning docs, the
book's own fact dictionary). A new book gets them; an existing book keeps its own.

---

## PROTECTED — never copied, never overwritten

<!-- sync:protected -->
chapters/
images/
d3/
output/
pantry/
editions/
.env
.git/
node_modules/
**/*.verified.json
voices/*/[0-9]*.md
facts/facts.json
facts/facts.json.verified.json
<!-- /sync:protected -->

The book's content (`chapters/`), figures, built artifacts, generated edition and
voice outputs, the fact dictionary's data, secrets (`.env`), and every
`.verified.json` sign-off sidecar are off-limits. `facts.json` and its sidecar
appear in both SEED and PROTECTED: seeded empty for a new book, never overwritten
after.

---

## How to propagate

```bash
# from the ai1-cli repo root — push canonical files into one book
scripts/sync-to-book.sh ../some-other-book

# preview without writing
scripts/sync-to-book.sh --dry-run ../some-other-book

# update every sibling book
for b in ../*/ ; do [ "$b" = "../ai1-cli/" ] || scripts/sync-to-book.sh "$b"; done
```

The sync **overwrites CANONICAL**, **seeds SEED only if missing**, and **never
touches PROTECTED**. Because downstream books treat canonical files as read-only,
the only place to change a script or recipe is here — then re-sync.
