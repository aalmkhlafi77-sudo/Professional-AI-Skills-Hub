# Admission Policy — Security-first

## Weighted score (100)

| Dimension | Maximum |
|---|---:|
| Security of skill instructions, scripts, dependencies and supply chain | 30 |
| Practical test results, reliability, and quality | 25 |
| Compatibility and isolation / minimal interference | 20 |
| Maintenance, source integrity, license | 15 |
| Documentation and usability | 10 |

**Approve only with score >= 90/100 AND every mandatory security gate PASS, plus a named human reviewer.**

## Mandatory gates (all required)

- Genuine upstream owner, canonical URL and exact immutable commit identified.
- File-by-file license and redistribution permissions verified.
- All SKILL.md, nested references, scripts, hooks, manifests, dependencies, install steps, plugins and MCP configurations reviewed.
- No prompt injection overriding user instructions or concealing data access or actions.
- No uncontrolled remote downloads, privileged execution or hidden network destinations.
- No unrestricted secret access, destructive writes, autonomous merge or deployment.
- Dependency vulnerabilities assessed and severe findings remediated.
- Meaningful passing and failure tests executed inside a disposable sandbox without sensitive credentials.
- Visual skills tested with inspected mobile/desktop screenshots, accessibility and reduced-motion behavior.
- Risks, limitations, rollback and future upgrades documented.

A missing test is PENDING, never PASS. A score does not override failure of any gate.

## Status

candidate: discovery only.
under_review: assessment in progress.
approved: all gates and evidence passed.
rejected: unacceptable.
retired: approval withdrawn.

## Implementation library versus skill

React Bits, Three.js, Motion and similar packages are development dependencies. Their source code is not automatically an agent skill. Document and assess them separately, and do not add conflicting animation runtimes automatically.
