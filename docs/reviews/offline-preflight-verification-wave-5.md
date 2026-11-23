# Offline preflight verification — 2026-11-23

Scope: independent first-party Python preflight only, **not** execution of the upstream Sentry scanner. No external dependencies installed, no production systems modified.

## Local reproducible test evidence

Executed in the working container with Python standard library:

```bash
cd /mnt/data/preflight-qa
python -m unittest -v test_safe_scan
```

Result: **12 tests run, 12 PASS** (0.012s). Original 7: clean, synthetic fake GitHub token redaction, instruction override, missing entrypoint, nested script, curl pipe bash, symlink escape. Additional 5: secret-bearing filename redaction, symlinked SKILL.md rejection, subprocess invocation, unsupported binary type, oversized file.

Source was reconstructed from the GitHub main scanner and enhanced in the local QA harness. The equivalent changes and regression tests were then committed to the PR branch; GitHub-hosted CI has **not** been observed. The command above refers to the local working directory and is not a CI artifact.

## Existing original skills — smoke screening

Ran local scanner against 11 available skill directories in `/mnt/data/skills-release`. Seven returned `no_pattern_matches`; four returned `review_required` due to a leftover `skill.zip` in their **local source directories** (unsupported archive file type), not a confirmed malicious finding. The scanner intentionally flags opaque archives for manual review. This is not a full admission audit.

## Residual risks / acceptance gates

- Pattern matching has limited coverage, including obfuscation and complex dynamic execution.
- Directory traversal is bounded by entry count and file size, but the script is not an OS-level sandbox; run on untrusted inputs in a container without secrets or network.
- The source tree itself is not a substitute for reviewing packaged archives, dependency trees, hooks, scripts and all nested file types.
- Filename redaction removes filenames from reports; reviewers may need a separate, access-controlled mapping.
- `catalog/approved.json` remains unchanged. External skills and the Sentry scanner remain UNDER REVIEW.
- Final production-grade acceptance requires independent review and reproducible CI evidence.

## Decision

**PASS**: 12 synthetic local regression tests for the independent scanner.
**PENDING**: CI execution, broad malicious fixture corpus, isolated OS-level security tests, named reviewer, full upstream skill admission.
