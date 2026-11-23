#!/usr/bin/env python3
"""Fail-closed catalog integrity checks. Does NOT execute third-party skills."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA40 = re.compile(r"[0-9a-f]{40}\Z")
IDENT = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
STATES = {"candidate", "under_review", "rejected", "retired"}
GATES = {
    "source_provenance", "license", "complete_file_review",
    "prompt_injection", "scripts_and_dependencies", "permissions_and_network",
    "vulnerability_assessment", "sandbox_functional_tests",
    "negative_security_tests", "compatibility", "human_review"
}
SCORE_WEIGHTS = {
    "security": 30, "practical": 25, "compatibility": 20,
    "source_license": 15, "documentation": 10
}


def require(value, message):
    if not value:
        raise ValueError(message)


def valid_sha(value):
    return isinstance(value, str) and SHA40.fullmatch(value) is not None


def load_catalog(path, key):
    data = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict), f"{path}: expected object")
    require(data.get("schema_version") == 1, f"{path}: invalid schema version")
    rows = data.get(key)
    require(isinstance(rows, list), f"{path}: {key} must be a list")
    return rows


def safe_evidence_path(value):
    if not isinstance(value, str) or not value.startswith("docs/reviews/"):
        return False
    p = Path(value)
    return not p.is_absolute() and ".." not in p.parts and p.suffix == ".md" and (ROOT / p).is_file()


def validate():
    candidates = load_catalog(ROOT / "catalog/candidates.json", "candidates")
    approved = load_catalog(ROOT / "catalog/approved.json", "approved")
    candidate_ids = set()
    for entry in candidates:
        require(isinstance(entry, dict), "candidate must be object")
        ident = entry.get("id")
        require(isinstance(ident, str) and IDENT.fullmatch(ident), "invalid candidate id")
        require(ident not in candidate_ids, "duplicate candidate")
        candidate_ids.add(ident)
        require(entry.get("url") == f"https://github.com/{ident}", f"{ident}: canonical URL mismatch")
        require(entry.get("status") in STATES, f"{ident}: unexpected status")
        if entry.get("commit_sha") is not None:
            require(valid_sha(entry["commit_sha"]), f"{ident}: invalid pinned commit")
        require(entry.get("score") is None, f"{ident}: partial scores must not masquerade as approvals")
        require(entry.get("security_review") in ("pending", "failed"), f"{ident}: unsupported security gate status")
        require(entry.get("sandbox_test") == "pending", f"{ident}: candidates cannot claim test pass")

    approved_ids = set()
    for entry in approved:
        require(isinstance(entry, dict), "approved entry must be object")
        ident = entry.get("id")
        require(isinstance(ident, str) and IDENT.fullmatch(ident), "invalid approved id")
        require(ident not in approved_ids and ident not in candidate_ids, f"{ident}: duplicate or conflicting approval")
        approved_ids.add(ident)
        require(entry.get("url") == f"https://github.com/{ident}", f"{ident}: invalid canonical URL")
        require(valid_sha(entry.get("commit_sha")), f"{ident}: no immutable source revision")
        require(entry.get("license_verified") is True, f"{ident}: license not verified")
        require(entry.get("security_review") == "passed", f"{ident}: security review missing")
        require(entry.get("sandbox_test") == "passed", f"{ident}: isolated test missing")
        require(entry.get("mandatory_gates_passed") is True, f"{ident}: gates not passed")
        gate_results = entry.get("gates")
        require(isinstance(gate_results, dict) and set(gate_results) == GATES, f"{ident}: incomplete gate matrix")
        require(all(v == "passed" for v in gate_results.values()), f"{ident}: unresolved gate")
        breakdown = entry.get("score_breakdown")
        require(isinstance(breakdown, dict) and set(breakdown) == set(SCORE_WEIGHTS), f"{ident}: invalid score breakdown")
        require(all(type(breakdown[k]) is int and 0 <= breakdown[k] <= max_points for k, max_points in SCORE_WEIGHTS.items()), f"{ident}: invalid score values")
        require(type(entry.get("score")) is int and entry["score"] == sum(breakdown.values()) and entry["score"] >= 90, f"{ident}: score below policy")
        require(isinstance(entry.get("reviewer"), str) and entry["reviewer"].strip(), f"{ident}: reviewer missing")
        require(safe_evidence_path(entry.get("evidence_path")), f"{ident}: evidence file missing")
        evidence = (ROOT / entry["evidence_path"]).read_text(encoding="utf-8")
        require(ident in evidence and entry["commit_sha"] in evidence, f"{ident}: evidence source/pin mismatch")

    for skill in (ROOT / "skills").glob("*/SKILL.md"):
        data = skill.read_text(encoding="utf-8")
        require(data.startswith("---\n"), f"{skill}: missing YAML header")
        header = data.split("\n---\n", 1)[0]
        require(f"name: {skill.parent.name}" in header and "description:" in header, f"{skill}: invalid skill metadata")
    print(f"PASS: {len(candidates)} candidate sources, {len(approved)} external approvals; gates enforced")


if __name__ == "__main__":
    validate()
