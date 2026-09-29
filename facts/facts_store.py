#!/usr/bin/env python3
"""facts_store.py — the canonical fact model. EVERY fact tool routes through here.

Holds the schema, the wording-similarity dedup, the derived consensus/voting, and
the read (`lookup`) / write (`record_evidence`) operations on `facts.json`.
The extractor and the fact-checker both import this — there is one store, one set
of rules. Dependency-light (stdlib + pyyaml); no network.
"""
import datetime
import difflib
import json
import os
import re

try:
    import yaml
except ImportError:
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
FACTS_JSON = os.path.join(HERE, "facts.json")
SOURCES_YAML = os.path.join(HERE, "facts-sources.yaml")
TODAY = datetime.date.today().isoformat()

MERGE_THRESHOLD = 0.82   # wording this close (numbers aside) = same claim
NEAR_THRESHOLD = 0.70    # close-but-not-sure = flag possible duplicate for review
_STOP = set("a an the is are was were be been being of to in on at by for with as that this these "
            "those it its and or not from into within can may will which who whose".split())


# ---------- source tiers ----------
def load_sources(path=SOURCES_YAML):
    if yaml and os.path.exists(path):
        return (yaml.safe_load(open(path)) or {}).get("sources", {})
    return {}


def source_meta(name, sources):
    s = sources.get(name, sources.get("unknown", {"tier": "low", "publisher": None}))
    return s.get("tier", "low"), s.get("publisher")


# ---------- text helpers ----------
def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower())
    return re.sub(r"[\s_-]+", "-", s).strip("-")[:60] or "fact"


