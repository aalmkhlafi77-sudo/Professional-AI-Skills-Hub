# External source readiness — prioritized intake (2026-11-23)

This is a **preparation and triage record**, not an admission or installation certificate. Evidence: `catalog/candidates.json`, `docs/reviews/official-wave-1.md`, `docs/reviews/alternatives-wave-1.md`, and `docs/ADMISSION_POLICY.md` on main.

## Priority A — review individual skills first

| Source / target | Pinned commit | Rationale | Known limits | Next evidence |
|---|---|---|---|---|
| greensock/gsap-skills: gsap-scrolltrigger, gsap-performance | aed9cfd3277740755f6bfc1155c7aa645403b760 | Directly relevant to cinematic React UI | MIT root reported; full per-file review and browser tests pending | Inventory every selected file, assess scroll/pin/mobile/reduced motion and test in isolated demo |
| getsentry/skills: skill-scanner | a582c51ee29d0f35e6ac321340796f77d43da733 | Useful independent security screening | Python scanner and uv workflow require script/dependency audit | Review scanner source line by line; offline negative fixtures and false positives |
| microsoft/playwright-cli: playwright-cli | c872a33cec77fa03c28fa7c6d1ad99d15d04ce42 | Official browser QA | Privileged browser, JS eval, cookies, uploads, alpha package reported | Complete capability inventory and isolated browser test with no credentials |
| MustBeSimo/web-design-studio: scroll-audit | 674f211abfeb9707d2424d553bb5b1af3613025f | Read-only scroll QA candidate | Scripts/examples elsewhere in repo; don't import wholesale | Inventory exact skill and references, verify MIT notices, run offline fixtures |

## Priority B — specialized or licensing/compatibility dependent

| Source | Pinned commit | Constraint / decision |
|---|---|---|
| vercel-labs/agent-skills | 5a37a6329fbad3666c3207392a6a7c0110e92efb | React guidance useful; per-file licensing and entire rule corpus pending |
| expo/skills | 88d9bd79f3fa8452a778fbac65bae162c0b32ce4 | Select mobile-specific skills only when mobile work resumes |
| supabase/agent-skills | c9be0e931b7930f7d02126d04774d904c381e7d7 | PostgreSQL only; not a MySQL skill |
| anthopics/skills (canonical: anthropics/skills) | e4bb5d960d87126ff3b3a8af1a104b7db67560ba | Per-skill licensing; frontend-design candidate, scripts require scrutiny |
| obra/superpowers | 22f0b463e7a5e579904dd6211a520321035526f7 | Avoid global using-superpowers dispatcher due to authority conflicts |
| vercel-labs/agent-browser | d2dfc782ccdd79d25a9b4f0acced9321789cecb8 | High-privilege CLI; compare with Microsoft before selecting |
| lackeyjb/playwright-skill | dd47a6a023e249eb1b36e9e943eab89d0900865d | Lower priority than official Microsoft alternative |
| openai/plugins | 981b02c0c44058b595f3b4180002c3ae3c806d40 | Plugin registry, not a single skill; only select narrowly scoped entries |

## Rejected as-is

- `zubair-trabzada/scroll-cinematic-claude` @ `5f3cc0e65e474dab1d80ee3fda1e847f3552f708`: unverified moving binary download and immediate execution in ffmpeg installer; no installation or bundling.

## Mandatory review gates and release policy

All external candidates above: **under_review**; no external admission score assigned. Pinned identity is recorded, but all-file inventories, licenses (where applicable), dependency vulnerability assessments, prompt-injection checks, negative tests and isolated runtime tests remain **PENDING**. Root license observation does not establish per-file redistribution permission.

Do not change `catalog/approved.json` or claim score >=90 until every mandatory gate in `docs/ADMISSION_POLICY.md` passes, with reproducible evidence and named human reviewer. Keep source code and installers outside the distribution until approval. Original instruction-only adapters already in the repo are **not** upstream installations.

## Next review batches

1. Static full-file audit of **selected GSAP skills** and **Sentry scanner**, including source/permissions/license and explicit negative cases.
2. Isolated browser QA evaluation of **Microsoft Playwright CLI** and **scroll-audit**, with no production credentials or writes.
3. Revisit React rule corpus and per-file licensing; admit only independently validated, practical individual skills.

Prepared using existing repository review evidence; no third-party commands executed and no new external safety claims made.
