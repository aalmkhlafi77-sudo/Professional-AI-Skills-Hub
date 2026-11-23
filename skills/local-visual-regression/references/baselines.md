# Deterministic baseline protocol

1. Record exact Playwright package and browser revisions, OS, fonts, locale, timezone, color scheme, device scale factor and viewport.
2. Use a local static fixture or isolated test server; seed deterministic data and mock nondeterministic network endpoints.
3. Wait for `document.fonts.ready`, loaded images and meaningful app readiness, not arbitrary long sleeps.
4. Freeze clock where the application uses time; disable or deterministically seek animations and transitions for static baselines. For GSAP, ensure final intended scroll state before capture.
5. Capture explicit desktop (1440×900) and mobile (390×844) viewport screenshots, plus at least one intermediate responsive width. Include RTL and reduced-motion when supported.
6. Assert no horizontal overflow with documentElement.scrollWidth <= viewport width, allowing documented tolerance only for deliberate offscreen animation.
7. Capture focus-visible states and check keyboard reachability; use dedicated accessibility audits for semantics and contrast.
8. Store approved screenshots in version control only when privacy-safe. Capture failure diffs as CI artifacts with limited retention.
9. Compare with a documented per-project tolerance. Start with strict matching, investigate any deviations and never increase tolerance to conceal defects.
10. Never auto-update baseline snapshots in CI. Human reviewer approves every intentional visual change and records why.
