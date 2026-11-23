# GSAP intake closure — final decision (2026-11-23)

## Final outcome

**The GSAP external-source intake is CLOSED for this revision.** No further review rounds are scheduled for `greensock/gsap-skills@aed9cfd3277740755f6bfc1155c7aa645403b760`.

- **Usable now:** repository's existing first-party `skills/cinematic-gsap-review/SKILL.md`. It is an instruction-only review workflow for React cinematic interfaces and requires no GSAP runtime install.
- **Staged, not activated:** seven pinned official GSAP instruction-only packages in `candidates/greensock-gsap/`, with MIT attribution. These were intentionally not installed under active `skills/`.
- **Excluded:** upstream `gsap-scrolltrigger` due to broken `Max.max` and mixed pixel/percentage example; upstream demo applications due to independent code defects and unverified dependencies.
- **External approvals:** zero. `catalog/approved.json` remains unchanged, as required by `docs/ADMISSION_POLICY.md`.
- **No production project was modified; no third-party npm install, external code execution or deployment occurred.**

## Evidence already obtained

- Official upstream tree at immutable SHA: 66 entries, `truncated:false`; eight instruction-only skill directories.
- Root MIT license and plugin manifests reviewed.
- All eight `SKILL.md` entrypoints reviewed.
- Four arithmetic regression cases documented; these do **not** constitute GSAP browser testing.
- Source and prior review: `docs/reviews/gsap-eight-skill-wave-6.md`, `docs/reviews/gsap-wave-7-license-arithmetic.md`, `docs/reviews/gsap-pinned-static-staging.md`.

## Why no external installation

Admission policy requires complete security, dependency, functional, accessibility and named-reviewer gates. Browser/runtime verification and dependency assessment were not completed. Static inspection cannot establish absence of vulnerabilities. Promoting candidates to active `skills/` or recording them as `approved` would misrepresent the evidence and violate the repository's security-first rule.

## Operational end state

1. **Use the existing `cinematic-gsap-review` skill immediately** for GSAP reviews and plans; it is already in the active repository folder.
2. Keep the seven external packages as provenance-pinned reference candidates, not active instructions.
3. Stop the GSAP intake workflow here. Reopen only on a **new explicit request** with an environment able to perform the missing checks, or after a new upstream release is selected.
4. Repository status: **GSAP intake CLOSED, first-party skill AVAILABLE, external admission NOT APPROVED.**

This is a final release decision, not a pending request for further approval or tests.
