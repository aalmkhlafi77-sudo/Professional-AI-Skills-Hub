# n8n official skills — capability-by-capability review (2026-11-23)

Source: https://github.com/n8n-io/skills at immutable commit `626f50fdf2934116eea2c5469339e03d2d524e83` (Apache-2.0 repository license observed). **Status: under_review. Not approved.**

## Scope and evidence

Git tree at the pinned commit contains 157 entries, **113 files**, of which 80 files live under `skills/`: 15 `SKILL.md` entrypoints and 65 other skill files. Outside `skills/` are 33 files including 10 shell hooks (SessionStart, pre/post tool), `opencode/plugin.ts`, an Antigravity builder, plugin manifests, lockfile, tests and README. These are **not** inert skill text and must never be imported implicitly.

Read the full 15 SKILL.md entrypoints and sampled high-risk supporting files: `hooks/hooks.json`, `hooks/session-start.sh`, `hooks/pre-tool-use/_emit.sh`, `hooks/post-tool-use/validate-workflow.sh`, `.codex-plugin/plugin.json`, `skills/n8n-agents-official/references/APPROVALS.md`, `skills/n8n-workflow-lifecycle-official/references/TESTING.md`, `package.json`, `LICENSE`. **The remaining supporting references, plugins, scripts and dependency lockfile are not yet fully reviewed.**

## Capability classification and risk

| Skill | Practical role | Risk / admission note | Priority |
|---|---|---|---|
| n8n-workflow-lifecycle-official | Plan → build → validate → test → publish | Publishing and testing have side effects; require explicit approval | High |
| n8n-subworkflows-official | Reusable subworkflows and invocation | Subworkflow execution may escape test pinning | High |
| n8n-error-handling-official | Retry, webhooks, error paths | Potential repeated writes; idempotency checks required | High |
| n8n-credentials-and-security-official | OAuth/API credential handling | Secrets, account scope and credential selection | High |
| n8n-node-configuration-official | Node setup and parameter validation | Wrong target service or credentials | High |
| n8n-expressions-official | Data mapping and expressions | Untrusted inputs and sensitive fields | High |
| n8n-loops-official | Pagination, batching, fanout | Unbounded execution, duplicate operations | High |
| n8n-debugging-official | Trace and diagnose broken workflows | Logs and traces may expose private data | High |
| n8n-agents-official | Agent lifecycle, tool approval and channels | Agent publishing, message sends, spending | High; restricted |
| n8n-ai-nodes-official | AI nodes and tool chains | External model requests, PII, tool side effects | High; restricted |
| n8n-extending-mcp-official | Expose workflows as MCP tools | **High privilege:** wrappers for missing REST operations, including deletes/credential creation | Hold pending deep review |
| n8n-code-nodes-official | Custom JavaScript/Python logic | Arbitrary execution in consuming n8n runtime | Restricted |
| n8n-data-tables-official | Persistent workflow data | Real writes, deletes, weak relational integrity | Restricted |
| n8n-binary-and-data-official | Files, attachments and images | Uploads, outbound URLs and data exfiltration | Restricted |
| using-n8n-skills-official | Meta routing protocol | Automatic session context and instruction priority claims | **Do not auto-activate** |

## Confirmed hazards, not hypothetical

1. **Testing can write real data.** The upstream `references/TESTING.md` says `test_workflow` auto-pins triggers, credentialed nodes and HTTP nodes, **but not Data Tables, Execute Command, file read/write, or invoked subworkflows**. Subworkflows may run credentialed nodes for real. A workflow validation success is not a safe execution guarantee.
2. **MCP extension can escalate tool surface.** `n8n-extending-mcp-official/SKILL.md` describes wrapping REST API operations not present in the native MCP, including folder/project mutation and credential creation, and notes that agent-created workflows default to `availableInMCP: true`. No such wrapper is authorized for this library.
3. **Approval UX may be insufficient.** `n8n-agents-official/references/APPROVALS.md` notes channel approvals may not show parameters, and shared-channel cards can be approved by anyone who can see them. For financial changes, deletes or sends, require an explicit authenticated approver with full payload details and a server-side permission check.
4. **Session hooks alter agent context.** `hooks/session-start.sh` injects the meta-skill every session, and pre-tool hooks write marker files. The Codex plugin manifest references `hooks/hooks.json`. Do not copy, register or execute these hooks as part of skill import.
5. **Untrusted instruction precedence.** The routing skill instructs agents to trust skill text over model knowledge and invokes tools automatically. Such upstream guidance is advisory and must not override user approvals, host policies or the admission gates.
6. **Credential handling is generally safety-positive** in the dedicated credentials skill: it warns against plain-text secrets and asks users to create credentials in the UI. This is not proof of security across all references or runtime integrations.

## Safe import boundary

- **Allowed for further review:** independently pinned `SKILL.md` and its needed `references/` under a quarantined path, with exact file hashes, copyright notices and license.
- **Excluded by default:** `hooks/`, `.codex-plugin/`, `.claude-plugin/`, `.antigravity-plugin/`, `opencode/`, installers, package scripts, MCP server configuration, OAuth setup and runtime dependencies.
- **Never auto-enable:** workflow publish, external MCP access, credential creation, deletions, production tests, autonomous agent channel activation, API key storage or cross-service writes.
- **Required before import:** review all references for each selected skill, confirm per-file redistribution rights and hash provenance, run a source-text instruction-injection review and negative-case fixtures. Import is **not** the same as approval.
- **Required before production approval:** meaningful isolated end-to-end tests, dependency audit where code is included, named reviewer, score >=90 and all mandatory gates PASS.

## Remaining mandatory gates

| Gate | Result |
|---|---|
| Canonical source and pinned commit | PASS |
| Full SKILL.md entrypoint inventory | PASS |
| Full supporting reference/script/hook inspection | PENDING |
| Per-file licensing | PENDING |
| Dependency vulnerabilities | PENDING |
| Instruction injection / override review | PENDING |
| No unauthorized writes or secret access | PENDING |
| Isolated positive and negative execution tests | PENDING |
| Compatibility and rollback verified | PENDING |
| Named reviewer and score >=90 | PENDING |

**Decision:** continue targeted static inspection and safe quarantined import of individually cleared skills only. Do not install the upstream plugin or connect a real n8n instance as part of this review.
