# GSAP final acceptance check — 2026-11-23

**User's requested provisional score threshold: 80%.** This changes the requested numeric threshold for this decision, but does not supply missing security, functional, or visual evidence. The repository's `docs/ADMISSION_POLICY.md` still formally requires 90/100 and **all** mandatory gates PASS. No formal policy amendment was authorized or made.

## Scope and evidence

- Official source pinned at `greensock/gsap-skills@aed9cfd3277740755f6bfc1155c7aa645403b760`.
- Full 66-entry repository tree retrieved with `truncated:false`, 8 entrypoints read; 7 staged in `candidates/greensock-gsap/`.
- MIT attribution preserved; no scripts, hooks or dependency manifests in the staged seven skill folders.
- Example apps and external installation scripts are not staged or executed. Excluded defective `gsap-scrolltrigger`.
- **Final local isolated check:** Node v22.16.0, 5/5 arithmetic assertions PASS, including undefined `Max.max` negative case. This tests formula math only, **not** GSAP functionality or individual skill instructions.
- **Final Chromium check:** `timeout 12 chromium --headless --no-sandbox --disable-gpu --disable-dev-shm-usage --disable-background-networking --dump-dom file:///mnt/data/gsap-wave6-qa/horizontal-check.html` returned exit **124**, produced zero HTML output. Browser functional, mobile, visual, reduced-motion and accessibility gates remain PENDING.
- No external dependency resolution or vulnerability database verification performed. No remote npm install, secrets, production writes or third-party code execution.

## Per-skill final decision

| Candidate | Source/content static review | Browser/runtime | Mandatory gates | Final |
|---|---|---|---|---|
| gsap-core | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-timeline | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-plugins | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-utils | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-react | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-performance | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-frameworks | PASS | PENDING | PENDING | UNDER REVIEW |
| gsap-scrolltrigger | FAIL: broken example | PENDING | FAIL | EXCLUDED |

**Scoring:** No defensible overall 80/100 score can be assigned to any of the seven, because practical test results (25 points) and dependency/security gates are unverified. A 100% static-entrypoint review is **not** an 80% security approval. Scores remain **UNSCORED**, not zero-quality.

## Decision

**0 external skills approved or activated.** Existing first-party `skills/cinematic-gsap-review` remains usable. Preserve staged seven packages and `catalog/approved.json` unchanged. No further repeated testing is scheduled; completing actual browser tests and supply-chain verification in a functioning isolated environment is the precise unblock for future approval.
