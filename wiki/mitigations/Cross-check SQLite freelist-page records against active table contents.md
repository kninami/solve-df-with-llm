---
id: DFM-1006
type: mitigation
name: Cross-check SQLite freelist-page records against active table contents
source_refs:
  - DFCite-1004
updated_at: 2026-08-09
status: complete
---

# Cross-check SQLite freelist-page records against active table contents

## Summary

Before reporting a record recovered from a freelist page as "deleted," compare it against the database's current live table contents; if the record is still present, it was relocated by B-tree rebalancing rather than deleted, and should not be reported as recovered deleted data.

## Addresses

- [[weaknesses/SQLite B-tree rebalancing causes valid data in freelist pages to be misidentified as deleted]]

## How To Apply

After extracting candidate records from freelist pages via freeblock/freelist traversal, run each recovered record's key fields against a full scan of the database's currently active tables. Records that match live rows should be excluded from the "deleted records" findings and instead noted as artifacts of B-tree rebalancing, since only records absent from the live tables represent genuinely deleted data.

## References

- [DFCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
