# Skill-level security triage — Wave 2

Date: 2026-11-23. Decision: **No external skill admitted.** Static review only; no third-party installation or execution.

## Scope and reproducible evidence

### GreenSock official GSAP skills

Canonical repository: https://github.com/greensock/gsap-skills
Pinned commit: `aed9cfd3277740755f6bfc1155c7aa645403b760`
Root license: MIT, `LICENSE` inspected. Recursive Git tree contains 66 paths. All eight `SKILL.md` entrypoints reviewed at this commit; no additional script files inside the eight skill directories.

| Skill entrypoint | File blob SHA | Static instruction inspection |
|---|---|---|
| gsap-core | `98639432f4112b664aa5e53cf5d8ea1a4697eff9` | Motion primitives, GSAP docs |
| gsap-frameworks | `3c2df8611b61d0c97abb8d32ed922ce8207424e5` | Lifecycle guidance |
| gsap-performance | `05792acf5b0ea7fd30042cdc5e91282e8e047898` | Render performance guidance |
| gsap-plugins | `bb5f7483038adf26a889c8b2b85e3ef2cf0141dc` | Contains npm install guidance — not executed |
| gsap-react | `e2e51805457943cd4982fe792b858c14fa2c3c8f` | npm install guidance, React integration |
| gsap-scrolltrigger | `6d8c09f2136c108595c9e0db859c4a39460e99cf` | ScrollTrigger examples and API references |
| gsap-timeline | `1fed372b0e5276b2a207d80bc23f81180a0dff55` | Animation sequencing guidance |
| gsap-utils | `367e405e027936ce6b5fb85ec996beb135715194` | GSAP utility descriptions |

Static scan: looked for instructions involving remote installers, shell privilege escalation, secret/environment access and runtime `eval/exec` patterns in the eight entrypoint texts; did not identify executable scripts packaged within those individual skill folders. An automated keyword review cannot prove absence of prompt injection or insecure instruction patterns. Official license and provenance are established, but tests on a rendered demo, dependency vulnerability checks, reduced-motion functionality and operator approval remain PENDING.

**Adoption priority:** `gsap-performance`, `gsap-scrolltrigger`, `gsap-react` and `gsap-timeline`. Do not install blindly; inspect target application's animation stack first.

### GetSentry skill-scanner

Canonical: https://github.com/getsentry/skills
Pinned commit: `a582c51ee29d0f35e6ac321340796f77d43da733`.
Individual skill: `skills/skill-scanner/`.
Root license: Apache-2.0, but inspect skill-specific notices before copying.
`SKILL.md` describes a Python script invoked through `uv` and requiring `pyyaml`. Scanner source `scripts/scan_skill.py` at blob `14aaa7b059c659ea5c2719fa266f19641dfd9d3d` was inspected for top-level imports and primitive process/network execution patterns. The occurrences of `curl`, `wget`, `exec`, and `subprocess` in sampled sections were **detection regexes**, not evidence the scanner executes them. No third-party code was executed. Full function-by-function dataflow and sandbox negative tests remain PENDING.

**Adoption priority:** High for security automation, subject to independent validation. Detector alerts require contextual review to avoid false positives.

### Other sources under review

- Vercel Web Design Guidelines: `SKILL.md` bundles a pinned rules reference; licensing for redistribution not yet verified. Keep PENDING.
- Microsoft Playwright CLI: browser automation and storage access require sandbox/permission boundary tests; alpha dependency snapshot noted. Keep PENDING.
- Expo and Supabase: environment-specific guidance; native mobile and PostgreSQL tests remain PENDING.

## Hard-gate matrix

| Gate | GSAP (8 skills) | Sentry scanner |
|---|---|---|
| Upstream identity + immutable commit | PASS | PASS |
| License and per-file redistribution | PASS for GSAP root/license; no copied code | PENDING for notices and copied components |
| Complete instruction + companion-file review | PASS for 8 GSAP entrypoints; companion tooling separate | PENDING |
| Prompt injection and operator-permission review | PENDING | PENDING |
| Dependency / install script audit | PENDING if GSAP runtime is installed | PENDING uv/pyyaml and Python functions |
| Credential, network and filesystem boundaries | PENDING runtime | PENDING |
| Vulnerability assessment | PENDING | PENDING |
| Isolated functional tests | PENDING | PENDING |
| Negative-case security tests | PENDING | PENDING |
| Compatibility with target projects | PENDING | PENDING |
| Human review | PENDING | PENDING |

No production-grade assurance is claimed. **Approved list remains empty.**

## Admission infrastructure improvement

The new `scripts/validate_catalog.py` enforces an exact 11-gate evidence matrix, a weighted score breakdown (30/25/20/15/10), verified 40-character commit SHA and review document path, and consistency between the pinned revision and report. It uses explicit errors (not `assert`), so Python optimized mode cannot silently disable checks. Tests include intentionally forged approvals and missing evidence paths.

The validator checks the **presence and self-consistency of evidence**, not its authenticity or the real-world quality of a test. A named reviewer and an actual human review are still required. A malicious committer with direct write access could forge catalog and documentation; protect main through branch protection and required checks.

## Next acceptance work

1. Run GSAP animation demo tests in a disposable local browser for both desktop and mobile, including scroll/reduced-motion/cleanup.
2. Complete Sentry scanner source review and run deterministic malicious/benign fixture tests without outbound network or sensitive files.
3. Review Vercel's licensing and choose individual skills for testing.
4. Only update `approved.json` after every gate has independent evidence and approval.
