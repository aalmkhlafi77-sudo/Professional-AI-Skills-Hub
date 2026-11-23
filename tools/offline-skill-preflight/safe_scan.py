#!/usr/bin/env python3
"""Independent offline, read-only skill preflight; not an upstream Sentry fork."""
import argparse
import json
import re
from pathlib import Path

PATTERNS = {
    "injection": re.compile(r"ignore\s+(all\s+)?previous\s+instructions|new\s+system\s+prompt\s*:", re.I),
    "secret": re.compile(r"ghp_[A-Za-z0-9]{36}|AKIA[A-Z0-9]{16}|-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----"),
    "remote_execution": re.compile(r"curl\s+[^\n|]+\|\s*(sh|bash)|wget\s+[^\n|]+\|\s*(sh|bash)", re.I),
}
MAX_FILE = 1024 * 1024
MAX_FILES = 200

def scan(root):
    root = Path(root).absolute()
    if root.is_symlink() or not root.is_dir():
        raise ValueError("target must be a real directory")
    entries = sorted(root.rglob("*"))
    if len(entries) > MAX_FILES:
        raise ValueError("too many files")
    findings = []
    for p in entries:
        rel = str(p.relative_to(root))
        if p.is_symlink():
            findings.append({"file": rel, "type": "symlink_rejected"})
            continue
        if not p.is_file():
            continue
        if p.stat().st_size > MAX_FILE:
            findings.append({"file": rel, "type": "oversized_file_skipped"})
            continue
        if p.suffix.lower() not in {".md", ".py", ".sh", ".js", ".ts", ".json", ".yaml", ".yml", ".toml"}:
            findings.append({"file": rel, "type": "unscanned_file_type"})
            continue
        try:
            data = p.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            findings.append({"file": rel, "type": "unreadable_file"})
            continue
        for lineno, line in enumerate(data.splitlines(), 1):
            for kind, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append({"file": rel, "line": lineno, "type": kind})
    if not (root / "SKILL.md").is_file():
        findings.append({"file": "SKILL.md", "type": "missing_entrypoint"})
    return {"status": "review_required" if findings else "no_pattern_matches", "findings": findings, "scanned_entries": len(entries), "note": "Pattern screening is not a security certification. No matched source text is returned."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir")
    args = parser.parse_args()
    try:
        print(json.dumps(scan(args.skill_dir), indent=2))
    except (ValueError, OSError) as exc:
        print(json.dumps({"error": str(exc)}))
        raise SystemExit(2)
