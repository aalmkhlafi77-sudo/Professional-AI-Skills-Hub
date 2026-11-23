---
name: excel-import-integrity
description: Review spreadsheet import pipelines for duplicate entities, atomic transactions, validation, preview, mapping and rollback. Use when CSV or XLSX imports repeat customers, products or suppliers, corrupt existing records or fail to persist.
---

# Excel Import Integrity

1. Trace parser, normalization, identity matching and commit stages; distinguish new records from updates.
2. Define canonical keys, duplicate detection, stable IDs and explicit collision policies; never silently overwrite records.
3. Require preview of insert/update/skip/error counts, transaction atomicity and rollback on validation failure.
4. Specify test fixtures for repeated rows, reimports, mixed valid-invalid data and concurrent uploads.
5. Produce minimal code-level recommendations and expected tests; do not import production files or write data without approval.

This is an original instruction-only skill. It includes no scripts, executables, dependencies or network installation steps.
