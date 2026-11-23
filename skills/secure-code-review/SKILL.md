---
name: secure-code-review
description: Review application code and deployment configuration for common security flaws, secrets exposure, authorization bypass, unsafe uploads, session handling and injection risks. Use for security audits of PHP, Node, React and MySQL projects; provide evidence and severity without running attacks or changing production.
---

# Secure Code Review

1. Define trust boundaries and inspect authentication, authorization and owner-only routes, including server-side enforcement.
2. Check SQL parameterization, output encoding, CSRF protections, session cookie attributes, rate limiting and CORS.
3. Inspect upload MIME/signature/size/path validation, storage isolation and media serving policies.
4. Inspect secret handling and logs without copying sensitive values; avoid active exploitation and production stress tests.
5. Report evidence, likelihood, impact, remediation and safe verification steps; never claim absolute security.

This original skill is instruction-only and includes no executable scripts, network hooks or third-party dependencies. Consult `references/PROVENANCE.md` for source-review limits.
