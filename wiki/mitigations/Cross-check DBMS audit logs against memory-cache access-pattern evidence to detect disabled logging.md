---
id: LWM-1148
type: mitigation
name: Cross-check DBMS audit logs against memory-cache access-pattern evidence to detect disabled logging
source_refs:
  - LWCite-1144
updated_at: 2026-08-12
status: complete
---

# Cross-check DBMS audit logs against memory-cache access-pattern evidence to detect disabled logging

## Summary

Do not treat a DBMS's own audit log as self-verifying; capture a memory snapshot of the DBMS process as early as possible in an investigation and check whether every table/page access pattern visible in the I/O buffer and sort area is explained by a corresponding logged query, flagging any unexplained pattern as evidence of possible disabled or bypassed logging.

## Addresses

- [[weaknesses/A privileged database user can disable audit logging without leaving a log-based trace of query activity]]

## How To Apply

As early as possible in a suspected-breach or insider-misuse investigation, acquire a trusted memory snapshot of the DBMS process using a live-analysis capable tool, since the relevant page cache and sort-area artifacts are volatile and can be overwritten by ordinary continued database activity. Carve the snapshot for table Object IDs and Page IDs to identify which tables and pages were accessed, then walk the audit log's recorded queries to check whether each observed access pattern (full table scan, index access) is explained by at least one logged operation, allowing for the fact that multiple logged queries covering overlapping value ranges can jointly explain a given access pattern. Flag any full-table-scan or index-access pattern with no explaining log entry as a candidate for undisclosed query activity, and prioritize memory acquisition frequency relative to the DBMS's I/O buffer/sort-area size so that transient artifacts are not missed between snapshots.

## References

- [LWCite-1144] Wagner, Nissan and Rasin, 2023, "Database memory forensics: Identifying cache patterns for log verification", FSI: Digital Investigation 45.
