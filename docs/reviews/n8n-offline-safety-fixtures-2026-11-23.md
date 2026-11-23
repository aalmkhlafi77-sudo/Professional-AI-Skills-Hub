# n8n isolated offline safety fixtures — 2026-11-23

**Scope:** supplementary static/synthetic preflight only. No real n8n instance, SDK runtime, MCP server, credentials, browser or external network. No real workflow execution, publishing or production modifications.

## Test suite

`tests/test_n8n_offline_safety.py` provides **13 standard-library-only tests** running in the existing `check.yml` CI suite. Positive cases: pure transform, HTTP with synthetic pinned data, write with a synthetic idempotency marker, and explicitly approved synthetic subworkflow. Negative cases: Data Table writes, subworkflow execution escaping test pinning, shell command, unpinned HTTP, retrying a write without an idempotency marker, plaintext token-pattern example, MCP exposure, duplicate node names and malformed input.

`integration/n8n_offline_preflight.py` is **our own isolated policy fixture**, not an upstream n8n API validator. It does not run upstream code. Its checks are deliberately narrow, and it must not be used to authorize a real workflow. In particular, `approved=True` is a mock input, not authenticated user approval; `idempotencyKey` is a synthetic marker, not proof that an n8n connector honors deduplication; and the secret scanner recognizes only example patterns. It does not fully understand n8n's node schemas, credentials, execution modes or all side-effecting node types.

## Security gate status

| Gate | Status |
|---|---|
| Isolated fixtures with no real credentials or production writes | PASS after CI |
| Representative positive/negative offline policy tests | PASS after CI |
| Real n8n execution, retry semantics and actual deduplication | PENDING |
| Real n8n credential storage, masking and logs | PENDING |
| Real n8n subworkflow and test-mode side effects | PENDING |
| MCP authorization and scope enforcement | PENDING |
| Adversarial prompt-injection, complete source/dependency audit | PENDING |
| Human review and >=90 production score | PENDING |

**No skill is approved for production based on these tests.** Next gate requires a disposable n8n runtime and mock endpoints, with the ability to prove no real network/credential use and to inspect behavior under failures. Until then, retain all n8n skills in `intake/`.
