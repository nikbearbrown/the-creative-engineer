#!/usr/bin/env python3
"""Read-only inventory and narrow structural validation; never signs approvals."""
import argparse
import json
import math
import re
from pathlib import Path

STAGES = ("Predict", "Build It", "Use It", "Ship It", "Verify")
ARTIFACTS = ("syllabus", "course_guide", "prerequisites", "ai_policy",
             "submission_template", "reading_map")
NEU_RUBRIC = dict(implementation=60, frictional=10, github=10, relative_quartile=20)
POLICY = "https://youtu.be/8Ut0Cdl6vMw"


def inventory(root):
    """Adapt the two observed metadata layouts without changing their files."""
    data = json.loads((root / "course.json").read_text())
    key = "lessons" if "lessons" in data else "weeks"
    rows = data.get(key, [])
    if not isinstance(rows, list):
        raise ValueError(f"{key} must be a list")
    return {"root": str(root), "schema": key, "count": len(rows),
            "entries": rows,
            "note": "Metadata inventory only; resolve readings and inspect content separately."}


def validate(root, data, files=False):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def seq(value, label):
        if not isinstance(value, list) or not value:
            errors.append(f"{label}: expected nonempty list")
            return []
        return value

    def refs(value, allowed, label):
        items = seq(value, label)
        for item in items:
            require(isinstance(item, str) and item in allowed,
                    f"{label}: unknown reference {item!r}")
        return [x for x in items if isinstance(x, str) and x in allowed]

    def path(value, label, released=True):
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: expected relative file path")
            return None
        p = Path(value)
        resolved = (root / p).resolve()
        if p.is_absolute() or ".." in p.parts or not resolved.is_relative_to(root):
            errors.append(f"{label}: path escapes course root: {value}")
            return None
        if files and released and not resolved.is_file():
            errors.append(f"{label}: missing file: {value}")
        return resolved

    def points(value, label):
        if not isinstance(value, dict) or not value:
            errors.append(f"{label}: expected nonempty points object")
            return None
        vals = list(value.values())
        if any(type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in vals):
            errors.append(f"{label}: points must be finite nonnegative numbers")
            return None
        return sum(vals)

    def records(key):
        rows, seen = [], set()
        for row in seq(data.get(key), key):
            if not isinstance(row, dict):
                errors.append(f"{key}: expected object")
                continue
            ident = row.get("id")
            if not isinstance(ident, str) or not ident.strip():
                errors.append(f"{key}: missing string id")
                continue
            require(ident not in seen, f"{key}: duplicate id {ident}")
            seen.add(ident)
            require(type(row.get("released")) is bool, f"{ident}: released must be boolean")
            if data.get("release") == "full":
                require(row.get("released") is True, f"full release omits {ident}")
            rows.append(row)
        return rows

    if not isinstance(data, dict):
        return ["plan must be a JSON object"]
    require(data.get("schema_version") == 1, "schema_version must be 1")
    require(data.get("profile") in ("neu", "custom"), "profile must be neu or custom")
    require(data.get("release") in ("full", "partial"), "release must be full or partial")
    for field in ("title", "term"):
        require(isinstance(data.get(field), str) and bool(data[field].strip()), f"{field} is required")
    cadence = data.get("assignment_cadence_days")
    require(type(cadence) is int and cadence > 0, "cadence must be a positive integer")
    if data.get("profile") == "neu":
        require(cadence == 10, "NEU assignments must be every 10 days")
    outcomes = seq(data.get("outcomes"), "outcomes")
    require(all(isinstance(x, str) and x.strip() for x in outcomes), "outcomes must be nonempty strings")
    outcomes = [x for x in outcomes if isinstance(x, str) and x.strip()]
    require(len(set(outcomes)) == len(outcomes), "duplicate outcome ids")
    artifacts = data.get("artifacts", {})
    if not isinstance(artifacts, dict):
        artifacts = {}
    for key in ARTIFACTS:
        p = path(artifacts.get(key), key)
        if files and key == "ai_policy" and data.get("profile") == "neu" and p and p.is_file():
            require(POLICY in p.read_text(), "prerequisites: missing AI policy video link")
    modules = records("modules")
    by_id = {m["id"]: m for m in modules}
    assessment_ids = set()
    module_outcomes = {}
    for mod in modules:
        ident, released = mod["id"], mod.get("released") is True
        module_outcomes[ident] = refs(mod.get("outcomes"), outcomes, ident + " outcomes")
        for reading in seq(mod.get("readings"), ident + " readings"):
            path(reading, ident + " reading", released)
        p = path(mod.get("lesson"), ident + " lesson", released)
        if files and released and p and p.is_file():
            headings = re.findall(r"^##\s+(.+?)\s*$", p.read_text(), re.M)
            actual = [h for h in headings if h in STAGES]
            require(actual == list(STAGES), f"{ident}: missing, repeated or unordered teaching stages")
        for assessment in seq(mod.get("assessments"), ident + " assessments"):
            if not isinstance(assessment, dict):
                errors.append(f"{ident}: assessment must be object")
                continue
            aid = assessment.get("id")
            if not isinstance(aid, str) or not aid.strip():
                errors.append(f"{ident}: assessment id required")
            else:
                require(aid not in assessment_ids, f"duplicate assessment id {aid}")
                assessment_ids.add(aid)
            require(assessment.get("graded") is False, f"{ident}: Assessments must be ungraded")
            path(assessment.get("path"), ident + " assessment", released)
    assignments = records("assignments")
    covered = set()
    assessed_outcomes = set()
    for item in assignments:
        ident, released = item["id"], item.get("released") is True
        mids = refs(item.get("modules"), by_id, ident + " modules")
        covered.update(mids)
        oids = refs(item.get("outcomes"), outcomes, ident + " outcomes")
        assessed_outcomes.update(oids)
        taught = {o for mid in mids for o in module_outcomes[mid]}
        require(set(oids) <= taught, f"{ident}: assesses outcomes absent from linked modules")
        if released:
            require(all(by_id[mid].get("released") is True for mid in mids),
                    f"{ident}: released assignment depends on unreleased module")
        total = item.get("points")
        require(type(total) in (int, float) and math.isfinite(total) and total > 0,
                f"{ident}: invalid total points")
        rubric = item.get("rubric")
        rubric_sum = points(rubric, ident + " rubric")
        require(rubric_sum is not None and rubric_sum == total, f"{ident}: rubric does not sum to points")
        impl_sum = points(item.get("implementation_criteria"), ident + " implementation criteria")
        require(isinstance(rubric, dict) and impl_sum is not None and impl_sum == rubric.get("implementation"),
                f"{ident}: implementation criteria total mismatch")
        if data.get("profile") == "neu":
            require(total == 100 and rubric == NEU_RUBRIC, f"{ident}: requires 100 points split 60/10/10/20")
        p = path(item.get("path"), ident + " assignment", released)
        if files and released and p and p.is_file() and data.get("profile") == "neu":
            require(POLICY in p.read_text(), f"{ident}: missing AI policy video link")
    require(set(by_id) <= covered, "some planned modules have no Assignment mapping")
    require(set(outcomes) <= assessed_outcomes, "some outcomes have no graded evidence mapping")
    require(any(m.get("released") is True for m in modules), "release contains no modules")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=("inventory", "validate"))
    ap.add_argument("root", type=Path)
    ap.add_argument("--files", action="store_true", help="also inspect released artifact files")
    args = ap.parse_args()
    root = args.root.resolve()
    try:
        if args.mode == "inventory":
            print(json.dumps(inventory(root), indent=2))
            return 0
        data = json.loads((root / "course-plan.json").read_text())
        errors = validate(root, data, args.files)
    except (OSError, ValueError) as exc:
        print(json.dumps({"errors": [str(exc)], "human_approval": "not checked"}))
        return 2
    print(json.dumps({"mechanical_check": "fail" if errors else "pass",
                      "errors": errors, "human_approval": "not checked",
                      "content_accuracy_and_LMS_import": "not checked"}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
