# MySQL / MariaDB transaction correctness

1. Confirm tables use transactional engine (typically InnoDB), foreign keys exist and database/sql_mode/isolation are known.
2. For multi-row changes, use beginTransaction / commit / rollBack with try/catch/finally; rollback on **every** exception, including downstream validation failure. Do not send success before commit.
3. For concurrent balance/stock changes, use row locks (SELECT ... FOR UPDATE) inside transaction, deterministic lock ordering, and a bounded retry policy only for classified deadlock/serialization failures. Do not blindly retry non-idempotent side effects.
4. Enforce request idempotency with a unique key scoped to actor and operation, persist request/result atomically, and reject reuse with a different payload. Unique constraints must be in the database, not just PHP prechecks.
5. Keep all monetary amounts in integer minor units or fixed-scale DECIMAL; specify currency precision, rounding, sign rules and invariants. Avoid PHP floats for ledger balances.
6. For transfers, debit/credit records, account balance update and idempotency record must commit or roll back together. Reconcile totals and prevent negative balances only where business rules require it.
7. Do not use unsafe external API calls or file moves inside a DB transaction as though rollback reverses them; use an outbox or compensating cleanup.
8. Verify failures: missing product image DB insert; rollback on second write; duplicate order POST; simultaneous balance updates; deadlock handling; stale read; missing FK; backup/restore on isolated database.
9. Require explicit database migration versioning, forward and rollback plan, backups, index verification and compatible rollout. MySQL DDL may implicitly commit; do not claim it is transactional.
