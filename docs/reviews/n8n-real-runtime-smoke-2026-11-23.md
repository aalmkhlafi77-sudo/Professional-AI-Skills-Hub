# n8n 2.2.0 real runtime — isolated smoke evidence (2026-11-23)

**Result:** PASS for two narrowly scoped real-runtime fixtures, on GitHub Actions run [45211751779](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45211751779).

## Observed execution

- Actual container image: `docker.n8n.io/n8nio/n8n:2.2.0` (tag pinned to version, **digest not yet pinned**).
- The CI runner downloaded the image, imported both disposable workflows into a temporary SQLite state, and executed them with n8n CLI `execute --id=...`.
- **Positive:** Manual Trigger → Set Fixture executed; runtime output contained `"executionStatus": "success"` and `"fixture": "offline-ok"`.
- **Negative:** Manual Trigger → HTTP Request to `http://example.com/` was run with Docker `--network none`. The run failed as expected, and the negative log contained HTTP/network failure evidence. Final CI output: `PASS: isolated real runtime positive and blocked-network fixtures`.
- Runtime container restrictions: `--network none`, `--cap-drop ALL`, `no-new-privileges`, read-only fixture mount, disposable local SQLite state, no real credentials or production endpoints, 100-second execution timeout. GitHub Actions still has network access to pull the image; only the **container** is network-disabled.

## Debugging evidence

Earlier runs failed before validating runtime behavior:
- [45210565293](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45210565293): n8n CLI requires `--id`; `execute --file` did not execute.
- [45211011008](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45211011008): fixture mount path pointed to wrong directory.
- [45211216765](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45211216765): import required `versionId`.
- [45211491248](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45211491248): positive node executed correctly, but success assertion looked for the wrong text; replaced with actual node JSON evidence.
- [45211751779](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45211751779): **PASS**.

## Scope limitations and remaining gates

This verifies **real n8n execution of a Set node and network blocking of one HTTP Request**, not the full imported skill bundles. It does **not** establish:
- Credential encryption, access controls, log redaction or OAuth safety.
- Actual retry/idempotency behavior with a mock database.
- Data Table, subworkflow, shell/file node side effects in test mode.
- Agent approvals, external MCP tool permissions or malicious input resistance.
- Image digest integrity or complete dependency vulnerability assessment.
- Production readiness, named reviewer, or score >=90.

**Admission decision:** All four imported n8n skills remain `under_review` and quarantined. This successful smoke test must not be misrepresented as full skill certification.
