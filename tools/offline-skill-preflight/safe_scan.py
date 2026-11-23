#!/usr/bin/env python3
"""Independent offline, read-only skill preflight; not an upstream Sentry fork."""
import argparse
import json
import re
from pathlib import Path

PATTERNS = {
    "injection": re.compile(r"ignore\s+(all\s+)?previous\s+instructions|new\s+system\s+prompt\s*:", re.I),
    "secret": re.compile(r"ghp_[A-Za-z0-9]{36}|AKIA[A-Z0-9]{16}|-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----"),
    "dangerous_execution": re.compile(r"\b(?:eval|exec)\s*\(|subprocess\.(?:run|Popen)\s*\(|os\.(?:system|popen)\s*\(", re.I),
    "config_modification": re.compile(r"(?:CLAUDE\.md|MEMORY\.md|\.mcp\.json|\.git/hooks|settings\.json).{0,100}(?:write|append|chmod)|(?:write_text|open\().{0,100}(?:CLAUDE\.md|MEMORY\.md|\.mcp\.json)", re.I),
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
    for index, p in enumerate(entries):
        # Avoid echoing untrusted filenames that may themselves contain credentials.
        rel = f"entry_{index}"
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
    if not (root / "SKILL.md").is_file() or (root / "SKILL.md").is_symlink():
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