def normalize(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", s.lower())).strip()


def _content_tokens(s):
    return [t for t in re.findall(r"[a-z]+", s.lower()) if t not in _STOP]


def numbers(s):
    return set(re.findall(r"\d+(?:\.\d+)?", s))


def _strip_numbers(s):
    return re.sub(r"\d+(?:\.\d+)?", "", s)


def wording_similarity(a, b):
    """0..1 similarity of wording, numbers ignored. Token-sort ratio + Jaccard."""
    ta, tb = _content_tokens(_strip_numbers(a)), _content_tokens(_strip_numbers(b))
    if not ta or not tb:
        return 0.0
    seq = difflib.SequenceMatcher(None, " ".join(sorted(ta)), " ".join(sorted(tb))).ratio()
    A, B = set(ta), set(tb)
    return 0.5 * seq + 0.5 * (len(A & B) / len(A | B))


# ---------- consensus (DERIVED, never set by hand) ----------
def recompute_consensus(fact, sources):
    ev = fact["evidence"]
    supporters = {e["source"] for e in ev if e.get("verdict") == "SUPPORTS"}
    publishers = {(e.get("publisher") or e["source"]) for e in ev if e.get("verdict") == "SUPPORTS"}
    has_refute = any(e.get("verdict") == "REFUTES" for e in ev)
    has_partial = any(e.get("verdict") == "PARTIAL" for e in ev)
    votes = len(supporters)
    if has_refute:
        consensus = "conflict"
    elif votes >= 2:
        consensus = "agreement"
    elif has_partial and votes >= 1:
        consensus = "partial"
    else:
        consensus = "unverified"
    fact["votes"] = votes
    fact["consensus"] = consensus
    fact["same_publisher"] = (len(publishers) <= 1)
    fact["needs_review"] = (consensus == "conflict")
    return fact


def make_fact(extracted, citation, tier, sources):
    """Build a source-attested fact from an extraction (verdict always SUPPORTS)."""
    fact = {
        "fact_id": slugify("-".join(extracted.get("domain", ["gen"])[:1] + [extracted["canonical"]])),
        "canonical": extracted["canonical"].strip(),
        "domain": extracted.get("domain", []),
        "stable": bool(extracted.get("stable", True)),
        "status": "source-attested",
        "verified": False,
        "verified_by": None, "verified_at": None, "human_note": None,
        "consensus": "unverified", "votes": 0, "same_publisher": True, "needs_review": False,
        "evidence": [{**citation, "tier": tier,
                      "verbatim": extracted.get("verbatim", "").strip(),
                      "retrieved": TODAY, "verdict": "SUPPORTS"}],
        "books": [],
        "category": extracted.get("category", "BASIC"),
        "expires": None,
    }
    return recompute_consensus(fact, sources)


def _append_evidence(fact, ev_list, sources):
    sig = {(e.get("source"), e.get("module"), e.get("url")) for e in fact["evidence"]}
    for e in ev_list:
        if (e.get("source"), e.get("module"), e.get("url")) not in sig:
            fact["evidence"].append(e)
    recompute_consensus(fact, sources)


def _best_match(facts, canonical):
    best_sim, best = 0.0, None
    for f in facts:
        sim = 1.0 if normalize(f["canonical"]) == normalize(canonical) else wording_similarity(canonical, f["canonical"])
        if sim > best_sim:
            best_sim, best = sim, f
    return best_sim, best


def merge_fact(facts, new_fact, sources):
    """Merge an extracted fact. Returns: merged | flagged-numeric-conflict | added-near-dup | added."""
    can = new_fact["canonical"]
    best_sim, best = _best_match(facts, can)
    if best is not None and best_sim >= MERGE_THRESHOLD:
        if numbers(can) == numbers(best["canonical"]):
            _append_evidence(best, new_fact["evidence"], sources)
            return "merged"
        new_fact["needs_review"] = True
        new_fact["numeric_conflict_with"] = best["fact_id"]
        facts.append(new_fact)
        return "flagged-numeric-conflict"
    if best is not None and best_sim >= NEAR_THRESHOLD:
        new_fact["needs_review"] = True
        new_fact["possible_duplicate_of"] = best["fact_id"]
        facts.append(new_fact)
        return "added-near-dup"
    facts.append(new_fact)
    return "added"


# ---------- read / write facts.json ----------
def load_facts(path=FACTS_JSON):
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    return []


def save_facts(facts, path=FACTS_JSON):
    json.dump(facts, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)


def lookup(facts, claim):
    """READ: best existing fact for a claim. Returns (fact_or_None, similarity).
    A fact-checker calls this BEFORE any external lookup."""
    sim, best = _best_match(facts, claim)
    if best is not None and sim >= NEAR_THRESHOLD:
        return best, sim
    return None, sim


def record_evidence(facts, claim, evidence, sources, *,
                    canonical=None, domain=None, category="BASIC", stable=True):
    """WRITE: attach a finding to facts.json. Appends to a matching fact (same
    wording + same numbers) or creates a new source-attested fact. Never overwrites
    a verified entry — it only appends evidence. Returns (action, fact).
    `evidence` needs at least {source, verdict}; tier/retrieved are filled if absent."""
    canonical = (canonical or claim).strip()
    ev = dict(evidence)
    ev.setdefault("retrieved", TODAY)
    if "tier" not in ev:
        ev["tier"], pub = source_meta(ev.get("source", "unknown"), sources)
        ev.setdefault("publisher", pub)
    ev.setdefault("verdict", "SUPPORTS")

    best_sim, best = _best_match(facts, canonical)
    if best is not None and best_sim >= MERGE_THRESHOLD and numbers(canonical) == numbers(best["canonical"]):
        _append_evidence(best, [ev], sources)         # append vote/refute; consensus recomputes
        return ("appended", best)

    fact = {
        "fact_id": slugify("-".join((domain or ["gen"])[:1] + [canonical])),
        "canonical": canonical, "domain": domain or [], "stable": bool(stable),
        "status": "source-attested", "verified": False,
        "verified_by": None, "verified_at": None, "human_note": None,
        "consensus": "unverified", "votes": 0, "same_publisher": True, "needs_review": False,
        "evidence": [ev], "books": [], "category": category, "expires": None,
    }
    recompute_consensus(fact, sources)
    facts.append(fact)
    return ("created", fact)
