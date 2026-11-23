# Current skill coverage vs. next non-duplicate acquisitions (2026-11-23)

## Verified repository snapshot

- **17 unique skill entrypoints**, **6 upstream repositories**, **100 source files with pinned provenance**.
- Imported source skills are in `intake/`, **not approved for execution**.
- The inventory had duplicate records for `find-bugs`, `code-review`, `expo-design-system`, and `frontend-design`. This change removes duplicate **catalog records only**, not any skill files.
- The repository changed while an earlier branch was under review. This report reflects the **newer main branch**, not the older 15-skill snapshot.

## Existing vs. planned, by distinct deliverable

| Domain | Already imported | Complementary skill to evaluate next | Do not add |
|---|---|---|---|
| Web UI and cinematic motion | `frontend-design`, `cinematic-scroll`, `gsap-core`, `gsap-react`, `gsap-scrolltrigger`, `gsap-performance`, `gsap-timeline` | Accessibility audit with WCAG evidence; real-time 3D scene engineering with concrete performance checks | Another generic UI-design or GSAP tutorial |
| Scroll and browser QA | `scroll-audit`, `playwright-cli` | Deterministic screenshot visual-regression review and mobile viewport artifacts | Another browser-driving wrapper without additional evidence |
| Mobile | `expo-animation`, `expo-design-system`, `expo-native-ui` | Navigation architecture, offline persistence and real-device testing | Another animation/design-system restatement |
| Security | `skill-scanner`, `gha-security-review`, `security-review` | Backend authorization / database row-access tests and dependency supply-chain verification | Generic security review duplicating existing coverage |
| Code review | `find-bugs`, `code-review` | Stack-specific PHP/MySQL correctness and schema migration safety | A third general code reviewer |
| Data and persistence | — | Postgres performance/indexing and RLS; MySQL transactions, migrations and persistence | Vendor-only marketing guidance or untested SQL recipes |
| Backend and operations | — | Secure PHP API, Node.js backend testing, Hostinger deployment/rollback | Privileged installers or broad deployment automation without sandbox and approval |

## Candidate sources for targeted evaluation

1. `supabase/agent-skills` — evaluate `supabase-postgres-best-practices` for measurable Postgres query/index and RLS coverage; check licensing and version first.
2. `expo/skills` — evaluate a routing/architecture or data-fetching skill; select only one distinct capability per evaluation.
3. `anthropics/skills` — evaluate `webapp-testing` **only** if it materially improves visual regression or test evidence beyond existing Playwright.
4. Additional vetted maintainers — look for PHP/MySQL migration and production rollback workflows; reject sources with missing licenses or opaque remote-install scripts.

## Gatekeeping rules

- Compare task triggers, input/output, dependencies and test artifacts before accepting a second skill in the same category.
- A new skill must cover a distinct function or deliver demonstrably better evidence; otherwise reject it.
- Pin source commits, preserve per-file licenses, verify Git blobs and run only relevant checks.
- `intake` is quarantined. Promotion requires every security gate PASS, score >=90/100, practical evidence and human approval.
