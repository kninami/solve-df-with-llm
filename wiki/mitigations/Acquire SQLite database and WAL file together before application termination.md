---
id: LWM-1008
type: mitigation
name: Acquire SQLite database and WAL file together before application termination
source_refs:
  - LWCite-1004
updated_at: 2026-08-09
status: complete
---

# Acquire SQLite database and WAL file together before application termination

## Summary

Collect the main `.db` file and its associated `.db-wal` file as a matched pair, and where feasible acquire them before the generating application or device is powered off or its database connection closed, since termination can trigger a checkpoint that discards recoverable deleted data still resident in the WAL.

## Addresses

- [[weaknesses/SQLite WAL checkpoint discards deleted data before recovery]]

## How To Apply

When triaging a live device or system using SQLite in WAL mode, prioritize acquiring the `.db-wal` file alongside the main database before shutting down the source application, since a graceful or forced termination may trigger an automatic checkpoint that folds valid data back into the main file and discards anything only present in the WAL. If the device has already been powered off before acquisition, still collect any `.db-wal` file present, since not all shutdowns trigger a checkpoint.

## References

- [LWCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
