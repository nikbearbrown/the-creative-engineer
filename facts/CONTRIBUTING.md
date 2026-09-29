# Contributing to the Fact Commons

An open, expert-reviewed knowledge commons — the spirit of Wikipedia, but the unit
is a **cited, structured fact** (or key term, or concept-graph edge) with
transparent provenance and a *derived* consensus. The goal: build something that
helps everyone, that anyone — physicists, biologists, other sources, and AI — can
add to, and that domain experts vouch for.

## How contribution works

- **You add *evidence*, you never overwrite.** Each fact accumulates evidence
  records `{source, tier, url, verbatim, verdict}`. Consensus
  (`agreement` / `partial` / `conflict` / `unverified`) is **computed from the
  evidence, never declared**. Two sources agreeing = 2 votes; a disagreement
  surfaces as `conflict` for a human — nothing is silently "fixed."
- **Trust is by source tier** (`facts-sources.yaml`): `trusted` (textbooks,
  standards bodies) > `solid` (journals, PubMed, Wikipedia) > `low` (general web,
  AI, social). Weights refine the tiers later.
- **Experts confer authority by signing.** A domain expert reviews a claim and its
  evidence, then `python ../scripts/verify.py sign <file> --by <name> --note "…"` —
  a named, dated sign-off. That, not fluency, is the authoritative stamp.
- Every contribution is in the audit trail (the `evidence` array + `verified_by`),
  so credit and provenance are public and inspectable.

## The role of AI (including Claude)

**AI is a candidate generator and cross-checker — never an authority.** An
AI-proposed fact enters as `source: claude` (or `ai`), `tier: low`,
`status: source-attested`, `verified: false` — a **hypothesis**, not truth. It
becomes settled only when **corroborated by a higher-tier source** or **signed by
an expert**.

This is deliberate, and it is the project's own thesis turned on itself: fluent AI
output is exactly the plausible-but-unverified claim this commons exists to catch
(the *fluency trap*). AI can accelerate coverage and flag gaps; **humans and
primary sources confer authority.** An AI contribution that no source and no
expert ever backs stays a candidate forever — which is correct.

## Refuting requires a source

You may not flip a fact on an opinion. A `REFUTES` or `PARTIAL` contribution
**must cite where it comes from** — a URL and/or the exact passage. `facts.py`
rejects an unsourced disagreement. A *sourced* refutation is welcome: it creates a
`conflict`, which goes to expert review. Disputes here are settled with evidence,
not assertion.

## First-pass moderation — keep out attacks & noise

Before any contribution is recorded, an **AI screen** checks that it is
good-faith, on-topic, and substantive. It **accepts** substantive contributions —
*including well-sourced disagreement, which is exactly what we want* — and
**rejects**: spam/advertising, vandalism or attacks, off-topic content, empty or
noise submissions, and unsourced refutations. Rejected items are logged, not recorded.

**The screen judges good faith, never truth.** It must never reject a claim for
being contrarian or unpopular — truth is settled downstream by sources and
experts, not by the moderator. AI's two jobs here are clear and bounded: *propose
candidates* (low tier) and *filter junk* — it never decides what is true.

## Reviewing (for domain experts)

You are reviewing structured claims with provenance, not rewriting prose:
1. `python ../facts/facts.py status` → see the review queue (conflicts + candidates).
2. For a claim, read its `canonical` statement and its `evidence` (each source +
   verbatim). Then either **sign** it (you vouch for it) or **add an evidence
   record** that supports/refutes it (`facts.py record … --verdict …`).
3. Conflicts (`needs_review`) are the priority — two sources disagree; your call resolves it.

## License & openness

Facts are not copyrightable; the curated dictionary is shared openly so it helps
everyone (data as CC0; the structure and any *recreated* figures as CC-BY-SA).
Recreated diagrams are our own work — we never redistribute copyrighted source
images, only references for recreation. Contributors are credited through the
evidence trail and sign-offs.
