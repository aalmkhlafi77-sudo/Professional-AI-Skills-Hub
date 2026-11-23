# Automation sources — initial security intake (2026-11-23)

**Decision:** under_review; no imported automation skills, no plugin installation, no live MCP connections, no credentials, no execution.

## Candidate inventory, pinned commits

| Canonical source | Immutable commit | Role | License observation | Decision |
|---|---|---|---|---|
| [n8n-io/skills](https://github.com/n8n-io/skills) | `626f50fdf2934116eea2c5469339e03d2d524e83` | Actual agent skill bundles | Repository Apache-2.0 | **under_review**, first priority |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | `2337aff0213d28db41d3e3daf48cee19b3d0bd82` | MCP browser server, not a skill | Apache-2.0 | candidate; assess as integration, not copy as skill |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | `29e8275ba8367640a800e31e261d1adc127cbac0` | App connector/workflow engine, not a skill | GitHub license NOASSERTION | candidate; component-by-component licensing needed |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | `6c4e4a29cd08eef454db6980d74da6afc8939d24` | Agent SDK, not a skill | MIT | candidate |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | `c6335a4255dc1d8abc25a7677f9c072c7ab27b9c` | Stateful agent framework, not a skill | MIT | candidate |
| [temporalio/sdk-typescript](https://github.com/temporalio/sdk-typescript) | `f5107ac96256c217cccf98cff278175bfa35b21e` | Durable workflow SDK, not a skill | MIT | candidate |

GitHub repository-level license metadata is **not** a substitute for per-file licensing review.

## n8n first-pass findings

- Official repository at the pinned commit contains **15 SKILL.md entrypoints**, not 14 total: **14 capability skills plus 1 routing meta-skill**.
- 67 paths under skill reference directories, plus plugin manifests, shell hooks, an OpenCode TypeScript plugin, package.json, tests and build tooling. Full file-by-file review remains open.
- README requires a separately provisioned n8n instance with instance-level MCP enabled; minimum n8n 2.2.0. No n8n instance is connected or configured by this review.
- The plugin supplies SessionStart, PreToolUse and PostToolUse hooks. The SessionStart hook injects the routing skill into every session and writes cache/session state. The pre-tool hook writes marker files. These hooks must **not** be imported or activated automatically.
- The workflow lifecycle skill instructs users to validate, verify connections and test before publishing; it explicitly warns that tests may execute side effects. The credentials skill directs users to store secrets in n8n credential storage, not plain-text nodes.
- The routing meta-skill includes strong instruction-priority language (`Trust the skills ... over recollection`) and automatic skill invocation. Treat as untrusted upstream instructions, subordinate to user approvals and repository policy.
- The published install instructions invoke marketplace installation, external MCP OAuth and hooks. **No installer, remote connection, hook or third-party command was executed.**
- n8n guidance is platform-specific; it is not a general replacement for local browser automation or arbitrary app connectors.

### Mandatory gates

| Gate | Status | Evidence / outstanding work |
|---|---|---|
| Canonical owner and pinned commit | PASS | Official n8n owner; immutable commit above |
| Per-file licensing and redistribution | PENDING | Root Apache-2.0 observed; nested files not individually cleared |
| Full scripts/hooks/manifests/dependency audit | PENDING | Hook behaviors sampled; 157 tree entries require complete review |
| Prompt-injection and instruction-override audit | PENDING | Routing skill contains assertive instructions; all skill text must be assessed |
| Remote installation, privileges and network | PENDING | Installation and OAuth surfaces identified; full code-path review pending |
| Secret access and destructive writes | PENDING | Credential policy positive; actual MCP tool scopes and side effects untested |
| Dependency vulnerability assessment | PENDING | package.json seen; lockfiles/dependencies not audited |
| Isolated practical positive/negative tests | PENDING | No sandbox runtime or n8n instance used |
| Risk, rollback, upgrades | PENDING | No activation; rollback will remove staged files/hooks if imported |
| Named reviewer and >=90 score | PENDING | No production approval or score assigned |

**No approval or numerical quality score is justified yet.**

## Recommended safe next intake

1. Audit the 15 SKILL.md files and all referenced documents, scripts, hooks, plugin configurations, license files and package manifests at the pinned commit.
2. Prefer copying only individually audited documentation-only skill bundles to a quarantined namespace; exclude hooks, auto-installers and remote connection setup by default. Preserve original license and exact blob provenance.
3. Run isolated negative tests for credential leakage, unauthorized publish, unapproved side effects, duplicate execution, malicious web content and MCP permission escalation; test representative workflow creation with mocked endpoints.
4. Separately assess Playwright MCP and application connector engines as **integration technologies**. Write dedicated first-party skills only if an actual skill gap remains.
5. Require a named human review, complete gate evidence and >=90 score before adding any entry to `catalog/approved.json`.

**This is a source-intake checkpoint, not a completed security audit.**
