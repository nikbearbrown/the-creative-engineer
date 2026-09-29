#!/bin/bash
# build-canvas.sh — build the portable Canvas/LMS package (.imscc).
# Thin wrapper around build-imscc-standard.py so every target builds the same way.
set -e
PY=$(command -v python3 || command -v python)
[ -z "$PY" ] && { echo "Python 3 not found on PATH."; exit 1; }
cd "$(dirname "$0")"
"$PY" build-imscc-standard.py "$@"
