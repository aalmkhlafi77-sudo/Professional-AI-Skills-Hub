import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_catalog", ROOT / "scripts/validate_catalog.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class CatalogTests(unittest.TestCase):
    def test_validator_cli(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_catalog.py")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_no_unverified_approved(self):
        data = json.loads((ROOT / "catalog/approved.json").read_text(encoding="utf-8"))
        self.assertEqual(data["approved"], [])

    def test_candidate_lifecycle(self):
        data = json.loads((ROOT / "catalog/candidates.json").read_text(encoding="utf-8"))
        self.assertEqual(len({item["id"] for item in data["candidates"]}), len(data["candidates"]))
        self.assertTrue(all(item["status"] in validator.STATES for item in data["candidates"]))

    def test_reject_fake_approval_missing_gates(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            (tmp / "catalog").mkdir()
            (tmp / "skills").mkdir()
            (tmp / "catalog/candidates.json").write_text('{"schema_version":1,"candidates":[]}', encoding="utf-8")
            (tmp / "catalog/approved.json").write_text(json.dumps({
                "schema_version": 1, "approved": [{
                    "id": "example/test", "url": "https://github.com/example/test",
                    "commit_sha": "a" * 40, "license_verified": True,
                    "security_review": "passed", "sandbox_test": "passed",
                    "mandatory_gates_passed": True, "score": 100, "reviewer": "test",
                    "evidence_path": "docs/reviews/test.md"
                }]
            }), encoding="utf-8")
            old_root = validator.ROOT
            try:
                validator.ROOT = tmp
                with self.assertRaisesRegex(ValueError, "incomplete gate matrix"):
                    validator.validate()
            finally:
                validator.ROOT = old_root

    def test_reject_score_inconsistency_and_fake_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            (tmp / "catalog").mkdir()
            (tmp / "skills").mkdir()
            (tmp / "catalog/candidates.json").write_text('{"schema_version":1,"candidates":[]}', encoding="utf-8")
            row = {
                "id": "example/test", "url": "https://github.com/example/test",
                "commit_sha": "a" * 40, "license_verified": True,
                "security_review": "passed", "sandbox_test": "passed",
                "mandatory_gates_passed": True, "score": 100, "reviewer": "test",
                "evidence_path": "docs/reviews/nonexistent.md",
                "gates": {gate: "passed" for gate in validator.GATES},
                "score_breakdown": {"security": 30, "practical": 25, "compatibility": 20, "source_license": 15, "documentation": 0}
            }
            p = tmp / "catalog/approved.json"
            p.write_text(json.dumps({"schema_version": 1, "approved": [row]}), encoding="utf-8")
            old_root = validator.ROOT
            try:
                validator.ROOT = tmp
                with self.assertRaisesRegex(ValueError, "score below policy"):
                    validator.validate()
                row["score"] = 90
                p.write_text(json.dumps({"schema_version": 1, "approved": [row]}), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "evidence file missing"):
                    validator.validate()
            finally:
                validator.ROOT = old_root

    def test_reject_optimized_python_bypass(self):
        result = subprocess.run(
            [sys.executable, "-O", str(ROOT / "scripts/validate_catalog.py")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
