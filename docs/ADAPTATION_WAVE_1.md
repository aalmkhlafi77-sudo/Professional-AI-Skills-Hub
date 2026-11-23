# External skill adaptation — wave 1

## Scope and order

1. **GSAP ScrollTrigger and performance** — highest fit for cinematic UI. Preserve animation semantics; require reduced-motion and desktop/mobile verification. Official source: greensock/gsap-skills at `aed9cfd3277740755f6bfc1155c7aa645403b760`.
2. **React best practices / web design guidelines** — inspect full rules and per-file license before redistribution. Official source: vercel-labs/agent-skills at `5a37a6329fbad3666c3207392a6a7c0110e92efb`.
3. **Playwright browser testing** — browser access is a privileged capability; prohibit production logins, saved browser profiles, external browsing and unreviewed install scripts in sandbox. Official source: microsoft/playwright-cli at `c872a33cec77fa03c28fa7c6d1ad99d15d04ce42`.

## Adaptation acceptance checklist

- [ ] Exact selected skill and complete file inventory
- [ ] Original license and attribution checked file-by-file
- [ ] Security analysis including prompt injection, scripts, hooks, network, credentials and dependencies
- [ ] ChatGPT manifest, single-skill ZIP and validation
- [ ] Codex SKILL.md and isolated discovery test
- [ ] Representative positive and negative tests, visual checks where relevant
- [ ] >=90/100 and every mandatory security gate PASS
- [ ] Named human reviewer approval

All boxes are initially unchecked. This document is an actionable work queue, **not** a claim of completed security review, packaging or installation.
