#!/bin/bash
set -e

cd "$(dirname "$0")"
BOOK_SLUG="$(basename "$(pwd)")"   # derive from the book's directory name (canonical, no per-book edit)
METADATA="metadata.yaml"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

cat $METADATA chapters/*.md > "$OUTPUT_DIR/combined.md"

pandoc "$OUTPUT_DIR/combined.md" \
  --from markdown \
  --to epub3 \
  --epub-cover-image=cover.jpg \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --toc --toc-depth=2 \
  --output="$OUTPUT_DIR/$BOOK_SLUG.epub"

pandoc "$OUTPUT_DIR/combined.md" \
  --from markdown \
  --to html5 \
  --standalone \
  --css=styles/kindle.css \
  --css=styles/kindle-book.css \
  --toc \
  --output="$OUTPUT_DIR/$BOOK_SLUG.html"

echo "Built: $OUTPUT_DIR/$BOOK_SLUG.epub"
echo "Built: $OUTPUT_DIR/$BOOK_SLUG.html"
