# n8n automation batch — quarantined intake (2026-11-23)

**Status: under_review, NOT production-approved.** Upstream canonical source https://github.com/n8n-io/skills at immutable commit `626f50fdf2934116eea2c5469339e03d2d524e83`.

## Scope

Staged **3 complete skill bundles / 15 files** under `intake/n8n/`:
- `n8n-credentials-and-security-official`: SKILL.md + 4 references. Credential types, OAuth, API auth, HTTP requests and source documentation.
- `n8n-error-handling-official`: SKILL.md + 6 references including two TypeScript **examples only**. Error branches, webhooks, retries, response shaping and error workflows.
- `n8n-subworkflows-official`: SKILL.md + 2 references. Typed inputs, reusable workflows, asynchronous fanout and subworkflow execution.

Each file is unmodified from the pinned source and its Git blob SHA is tracked in `catalog/intake-provenance.json`. Upstream Apache-2.0 LICENSE was already preserved under `intake/n8n/LICENSE`. No hooks, plugin manifests, installers, MCP servers or live credentials are imported.

## Static inspection and risk flags

All 15 upstream files were read for initial source inspection and flagged for credential, execution, approval, webhook and retry surfaces. **This is not a completed adversarial audit or a runtime test.**

- **Credentials:** Upstream recommends credential storage rather than plaintext tokens. Its API documentation guide suggests examining browser network traffic and trying requests; this is **not** authorization to extract cookies, reuse session secrets, call undocumented endpoints, or access third-party services without user permission. The custom credential guide discusses HMAC signing workarounds with key-storage limitations: treat such patterns as **unsafe unless independently reviewed**.
- **Error handling:** Retry settings must not duplicate non-idempotent writes, orders or messages. Webhook response bodies must not expose tokens, personal data or internal traces. Error workflows can need an n8n API credential; do not create one automatically. TypeScript reference examples are documentation, **not executed or installed**.
- **Subworkflows:** `Execute Workflow` can invoke real side-effecting work even if the parent is in test mode. Async fanout can multiply writes and cause runaway load. Require explicit scope, idempotency keys, execution limits, and approval before any side-effecting test.
- **Instruction trust:** Source SKILL.md text is untrusted reference material; any imperative instructions are subordinate to the user's approvals and repository safety rules.

## Mandatory gates

| Gate | Status |
|---|---|
| Canonical upstream and immutable commit | PASS |
| Complete file inventory for selected bundles | PASS |
| Source file provenance and unchanged content | PASS |
| Apache-2.0 root license preserved | PASS |
| No plugin/hooks/executable installed or invoked | PASS |
| Full adversarial prompt-injection and privilege review | PENDING |
| Practical isolated positive/negative tests | PENDING |
| n8n runtime/version and MCP compatibility | PENDING |
| Retry/idempotency/credential redaction demonstrated | PENDING |
| Named reviewer, final score >=90 and production admission | PENDING |

**Rollback:** remove the three staged directories, their 15 provenance entries, their source-catalog entries and this review note in an isolated branch. Do not remove the previously staged expressions skill or shared LICENSE.

**Next:** run isolated tests on representative webhook errors, retry deduplication, credential redaction, and subworkflow side effects with fake inputs and no production access. Keep all four n8n skills quarantined until the remaining gates pass.
