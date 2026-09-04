---
id: LWW-1146
type: weakness
name: Standard deleted-file recovery misses document data remnants left by Microsoft 365 applications
description: Conventional deleted-file recovery and carving techniques target unallocated space and known artifact types, so they miss document data remnants that Microsoft 365 applications retain in previously unstudied cache, sync-log, and activity-tracking files, even when those remnants are readily accessible in allocated space.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1146
source_refs:
  - LWCite-1142
updated_at: 2026-08-12
status: complete
---

# Standard deleted-file recovery misses document data remnants left by Microsoft 365 applications

## Summary

Traditional digital forensic recovery and carving techniques primarily target unallocated space and rely on documented, previously studied artifact structures. Microsoft 365 applications generate a range of cache, offline-sync, and activity-log files whose structure has not been previously documented, and these files can retain a deleted document's filename, path, timestamps, size, or content well after the source file and its standard NTFS traces are gone — but only if an examiner specifically knows to look for and parse them, since they sit outside the scope of conventional recovery methods.

## Why It Matters

An investigator who relies solely on unallocated-space recovery and well-known artifact locations may conclude that a deleted Microsoft 365 document left no recoverable trace, when in fact its filename, path, or content remains intact in an application-generated file the investigator did not know to examine. As operating systems and applications are frequently updated, the specific set of files that retain remnants also changes, so this gap can silently reopen even for previously well-covered application versions.

## Related Mitigations

- [[mitigations/Search known Microsoft 365 remnant locations for recoverable document data using differential analysis]]

## Used By

- [[techniques/Identify document data remnants in Windows and Microsoft 365 using differential snapshot analysis]]

## References

- [LWCite-1142] Joun, Lee and Park, 2023, "Data remnants analysis of document files in Windows: Microsoft 365 as a case study", FSI: Digital Investigation 46.
