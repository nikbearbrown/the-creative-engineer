# Choosing the model — always your call

Every tool here that needs an LLM (`extract-facts`, `build-anki`, `build-quizzes`,
`build-exercises`, the Phase-4 fact-checker, the voices) does its LLM step in one
of three ways. **You choose. You are never required to use Claude, and never
required to hold an API key.**

> **Non-technical users (the default):** if you're working in Cowork / Claude
> Desktop, you don't choose anything — the agent is the model and runs every
> step for you with no key and no terminal. The modes below matter only if you
> run the scripts yourself.

## The three modes

1. **Agent mode (no key).** Inside Cowork / Claude Code / Codex, the agent *is*
   the model and does the LLM step directly — covered by your subscription.
   Nothing to configure. Best for working a book interactively with a human watching.

2. **API mode (a key).** The script calls an LLM API unattended. Put the key in
   `.env`. Best for large batches with no one watching. *(The default provider is
   Anthropic; pointing it at another provider is a small endpoint/model edit.)*

3. **Handoff mode (any LLM, no key).** The script does the deterministic work,
   then **prints the prompt + input**. You run it through **any LLM** in a chat
   window — ChatGPT, Gemini, Claude, a local model — save the reply, and the
   script ingests it. This is the path when you're not using Claude and don't want
   a key.

## Handoff, step by step (facts extractor — the reference implementation)

```bash
python facts/extract-facts.py <book> --module mXXXXX --prepare
#   → writes facts/_handoff/<module>.prompt.md
# open that file, paste it into your LLM of choice, and save the JSON reply as
#   facts/_handoff/<module>.result.json
python facts/extract-facts.py <book> --ingest
#   → merges the results into facts.json, cited and tiered, no key used
```

The deterministic bookkeeping (dedup, consensus, citation, the `facts.json`
read/write) is identical across all three modes — only *who runs the LLM* changes.

## Support today

| Tool | Agent | API | Handoff |
|---|---|---|---|
| `facts/extract-facts.py` | ✓ | ✓ | ✓ (`--prepare` / `--ingest`) |
| `build-anki` · `build-quizzes` · `build-exercises` · fact-check | ✓ | ✓ (key) | pattern documented; add `--prepare`/`--ingest` the same way |

## The principle

The repo never assumes a vendor. Agent mode for convenience, API for scale,
handoff for full freedom with zero key. **The model is the user's choice, every
time** — including the choice not to use Claude at all.
