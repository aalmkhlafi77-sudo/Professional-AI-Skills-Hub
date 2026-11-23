# Professional AI Skills Hub

A security-first, quality-gated catalog of reusable AI agent skills for professional software delivery. **Third-party skills are not installed or automatically executed.**

## Current status

- One locally authored source-review skill: `skills/skill-source-auditor/`.
- 13 third-party discovery candidates in `catalog/candidates.json` (unreviewed).
- Zero externally approved skills: `catalog/approved.json` is intentionally empty.
- Feature-branch foundation only; merge to `main` requires explicit approval.

## Security and quality policy

1. Approval requires a score of at least **90/100**, all mandatory security gates passed, reproducible sandbox evidence and a named human reviewer.
2. Treat upstream `SKILL.md`, scripts, hooks, dependencies, plugin configuration and install commands as **untrusted**.
3. Pin immutable upstream commits and verify licensing and redistribution permission.
4. Do not grant production credentials, unrestricted filesystem access, write access or unknown outbound network access by default.
5. Test realistic workflows, failures, accessibility, performance and visual quality where applicable.
6. No repo merge, deployment, payment or other side effect without explicit permission.
7. Never claim absolute security; unresolved risks remain unapproved.

## Layout

- `skills/`: locally-authored skill entrypoints and any independently reviewed packages.
- `catalog/candidates.json`: third-party discovery queue, not installed or trusted.
- `catalog/approved.json`: externally approved skills, currently empty.
- `docs/ADMISSION_POLICY.md`: mandatory gates and weighted scoring rubric.
- `docs/REVIEW_TEMPLATE.md`: evidence report template.
- `scripts/validate_catalog.py`: read-only structure and policy consistency validation.
- `tests/`: catalog policy tests.
- `AGENTS.md`: agent operational restrictions.

## Local validation

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

These tests validate repository rules and structure; **they do not constitute a security audit of third-party code**.

## License

Original repository content is distributed under MIT. Third-party content is not relicensed and cannot be copied without checking its original license.
