# GSAP official eight-skill review — wave 6

Date: 2026-11-23. Immutable source: `greensock/gsap-skills@aed9cfd3277740755f6bfc1155c7aa645403b760`.
Canonical: https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760

## Scope and evidence

Read the complete contents of all eight `skills/<name>/SKILL.md` files through the GitHub connector at the pinned SHA. Also read `skills/llms.txt`. This is a **SKILL.md-level static review**, not a full 66-file inventory audit, dependency review, browser QA or admission certification. A direct clone in the isolated container failed because github.com DNS resolution was unavailable. No third-party code was executed or installed.

| Skill | Lines | Blob SHA | Static notes | Decision |
|---|---:|---|---|---|
| gsap-core | 255 | `98639432f4112b664aa5e53cf5d8ea1a4697eff9` | `gsap.matchMedia` and reduced-motion guidance present | UNDER REVIEW |
| gsap-timeline | 108 | `1fed372b0e5276b2a207d80bc23f81180a0dff55` | sequencing and kill guidance | UNDER REVIEW |
| gsap-scrolltrigger | 297 | `6d8c09f2136c108595c9e0db859c4a39460e99cf` | **Defective horizontal scrolling example**: `Max.max(...)` is not standard JavaScript; `xPercent` usage also needs validation against the intended pixel offset | UNDER REVIEW |
| gsap-plugins | 434 | `bb5f7483038adf26a889c8b2b85e3ef2cf0141dc` | installation guidance for public npm GSAP; licensing claims about plugin use require independent verification | UNDER REVIEW |
| gsap-utils | 285 | `367e405e027936ce6b5fb85ec996beb135715194` | utility API guidance | UNDER REVIEW |
| gsap-react | 136 | `e2e51805457943cd4982fe792b858c14fa2c3c8f` | `useGSAP`, `contextSafe`, unmount cleanup and SSR precautions | UNDER REVIEW |
| gsap-performance | 80 | `05792acf5b0ea7fd30042cdc5e91282e8e047898` | transform/opacity performance tips; real performance measurements absent | UNDER REVIEW |
| gsap-frameworks | 267 | `3c2df8611b61d0c97abb8d32ed922ce8207424e5` | Vue/Svelte lifecycle cleanup examples | UNDER REVIEW |

## Defect requiring correction before admission

In `gsap-scrolltrigger/SKILL.md` horizontal-scroll sample:

```js
xPercent: () => Max.max(0, window.innerWidth - scrollingEl.offsetWidth),
```

`Max` is not a standard JavaScript global (likely a typo for `Math`). Even replacing the name alone is insufficient: horizontal scroll distance and `xPercent` units must be validated in a browser. Do not auto-copy this example into approved templates. Verify against current GSAP docs and test narrow/mobile widths, reduced-motion, resize and cleanup.

## Mandatory admission gates

| Gate | Status | Evidence / reason |
|---|---|---|
| Canonical owner and immutable commit | PASS | official upstream and pinned SHA |
| File-by-file license and redistribution | PENDING | root MIT identified in earlier intake; nested assets/notices not fully verified |
| Full file inventory / scripts / hooks / manifests | PENDING | eight entrypoints + index reviewed; remaining repository files not exhaustively inventoried |
| Prompt injection / hidden operations | PENDING | no obvious direct install hooks in sampled instruction lines; full cross-file threat review absent |
| No uncontrolled downloads / privileged execution | PENDING | skill instructions mention npm packages; dependency and install workflow not tested |
| Secrets, destructive writes, autonomous actions | PENDING | complete permission inventory absent |
| Dependency vulnerability assessment | PENDING | no locked dependency audit |
| Isolated positive and negative tests | PENDING | browser unavailable; no upstream execution |
| Visual desktop/mobile, accessibility and reduced-motion | PENDING | documented guidance is not screenshot or runtime evidence |
| Risks, rollback and upgrades | PENDING | require test matrix and pinned candidate artifact |

Score: **NOT ASSIGNED** (insufficient evidence; do not manufacture >=90).
Named human reviewer: **PENDING**.
Decision: **UNDER REVIEW** for all eight; **zero external approvals**. Keep `catalog/approved.json` unchanged.

## Next executable steps

1. Acquire a verifiable immutable source snapshot with all files and hashes; inspect licenses, references, hidden files and package manifests.
2. Prepare an inert local test page using a vetted, pinned GSAP dependency in a disposable browser environment. No production project changes.
3. Reproduce and fix horizontal scroll example; check desktop/mobile, reduced-motion, resize, keyboard, memory cleanup and frame timing with screenshots/logs.
4. Run security and dependency checks offline where possible, then obtain a named human review and per-skill score.
5. Only after all gates PASS and >=90/100, import a specifically approved skill with attribution and separate merge.

This report documents confirmed findings and blocked gates, not a claim of security approval.
