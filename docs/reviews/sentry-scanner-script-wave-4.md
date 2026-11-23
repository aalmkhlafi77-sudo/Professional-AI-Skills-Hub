# Sentry skill-scanner: script-level static assessment (wave 4)

Date: 2026-11-23. Source: `getsentry/skills` at immutable commit `a582c51ee29d0f35e6ac321340796f77d43da733`.

## Files inspected directly
- `skills/skill-scanner/SKILL.md`
- `skills/skill-scanner/scripts/scan_skill.py` (675 lines)
- `skills/skill-scanner/references/prompt-injection-patterns.md`
- `skills/skill-scanner/references/dangerous-code-patterns.md`
- `skills/skill-scanner/references/permission-analysis.md`

The scanner declares Python >=3.9 and `pyyaml` in PEP 723 script metadata; SKILL.md prescribes `uv run scripts/scan_skill.py`, which can resolve/download dependencies unless explicitly controlled. **No third-party script executed or installed during this review.**

## Code-path assessment
- The inspected script uses `pathlib`, `re`, `json`, `base64`, `sys`, and `yaml.safe_load` to inspect skill content and emit JSON to stdout.
- No direct `requests`, `urllib`, `subprocess`, `os.system`, `eval` or `exec` invocation was identified in the inspected script's main scanning workflow. This is a limited static observation, **not** a proof of zero malicious behavior.
- Script recursively walks a supplied skill directory for structural checks, reads Markdown/script/package files and PNG bytes. Its scope is governed by the supplied path, and links/files outside that scope require explicit protection.
- `check_structural_attacks` calls `Path.is_relative_to`, which requires Python >=3.9 and is consistent with declared minimum.
- References contain attack strings as **detection examples**, not operational commands. Treat as data, not instructions.

## Security and reliability findings

1. **Execution boundary / dependency resolution — MEDIUM, unresolved.** Upstream SKILL.md grants `Read Grep Glob Bash` and instructs `uv run`. Do not run on a machine with credentials or unrestricted network; first pin and locally supply dependencies in an isolated environment.
2. **Symlink and target path boundary — MEDIUM, unresolved.** Scanner enumerates and reads user-supplied skill paths, and `Path.resolve` can follow links. A controlled root and explicit symlink rejection should precede any scan of untrusted input.
3. **Secret leakage in report output — MEDIUM, unresolved.** `check_secrets` says it masks evidence but uses `line.strip()[:200]` in findings. This can include the detected secret verbatim. **Do not publish raw scanner JSON or logs** until redaction is fixed and tested.
4. **False positives — LOW/expected.** Detection references intentionally contain injection, reverse-shell and secret-like examples. Review context before labeling malicious.
5. **Coverage limits — MEDIUM.** Scanner focuses on Markdown references and selected script extensions in immediate directories, while structural checks recurse. Nested scripts, binary payloads, nonstandard extensions and dependency manifests need independent audit.

## Admission status
- Canonical owner/immutable revision: PASS.
- Selected five-file content review: PASS (static; script workflow inspected).
- Full skill directory inventory and per-file licensing: PENDING.
- Dependency pinning and vulnerability assessment: PENDING.
- Symlink, redaction and offline negative tests: PENDING.
- Safe isolated runtime evaluation: PENDING.
- Named human reviewer, score >=90 and all mandatory gates: PENDING.
- **Decision: UNDER REVIEW — NOT APPROVED for execution or installation.**

## Next controlled tests
Use disposable, credential-free, network-restricted environment. Before executing upstream code, add a temporary test harness that redacts secret evidence and refuses symlink escapes. Test a synthetic fake key, nested scripts, symlink escape, invalid YAML, injected instruction, and clean sample; capture expected/actual findings. No production credentials or repositories.

This is a static security review, not a certification or finding of malicious intent.
