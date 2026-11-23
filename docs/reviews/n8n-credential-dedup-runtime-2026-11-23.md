# n8n credential / retry / authorization verification — 2026-11-23

## Isolation and source
- Upstream skill bundles pinned to `n8n-io/skills@626f50fdf2934116eea2c5469339e03d2d524e83` and remain quarantined.
- Runtime test uses `docker.n8n.io/n8nio/n8n:2.2.0` (version tag, **not digest pinned**). Network is disabled inside container; runner needs network to pull image.
- Credential test uses a clearly fake sentinel and a disposable n8n SQLite database. It checks `credentials_entity.data` is nonempty, does not contain the plaintext sentinel or header name, and that the CLI import log does not contain the sentinel. It **does not prove cryptographic strength, secure key storage, key rotation, full log redaction, or access controls**.
- Atomic retry test uses a separate disposable SQLite database, eight concurrent processes, a unique operation key, and a rollback case. It **does not exercise n8n connector retries, multiple n8n workers, webhook duplicates, or a real downstream service**.
- MCP and subworkflow authorization have only prior offline synthetic policy tests; there is **no real identity-scoped n8n MCP test** in this PR. They remain pending.

## Gates and decision

| Gate | Status |
|---|---|
| Isolated n8n credential import and plaintext-at-rest/log sentinel check | PASS (limited): [run 45216783144](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45216783144) |
| SQLite concurrent unique-key dedup and rollback | PASS (SQLite only): [catalog tests](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45216782779) |
| n8n credential encryption algorithm, rotation and real log masking | PENDING |
| Actual n8n retry dedup with concurrent workers | PENDING |
| n8n subworkflow, Data Table and MCP scoped identity tests | PENDING |
| Full source/dependency audit, prompt-injection tests and named reviewer | PENDING |

**Admission:** all four n8n skills remain `under_review`. Passing these targeted tests must not be treated as production approval. No production data, secrets or existing sites are accessed.
