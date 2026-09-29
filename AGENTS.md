<!-- GENERATED FILE — do not edit by hand.
     Source: instructions/ (_shared/ modules + project file) · manifest: instructions/manifest.yml
     Rebuild: node scripts/build-instructions.mjs   ·   Promote: --promote
     Hand edits are overwritten on the next build. -->

# Agent Instructions

## Visual media — follow `brutalist/`

All visual output in this repository — slides, SVG figures, D3 charts, diagrams, images, and any
generated graphic — follows the guidelines in the repo-root **`brutalist/`** folder. It is the
single source of truth and ships with the repo: clone it and you have the whole visual system.

- `brutalist/DESIGN.md` — brand: color tokens, typography, spacing, contrast, dark mode.
  **Change brand colors and fonts here**; every figure, slide, and SVG inherits the change.
- `brutalist/D3.md` — the D3 v7 figure-code constitution (pinned CDN, `var(--color-*)`, accessibility).
- `brutalist/SLIDES.md` — slide-deck rules; decks live in `slides/<deck-name>/index.html`.

Use only the DESIGN.md palette tokens (no hardcoded hex outside those tokens) and its type stack,
and meet its contrast minimums. To re-skin this repo's brand, edit `brutalist/DESIGN.md` only.
(`bear-textbooks/brutalist/` is an upstream backup; the in-repo `brutalist/` is authoritative.)
## Figure QA — two passes, always after (re)generating images

Whenever a figure is generated or regenerated (`npm run svg-to-png`), run BOTH review passes
before committing. Keep them separate — a layout fix never resolves a substance flag.

1. **Layout (geometry, deterministic):** `npm run audit:layout` — flags text outside the canvas,
   overflow, text struck by a line/arrow, overlapping labels, and risky glyphs. This runs
   automatically after `npm run svg-to-png` (see the `postsvg-to-png` script). Fix geometry first.
2. **Accuracy (substance, domain expert):** follow **`ACCURACY-REVIEW.md`** — paste the chapter and
   its figures; verify domain correctness by computation/source, check notation/rendering, audit the
   chapter's stats/tables/formulas, and resolve every `**[verify]**` tag.

Order: layout first, accuracy second.

## Governance

This repository is built phase-by-phase through a gated pipeline.

**Read `AI1.md` first — it is the source of truth for the AI+1 system** (one human plus AI agents making books neither could make alone). It authorizes `CONDUCTOR.md` as the build spine; read that next, then `STATUS.md` to see which phase is active and which gates are signed. If any file conflicts with `AI1.md`, `AI1.md` governs and the conflict is a bug — report it to the human and record it.

## `help`

If the user types `help` (or seems new, or asks "what can I do?"), **read `HELP.md` and present it** — the friendly, non-technical orientation for someone who just opened this repo and wants to talk to the book. For the full briefing on the two build paths and how the agent works, see `HOW-TO-USE.md`.

## The human is non-technical; the agent does the typing (P5)

Assume the user is non-technical — email and chatting with the agent on a website, nothing more. **Never ask them to open a terminal, edit a file, run a command, or obtain an API key.** *You* run the scripts, edit the files, and build the outputs, then report in plain language. Default to **agent mode**: you are the model, so the LLM steps need no API key.

## Secure key path (P5)

If a key is ever genuinely required (e.g. ElevenLabs audio), use the **secure path** so the key never passes through chat: create `.env` from `.env.example` if missing, **open it** for the user (e.g. `open .env`), have them paste the key on its line and save, then confirm it's set with a non-echoing check (`grep -q '^ELEVENLABS_API_KEY=.\+' .env`). **Never print, echo, log, or repeat a key back, and never commit `.env`.** Only offer the paste-in-chat shortcut if they prefer convenience, and warn once that it sends the key through the chat. See `KEYS.md` and `MODES.md`.

## Phase gates, in order (P1, P3)

Work one phase at a time, in order — do not skip a gate. Do not start a phase until the previous phase's gate is signed off in `STATUS.md`. Phase instructions live in `conductor/<phase>/`; executable code lives in `scripts/`. **GATE 3 (Human Rewrite) is human-only — never sign it yourself**, and never sign anything you cannot honestly attest.

## Generation is the fallback, not the default (P2)

**Before generating any artifact, check it isn't already verified:** run `python scripts/verify.py check <artifact>`. If verified (exit 0), **use the existing file — do not regenerate.** If unverified, stop and say so. If absent, generate it, run `python scripts/verify.py stub <artifact> --phase <phase>`, and **STOP** for human sign-off. Only a human runs `python scripts/verify.py sign`. The sidecar (`<name>.verified.json`) is the artifact's passport. See `conductor/VERIFICATION.md`.

## Leave a trail (P7)

Research notes, fact-check reports, audit output, and `.verified.json` sidecars are artifacts — **commit them, do not discard.** Never delete a hand-made artifact or a sidecar; the only safe removals are rebuildable outputs (`output/`, `__pycache__/`, `*.pyc`). When unsure, stop and ask the human — a wrong autonomous phase is expensive to unwind.

## AI1 CLI

This repo writes books with the **AI+1** method — one human plus AI agents making a book neither could make alone. The agent executes (research, drafting, fact-lookup, figures, builds, audits); the **+1**, the human, does what cannot be delegated: deciding what the book *is*, rewriting it until it carries their voice, and signing every gate. The seven-phase spine runs Blueprint → Research → Draft → Human Rewrite → Fact Check → Images → Check Images, with optional `conductor/editions/` and `voices/` after the spine.

Everything operational lives in `CONDUCTOR.md` (the spine), `STATUS.md` (current phase + gate state), `MODES.md` / `KEYS.md` (agent mode and the secure key path), and `SOURCE-MANIFEST.md` (what syncs downstream).

For a **complete course**, not merely a chapter export, read `.claude/skills/full-course/SKILL.md`. It covers course blueprints, reading-to-lesson mappings, syllabus, ungraded Assessments, graded Assignments and rubrics, prerequisites, submissions, Canvas delivery and instructor film plans. It supports the NEU **Predict → Build It → Use It → Ship It → Verify** profile and partial releases. Human book/course gates still apply; creating a course does not authorize publishing or starting continuous workers.
