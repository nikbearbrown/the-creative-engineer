#!/usr/bin/env python3
"""verify.py — the verified-artifact gate.

Every artifact (foo.md, foo.py, ...) may have a sidecar foo.verified.json that
records human sign-off. The agent checks for a verified sidecar BEFORE generating;
if verified, it uses the existing artifact instead of regenerating.

  python scripts/verify.py check  <artifact>            # exit 0 verified+fresh, 1 unverified, 2 stale
  python scripts/verify.py stub   <artifact> --phase P  # agent: write verified:false sidecar (if none)
  python scripts/verify.py sign   <artifact> --by NAME [--note "..."]   # HUMAN: approve + record sha256
  python scripts/verify.py status [paths...]            # dashboard of gate + sidecar states

Rules: agents may `stub` and `check`. Only a human runs `sign`.
Sidecars are committed (audit trail) — do not gitignore them.
"""
import argparse
import datetime
import glob
import hashlib
import json
import os
import sys

# Spine phase gates (single-file artifacts). Per-file artifacts (chapters,
# scripts, editions, voices, data) get sidecars as they are produced and are
# picked up automatically by `status`.
PHASE_GATES = [
    ("intent", ["book.md"]),
    ("blueprint", ["vision.md", "architecture.md", "chapters-spec.md", "risks.md", "outline.md"]),
    ("factcheck", ["factcheck/report.md"]),
]


# Sidecar is "<artifact>.verified.json" (keeps the original extension visible).
def _sidecar(artifact):
    return artifact + ".verified.json"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_sidecar(artifact):
    p = _sidecar(artifact)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def state(artifact):
    """Return (code, label). 0=verified+fresh, 1=unverified/missing, 2=stale."""
    meta = load_sidecar(artifact)
    if not meta or not meta.get("verified"):
        return 1, "UNVERIFIED" if meta else "NO SIDECAR"
    recorded = meta.get("sha256")
    if recorded and os.path.exists(artifact):
        if sha256(artifact) != recorded:
            return 2, "STALE (modified since sign-off)"
    return 0, "verified"


def cmd_check(args):
    code, label = state(args.artifact)
    print(f"{args.artifact}: {label}")
    sys.exit(code)


def cmd_stub(args):
    p = _sidecar(args.artifact)
    if os.path.exists(p):
        meta = load_sidecar(args.artifact)
        print(f"sidecar exists ({'verified' if meta.get('verified') else 'unverified'}): {p} — not overwriting")
        return
    meta = {
        "artifact": os.path.basename(args.artifact),
        "phase": args.phase or "",
        "verified": False,
        "verified_by": "",
        "verified_at": "",
        "note": "",
        "sha256": "",
    }
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2)
        fh.write("\n")
    print(f"wrote stub (verified:false): {p}")
    print("STOP: artifact awaits human sign-off. Run `verify.py sign` after review.")


def cmd_sign(args):
    if not os.path.exists(args.artifact):
        sys.exit(f"artifact not found: {args.artifact}")
    if not args.by:
        sys.exit("refusing to sign without --by NAME (sign-off must name a human)")
    meta = load_sidecar(args.artifact) or {"artifact": os.path.basename(args.artifact)}
    meta.update({
        "artifact": os.path.basename(args.artifact),
        "phase": args.phase or meta.get("phase", ""),
        "verified": True,
        "verified_by": args.by,
        "verified_at": datetime.date.today().isoformat(),
        "note": args.note or meta.get("note", ""),
        "sha256": sha256(args.artifact),
    })
    p = _sidecar(args.artifact)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2)
        fh.write("\n")
    print(f"signed: {args.artifact} by {args.by} ({meta['verified_at']})")


def cmd_status(args):
    seen = set()
    rows = []

    def add(artifact, phase):
        if artifact in seen:
            return
        seen.add(artifact)
        exists = os.path.exists(artifact)
        code, label = state(artifact)
        rows.append((phase, artifact, "yes" if exists else "MISSING", label))

    # phase gates
    targets = args.paths or None
    if targets:
        for t in targets:
            for f in sorted(glob.glob(t)) or [t]:
                add(f, "")
    else:
        for phase, arts in PHASE_GATES:
            for a in arts:
                add(a, phase)
        # any existing sidecars anywhere (the per-file artifacts)
        for sc in sorted(glob.glob("**/*.verified.json", recursive=True)):
            add(sc[:-len(".verified.json")], load_sidecar(sc[:-len(".verified.json")]).get("phase", ""))

    print(f"{'PHASE':<12} {'ARTIFACT':<40} {'FILE':<8} STATE")
    print("-" * 78)
    for phase, art, exists, label in rows:
        print(f"{phase:<12} {art:<40} {exists:<8} {label}")
    nverified = sum(1 for r in rows if r[3] == "verified")
    print("-" * 78)
    print(f"{nverified}/{len(rows)} verified")


def main():
    ap = argparse.ArgumentParser(description="Verified-artifact gate.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check"); c.add_argument("artifact"); c.set_defaults(fn=cmd_check)
    s = sub.add_parser("stub"); s.add_argument("artifact"); s.add_argument("--phase"); s.set_defaults(fn=cmd_stub)
    g = sub.add_parser("sign"); g.add_argument("artifact"); g.add_argument("--by"); g.add_argument("--note"); g.add_argument("--phase"); g.set_defaults(fn=cmd_sign)
    t = sub.add_parser("status"); t.add_argument("paths", nargs="*"); t.set_defaults(fn=cmd_status)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
