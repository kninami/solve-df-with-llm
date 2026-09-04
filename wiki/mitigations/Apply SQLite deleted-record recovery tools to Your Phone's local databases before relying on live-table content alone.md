---
id: LWM-1281
type: mitigation
name: Apply SQLite deleted-record recovery tools to Your Phone's local databases before relying on live-table content alone
source_refs:
  - LWCite-1308
updated_at: 2026-08-15
status: complete
---

# Apply SQLite deleted-record recovery tools to Your Phone's local databases before relying on live-table content alone

## Summary

Run established SQLite deleted-record recovery methods (freeblock/freelist traversal, cell-structure carving, or WAL-frame parsing) against Your Phone's `notifications.db` and its other SQLite3 databases rather than reading only the live table content, so that acknowledged notifications and other removed rows are recovered alongside currently pending ones.

## Addresses

- [[weaknesses/Your Phone deletes a notification record from its local database as soon as it is acknowledged on the phone]]

## How To Apply

Before drawing conclusions from a live-table query of `notifications.db` (or Your Phone's other SQLite3 databases), run a general-purpose SQLite recovery tool against each database — the source paper used `undark`, `SQLite-Deleted-Records-Parser`, and `bring2lite`, but any tool implementing [[techniques/Recover deleted SQLite records]]'s metadata-based, carving-based, or WAL-based approaches is applicable. Cross-check recovered rows for internal consistency (timestamp ordering, plausible originating-app values) before including them in a report, and note in the report that live-table-only figures understate true notification volume.

## References

- [LWCite-1308] Domingues, Andrade, and Frade, 2021, "Microsoft's Your Phone environment from a digital forensic perspective", FSI: Digital Investigation 38, 301177.
