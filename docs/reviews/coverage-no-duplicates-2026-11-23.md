# Skills coverage and non-duplication roadmap — 2026-11-23

## Status and admission boundary

- Existing `main`: **11** imported, unapproved skills from **5** upstream repositories, **59** pinned source files.
- This branch adds **4 distinct skills**, **9** additional pinned files, and **1** new upstream repository.
- After this branch: **15 distinct** imported, unapproved skills, **6** upstream repositories, **68** pinned files.
- All source snapshots are quarantined under `intake/`. **Zero production approvals**. Source fidelity and CI checks are not sufficient for admission.
- Every proposal below is a **discovery target**, not a verified or approved import.

## Coverage matrix

| Capability | Existing in main | Added on this branch | Next unique capability / non-overlap |
|---|---|---|---|
| Animation and cinematic UI | `gsap-core`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-performance`, `cinematic-scroll` | — | Only a real-time 3D-specific skill if it demonstrates a separate build/asset pipeline; reject generic animation restatements |
| Web design | `cinematic-scroll` | Anthropic `frontend-design` | Accessibility validation with measurable WCAG evidence, not another generic styling guide |
| Scroll UX and QA | `scroll-audit`, `playwright-cli` | — | Visual regression / screenshot-diff workflow if it produces verifiable artifacts beyond basic browser automation |
| Native mobile | `expo-animation` | Expo `expo-design-system` | Mobile navigation, data/offline sync, and real-device test skills if independently useful |
| Security and CI | `skill-scanner`, `gha-security-review` | — | Dependency/supply-chain review and backend authorization testing, not another generic scanner |
| Code quality | — | Sentry `find-bugs` and `code-review` | Domain-specific PHP/MySQL correctness review or migration testing; avoid a third general code reviewer |
| Databases | — | — | PostgreSQL indexing, query planning, RLS policy verification; MySQL transaction and migration correctness |
| Backend | — | — | PHP secure API patterns and Node.js API integration testing; validate applicability to target stack |
| Deploy and operations | — | — | Hostinger deployment/rollback and MySQL persistence validation, only with explicit credential and write boundaries |

## Overlap decisions

1. **`frontend-design` vs `cinematic-scroll`: retain both as complementary**, not duplicates. The first focuses on overall frontend design quality; the second on scroll-led cinematic experiences. Admission review must confirm distinct deliverables.
2. **`expo-design-system` vs `expo-animation`: retain both**. Native design system consistency vs interaction and animation engineering.
3. **`find-bugs` vs `code-review`: retain provisionally**. The first seeks defects in code; the second reviews change quality. If later evaluation shows indistinguishable outputs, keep the stronger skill only.
4. **`scroll-audit` vs `playwright-cli`: complementary**. Experience diagnosis vs general browser control; neither replaces a visual-regression methodology.
5. **Do not import** additional generic GSAP, frontend styling, or code-review skills without a demonstrated missing function and measurable improvement.
6. **No auto-approval:** all hard gates must be PASS, evidence-backed >=90/100, named human review, appropriate licenses, and relevant isolated practical tests.

## Next-source priorities (evaluate before importing)

| Priority | Candidate upstream | Unique value sought | Gate / rejection criterion |
|---|---|---|---|
| P1 | `supabase/agent-skills` | Postgres schema, query performance and row-level security | Confirm exact scope, upstream license, security, and non-overlap |
| P1 | `expo/skills` | Native app routing, architecture and data fetching | Only choose skills distinct from existing animation/design coverage |
| P1 | `anthropics/skills` | Web application testing or accessibility workflows | Reject if duplicating `playwright-cli` without stronger validation |
| P2 | `getsentry/skills` | Focused security model and backend threat analysis | No duplication with `skill-scanner` or `gha-security-review` |
| P2 | New upstream search | PHP/MySQL migration and secure deployment | Demand credible maintainer, permissive file-level license, repeatable examples, no remote install scripts |

## Process

Discover source → compare unique deliverables → pin immutable commit → inspect license and dependencies → import complete required files into quarantine → verify blob hashes and CI → merge safe intake updates under user's standing authorization. **Promoting to approved skills is a separate higher bar.**
