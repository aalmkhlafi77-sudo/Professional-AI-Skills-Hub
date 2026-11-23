# GSAP wave 7 — licensing, plugin manifests and isolated arithmetic test

Date: 2026-11-23. Pinned upstream: `greensock/gsap-skills@aed9cfd3277740755f6bfc1155c7aa645403b760`.

## Newly inspected upstream files
- `LICENSE` — MIT, copyright 2026 GreenSock, full permission notice retrieved.
- `.claude-plugin/plugin.json` — `skills: ./skills/`, version 1.0.0.
- `.claude-plugin/marketplace.json` — local plugin source `./`, owner GreenSock.
- `.cursor-plugin/plugin.json` — MIT metadata, local `skills` directory and logo reference.
- `.cursor-plugin/marketplace.json` — local source `./`.
- `README.md` — installation guidance invokes `npx skills add`; **do not execute** unpinned CLI.
- `skills/llms.txt` and eight `SKILL.md` files were read in prior wave.
- Root `package.json` returned 404 at pinned revision; **absence of this path is not proof that no nested manifests exist**.

All above files were read through GitHub connector at the immutable commit. Remaining hidden files, assets, examples, nested manifests and any symlinks remain PENDING until complete tree inventory is obtained.

## Confirmed defect — horizontal-scroll example

Upstream `skills/gsap-scrolltrigger/SKILL.md`, line 235:

```js
xPercent: () => Max.max(0, window.innerWidth - scrollingEl.offsetWidth),
```

Two problems: `Max` is undefined in ordinary JavaScript; `xPercent` takes a percentage, whereas viewport/content width difference is measured in pixels. Correct approach for an element wider than viewport: `x: () => -Math.max(0, scrollingEl.scrollWidth - viewportWidth)` or percentage `xPercent: () => -100 * Math.max(0, scrollingEl.scrollWidth - viewportWidth) / scrollingEl.scrollWidth` (with zero-width guard). These are **mathematical alternatives**, not browser-verified GSAP integration fixes.

## Local isolated JavaScript arithmetic tests

Executed **only independent arithmetic**, not upstream code, using Node.js 22.16.0 in the working container; no network, packages, credentials or project writes.

| Viewport px | Content px | Upstream `Max.max` | Expected x px | Equivalent xPercent | Result |
|---:|---:|---|---:|---:|---|
| 1280 | 3000 | ReferenceError | -1720 | -57.333333% | PASS |
| 390 | 1100 | ReferenceError | -710 | -64.545455% | PASS |
| 1280 | 800 | ReferenceError | 0 | 0% | PASS |
| 320 | 320 | ReferenceError | 0 | 0% | PASS |

**4/4 arithmetic checks passed**, confirming the original example fails and the replacement expressions are dimensionally consistent for these cases. This does not verify pinning, ScrollTrigger refresh, animation performance, accessibility, browser compatibility or screenshot quality.

## Browser test blocker

Chromium executable is present, but a minimal headless `--dump-dom` invocation timed out in this container. GSAP, Playwright and Puppeteer npm packages are not installed. GitHub clone also fails DNS resolution. **No browser screenshot, GSAP runtime, responsive, reduced-motion, memory or animation test was completed.** Do not mark visual gates PASS.

## Mandatory gates and decision

| Gate | Status |
|---|---|
| Official upstream and immutable SHA | PASS |
| Root MIT license | PASS |
| File-by-file license and redistribution for all nested files | PENDING |
| Full tree, hooks, scripts and dependency inventory | PENDING |
| Prompt-injection/privileged side-effect audit across all files | PENDING |
| Dependency vulnerabilities and install chain | PENDING |
| Positive and negative isolated arithmetic test | PASS (narrow scope only) |
| GSAP runtime browser, desktop/mobile screenshots, accessibility | PENDING |
| Named human reviewer and >=90/100 score | PENDING |

**Decision: UNDER REVIEW; no external GSAP skill imported or approved.** Keep `catalog/approved.json` unchanged.

## Next unblock

Obtain immutable upstream tree via verified archive or GitHub tree API, audit all nested content and dependencies, then run pinned GSAP in a disposable browser with screenshots, reduced-motion, resize and cleanup tests. Preserve MIT notice if redistribution is approved. Never modify user production projects.
