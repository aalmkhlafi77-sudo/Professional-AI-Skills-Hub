# Official Skills Wave 1 — Static Intake Review

Date: 2026-11-23. Branch: `review/official-skills-wave-1`. **Review only, no execution, install, approval or merge.**

## Objective

Prioritize official source skills over similar community alternatives and admit only skills passing ALL gates in [admission policy](../ADMISSION_POLICY.md) and a documented score >=90/100.

## Evidence inventory

| Source | Immutable revision | License check | SKILL.md sampled | Status |
|---|---|---|---|---|
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760) | `aed9cfd32777` | MIT: repository LICENSE | Yes | UNDER REVIEW |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/5a37a6329fbad3666c3207392a6a7c0110e92efb) | `5a37a6329fba` | PENDING: no top-level LICENSE in 479-entry tree; some skill frontmatter claims MIT, redistribution must be verified. | Yes | UNDER REVIEW |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/tree/c872a33cec77fa03c28fa7c6d1ad99d15d04ce42) | `c872a33cec77` | Apache-2.0: repository LICENSE | Yes | UNDER REVIEW |
| [expo/skills](https://github.com/expo/skills/tree/88d9bd79f3fa8452a778fbac65bae162c0b32ce4) | `88d9bd79f3fa` | MIT: root LICENSE; skill-specific LICENSE available for expo-animation | Yes | UNDER REVIEW |
| [supabase/agent-skills](https://github.com/supabase/agent-skills/tree/c9be0e931b7930f7d02126d04774d904c381e7d7) | `c9be0e931b79` | MIT: repository LICENSE | Yes | UNDER REVIEW |

## Findings by source

### greensock/gsap-skills

Official 8 GSAP skills. Static sample inspected: gsap-scrolltrigger, gsap-performance. No scripts apparent in 66-file tree. Detailed cross-file instruction review and browser performance tests pending.

- Snapshot commit: `aed9cfd3277740755f6bfc1155c7aa645403b760`
- Licensing: MIT: repository LICENSE
- Static review: PARTIAL; additional files not exhaustively inspected.
- Source and initial skill discovery: PASS.
- Full license/redistribution: PENDING (check nested content and notices).
- All instruction/script/dependency and prompt-injection gates: PENDING.
- Isolated reproducible tests / security checks / visual or device checks: PENDING.
- Score: NOT ASSIGNED; evidence insufficient.
- Admission decision: **NOT APPROVED**.

### vercel-labs/agent-skills

9 SKILL.md found; react-best-practices (70 rules) and web-design-guidelines inspected. Bundled pinned command.md exists. Full rule corpus, licenses and any package scripts not yet fully audited.

- Snapshot commit: `5a37a6329fbad3666c3207392a6a7c0110e92efb`
- Licensing: PENDING: no top-level LICENSE in 479-entry tree; some skill frontmatter claims MIT, redistribution must be verified.
- Static review: PARTIAL; additional files not exhaustively inspected.
- Source and initial skill discovery: PASS.
- Full license/redistribution: PENDING (no root LICENSE).
- All instruction/script/dependency and prompt-injection gates: PENDING.
- Isolated reproducible tests / security checks / visual or device checks: PENDING.
- Score: NOT ASSIGNED; evidence insufficient.
- Admission decision: **NOT APPROVED**.

### microsoft/playwright-cli

Official playwright-cli skill includes browser navigation, storage and network interception. Package currently uses Playwright 1.66.0-alpha-2026-11-18; caution about alpha dependencies. No browser executed; privacy/permissions and isolation tests pending.

- Snapshot commit: `c872a33cec77fa03c28fa7c6d1ad99d15d04ce42`
- Licensing: Apache-2.0: repository LICENSE
- Static review: PARTIAL; additional files not exhaustively inspected.
- Source and initial skill discovery: PASS.
- Full license/redistribution: PENDING (check nested content and notices).
- All instruction/script/dependency and prompt-injection gates: PENDING.
- Isolated reproducible tests / security checks / visual or device checks: PENDING.
- Score: NOT ASSIGNED; evidence insufficient.
- Admission decision: **NOT APPROVED**.

### expo/skills

Multiple skills in plugins/expo including expo-animation. Some instructions prescribe implementation choices and tooling; audit nested scripts, privileges and dependencies before any usage. Real low-end mobile release verification pending.

- Snapshot commit: `88d9bd79f3fa8452a778fbac65bae162c0b32ce4`
- Licensing: MIT: root LICENSE; skill-specific LICENSE available for expo-animation
- Static review: PARTIAL; additional files not exhaustively inspected.
- Source and initial skill discovery: PASS.
- Full license/redistribution: PENDING (check nested content and notices).
- All instruction/script/dependency and prompt-injection gates: PENDING.
- Isolated reproducible tests / security checks / visual or device checks: PENDING.
- Score: NOT ASSIGNED; evidence insufficient.
- Admission decision: **NOT APPROVED**.

### supabase/agent-skills

2 SKILL.md files identified; Postgres best practices SKILL.md inspected. Suitable for PostgreSQL, not a MySQL guide. Full references, SQL migration and RLS security test evaluation pending.

- Snapshot commit: `c9be0e931b7930f7d02126d04774d904c381e7d7`
- Licensing: MIT: repository LICENSE
- Static review: PARTIAL; additional files not exhaustively inspected.
- Source and initial skill discovery: PASS.
- Full license/redistribution: PENDING (check nested content and notices).
- All instruction/script/dependency and prompt-injection gates: PENDING.
- Isolated reproducible tests / security checks / visual or device checks: PENDING.
- Score: NOT ASSIGNED; evidence insufficient.
- Admission decision: **NOT APPROVED**.


## Next inspection steps

1. Inspect every file of each selected skill and only the required companion references, including hidden manifests, scripts and hooks. Verify hashes and licenses.
2. Produce a permissions/side-effects inventory and conduct targeted threat analysis, including embedded instructions, network access, secret handling, writes and deletion.
3. In a disposable non-privileged environment without credentials, perform representative functional and negative-case tests, mobile/desktop visual checks as applicable.
4. Produce per-skill signed-off admission reports. Update `catalog/approved.json` **only** after all hard gates pass and score is >= 90.
5. Reassess community candidates and alternative sources, favoring official high-quality equivalents.

**This is a partial static triage, not a clean bill of security or quality certification.**
