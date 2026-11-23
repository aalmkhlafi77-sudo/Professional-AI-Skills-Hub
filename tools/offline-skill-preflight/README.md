# Offline skill preflight (independent tool)

This is **not** the upstream Sentry scanner and is not an approved replacement for full source review. It uses only Python standard library and performs read-only pattern checks.

Run: `python tools/offline-skill-preflight/safe_scan.py path/to/skill`

- Does not output matched source text or credential values.
- Rejects symlink entries and does not open their targets.
- Checks nested text/script files; flags unsupported formats and oversized files for manual review.
- No dependency installation, network calls or shell execution.
- A clean result means **no supported pattern matched**, not that the skill is safe to install.
- For untrusted directories, run in an OS-level sandbox with no credentials, no network, and read-only mounts. This script does not itself enforce OS isolation.

Seven synthetic unit tests passed in the local working container on 2026-11-23 (clean, fake secret redaction, injection, symlink, missing SKILL.md, remote execution, nested script). The published source should be independently retested in CI before it is used as a release gate.

Original Sentry source remains UNDER REVIEW; `catalog/approved.json` unchanged.
