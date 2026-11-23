# Visual QA candidate gate review — 2026-11-23

Scope: identify a non-overlapping visual regression/accessibility QA skill without weakening `docs/ADMISSION_POLICY.md`. **No candidate imported or activated.** Static source inspection only.

## Candidate A: browser-use/browser-use — `skills/qa`

- Canonical: https://github.com/browser-use/browser-use/tree/753d629d76eb2b670f4cf467f3355bbe750f6845/skills/qa
- Source commit: `753d629d76eb2b670f4cf467f3355bbe750f6845`; root MIT license.
- Inventory: `skills/qa/SKILL.md`, `references/browser-use-v2.md`, `references/methodology.md`; root `LICENSE`. The entrypoint requests Bash/Read/Task.
- Benefit: browser-driven QA verdicts, screenshots and flow evaluation; more than the current Playwright CLI automation skill.
- **Hard gate FAIL — uncontrolled installation / network / credentials:** entrypoint explicitly instructs an agent to install CLI via `curl ... | sh` and `uv tool install browser-use`, and obtain a Browser Use API key, potentially self-signing up, then use a third-party cloud browser. This conflicts with no uncontrolled downloads and no unrestricted secrets/remote operations. The entrypoint also explicitly forbids local browser fallback.
- Dependencies/remote execution: browser-use CLI, uv/pipx, cloud browser, API key; the remote task references were not exhaustively audited.
- Outcome: **rejected for intake in present form**, not a security assertion about the upstream product. A locally sandboxed, consent-based rewrite would constitute a distinct new skill needing its own review.
- Gates: source/commit PASS; root license PASS (file-by-file permissions PENDING); complete nested review PENDING; prompt-injection PENDING; remote installation **FAIL**; secrets/remote access **FAIL**; dependency assessment PENDING; sandbox pass/fail tests PENDING; screenshots/accessibility/reduced motion PENDING; rollback documentation PENDING.
- Weighted score: **not assigned** because hard gates fail; no production approval.

## Candidate B: vercel-labs/agent-skills — `skills/web-design-guidelines`

- Canonical: https://github.com/vercel-labs/agent-skills/tree/5a37a6329fbad3666c3207392a6a7c0110e92efb/skills/web-design-guidelines
- Source commit: `5a37a6329fbad3666c3207392a6a7c0110e92efb`.
- Inventory: `SKILL.md` and `references/command.md`. Entrypoint explicitly instructs reading bundled local rules and not fetching them at runtime. Update instructions mention network commands, but are not part of normal review execution.
- Benefit: **static** UI/accessibility/design rule auditing with file:line findings; complementary to Playwright browser execution and GSAP scroll audit, **not** a screenshot-diff or full visual regression system.
- **Hard gate PENDING — redistribution:** the GitHub repository metadata did not report an SPDX license and the inspected tree had no LICENSE-named file. Upstream licensing/redistribution permission must be positively verified; do not infer permission.
- Gates: source/commit PASS; license **PENDING**; full nested review PENDING; prompt injection PENDING; no uncontrolled runtime download PASS for entrypoint; secrets/network audit PENDING; dependency vulnerabilities PENDING; sandbox tests PENDING; visual screenshots PENDING; rollback PENDING.
- Outcome: **under_review, not imported**, pending verifiable license and the other admission gates.
- Weighted score: **not assigned** while essential evidence is missing.

## Decision and next research

Do not inflate the skill count or silently weaken security gates. Prioritize a vendor-neutral, locally runnable visual regression skill with pinned Playwright screenshot baselines, desktop/mobile viewport checks, accessibility and reduced-motion assertions, no credential capture or cloud dependency. Separately continue searching for secure **plain PHP + MySQL** skills; the existing Laravel skill is framework-specific and Supabase is PostgreSQL-specific.

No runtime tests or upstream commands were executed. No production files changed.
