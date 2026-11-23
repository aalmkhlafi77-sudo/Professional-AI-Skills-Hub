# ChatGPT / Codex installation matrix

Date: 2026-11-23. No automatic external installation has been performed.

| Skill/source | ChatGPT | Codex | Next action |
|---|---|---|---|
| Local skill-source-auditor | Available in this ChatGPT session (runtime skill) | Not verified | Validate and package Codex-compatible bundle; test |
| greensock/gsap-skills | Not installed by this workflow | Not installed | Audit individual GSAP skills, then package adapters |
| vercel-labs/agent-skills | Not installed by this workflow | Not installed | Audit React and web-design skill licenses and instructions |
| microsoft/playwright-cli | Not installed by this workflow | Not installed | Audit executable, browser privileges and dependencies |
| expo/skills | Not installed by this workflow | Not installed | Audit individual mobile skills |
| supabase/agent-skills | Not installed by this workflow | Not installed | PostgreSQL only; no MySQL claims |

## Distribution workflow

1. Select an individual upstream SKILL.md and exact pinned commit; never bulk-install a repository.
2. Audit complete selected skill tree and its dependency closure, scripts, hooks, references, assets and license.
3. Adapt frontmatter to `name` and `description`; retain original source attribution and required notices.
4. Add `agents/openai.yaml` for ChatGPT packaging and test Codex discovery separately; do not assume identical capabilities.
5. Package as a single-skill ZIP, run structural validation and isolated representative tests with no production secrets.
6. Record target-specific PASS/FAIL/PENDING and reviewer evidence. Approve only under `docs/ADMISSION_POLICY.md`.
7. Installation into a user's ChatGPT account or local Codex environment requires the supported account/client installation workflow. A GitHub commit is not an installation.

## Guardrails

No remote install script, network fetch, privileged execution, untrusted hook, credential access, deployment, or automatic merge. A missing runtime or authorization is PENDING, never PASS.
