#!/usr/bin/env python3
"""Cross-check intake inventory and provenance without executing imported content."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT):
    sources = json.loads((root / "catalog/intake-sources.json").read_text(encoding="utf-8"))
    provenance = json.loads((root / "catalog/intake-provenance.json").read_text(encoding="utf-8"))
    if any(x.get("schema_version") != 1 or x.get("status") != "quarantined-unapproved" for x in (sources, provenance)):
        raise ValueError("Both intake catalogs must remain quarantined and schema v1")
    records = provenance["files"]
    paths = {r["path"] for r in records}
    if len(paths) != len(records):
        raise ValueError("Duplicate provenance path")
    ids, skill_paths = set(), set()
    for source in sources["sources"]:
        ident, pin, prefix = source["id"], source["commit"], source["prefix"]
        if ident in ids:
            raise ValueError("Duplicate source ID")
        ids.add(ident)
        if not prefix.startswith("intake/") or ".." in Path(prefix).parts:
            raise ValueError("Unsafe source prefix")
        related = [r for r in records if r["source"] == ident]
        if not related:
            raise ValueError(f"No provenance files for {ident}")
        for r in related:
            if r["source_commit"] != pin or not r["path"].startswith(prefix) or not r["source_path"]:
                raise ValueError(f"Source pin/prefix mismatch: {r['path']}")
        license_file = source.get("license_file")
        if license_file and license_file not in paths:
            raise ValueError(f"Untracked license: {ident}")
        for entry in source["entries"]:
            skill = entry["path"]
            if skill in skill_paths or skill not in paths or not skill.startswith(prefix) or not skill.endswith("/SKILL.md"):
                raise ValueError(f"Duplicate, unsafe or untracked skill: {skill}")
            skill_paths.add(skill)
            content = (root / skill).read_text(encoding="utf-8")
            if not content.startswith("---\n") or "\n---\n" not in content[4:]:
                raise ValueError(f"Missing skill frontmatter: {skill}")
            frontmatter = content.split("\n---\n", 1)[0]
            if "name:" not in frontmatter or "description:" not in frontmatter:
                raise ValueError(f"Missing skill metadata: {skill}")
    if {r["source"] for r in records} != ids:
        raise ValueError("Uncataloged provenance source")
    print(f"PASS: {len(ids)} sources, {len(skill_paths)} skills, {len(paths)} files cross-checked; no external code executed")


if __name__ == "__main__":
    verify()
