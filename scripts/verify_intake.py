#!/usr/bin/env python3
"""Verify quarantined third-party snapshots against exact upstream Git blob hashes.

Read-only, Python standard library; never imports or executes external skills.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "intake-provenance.json"
HEX = set("0123456789abcdef")


def main():
    manifest = json.loads(CATALOG.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or manifest.get("status") != "quarantined-unapproved":
        raise ValueError("Intake manifest must remain unapproved and schema version 1")
    expected = set()
    for record in manifest["files"]:
        path = record["path"]
        source = record["source"]
        pin = record["source_commit"]
        sha = record["git_blob_sha"]
        if not (path.startswith("intake/") and ".." not in Path(path).parts):
            raise ValueError("Unsafe intake path")
        if not (source and len(pin) == 40 and set(pin) <= HEX and len(sha) == 40 and set(sha) <= HEX):
            raise ValueError(f"Invalid provenance: {path}")
        if path in expected:
            raise ValueError(f"Duplicate file: {path}")
        expected.add(path)
        file = ROOT / path
        if not file.is_file() or file.is_symlink():
            raise ValueError(f"Missing or unsafe file: {path}")
        data = file.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob != sha:
            raise ValueError(f"Upstream Git blob mismatch at {path}: expected {sha}, got {blob}")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / "intake").rglob("*") if p.is_file() and p.name != "README.md"}
    if actual != expected:
        raise ValueError(f"Unexpected/missing intake paths: {sorted(actual ^ expected)}")
    print(f"PASS: {len(expected)} quarantined upstream files match pinned Git object checksums; none executed")


if __name__ == "__main__":
    main()
