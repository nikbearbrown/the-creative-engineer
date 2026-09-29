# AI1

**Version:** 0.1.0 · **Date:** 2026-06-11 · **Canonical home:** the `ai1-cli` repo — this file syncs to every book via `scripts/sync-to-book.sh`. If you are reading this in another book's repo, it is a synced copy; change it only in `ai1-cli`.

**AI+1** is one human plus AI agents making books neither could make alone. The AI executes: research, drafting, fact-lookup, figures, builds, audits. The **+1** — the human — does what cannot be delegated: deciding what the book *is*, rewriting it until it carries their voice, and signing their name to every gate. The "+1" is not a reviewer bolted onto an AI pipeline; the +1 is the reason the output is a book and not a pile of fluent text.

## Precedence

This file is the source of truth for the AI+1 system. If any file in this repository conflicts with it, this file governs and the conflict is a bug — report it to the human and record it. `CONDUCTOR.md` is the build spine — the *procedure* this constitution authorizes — not a rival authority.

## Principles

**P1 — The +1 is load-bearing.** Every gate is signed by a human in `STATUS.md`. GATE 3 (Human Rewrite) is human-only — no agent may ever sign it, and an agent never signs anything it cannot honestly attest. A phase that requires human judgment is not friction; it is the product differentiator.
*Violated when:* an agent signs a gate, or proceeds past an unsigned one.

**P2 — Generation is the fallback, not the default.** Before producing any artifact, check whether a verified one exists (`python scripts/verify.py check <artifact>`). Verified → use it, never regenerate. Unverified → stop and say so. Absent → generate, stub the sidecar, stop for sign-off. The sidecar (`<name>.verified.json`, appended to the full filename) is the artifact's passport.
*Violated when:* a verified artifact is silently regenerated, or new output skips its sidecar.

**P3 — Gates are hard stops, in order.** Seven phases make the spine (Blueprint → Research → Draft → Human Rewrite → Fact Check → Images → Check Images); no phase begins until the previous gate is signed in `STATUS.md`. A drafted-but-unresearched chapter is worse than no chapter.
*Violated when:* phases run out of order or a gate check is waved through.

**P4 — Facts are records, not recollections.** Check `facts/facts.json` before any external lookup. New facts enter `verified: false` and stay unauthoritative until a human signs them. A `verified: true` entry is never overwritten — new evidence is appended. Conflicting sources are a hard block only a human resolves.
*Violated when:* a claim ships from model memory, or a verified fact is edited instead of appended to.

**P5 — The human is non-technical; the agent does the typing.** Never ask the human to open a terminal, edit a file, run a command, or obtain an API key — the agent runs it and reports in plain language. Default to agent mode (the agent *is* the model; no key). When a key is unavoidable, use the secure path in `KEYS.md`: the key never passes through chat, is never echoed, never committed.
*Violated when:* the human is handed a command to run, or a key appears in a chat transcript.

**P6 — Canonical flows downstream, never back.** `ai1-cli` owns the tooling and recipes. `SOURCE-MANIFEST.md` declares what is CANONICAL (overwritten on sync), SEED (copied once), and PROTECTED (never touched — the book's content, sign-offs, facts data, secrets). To change a script or recipe, change it here and re-sync; a patch made downstream dies on the next sync.
*Violated when:* a canonical file is edited in a downstream book.

**P7 — Leave a trail.** Research notes, fact-check reports, audit output, and sidecars are artifacts — committed, not discarded. When unsure, stop and ask the human; a wrong autonomous phase is expensive to unwind.
*Violated when:* work happens that the repo cannot show evidence of.

## The Map

| File | Role |
|---|---|
| `AI1.md` | this constitution — read first |
| `CONDUCTOR.md` | the build spine: seven phases, gates, verified-artifact rules, editions |
| `STATUS.md` | ground truth for which phase is active and which gates are signed |
| `SOURCE-MANIFEST.md` | what propagates to other books, and how |
| `HELP.md` | friendly orientation — present it when the user types `help` or seems new |
| `HOW-TO-USE.md` | the full paste-into-any-CLI briefing |
| `MODES.md` / `KEYS.md` | agent mode vs API mode; secure key handling |
| `conductor/` | phase prompts, editions menu, voices, design system, `VERIFICATION.md` |
| `scripts/`, `build-*` | the runnable tooling |
| `facts/` | fact dictionary, extractor, source-tier registry, integration docs |

## Three Ways In

AI+1 makes books through talking to a CLI. A new user takes one of three paths:

1. **Download a finished book** — clone a complete, fact-checked AI+1 book from GitHub and make it yours (rewrite, re-voice, rebuild).
2. **Learn by doing** — type `help` in this starter and work the exercises: build the EPUB, generate quizzes, rewrite a chapter in another voice.
3. **Build from scratch** — run **Blueprint** (`conductor/00-blueprint/`, formerly Tic TOC), the textbook-architecture consultant that produces the planning layer, then follow the spine phase by phase.

## Start

1. Human-facing: type `help` (the agent presents `HELP.md`).
2. Agent-facing: read `CONDUCTOR.md`, then `STATUS.md`, then act — one phase, one gate, stop.
