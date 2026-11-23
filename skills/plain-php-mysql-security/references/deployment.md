# Safe deployment checklist — PHP/MySQL on shared hosting

- Confirm production PHP version, PDO MySQL extension, MySQL/MariaDB version, file permissions, cron and rewrite rules.
- Keep configuration and secrets outside public web root; never commit .env, SQL dumps or private uploads.
- Separate test database/user from production with least privilege; test restore before changing production schema.
- Use versioned additive migrations, inspect DDL implicit commits and take verified backups; maintain backward compatibility during rollout.
- Deploy API and frontend in compatible order; run health checks that verify database connectivity **without exposing credentials**.
- Test save then refresh, second browser/device read, unauthorized read, duplicate POST, failed upload and failed DB write. Distinguish client-side optimistic display from durable persistence.
- Confirm HTTPS, secure cookie configuration, PHP execution disabled in upload directories, directory listing disabled, error logs private, production display_errors off.
- Monitor failed transactions, session expiry and disk quota; rollback application code and use tested DB recovery plan when schema rollback is unsafe.
- Do not access or modify live hosting without explicit authorization and an agreed rollback point.
