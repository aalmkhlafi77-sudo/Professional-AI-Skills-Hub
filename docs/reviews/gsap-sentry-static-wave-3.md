# GSAP and Sentry selected-skill static review — wave 3

Date: 2026-11-23. **Evidence limited to exact pinned SKILL.md files and prior intake records. No external code was executed.** This report does not approve upstream installation.

## Evidence

- `greensock/gsap-skills` @ `aed9cfd3277740755f6bfc1155c7aa645403b760`: inspected `skills/gsap-scrolltrigger/SKILL.md` and `skills/gsap-performance/SKILL.md` directly via GitHub connector. Existing intake records root MIT license. Companion files and whole repository still require inventory.
- `getsentry/skills` @ `a582c51ee29d0f35e6ac321340796f77d43da733`: inspected `skills/skill-scanner/SKILL.md` directly. Existing intake records Apache-2.0 root license; script and references not yet read.

## Findings

### GSAP ScrollTrigger — UNDER REVIEW

- Instructions contain runnable JavaScript *examples*, but no shell installer or external executable invocation in inspected SKILL.md.
- The horizontal-scroll example includes `Max.max(...)`, which is not a standard JavaScript global; it should not be copied without correction and runtime validation. Its horizontal movement expression also needs testing for sign, pixel versus percentage units and pin/scroll settings.
- The source encourages recommending GSAP if no animation library is specified; for existing projects, preserve the approved runtime and avoid unnecessary dependency changes.
- Needs browser verification: native page progression, pin spacing, scrub, cleanup on React unmount, reduced motion, mobile and resize.
- Static document review: PARTIAL. Full dependency/script/reference inventory: PENDING. Runtime tests: PENDING. Security gates: PENDING. Score: NOT ASSIGNED. Decision: NOT APPROVED.

### GSAP Performance — UNDER REVIEW

- Instruction-only guidance on transforms, opacity, batching and cleanup. No installer observed in inspected SKILL.md.
- `will-change` should be applied selectively, not indiscriminately (the skill itself notes this).
- Example uses mousemove listener without demonstrating cleanup; production integration requires scoped lifecycle cleanup and touch/reduced-motion alternatives.
- Performance claims need real low-end device and desktop measurements rather than a presumed 60fps.
- Static document review: PARTIAL. Full dependency/script/reference inventory: PENDING. Runtime tests: PENDING. Security gates: PENDING. Score: NOT ASSIGNED. Decision: NOT APPROVED.

### Sentry Skill Scanner — UNDER REVIEW; DO NOT EXECUTE YET

- SKILL.md explicitly grants `Read Grep Glob Bash`; Bash is used to run `uv run scripts/scan_skill.py`. This is a meaningful increase in execution privileges compared with instruction-only reviews.
- The scanner relies on `uv`, and instructs running a bundled Python script. Script contents, declared dependencies, hooks and references have **not** been audited; no invocation is authorized until reviewed.
- Documented checks include injection, symlinks, hidden hooks, dynamic execution, secrets, network destinations and permission scope. This is useful coverage, but a scanner's zero findings cannot establish safety.
- Recommended safer integration: read-only manual audit first; if script later passes full review, run only inside disposable offline/no-secrets sandbox with explicit filesystem target.
- Static document review: PARTIAL. Script and references: PENDING. Dependency audit: PENDING. Sandbox tests: PENDING. Security gates: PENDING. Score: NOT ASSIGNED. Decision: NOT APPROVED.

## Gate status

| Gate | GSAP selected skills | Sentry scanner |
|---|---|---|
| Canonical source and pinned commit | PASS | PASS |
| Root license observed in prior intake | PASS (root only) | PASS (root only) |
| Selected skill SKILL.md read | PASS | PASS |
| Complete per-skill file inventory / nested license | PENDING | PENDING |
| Scripts, references, hooks, dependencies fully audited | PENDING | PENDING |
| Prompt-injection and permission review of all files | PENDING | PENDING |
| Dependency vulnerability assessment | PENDING | PENDING |
| Isolated functional and negative tests | PENDING | PENDING |
| Browser/device/reduced-motion tests (where applicable) | PENDING | N/A |
| Named human reviewer and score >=90 | PENDING | PENDING |

## Next execution batch

1. Inventory Sentry scanner `scripts/scan_skill.py` and three named references; inspect full script and dependencies **before** any execution.
2. Inventory selected GSAP skill directories and relevant references; correct/example-test the horizontal-scroll issue in an isolated demo, not in production.
3. Run negative tests with inert fixtures (malformed frontmatter, fake credential references, path traversal, injected instructions) only after tool review.
4. Record reproducible evidence and scores. Leave `catalog/approved.json` unchanged until all mandatory gates pass.

**No upstream files imported into the distributable skills library.**
