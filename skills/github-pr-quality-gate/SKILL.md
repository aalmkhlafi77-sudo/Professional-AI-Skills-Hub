---
name: github-pr-quality-gate
description: Review GitHub pull requests for scope, build and test evidence, security regressions, changed files, conflicts and merge readiness. Use before deciding whether to merge a feature branch; do not merge automatically without explicit user approval.
---

# GitHub PR Quality Gate

1. Identify base/head branches, intended scope, diff and affected runtime or data contracts.
2. Check CI status, changed files, dependency changes, security-sensitive paths and rollback readiness using available evidence.
3. Distinguish completed checks from missing or unverified checks; never claim tests passed without logs.
4. Report blockers, risks and precise recommendation: ready, conditional or not ready.
5. Only merge when the user explicitly authorizes that PR or clearly scoped batch.

This is an original instruction-only skill. It includes no scripts, executables, dependencies or network installation steps.
