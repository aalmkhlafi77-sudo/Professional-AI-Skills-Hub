# GSAP pinned static intake — 2026-11-23

Source: https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760
Tree API `git/trees/<SHA>?recursive=1` returned `truncated:false`: **66 total entries**, eight skill entrypoints each consisting of one `SKILL.md`; no scripts, hooks, symlinks or package manifests **within the eight skill folders**. Repository root includes two symlinks `CLAUDE.md` and `GEMINI.md` (not imported), plugin manifests, assets and example apps. Full tree metadata was inspected. Root MIT notice preserved.

Seven pinned instruction-only skills copied unchanged into **candidates/greensock-gsap/**, which is not the live `skills/` path and is not in `catalog/approved.json`. No upstream scripts or examples copied; no third-party code run; no packages installed; no production projects changed.

**Excluded `gsap-scrolltrigger`** because its example uses `Max.max` (undefined) and pixel distances in `xPercent`. Other reviewed example defects reinforce the choice to exclude all demos: Nuxt `useGSAP.ts` duplicates `type Plugins`, Nuxt index.vue has an `onMounted` cleanup instead of `onUnmounted`, and Vue app.vue has a JavaScript comment before the SFC `<script setup>` tag. These are quality defects, not proven security breaches. Nuxt example `package.json` also declares `postinstall: nuxt prepare`; examples are **not installed**. Vanilla demo references a public CDN; not imported.

Static security observations: reviewed eight entrypoint texts and plugin manifests, no embedded executable scripts inside skill folders; GSAP npm installation is described, not performed. This is **not a security guarantee**; dependencies and all runtime/browser tests are unverified.

Mandatory gates:
- Canonical source, immutable commit, root MIT: PASS.
- Tree inventory and contents of eight entrypoints: PASS.
- No executable payload inside staged seven skill folders: PASS (tree metadata).
- Full file-by-file review of every example/asset, dependency vulnerability check: PENDING (examples intentionally excluded).
- Runtime security, sandbox positive/negative, visual mobile/desktop, reduced-motion: PENDING.
- Named human reviewer and >=90 admission score: PENDING.

**Decision: STAGED / UNDER REVIEW**, not approved or activated. No further testing performed at user's request. The admission policy prohibits marking these approved or installing them as active skills without the outstanding gates. To activate later, explicit acceptance of the risks and completion of policy gates are required.
