---
id: LWW-1301
type: weakness
name: Auto-vacuum-enabled wearable companion-app databases permanently destroy deleted notification and activity records
description: A wearable companion app's SQLite database configured with PRAGMA auto_vacuum set to FULL reclaims deleted-row storage immediately and continuously, rather than leaving deleted-record remnants in free pages or a rollback journal, so standard SQLite deleted-record recovery methods that rely on scanning freeblocks, freelists, or WAL frames find nothing to recover from an old, rotated-out notification or activity record.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1303
source_refs:
  - LWCite-1335
updated_at: 2026-08-15
status: complete
---

# Auto-vacuum-enabled wearable companion-app databases permanently destroy deleted notification and activity records

## Summary

Garmin Connect's `notification-database` retains only recent phone notifications relayed to the paired smartband and frequently purges older ones; verification confirmed the database has `PRAGMA schema.auto_vacuum` set to `FULL`, a SQLite setting that actively repacks the database file to reclaim space from deleted rows as part of normal operation, rather than leaving that space marked free but recoverable until the file happens to be overwritten later.

## Why It Matters

An investigator applying standard SQLite deleted-record recovery techniques (freeblock/freelist traversal, page carving, or WAL-frame parsing) against an auto-vacuum-`FULL` database will find no recoverable trace of a notification or record that has already rotated out of the live table, unlike in a database without this setting, where deleted content often remains recoverable for some time. Not checking a database's auto-vacuum configuration before investing effort in deleted-record recovery risks wasted analysis time and a false assumption that recovery tools simply failed rather than that the underlying data was never recoverable in the first place.

## Related Mitigations

- [[mitigations/Check a target SQLite database's auto-vacuum setting before attempting deleted-record recovery]]

## Used By

- [[techniques/Extract health, fitness, and location artifacts from a wearable's Android companion application]]

## References

- [LWCite-1335] Nunes, Domingues, and Frade, 2023, "Post-mortem digital forensic analysis of the Garmin Connect application for Android", FSI: Digital Investigation 47, 301624.
