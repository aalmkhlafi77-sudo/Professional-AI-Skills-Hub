---
name: backup-restore-assurance
description: Audit backup, restore and recovery flows for MySQL, JSON and uploaded media. Use for encrypted backups, recovery drills, data integrity checks and disaster recovery planning without exposing secrets or restoring production data.
---

# Backup Restore Assurance

1. Inventory database, attachments, encryption metadata, key handling, versioning and backup retention.
2. Check backup consistency, encryption/authentication, checksums and restore validation before replacement.
3. Require isolated restore target and compare record counts, relations, attachments and critical invariants.
4. Document recovery point and time objectives as requirements, not invented measurements.
5. Propose reversible recovery drills; never access secrets, overwrite production or run a restore without explicit approval.

This is an original instruction-only skill. It includes no scripts, executables, dependencies or network installation steps.
