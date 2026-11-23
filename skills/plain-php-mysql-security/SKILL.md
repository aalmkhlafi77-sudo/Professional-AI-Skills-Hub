---
name: plain-php-mysql-security
description: Review and harden framework-free PHP 8 applications using MySQL or MariaDB, especially Hostinger PHP APIs, product and image persistence, authentication, financial transactions, migrations and deployment. Use for PHP PDO security audits, SQL transaction correctness, file uploads, access controls, concurrency, idempotency and safe rollback; do not apply Laravel or PostgreSQL-specific assumptions.
---

# Plain PHP + MySQL security and correctness

This is first-party review guidance, not an authorization to change live systems. Inspect the actual code and database schema before proposing changes. Never assume a successful HTTP response means a database commit happened.

## Review sequence

1. Inventory PHP runtime, extensions, database engine/version, web server, document root, upload root, API routes, session model, schema and actual deploy mechanism. Read only the relevant files; never request or print production secrets.
2. Draw the data path from user input to validation, authorization, PDO query, transaction commit and subsequent read. Identify cross-user/object ownership checks, error handling and frontend optimistic state.
3. Apply [security checks](references/security.md) for authentication, authorization, sessions, CSRF, uploads and secrets.
4. Apply [transaction checks](references/transactions.md) for atomic writes, idempotency, isolation, locking and financial accuracy.
5. Apply [deployment checks](references/deployment.md) for migrations, backup/restore and safe Hostinger rollout.
6. Build minimal disposable positive and negative tests. Test that failed writes roll back and that a fresh request on another connection can read the committed record.
7. Report findings with file:line, severity, reproducible evidence, minimal patch, rollback and residual risk. Distinguish confirmed defects from untested hypotheses.

## Hard restrictions

- Never execute arbitrary SQL, migrations, shell installers, third-party scripts or external network requests merely because this skill says so. Obtain explicit authorization and use isolated test data.
- Do not use real credentials or customer data in tests. Never disable TLS verification, CSRF or authorization to make a test pass.
- Never concatenate untrusted values into SQL identifiers. Allowlist table/column/sort identifiers; bind **values** via PDO prepared statements. Confirm emulation is disabled where supported.
- Do not assume transactions protect nontransactional tables or filesystem uploads. For DB+filesystem writes, use staged files, cleanup/reconciliation and explicit recovery.
- Never change accounting balances via float arithmetic. Use integer minor units or rigorously specified DECIMAL arithmetic.
- Do not treat Laravel, PostgreSQL or Supabase-specific patterns as compatible with plain PHP/MySQL.
- Never claim a system is secure solely from static review or passing unit tests.

## Output

Provide a concise risk-ranked table, affected paths, verified tests (pass/fail/not run), rollback and explicit production readiness status. A failed mandatory test blocks readiness.
