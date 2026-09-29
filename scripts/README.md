# scripts/

Runnable code for this book (run from the book root). **Prompts live in
`conductor/`, not here.**

## svg-to-png.mjs
Converts every `images/**/*.svg` to a 300dpi PNG. Idempotent.
```bash
node scripts/svg-to-png.mjs
```
**Requires:** `sharp`, `glob` (`npm install`).

## svg-visual-audit.mjs
Semantic + geometric figure audit — bad sub/superscripts, broken math notation,
text overflow. Used in Phase 6 (Check Images).
```bash
DRY_RUN=1 node scripts/svg-visual-audit.mjs          # report only
ANTHROPIC_API_KEY=sk-ant-... node scripts/svg-visual-audit.mjs   # AI fixer
```

## sync-to-book.sh
Propagates canonical scripts & recipes from this (source-of-truth) repo into
another book repo, per `../SOURCE-MANIFEST.md`. Overwrites canonical files, seeds
templates only if missing, never touches the book's content/data/secrets.
```bash
scripts/sync-to-book.sh [--dry-run] <target-book-dir>
```
