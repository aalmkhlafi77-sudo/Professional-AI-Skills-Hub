# Upstream source and limitations

Source: https://github.com/microsoft/playwright-cli
Pinned commit: `c872a33cec77fa03c28fa7c6d1ad99d15d04ce42`
Reviewed sample: `skills/playwright-cli/SKILL.md`
Root license: Apache-2.0 (confirmed in repository)
The original skill permits privileged browser CLI commands, JavaScript evaluation, cookies, storage state, upload and network routing. Those capabilities are deliberately **not** included in this review-only adapter.
No upstream binaries, scripts or dependencies are bundled. Full upstream dependency/security audit and real-browser test are pending. The adapter is not a claim that Playwright CLI is installed.
