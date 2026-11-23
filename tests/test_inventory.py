import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_inventory", ROOT / "scripts/verify_inventory.py")
inventory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inventory)


class InventoryGateTests(unittest.TestCase):
    def test_live_inventory(self):
        inventory.verify(ROOT)

    def fixture(self, root):
        (root / "catalog").mkdir()
        (root / "intake/example/test").mkdir(parents=True)
        (root / "intake/example/LICENSE").write_text("MIT", encoding="utf-8")
        (root / "intake/example/test/SKILL.md").write_text("---\nname: test\ndescription: test\n---\n", encoding="utf-8")
        pin = "a" * 40
        src = {"schema_version": 1, "status": "quarantined-unapproved", "sources": [{
            "id": "example/source", "commit": pin, "prefix": "intake/example/",
            "license_file": "intake/example/LICENSE",
            "entries": [{"skill": "test", "path": "intake/example/test/SKILL.md"}]
        }]}
        files = {"schema_version": 1, "status": "quarantined-unapproved", "files": [
            {"source": "example/source", "source_commit": pin, "source_path": x,
             "path": "intake/example/" + x, "git_blob_sha": "b" * 40}
            for x in ("LICENSE", "test/SKILL.md")
        ]}
        return src, files

    def write(self, root, src, files):
        (root / "catalog/intake-sources.json").write_text(json.dumps(src), encoding="utf-8")
        (root / "catalog/intake-provenance.json").write_text(json.dumps(files), encoding="utf-8")

    def test_reject_source_pin_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src, files = self.fixture(root)
            files["files"][0]["source_commit"] = "c" * 40
            self.write(root, src, files)
            with self.assertRaisesRegex(ValueError, "pin/prefix mismatch"):
                inventory.verify(root)

    def test_reject_untracked_license(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src, files = self.fixture(root)
            files["files"] = files["files"][1:]
            self.write(root, src, files)
            with self.assertRaisesRegex(ValueError, "Untracked license"):
                inventory.verify(root)

    def test_reject_duplicate_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src, files = self.fixture(root)
            src["sources"][0]["entries"].append(dict(src["sources"][0]["entries"][0]))
            self.write(root, src, files)
            with self.assertRaisesRegex(ValueError, "Duplicate, unsafe or untracked skill"):
                inventory.verify(root)

    def test_reject_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src, files = self.fixture(root)
            (root / "intake/example/test/SKILL.md").write_text("no metadata", encoding="utf-8")
            self.write(root, src, files)
            with self.assertRaisesRegex(ValueError, "Missing skill frontmatter"):
                inventory.verify(root)


if __name__ == "__main__":
    unittest.main()
