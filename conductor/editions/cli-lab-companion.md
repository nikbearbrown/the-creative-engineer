# Command-Line Lab Companion

> **Edition stub.** Run only after the spine is complete (GATE 6 signed).
> Expand this into a full prompt when you decide to build it.

**What it is:** Hands-on labs that walk the reader through doing the book's work at a CLI (Cowork/Claude Code/Codex).

**When to use:** Your book teaches a skill best learned by doing it at the command line.

**Inputs:** the finished spine chapters in `chapters/` (and `research/` where relevant).

**Outputs:** `editions/labs/<NN>-<slug>.md` — step-by-step labs with checkpoints.

## Starter prompt

```
Design hands-on CLI labs that map to the chapters. Each lab: a goal, prerequisites, numbered steps with the exact commands/prompts to run, expected output at each checkpoint, and a 'you're done when...' check. Assume the reader has a CLI agent. Keep each lab to one sitting. Include a troubleshooting note for the most likely failure.
```
