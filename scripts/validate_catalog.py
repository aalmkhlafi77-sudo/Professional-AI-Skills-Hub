#!/usr/bin/env python3
"""Read-only structural validator; never executes third-party skills."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate():
    candidates = json.loads((ROOT / "catalog/candidates.json").read_text(encoding="utf8"))["candidates"]
    approved = json.loads((ROOT / "catalog/approved.json").read_text(encoding="utf8"))["approved"]
    seen = set()
    for item in candidates:
        assert item["id"] not in seen, "duplicate candidate"
        seen.add(item["id"])
        assert item["status"] in {"candidate", "under_review", "rejected", "retired"}
        assert item["url"].startswith("https://github.com/")
        assert item["score"] is None or 0 <= item["score"] <= 100
    approved_seen = set()
    for item in approved:
        assert item["id"] not in approved_seen, "duplicate approved"
        approved_seen.add(item["id"])
        assert item["score"] >= 90
        assert item["license_verified"] is True
        assert item["security_review"] == "passed"
        assert item["sandbox_test"] == "passed"
        assert isinstance(item.get("commit_sha"), str) and len(item["commit_sha"]) == 40
        assert item.get("reviewer") and item.get("evidence_path")
        assert item.get("mandatory_gates_passed") is True
    for path in (ROOT / "skills").glob("*/SKILL.md"):
        data = path.read_text(encoding="utf8")
        assert data.startswith("---\n") and "name:" in data and "description:" in data
    print(f"PASS: {len(candidates)} candidates, {len(approved)} external approvals; local skill structures checked")

if __name__ == "__main__":
    validate()
