---
name: mysql-data-integrity-review
description: Audit MySQL-backed PHP or Node applications for transaction safety, persistence defects, duplicate records, referential integrity, concurrency and backup/restore risks. Use for disappearing uploads, repeated Excel imports, ledger data consistency or database migrations; report read-only findings and require approval before changes.
---

# MySQL Data Integrity Review

1. Trace each write from UI request through API validation, SQL transaction, commit and subsequent read; distinguish optimistic UI state from persisted state.
2. Inspect primary and foreign keys, unique constraints, upserts, idempotency, transaction boundaries, isolation, locking and rollback paths.
3. Inspect upload metadata persistence, file ownership, path validation, orphan handling and consistency between storage and database.
4. Assess backup and restore validation, migration rollback and concurrency without exposing credentials or production records.
5. Give SQL or code suggestions only as proposed changes; do not execute production writes, migrations, restores or credential operations without approval.

This original skill is instruction-only and includes no executable scripts, network hooks or third-party dependencies. Consult `references/PROVENANCE.md` for source-review limits.
