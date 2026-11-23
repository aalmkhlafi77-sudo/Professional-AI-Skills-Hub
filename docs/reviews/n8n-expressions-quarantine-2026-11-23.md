# n8n expressions: isolated skill intake (2026-11-23)

- **Source:** https://github.com/n8n-io/skills
- **Immutable commit:** `626f50fdf2934116eea2c5469339e03d2d524e83`
- **Copied without modification:** `skills/n8n-expressions-official/SKILL.md` → `intake/n8n/n8n-expressions-official/SKILL.md`
- **Original Git blob SHA:** `76de420cb9b0be4782869598d791b5c2523ef74b`
- **License:** root Apache-2.0 `LICENSE`, original blob `c87e50b21d7195576cfda86509960d9f80a1d3bd`, copied to `intake/n8n/LICENSE`.
- **Status:** **under_review** / quarantined, not approved or enabled.

## Scope of static inspection

Read entire skill entrypoint (21,281 bytes). The pinned skill has no nested references, scripts or runtime dependencies within its own directory. It documents n8n expression syntax, node-name references, `.all()` aggregation, execute-once behavior, Luxon, JSON transformation and secret-handling advice. It contains no executable installer, bundled plugin or hook. The original repository does contain plugin hooks and lockfiles; **none were copied**. The skill is only relevant when working with n8n, not as general JavaScript guidance.

**Review caution:** Some advice is expressed as mandatory (e.g. preferring node-name references over `$json`, and avoiding Set nodes). This is opinionated implementation guidance, **not** authority to modify user workflows or override the user's requirements. It must be validated against actual n8n node semantics and version before use. Expressions may generate data for side-effecting downstream nodes; review the entire workflow before execution.

## Gate status

| Gate | Status | Basis |
|---|---|---|
| Canonical owner, immutable pin and file SHA | PASS | Verified against upstream tree and blob |
| Skill-local files, references and executables inventoried | PASS | One SKILL.md only |
| License and redistribution notice preserved | PASS | Upstream Apache-2.0 LICENSE copied verbatim; no local edits |
| No bundled hooks, installer, executable or external connection | PASS | Quarantine contains only text skill and license |
| Prompt injection/unsafe instruction effects | PENDING | Static read completed; adversarial instruction tests not executed |
| Dependency vulnerabilities | PASS for copied artifact | No dependencies bundled; actual n8n runtime is out of scope |
| Safe practical positive/negative n8n expression tests | PENDING | No n8n sandbox or live instance connected |
| Compatibility and semantic accuracy | PENDING | Requires actual pinned n8n runtime verification |
| Named human reviewer and >=90 score | PENDING | No score assigned; not production approved |

**Next:** isolated tests of n8n expression evaluation with known inputs, wrong/missing node references, aggregation and branching; ensure no network/credentials/production writes. Import of this documentation is **not** approval to install or run the upstream plugin.
