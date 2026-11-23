import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CatalogTests(unittest.TestCase):
    def test_validator(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate_catalog.py")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_no_unverified_approved(self):
        data = json.loads((ROOT / "catalog/approved.json").read_text())
        self.assertEqual(data["approved"], [])

    def test_all_candidates_unapproved(self):
        data = json.loads((ROOT / "catalog/candidates.json").read_text())
        self.assertTrue(all(item["status"] == "candidate" for item in data["candidates"]))

if __name__ == "__main__":
    unittest.main()
