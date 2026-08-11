---
id: DFW-1008
type: weakness
name: SQLite WAL checkpoint discards deleted data before recovery
description: When an application using SQLite in WAL mode terminates (or the WAL exceeds its size threshold), a checkpoint writes only currently valid data back to the main database file and discards deleted or uncommitted data still sitting in the WAL, permanently losing it if the WAL was not captured beforehand.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1008
source_refs:
  - DFCite-1004
updated_at: 2026-08-09
status: complete
---

# SQLite WAL checkpoint discards deleted data before recovery

## Summary

A checkpoint may be triggered automatically on application/connection termination even without an explicit request, and during this process only the current valid state is folded back into the main `.db` file; any deleted records or uncommitted changes that were only present in the WAL frames are discarded and are not written anywhere else.

## Why It Matters

If an investigator collects only the main database file after the generating application (or device) has already terminated and checkpointed, WAL-based recovery becomes impossible for that data, even though it may have been recoverable moments earlier. This creates a narrow but critical acquisition-order requirement: the database and its WAL file must both be collected, ideally before the source application or device is shut down, or recoverable deleted data can be silently and irreversibly lost.

## Related Mitigations

- [[mitigations/Acquire SQLite database and WAL file together before application termination]]

## Used By

- [[techniques/SQLite deleted record recovery]]

## References

- [DFCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
