# voices/

Voice rewrites of the book. Choosing a voice produces a **copy** of `chapters/`
rewritten in that voice. The originals in `chapters/` are never modified —
`voices/` holds derived editions.

## How it works

- Each voice has a folder `voices/<voice>/` containing a `VOICE.md` that defines
  the register and the conversion contract.
- Running a voice copies each `chapters/NN-*.md` into `voices/<voice>/NN-*.md`
  (same filenames), rewritten in that voice.
- `chapters/` stays canonical. `voices/` are alternate cuts a reader can choose.

## Rule (for the agent)

When doing a voice rewrite, **write only into `voices/<voice>/`**. Never edit
`chapters/`. Unless the voice's `VOICE.md` says otherwise, preserve each
chapter's title, all markdown comments, any LLM exercises, and any images.

## Available voices

| Voice | Folder | Register |
|---|---|---|
| **Wonder** | `wonder/` | Purer lecture cut — single hook, ~3,000 words, no added exercises, wonder + first principles |
| **Generic** | `generic/` | Warm, inclusive, neutral. Definition → worked example → practice problem, repeat. Accessible but flat *(OpenStax register)* |
| **Socratic** | `socratic/` | Tells you nothing directly — questions, surfaced confusion, the reader reasons it out |
| **Sardonic** | `sardonic/` | Dry, slightly sardonic, capable-adult, footnote jokes, hard problems *(Griffiths register)* |
| **Narrative** | `narrative/` | The discovery story — who was wrong first, the real confusion *(historical register)* |
| **Pragmatist** | `pragmatist/` | Formula → when to use it → ~12 practice problems. Zero personality *(engineering register)* |
| **Teardown** | `teardown/` | Take it apart, explain how each piece works, judge the design choices — intellectual honesty + design-critic lens (what it optimizes for, the trade-offs). Richer than the others: carries a command set (`/essay`, `/nart`, `/write`, `/bookmap`) and a **`/done` finishing pass** *(design-critic register; formerly Feynman × MKBHD)* |

Each folder has a `VOICE.md` with the full definition and an invoke block.

> **`/done` finishing pass:** the Teardown voice adds a finishing layer that runs on
> any completed draft — it adds a styled subtitle if none exists, adds graduated exercises if
> none exist, and seeds visual-suggestion HTML comments (invisible when rendered, visible in
> source). It adds only what's missing and rewrites nothing. See `teardown/VOICE.md`.

## Relationship to `conductor/editions/`

The alternate-voice editions in the editions menu are produced here.
`conductor/editions/` is the menu; `voices/` is where the rewrites live. (The
menu's "Griffiths-style" maps to the **Sardonic** voice; "OpenStax/Generic" is
the **Generic** voice.)
