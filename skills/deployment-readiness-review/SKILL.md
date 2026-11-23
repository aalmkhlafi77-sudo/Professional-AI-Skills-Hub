---
name: deployment-readiness-review
description: Review Node.js, Express, PHP, React and Vite deployments for Hostinger-style hosting, environment configuration, build outputs, media persistence and rollback readiness. Use before deploying or diagnosing failed production builds; report a non-destructive checklist and request approval before deployment.
---

# Deployment Readiness Review

1. Identify runtime, build command, entrypoint, web root, domain routing, API paths and database connection requirements.
2. Check environment-variable names and presence without printing secrets; inspect startup health and migration compatibility.
3. Review upload-root persistence, file permissions, CDN/browser cache behavior, SPA fallback and static asset paths.
4. Distinguish repository build failures, platform configuration failures and runtime failures using logs when available.
5. Deliver a minimal deployment/rollback plan; never modify live hosting, secrets, DNS or databases without approval.

This original skill is instruction-only and includes no executable scripts, network hooks or third-party dependencies. Consult `references/PROVENANCE.md` for source-review limits.
