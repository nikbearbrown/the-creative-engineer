#!/usr/bin/env python3
"""build-react-site.py — scaffold a Next.js site from the book markdown.

NOT YET IMPLEMENTED. See chapters/95-appendix-react-site.md for the full spec:
stdlib-only Python scaffolder that emits content/<slug>.mdx, app/<slug>/page.tsx,
app/page.tsx, app/layout.tsx, components/AskAI.tsx, mdx-components.tsx,
next.config.mjs, tsconfig.json, package.json into --out (default ./site).
"""
import sys

def main():
    sys.exit(
        "build-react-site.py is not implemented yet.\n"
        "Spec: chapters/95-appendix-react-site.md. The Canvas path "
        "(./build-canvas.sh) is the supported target today."
    )

if __name__ == "__main__":
    main()
