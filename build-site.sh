#!/bin/bash
# build-site.sh — scaffold the React/Next.js site from the book markdown.
# Thin wrapper around build-react-site.py.
set -e
PY=$(command -v python3 || command -v python)
[ -z "$PY" ] && { echo "Python 3 not found on PATH."; exit 1; }
cd "$(dirname "$0")"
"$PY" build-react-site.py "$@"
