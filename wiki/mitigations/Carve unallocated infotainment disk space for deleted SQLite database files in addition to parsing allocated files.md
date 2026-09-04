---
id: LWM-1220
type: mitigation
name: Carve unallocated infotainment disk space for deleted SQLite database files in addition to parsing allocated files
source_refs:
  - LWCite-1231
updated_at: 2026-08-13
status: complete
---

# Carve unallocated infotainment disk space for deleted SQLite database files in addition to parsing allocated files

## Summary

Always run file-carving software against an infotainment hard disk image's unallocated space to recover complete deleted SQLite database files, then apply deleted-record recovery to any carved files, rather than stopping the examination at the databases currently referenced by the live file system.

## Addresses

- [[weaknesses/Standard infotainment forensic analysis limited to allocated files misses deleted SQLite databases recoverable from unallocated space]]

## How To Apply

After acquiring a physical (not logical) forensic copy of the infotainment hard disk, run a signature-based file-carving tool (e.g. PhotoRec) against the disk's unallocated space, searching for the `SQLite format 3` header signature to recover complete deleted database files. Open each carved database with a standard SQLite browser to catalog its visible tables and records, then run a dedicated SQLite deleted-record recovery tool (e.g. one implementing freeblock/freelist traversal) against the carved file to surface additional records the carved copy's own visible tables do not show, since a carved file can itself contain further internally deleted data. Cross-reference recovered records against the live-file-system databases' schema and content to identify whether the carved files represent an earlier backup state, a pre-reset copy, or content otherwise absent from the currently active databases.

## References

- [LWCite-1231] Marques, Domingues, Frade and Negrão, 2026, "Forensic analysis of the infotainment system of BMW vehicles", FSI: Digital Investigation 56, 302066.
