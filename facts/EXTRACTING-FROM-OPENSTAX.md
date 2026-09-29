# Extracting Facts from OpenStax

How to mine an OpenStax CNXML textbook into the shared `facts.json` dictionary.
This is the process actually used to build the collection — written so it is
repeatable by an agent (no key), by the `extract-facts.py` script (API key), or
by a person.

---

## 0. What you're working with

OpenStax source books live next to this folder as `../books/osbooks-*`. Each is
a CNXML content repo:

```
osbooks-anatomy-physiology/
├── collections/<slug>.collection.xml   ← book structure: units → chapters → module refs
├── modules/mNNNNN/index.cnxml          ← one section's content (custom CNXML XML)
└── media/                              ← figures (not needed for facts)
```

- A **collection** defines the ordered chapter → module tree.
- A **module** (`mNNNNN`) is one section. Its `<content>` holds `<para>`, `<list>`,
  `<term>`, `<note>`, `<figure>` etc. We only need the readable text.
- A **bundle** (e.g. `osbooks-biology-bundle`) holds several collections sharing
  one module pool — convert one collection at a time (`--collection <name>`).

---

## 1. Two ways to run it

The deterministic plumbing (parse, dedup, consensus, write) is the same either
way. Only the **LLM step** — turning module text into facts — differs:

| Mode | LLM step done by | Key? | Best for |
|------|------------------|------|----------|
| **Agent mode** | Cowork / Claude in-session (you are the model) | none — your subscription | calibrating, curating, working a book in batches with a human watching |
| **API mode** | `extract-facts.py` calls the Anthropic API | `ANTHROPIC_API_KEY` in `.env` | unattended batch over a whole book/many books |

Validate quality in agent mode first; switch to API mode only once the output
is trusted, to avoid paying to generate facts you'd reject.

---

## 2. What counts as a fact

Extract **atomic, decontextualized, citable** claims. Each fact must be:

- **Atomic** — one claim. Split compound sentences.
- **Decontextualized** — a standalone present-tense statement. Resolve pronouns
  and "this/these" ("This process needs ATP" → name the process). A reader must
  understand it with no surrounding text.
- **Grounded** — directly supported by a real sentence in the module. That exact
  sentence goes in `verbatim`. Never invent or add outside knowledge.

**Prefer:** definitions, constants/quantities, structural & functional
relationships, mechanisms, classifications.
**Skip:** narrative/motivation, exercise prompts, figure-only captions, and bare
enumerations of names (e.g. lists of every bone or muscle — those are reference
tables, not atomic facts).

Mark `stable: true` for definitions, constants, anatomy, historical dates;
`false` for statistics, guidelines, approval status, or anything time-varying.

### Density

Curate, don't vacuum. Aim for roughly **4–7 facts per content module** — the
load-bearing concepts, not every sentence. A name-heavy module (e.g. skeletal
anatomy) yields fewer real facts than a definition-heavy one.

---

## 3. Citation & schema

Every fact carries `evidence[]`. For an OpenStax source the citation is:

```json
{
  "source":   "anatomy-and-physiology-2e",   // the BOOK slug (so two books = two votes)
  "publisher":"openstax",                    // groups same-publisher agreement
  "repo":     "osbooks-anatomy-physiology",
  "module":   "m45989",
  "url":      "https://openstax.org/books/anatomy-and-physiology-2e",
  "tier":     "trusted",                      // from facts-sources.yaml
  "verbatim": "the exact supporting sentence",
  "retrieved":"YYYY-MM-DD",
  "verdict":  "SUPPORTS"
}
```

The fact wrapper (`make_fact` builds this): `canonical`, `domain` (one or two
subject tags), `stable`, `category` (BASIC | DEFINITION | QUANTITY | MECHANISM |
CLASSIFICATION), `status: "source-attested"`, `verified: false`, plus the derived
`consensus` / `votes` / `same_publisher` / `needs_review`.

---

## 4. Consensus & dedup (handled by the helpers)

Never set consensus by hand — `merge_fact` + `recompute_consensus` derive it:

- 1 supporting source → `unverified` (candidate)
- 2+ distinct sources support → `agreement` (votes accrue; `same_publisher: true`
  flags agreement that's all within one publisher, e.g. two OpenStax books)
- same claim, different precision → `partial`
- any `REFUTES` → `conflict` → `needs_review: true` (the human queue)

Dedup is by **wording similarity with a numeric guard**: clear paraphrases
**merge** (evidence appended); same wording + different number → kept separate as
a `numeric_conflict`; close-but-uncertain → flagged `possible_duplicate`. Nothing
is human-`verified` from extraction; a person runs `verify.py sign` only on the
review queue.

---

## 5. The process, step by step

1. **Pick the book** (and collection, for a bundle). Confirm `collections/` and
   `modules/` exist.
2. **Parse the collection** → ordered `(chapter, module)` list. (Skip the
   `(front matter)` module; it's a splash page.)
3. **Per chapter, read each module's text** — load `index.cnxml`, take the
   `<content>` text (`itertext`), collapse whitespace.
4. **Extract facts** from that text per §2 — atomic, decontextualized, real
   `verbatim`, with `domain`/`stable`/`category`.
5. **Merge** each into `facts.json` via `merge_fact` (dedup + consensus happen
   automatically). Cross-chapter and cross-book repeats merge or get flagged.
6. **Checkpoint** after each batch: facts count, modules covered, review-queue size.
7. **Review** the queue (`needs_review: true`): resolve conflicts, confirm
   look-alikes are distinct, then `verify.py sign` what a human approves.

### Calibration before scale

On a new book, do **one module first** and check:

1. Are facts atomic and decontextualized (not run-on, not context-dependent)?
2. Is each `verbatim` actually present in the source?
3. Right density — load-bearing concepts, not every sentence or name list?
4. Domains tagged sensibly?

Only batch the rest once a calibration module passes.

---

## 6. Decisions locked for this collection

- **`facts.json` is shared and cross-book** (lives here in `facts/`, not inside a
  single book), so the same fact from different books accrues votes.
- **Cross-domain facts are kept.** The anatomy book states physics (first law of
  thermodynamics), chemistry (atoms, bonds), and history (Röntgen) facts — these
  are true, cited, and tagged by `domain`. The dictionary spans domains.
- **Source = book slug, publisher = openstax.** Two different OpenStax books
  agreeing = 2 votes, but `same_publisher: true` marks it as not-independent.
- **One OpenStax citation = `unverified` candidate**, not truth — OpenStax is
  vetted, not infallible. Corroboration (a second, ideally non-OpenStax source)
  raises it to `agreement`.
- **Front/back matter skipped**; name-enumeration modules yield few facts.

---

## 7. Commands

```bash
# API mode (unattended)
cd facts && cp .env.example .env       # add ANTHROPIC_API_KEY
python extract-facts.py ../books/osbooks-anatomy-physiology            # calibrate: 1 module, stop
python extract-facts.py ../books/osbooks-anatomy-physiology --all      # whole book
python extract-facts.py ../books/osbooks-biology-bundle --collection concepts-biology --all

# review queue → human sign-off
python ../books/ai1-cli/scripts/verify.py status      # (or inspect facts.json for needs_review)
```

In **agent mode** there is no command — Cowork reads the modules and writes facts
directly using the same helper functions, no key. See `README.md` for the schema
and consensus model.
