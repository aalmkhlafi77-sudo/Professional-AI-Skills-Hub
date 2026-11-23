# Alternative-source comparison and security triage

Date: 2026-11-23. **Static inspection only; no upstream code executed.**
Repository tree snapshots are recorded by commit SHA in `catalog/candidates.json`. Scores remain unassigned because runtime evidence and full all-file reviews have not been completed.

## Main findings

| Source | Source evidence | Admission state |
|---|---|---|
| [getsentry/skills](https://github.com/getsentry/skills) | Apache-2.0. Includes `skills/skill-scanner`, `security-review`, `gha-security-review`. Scanner has deterministic Python script but invokes `uv` in the documented workflow; review script and dependency chain before execution. | UNDER REVIEW: strong potential for security specialization |
| [MustBeSimo/web-design-studio](https://github.com/MustBeSimo/web-design-studio) | MIT, 3 useful skills: `cinematic-scroll`, `scroll-audit`, `launch-page-strategy`. The `scroll-audit` instruction explicitly requires authorized target and avoids credentials. Repo includes many scripts/examples; only chosen skill and references should be considered, not wholesale. | UNDER REVIEW |
| [obra/superpowers](https://github.com/obra/superpowers) | MIT. Includes 15 skill entrypoints and installation hooks. `using-superpowers` demands invocation before *any* response and asserts process priority. Conflicts with our user-controlled approval and least-privilege routing when unmodified. | UNDER REVIEW: do not install global dispatch skill; evaluate individual skills separately |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Apache-2.0. Powerful browser CLI and skill bundles; full implementation has >800 tree entries, subprocess/network/browser permissions. | UNDER REVIEW: high access scope |
| [anthropics/skills](https://github.com/anthropics/skills) | Per-skill licensing. `frontend-design` references a separate `LICENSE.txt`, not a uniform root MIT/Apache license. Many demos and bundled scripts. | UNDER REVIEW: evaluate skills separately |
| [openai/plugins](https://github.com/openai/plugins) | Official plugin registry, includes thousands of files and multiple integrations and MCP tools. It is *not* a single safe-to-install skill. | UNDER REVIEW: source of narrowly selected plugin skills only |
| [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) | MIT. Community browser automation skill; official Microsoft `playwright-cli` is higher-provenance candidate for general browser testing. | UNDER REVIEW: compare coverage, do not install both by default |
| [zubair-trabzada/scroll-cinematic-claude](https://github.com/zubair-trabzada/scroll-cinematic-claude) | Root license not identified; `scripts/ensure-ffmpeg.sh` downloads static binary from third-party public hosts and immediately executes it without a pinned digest or signature verification. Workflow also depends on external image/video generation service. | **REJECT AS-IS** pending redesign of installer and explicit license/permission verification |

## Security analysis detail

### Critical acceptance blocker: unverified remote binaries

The `scroll-cinematic-claude/scripts/ensure-ffmpeg.sh` fallback downloads a binary ZIP/TAR from a moving latest-release endpoint, changes its executable bit and runs `ffmpeg -version` on it immediately. No cryptographic hash/signature verification or strict pinned version exists in the script reviewed. This violates the current admission policy's rule barring uncontrolled remote downloads. This is **a confirmed policy failure**, not evidence of malicious intent or compromise.

### Process authority and instruction injection

`obra/superpowers/skills/using-superpowers/SKILL.md` contains forceful instructions to invoke skills across every conversation. This is expected function of that tool's orchestration methodology but it must **not** become an authority above the operator's explicit approval and the current host's governing rules. It remains outside approved scope.

### Strong alternative: Sentry skill-scanner

`getsentry/skills/skills/skill-scanner/SKILL.md` documents a Python-based scanner for prompt injection, excess permissions, malicious scripts and supply chain risks. It is a **candidate** addition to our own `skill-source-auditor`; scanner pattern alerts need human review and the scanner script itself needs its own full review. Do not use a scanner's zero findings as proof of complete safety.

### Best available browser-source preference

Microsoft `playwright-cli` has stronger maintainer provenance for Playwright testing. Compare to community `lackeyjb/playwright-skill` and the broader `vercel-labs/agent-browser` for actual test ergonomics. None is approved or installed.

## Next steps / pending gates

- Review complete file inventories for each **selected individual skill**, including references, scripts, manifests and installers.
- Reconfirm licenses at immutable commit, including Anthropic subfolder notices and any Vercel content lacking a root LICENSE.
- Run controlled, isolated tests without real secrets or write-enabled production credentials.
- Test adverse paths: offline operation, reduced motion, untrusted page prompts, path traversal, upload and network boundaries.
- Publish per-skill evidence under `docs/reviews/`; only after ALL gates PASS and score >=90 may an entry enter `catalog/approved.json`.

No downstream library, third-party script or MCP action was executed.
