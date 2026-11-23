# Security review and native UI intake — Wave 5

Status: **quarantined / unapproved**. Date: 2026-11-23.

## Imported skills

| Source | Skill | Immutable source commit | License evidence | Why selected | Remaining scope limits |
|---|---|---|---|---|---|
| GetSentry | `security-review` | `a582c51ee29d0f35e6ac321340796f77d43da733` | Dedicated skill Apache-2.0 license copied | Broad app security checklist covering auth, authorization, cryptography, CSRF, data protection, file security, SSRF, XSS and supply chain | Sentry-origin workflow and allowed tools require host adaptation; verify all security claims against target stack and current standards |
| Expo | `expo-native-ui` | `88d9bd79f3fa8452a778fbac65bae162c0b32ce4` | Expo plugin MIT license copied in prior intake | Native iOS/Android controls, icons, gradients, media, visual effects and WebGPU/Three guidance | Expo/React Native only; OS-specific API compatibility and device tests required |

The Sentry skill includes its SKILL.md, SPEC.md, dedicated LICENSE, Docker/JavaScript/Python guides, and 16 security references. Expo native UI includes SKILL.md, agent metadata and seven reference files. Source hashes are recorded in `catalog/intake-provenance.json`.

## Static screening notes

- No executable scripts or install hooks are included in these two selected skill bundles; they are instructions and references.
- Sentry's own Apache-2.0 license is preserved at the skill level. It is separate from the already mirrored repository license.
- Expo's parent plugin MIT license is preserved in the intake root.
- Skills are not automatically invoked from `intake/`.
- No target project, credentials, production database, browser session or deployment has been touched.
- No duplicate GSAP/Sentry smoke tests have been run.

## Admission

Both skills remain unapproved. Remaining gates include complete instruction/permission review, target-framework compatibility, practical task evaluations, negative security tests, accessibility/platform validation and human sign-off. No score assigned.
