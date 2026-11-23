# n8n admission stages 25–28 — evidence and decision (2026-11-23)

**Source:** https://github.com/n8n-io/skills at immutable commit `626f50fdf2934116eea2c5469339e03d2d524e83`. Four staged skills: `n8n-expressions-official`, `n8n-credentials-and-security-official`, `n8n-error-handling-official`, `n8n-subworkflows-official`. License: Apache-2.0; see `intake/n8n/LICENSE`. Original source file SHAs are tracked in `catalog/intake-provenance.json`.

## Stage 25 — credential handling

19 offline tests (shared with stages 26 and 27) include nested secret-key redaction, plaintext header detection, and a negative case. **Important:** redaction here is our own narrow Python fixture, not n8n's actual encryption or log-redaction implementation. No real credentials, OAuth token issuance, secret storage, key rotation, audit logs or database ciphertext were tested. **Runtime encryption gate: PENDING**.

## Stage 26 — retry and idempotency

The gate flags write-like retry operations as requiring external proof **even if a workflow claims an `idempotencyKey`**. A separate memory-only ledger fixture demonstrates duplicate suppression and missing-key rejection. This does not demonstrate a durable unique constraint, atomic transactions, concurrent workers, or n8n connector semantics. **Actual deduplication gate: PENDING**.

## Stage 27 — subworkflows and MCP

The gate blocks unapproved MCP exposure, subworkflow execution, Data Table writes, shell execution and unpinned HTTP in synthetic test fixtures. A synthetic boolean called `authenticated_approval` is a test-only marker, not proof of an authenticated human, payload-aware consent or access control. The gate does not enumerate every node or account permission. **Real authorization and side-effect gate: PENDING**.

## Stage 28 — admission review

Prior real n8n 2.2.0 runtime smoke: [CI run 45212032311](https://github.com/aalmkhlafi77-sudo/Professional-AI-Skills-Hub/actions/runs/45212032311), success for Manual Trigger → Set and blocked HTTP with Docker `--network none`. This does not certify the four imported skill bundles.

| Mandatory gate | Status | Evidence / reason |
|---|---|---|
| Canonical upstream and immutable commit | PASS | Pinned source and tracked Git blob SHA |
| Root license preserved | PASS | Apache-2.0 LICENSE staged unchanged |
| Complete imported-bundle file inventory | PASS | Catalog and provenance |
| All upstream hooks, manifests, scripts and dependency paths audited | PENDING | Upstream integration surfaces not fully security-cleared |
| Prompt injection and instruction override resilience | PENDING | Adversarial tests incomplete |
| No uncontrolled network or privileged execution in staged bundle | PASS | Only text/reference files; no plugins or hooks installed |
| No unrestricted secret access or destructive writes | PENDING | Real n8n privileges and runtime semantics not validated |
| Dependency vulnerabilities assessed | PENDING | Version-tagged runtime image not digest pinned; no comprehensive scan |
| Passing positive/negative sandbox tests | PASS (limited) | 19 synthetic tests and two real smoke fixtures |
| Real encryption, credential masking and log safety | PENDING | No runtime credential lifecycle tests |
| Real idempotency under concurrent retries | PENDING | No database-backed concurrency tests |
| Real subworkflow and MCP access boundaries | PENDING | No authenticated authorization or side-effect tests |
| Risks, limitations and rollback documented | PASS | This record and earlier review reports |
| Named reviewer and >=90 admission score | PENDING | No human sign-off; no defensible final score |

**Decision for all four skills: `under_review`. No production approval, no connection to user accounts, no runtime privileges, no installation of upstream hooks.** The four skills must remain in quarantine until every mandatory gate is PASS and a named reviewer signs off.

### Next evidence needed

1. Disposable n8n runtime with synthetic credentials: inspect encrypted database storage, redacted logs and key rotation behavior.
2. Disposable database and mock endpoint: prove atomic duplicate prevention with concurrent retries and failure injection.
3. Mock subworkflow, Data Table and MCP with scoped identities: verify side effects, negative authorization and payload-aware approval.
4. Complete upstream file/security/dependency review, runtime image digest pinning, then human review and final score.

**Rollback:** revert the test code and this report; existing quarantined skill files are unchanged.
