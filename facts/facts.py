#!/usr/bin/env python3
"""facts.py — the command-line interface to facts.json. EVERY fact tool routes
through here (or through facts_store directly). Used by the fact-checker to look
up a claim before any external check, and to record findings back.

  python facts/facts.py lookup "Homeostasis is the maintenance of stable internal conditions."
  python facts/facts.py record --claim "..." --source pubmed-123 --url https://... \
         --verbatim "exact sentence" --verdict SUPPORTS --domain physiology --category DEFINITION
  python facts/facts.py status

Verdicts: SUPPORTS | REFUTES | PARTIAL. Tier is auto-filled from facts-sources.yaml
if not given. Nothing is human-verified here — that is `scripts/verify.py sign`.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import facts_store as fs  # noqa: E402


def cmd_lookup(args):
    facts = fs.load_facts()
    fact, sim = fs.lookup(facts, args.claim)
    if not fact:
        print(f"NO MATCH (best similarity {sim:.2f}). Not in facts.json — external verification needed.")
        sys.exit(1)
    print(f"MATCH  similarity {sim:.2f}")
    print(f"  fact_id   : {fact['fact_id']}")
    print(f"  canonical : {fact['canonical']}")
    print(f"  consensus : {fact['consensus']}  (votes {fact['votes']}, same_publisher {fact['same_publisher']})")
    print(f"  status    : {fact['status']}  verified={fact['verified']}  needs_review={fact['needs_review']}")
    print(f"  evidence  : " + "; ".join(f"{e.get('source')}[{e.get('verdict')}]" for e in fact["evidence"]))
    # exit code signals usability: 0 = trust it (agreement/verified), 2 = candidate/conflict
    trusted = fact["verified"] or fact["consensus"] == "agreement"
    sys.exit(0 if trusted else 2)


def cmd_record(args):
    # A disagreement must cite where it comes from — no unsourced refutations.
    if args.verdict in ("REFUTES", "PARTIAL") and not (args.url or args.verbatim):
        sys.exit(f"A {args.verdict} contribution must cite a source: pass --url and/or "
                 f"--verbatim (the exact passage). Unsupported disagreements are rejected — "
                 f"see facts/CONTRIBUTING.md.")
    facts = fs.load_facts()
    sources = fs.load_sources()
    evidence = {"source": args.source, "verdict": args.verdict, "verbatim": args.verbatim or "", "url": args.url}
    if args.publisher:
        evidence["publisher"] = args.publisher
    if args.tier:
        evidence["tier"] = args.tier
    action, fact = fs.record_evidence(
        facts, args.claim, evidence, sources,
        canonical=args.canonical, domain=(args.domain.split(",") if args.domain else None),
        category=args.category, stable=not args.unstable)
    fs.save_facts(facts)
    print(f"{action}: {fact['fact_id']}")
    print(f"  consensus now: {fact['consensus']} (votes {fact['votes']})"
          + ("  <- CONFLICT, human review" if fact["needs_review"] else ""))


def cmd_status(args):
    facts = fs.load_facts()
    from collections import Counter
    c = Counter(f["consensus"] for f in facts)
    print(f"facts.json: {len(facts)} facts")
    print(f"  agreement={c['agreement']} partial={c['partial']} unverified={c['unverified']} conflict={c['conflict']}")
    print(f"  review queue (needs_review): {sum(1 for f in facts if f.get('needs_review'))}")


def main():
    ap = argparse.ArgumentParser(description="Interface to facts.json (the fact dictionary).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    lk = sub.add_parser("lookup"); lk.add_argument("claim"); lk.set_defaults(fn=cmd_lookup)
    rc = sub.add_parser("record")
    rc.add_argument("--claim", required=True)
    rc.add_argument("--canonical")
    rc.add_argument("--source", required=True)
    rc.add_argument("--url", default="")
    rc.add_argument("--verbatim", default="")
    rc.add_argument("--verdict", choices=["SUPPORTS", "REFUTES", "PARTIAL"], default="SUPPORTS")
    rc.add_argument("--publisher")
    rc.add_argument("--tier", choices=["trusted", "solid", "low"])
    rc.add_argument("--domain")
    rc.add_argument("--category", default="BASIC")
    rc.add_argument("--unstable", action="store_true")
    rc.set_defaults(fn=cmd_record)
    st = sub.add_parser("status"); st.set_defaults(fn=cmd_status)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
