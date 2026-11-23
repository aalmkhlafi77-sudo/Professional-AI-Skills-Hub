# Acceptance plan — all 21 quarantined skills

**Status:** Test specifications only. No imported skill was executed. No skill is production-approved. A passing catalog CI run proves integrity, not skill correctness.

## Required evidence for each skill
- Immutable upstream commit and byte-for-byte provenance; license review for every redistributed file.
- Read all references, scripts, hooks, dependency and network behavior. No hidden downloads, secret reads or automatic deployment.
- Run a success case and a deliberately failing case in a disposable project without credentials or production connectivity.
- Record commands, expected vs actual outputs, artifacts, version compatibility, failure recovery, rollback, reviewer and date.
- Visual tasks additionally require **inspected** desktop/mobile screenshots, keyboard/accessibility and reduced-motion tests.
- Only then score security 30, practical 25, compatibility 20, source/license 15, documentation 10; minimum 90 and all mandatory gates PASS.

## Distinct acceptance cases

| Source | Skill | Positive test | Negative / regression test |
|---|---|---|---|
| GreenSock | gsap-core | Animate isolated element without layout shift | Missing target and unmount cleanup |
| GreenSock | gsap-react | React StrictMode animation lifecycle | Double-mount memory leak / stale context |
| GreenSock | gsap-scrolltrigger | Scroll animation at desktop/mobile sizes | Resize, reverse scroll, pinned overflow |
| GreenSock | gsap-performance | Profile frame timing and layout work | Heavy paint/reflow regression |
| GreenSock | gsap-timeline | Reversible multi-step sequence | Rapid interruption and replay |
| Sentry | skill-scanner | Detect unsafe fixture instructions | Obfuscated exfiltration and false positives |
| Sentry | gha-security-review | Detect unpinned action and unsafe permissions | Malicious workflow expression injection |
| Sentry | find-bugs | Reproduce a real defect in disposable code | Clean fixture must not invent a defect |
| Sentry | code-review | Actionable diff-level review with line evidence | Harmless diff must not create noise |
| Sentry | security-review | Identify seeded auth/secret handling defect | Secure fixture and prompt-injection attempts |
| Microsoft | playwright-cli | Local navigation, screenshot and form test | Timeout, inaccessible control, test isolation |
| Web Design Studio | cinematic-scroll | Cinematic effect with reduced-motion alternative | Scroll lock, clipping and mobile jank |
| Web Design Studio | scroll-audit | Identify broken scroll/overflow | Clean responsive fixture; keyboard navigation |
| Expo | expo-animation | Smooth device animation with reduced motion | Unmount and low-end-device fallback |
| Expo | expo-design-system | Consistent native component rendering | Accessibility labels, dynamic type overflow |
| Expo | expo-native-ui | Native controls on supported platform | Unsupported-platform fallback |
| Expo | expo-data-fetching | Loading, retry and cache lifecycle | Offline, race conditions, cancelled request |
| Expo | expo-router | Nested navigation and deep links | Invalid route and back-stack restoration |
| Anthropic | frontend-design | Cohesive responsive page with screenshot evidence | Generic output, contrast and focus failures |
| Supabase | supabase-postgres-best-practices | Explain query plan on isolated PostgreSQL | Bad index advice and unsafe migration |
| Laravel | laravel-best-practices | Validate input, authorization and transaction in test Laravel app | Cross-user access, SQL injection and rollback failure |

## Critical project coverage gaps

### Plain PHP + MySQL (Hostinger)
The Laravel skill is **not applicable** to a plain PHP application. Require a separate skill or rigorously reviewed first-party guidance with: PDO prepared statements, strict input validation, output encoding, session cookie flags, CSRF tokens, password hashing, file upload MIME/size/storage boundaries, least-privilege MySQL grants, transactions, deadlock retries, atomic writes, idempotent order endpoints, schema migration rollback, secret handling and safe deployment. Test concurrent balance updates, duplicate request replay, failed image insert, cross-user access, backup restore and database rollback. Never run against live customer data.

### Local visual regression
Require a reproducible local Playwright fixture with pinned browser/version, baseline screenshots for mobile and desktop, explicit pixel-diff tolerance, font readiness, animations disabled or stabilized, deterministic data/time, keyboard focus and contrast checks, reduced-motion and RTL layouts, scroll pinning and responsive overflow. A screenshot file alone does not prove quality: require human visual inspection and documented differences.

### Financial transaction correctness
For ledger applications, test decimal minor units, balanced double-entry or documented accounting invariants, concurrent transfer locking, idempotency keys, partial failure rollback, immutable audit events where required, timezone boundaries, independent opening balances and reconciliation. These checks must be adapted to each product's actual accounting model.

## Prioritization
1. Complete full-file static security/license review and dependency inventory for all 21 skills.
2. Execute focused isolated positive/negative tests, starting with Sentry security review, Playwright CLI and GSAP.
3. Source or author and separately validate **plain PHP/MySQL** and **local visual regression** guidance; do not mislabel Laravel/PostgreSQL or cloud QA as substitutes.
4. Collect named human review, actual test artifacts and scorecards before moving any skill to `catalog/approved.json`.

No production activation or automatic installation is authorized by this document.
