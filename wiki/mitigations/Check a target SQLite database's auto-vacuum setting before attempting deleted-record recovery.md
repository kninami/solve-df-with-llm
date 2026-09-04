---
id: LWM-1303
type: mitigation
name: Check a target SQLite database's auto-vacuum setting before attempting deleted-record recovery
source_refs:
  - LWCite-1335
updated_at: 2026-08-15
status: complete
---

# Check a target SQLite database's auto-vacuum setting before attempting deleted-record recovery

## Summary

Before applying deleted-record recovery techniques to a SQLite database, query its `PRAGMA schema.auto_vacuum` (and check for a rollback journal or WAL file) to determine whether the database actively reclaims deleted-row space; if it does, redirect recovery effort toward alternative sources (cloud-synced copies, backups, or the paired device's own storage) rather than continuing to attempt local file recovery.

## Addresses

- [[weaknesses/Auto-vacuum-enabled wearable companion-app databases permanently destroy deleted notification and activity records]]

## How To Apply

Before running [[techniques/Recover deleted SQLite records]] against a wearable companion app's database (or any SQLite database where deleted-record recovery matters to the case), check its `PRAGMA schema.auto_vacuum` setting. If set to `FULL` (or `INCREMENTAL` combined with regular incremental-vacuum calls), do not expect meaningful deleted-record recovery from the local file alone; instead pursue the paired wearable device's own on-device storage, any cloud backup or sync history associated with the account, or a device image captured before the relevant deletion occurred. Document the auto-vacuum finding in the case notes to explain why local recovery was not pursued further.

## References

- [LWCite-1335] Nunes, Domingues, and Frade, 2023, "Post-mortem digital forensic analysis of the Garmin Connect application for Android", FSI: Digital Investigation 47, 301624.
