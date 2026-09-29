# Verified Artifacts

**Generation is the fallback, not the default.** Before producing any artifact,
the agent checks whether a human has already reviewed and signed off on it. If a
verified version exists, use it — do not regenerate. If not, generate it, write a
`verified:false` stub, and **stop** for human sign-off before the next phase.

This is the machine-checkable layer beneath the spine gates. `STATUS.md` is the
human-readable dashboard; the `.verified.json` sidecars are what the agent and
`scripts/verify.py` actually read to decide generate-vs-use and to resume.

---

## Sidecar format

Each artifact `foo.md` (or `.py`, `.csv`, `.svg`, …) has a sibling
`foo.md.verified.json`:

```json
{
  "artifact": "foo.md",
  "phase": "draft",
  "verified": true,
  "verified_by": "nik",
  "verified_at": "2026-06-09",
  "note": "structure approved, proceed to revision",
  "sha256": "hash of the artifact at sign-off"
}
```

No sidecar, or `verified:false`, means **unverified**. A signed sidecar whose
`sha256` no longer matches the file means **stale** (the artifact changed after
sign-off) — treated as unverified until re-signed.

**Sidecars are committed** — they are the audit trail. Do not gitignore them.

---

## Routing logic (the agent follows this)

Before generating artifact `X`:

```bash
python scripts/verify.py check X
```

- **exit 0** (verified + fresh) → load and use `X`. **Do not regenerate.**
- **exit 1 or 2** (unverified / stale) → generate `X`, then:
  ```bash
  python scripts/verify.py stub X --phase <phase>
  ```
  and **STOP**. Do not start the next phase.

The human reviews `X`, then signs:

```bash
python scripts/verify.py sign X --by <name> --note "..."
```

On resume, `check X` now returns 0 and the agent proceeds.

> **Agents may `stub` and `check`. Only a human runs `sign`.** This is the same
> principle as GATE 3 (Human Rewrite): the agent never approves its own work.

---

## Phase → verified artifact map

| Phase | Verified artifact(s) |
|---|---|
| 0 Blueprint | `book.md`, `vision.md`, `architecture.md`, `chapters-spec.md`, `risks.md`, `outline.md` |
| 1 Research | `research/<chapter>.md` (per chapter) |
| 2 Draft | `chapters/<chapter>.md` |
| 3 Human rewrite | `chapters/<chapter>.md` (re-signed after the rewrite) |
| 4 Fact check | `factcheck/report.md` |
| 5 Images | `images/<figure>.svg` (per figure) |
| 6 Check images | the audit output / signed figures |
| Editions | `conductor/editions/*` outputs |
| Voices | `voices/<voice>/<chapter>.md` |
| Scripts | `scripts/<name>.py` |
| Data | `data/<name>` |

A phase's gate is met when its artifacts are signed. Reflect the milestone in
`STATUS.md` so the dashboard stays current.

---

## Commands

```bash
python scripts/verify.py status            # dashboard: every gate + sidecar, with drift
python scripts/verify.py check  <artifact> # 0 verified+fresh · 1 unverified · 2 stale
python scripts/verify.py stub   <artifact> --phase <phase>     # agent, after generating
python scripts/verify.py sign   <artifact> --by <name> --note "..."   # human approval
```

---

## Why this works

- **Token budget is gated** — expensive generation only runs on approved input.
- **Errors don't compound** — drift is caught early, when it's cheap to fix.
- **Sessions are resumable** — the sidecars always record the last verified state.
- **The pipeline is auditable** — who checked what, and when.

The human is the gate. The agent is the engine. Neither runs ahead of the other.
