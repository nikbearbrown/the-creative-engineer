"""Synthetic fixtures only; no production files or approval records changed."""
import copy
import json
import re
import tempfile
import unittest
from pathlib import Path
from course_check import ARTIFACTS, NEU_RUBRIC, POLICY, STAGES, inventory, validate


class CourseCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.plan = dict(schema_version=1, profile="neu", title="Fixture", term="Test",
                         release="full", assignment_cadence_days=10, outcomes=["O1"],
                         artifacts={k: k + ".md" for k in ARTIFACTS},
                         modules=[dict(id="M1", released=True, outcomes=["O1"],
                                       readings=["reading.md"], lesson="lesson.md",
                                       assessments=[dict(id="A1", graded=False, path="assessment.md")])],
                         assignments=[dict(id="AS1", released=True, modules=["M1"], outcomes=["O1"],
                                           path="assignment.md", points=100, rubric=NEU_RUBRIC.copy(),
                                           implementation_criteria={"mechanism": 40, "verification": 20})])
        for name in list(self.plan["artifacts"].values()) + ["reading.md", "assessment.md", "assignment.md"]:
            (self.root / name).write_text(POLICY + "\nSynthetic fixture\n")
        (self.root / "lesson.md").write_text("\n".join("## " + x for x in STAGES))

    def errors(self):
        return validate(self.root, self.plan, files=True)

    def test_complete_fixture(self):
        self.assertEqual(self.errors(), [])

    def test_missing_reading(self):
        (self.root / "reading.md").unlink()
        self.assertTrue(any("missing file" in e for e in self.errors()))

    def test_path_escape(self):
        self.plan["modules"][0]["readings"] = ["../private.md"]
        self.assertTrue(any("escapes" in e for e in self.errors()))

    def test_symlink_escape(self):
        (self.root / "outside.md").symlink_to(self.root.parent / "private.md")
        self.plan["modules"][0]["readings"] = ["outside.md"]
        self.assertTrue(any("escapes" in e for e in self.errors()))

    def test_bad_rubric_and_boolean_points(self):
        self.plan["assignments"][0]["rubric"]["github"] = True
        self.assertTrue(any("finite nonnegative" in e for e in self.errors()))

    def test_implementation_total(self):
        self.plan["assignments"][0]["implementation_criteria"]["mechanism"] = 35
        self.assertTrue(any("implementation criteria total" in e for e in self.errors()))

    def test_graded_assessment(self):
        self.plan["modules"][0]["assessments"][0]["graded"] = True
        self.assertTrue(any("ungraded" in e for e in self.errors()))

    def test_duplicate_ids(self):
        self.plan["modules"].append(copy.deepcopy(self.plan["modules"][0]))
        self.assertTrue(any("duplicate id" in e for e in self.errors()))

    def test_stage_order(self):
        (self.root / "lesson.md").write_text("\n".join("## " + x for x in reversed(STAGES)))
        self.assertTrue(any("teaching stages" in e for e in self.errors()))

    def test_policy_required(self):
        (self.root / "assignment.md").write_text("No link")
        self.assertTrue(any("AI policy" in e for e in self.errors()))

    def test_partial_release(self):
        self.plan["release"] = "partial"
        future = dict(id="M2", released=False, outcomes=["O1"], readings=["future.md"],
                      lesson="future-lesson.md", assessments=[dict(id="A2", graded=False, path="future-a.md")])
        self.plan["modules"].append(future)
        future_a = copy.deepcopy(self.plan["assignments"][0])
        future_a.update(id="AS2", released=False, modules=["M2"], path="future-assignment.md")
        self.plan["assignments"].append(future_a)
        self.assertEqual(self.errors(), [])
        self.plan["release"] = "full"
        self.assertTrue(any("full release omits" in e for e in self.errors()))
        self.plan["release"] = "partial"
        future_a["released"] = True
        self.assertTrue(any("depends on unreleased" in e for e in self.errors()))

    def test_unknown_mapping_and_outcome(self):
        self.plan["assignments"][0].update(modules=["missing"], outcomes=["absent"])
        self.assertTrue(any("unknown reference" in e for e in self.errors()))

    def test_malformed_shapes(self):
        self.plan.update(modules=[None, {"id": []}], assignments=[False], outcomes=[{}])
        self.assertTrue(self.errors())
        self.assertTrue(validate(self.root, []))

    def test_inventory_schemas(self):
        for key in ("weeks", "lessons"):
            (self.root / "course.json").write_text(json.dumps({key: [{"path": "lesson-directory"}]}))
            report = inventory(self.root)
            self.assertEqual(report["schema"], key)
            self.assertEqual(report["count"], 1)

    def test_documented_template(self):
        template = Path(__file__).resolve().parents[1] / "assets/course-templates.md"
        block = re.search(r"```json\n(.*?)\n```", template.read_text(), re.S).group(1)
        self.assertEqual(validate(self.root, json.loads(block)), [])

    def test_custom_profile(self):
        self.plan.update(profile="custom", assignment_cadence_days=7)
        item = self.plan["assignments"][0]
        item.update(points=25, rubric={"implementation": 20, "reflection": 5},
                    implementation_criteria={"mechanism": 15, "verification": 5})
        self.assertEqual(self.errors(), [])


if __name__ == "__main__":
    unittest.main()
