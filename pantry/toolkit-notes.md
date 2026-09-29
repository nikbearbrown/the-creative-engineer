# Toolkit Setup Notes

Source: ../ai1-cli. Date: 2026-09-29.

The project uses the supplied AI+1 constitution, conductor spine, synchronization script, verification script, and Blueprint scaffold method. Blueprint synthesis uses the author's existing schedule and course discussion; it does not skip the human Gate 0 required before Research.

## Observed upstream inconsistencies

- The source STATUS.md permits agent confirmation for some gates. AI1.md requires human sign-off for every gate; the new book follows AI1.md.
- conductor/VERIFICATION.md permits generation for an unverified artifact, while AI1.md says an existing unverified artifact is a stop. Follow AI1.md; do not overwrite unverified user work.
- The source Blueprint library includes biology-specific framing unrelated to this book. Use only the generic scaffold structure and the author's explicit design/agentic-AI subject. Do not import biology content or silently claim that source material is appropriate.
- The synchronization script uses Bash 4 mapfile; this Mac provides Bash 3.2. A temporary compatibility function supports its two fixed array reads without editing canonical tooling.
- The manifest does not supply every file mentioned by every export or figure command. Exports, figures, and optional editions are deferred; audit their dependencies at their authorized phases.

No credentials, node_modules, completed ai1-cli chapters, or human sign-offs are copied into this book. Per-book planning files were created before sync so the source book's filled seed templates cannot replace them.
