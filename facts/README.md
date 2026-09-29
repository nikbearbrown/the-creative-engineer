# facts/ — Shared Fact Dictionary

A cross-book collection of atomic, cited facts mined from **vetted sources**.
Any book's fact-check phase queries `facts.json` before looking anything up
externally. Facts accumulate; they are never silently overwritten.

## How facts are trusted

Each fact carries **evidence** records, each naming a **source** and a **tier**
(`facts-sources.yaml`). Consensus is **derived** from the evidence, not set by hand:

| Evidence | consensus | meaning |
|---|---|---|
| 1 supporting source | `unverified` | candidate — cited but uncorroborated |
| 2+ sources support | `agreement` | corroborated |
| same claim, different precision | `partial` | soft agreement |
| any source refutes | `conflict` | **human review queue** |

- A **vote** = a distinct *source* (a specific book/page). Two different OpenStax
  books = 2 votes — but `same_publisher: true` flags that it's not independent
  confirmation. OpenStax + PubMed = 2 votes, `same_publisher: false` (strongest).
- `status` is `source-attested` (extracted from a vetted source) until a human
  runs sign-off, which sets `status: human-verified`, `verified: true`.
- The human only needs to touch **conflicts** (`needs_review: true`).

## Source tiers (`facts-sources.yaml`)

`trusted` (OpenStax, textbooks) · `solid` (PubMed, journals) · `low` (web search).
Weights are deferred — tiers are recorded now so formal weighting can come later.

## Collect facts

```bash
cp .env.example .env   # add your ANTHROPIC_API_KEY
python extract-facts.py ../books/osbooks-anatomy-physiology            # calibrate: first module, then STOP
python extract-facts.py ../books/osbooks-anatomy-physiology --all      # batch the whole book
python extract-facts.py ../books/osbooks-biology-bundle --collection concepts-biology --all
```

Each fact is cited to its OpenStax book (`source` = book slug, `publisher` =
openstax, `repo`, `module`, `url`) with the exact supporting `verbatim` sentence.

## Entry shape (excerpt)

```json
{
  "canonical": "Homeostasis is the maintenance of stable internal conditions.",
  "domain": ["physiology"], "stable": true,
  "status": "source-attested", "verified": false,
  "consensus": "agreement", "votes": 2, "same_publisher": false, "needs_review": false,
  "evidence": [
    {"source": "anatomy-and-physiology-2e", "publisher": "openstax", "tier": "trusted",
     "repo": "osbooks-anatomy-physiology", "module": "m45985",
     "url": "https://openstax.org/books/anatomy-and-physiology-2e",
     "verbatim": "Homeostasis is the …", "retrieved": "2026-06-10", "verdict": "SUPPORTS"}
  ],
  "category": "DEFINITION", "expires": null
}
```

## Known next steps

- **Embedding-based dedup.** Lexical matching (wording similarity + numeric guard)
  catches clear paraphrases and flags the rest for review; true paraphrase *recall*
  ("X is called Y" vs "Y is the X") needs sentence embeddings — deliberately deferred.
- **Deep-link URLs.** Citations are book-level today; per-section OpenStax page
  URLs can be added from the collection's page mapping.

## Dedup & conflict detection (implemented)

Merge matches on **wording similarity** with numbers ignored, then:
clear paraphrase + same numbers → **merged**; same wording + **different number**
→ kept separate with `numeric_conflict_with` (review queue); close-but-uncertain
→ `possible_duplicate_of` (review queue); else **added**. Conservative by design —
it flags rather than risks a wrong merge. Thresholds are tunable in the script.
