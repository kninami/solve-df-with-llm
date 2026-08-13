---
id: DFW-1213
type: weakness
name: SQLite VACUUM overwrites freed record data with null bytes, preventing deleted-message recovery
description: An application that periodically runs SQLite's VACUUM command physically rewrites its database file, overwriting the freed space previously occupied by deleted rows with null bytes rather than merely marking it free, which permanently destroys the record remnants that unallocated-space carving techniques would otherwise recover.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1213
source_refs:
  - DFCite-1225
updated_at: 2026-08-13
status: complete
---

# SQLite VACUUM overwrites freed record data with null bytes, preventing deleted-message recovery

## Summary

Attempts to recover deleted messages and contact records from Monal's `sworim.sqlite` database using established SQLite deleted-data-recovery tools (Undark and Cellebrite Physical Analyzer's SQLite recovery feature) were unsuccessful because the database fields that would normally hold recoverable freed-cell remnants had already been overwritten with null bytes upon deletion, confirming the application invokes SQLite's VACUUM command during normal operation.

## Why It Matters

Standard SQLite deleted-record-carving techniques assume deleted rows remain physically present in unallocated pages of the database file until overwritten by unrelated new data; an application that runs VACUUM defeats this assumption deterministically and immediately upon deletion, rather than only eventually or probabilistically as ordinary page reuse would. An investigator who assumes deleted SQLite records are generally recoverable, without first checking whether the specific application performs VACUUM, may wrongly expect success and fail to look for alternative evidence sources for the same deleted content.

## Related Mitigations

- [[mitigations/Acquire a database snapshot before a scheduled or triggered VACUUM can run, or seek deleted content elsewhere]]

## Used By

- [[techniques/Extract OMEMO-encrypted XMPP chat artifacts from iOS multi-client SQLite databases]]

## References

- [DFCite-1225] Akinbi and Ojie, 2021, "Forensic analysis of open-source XMPP multi-client social networking apps on iOS devices", FSI: Digital Investigation 36.
