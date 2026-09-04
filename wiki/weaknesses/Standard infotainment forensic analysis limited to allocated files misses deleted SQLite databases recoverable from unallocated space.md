---
id: LWW-1220
type: weakness
name: Standard infotainment forensic analysis limited to allocated files misses deleted SQLite databases recoverable from unallocated space
description: An in-vehicle infotainment hard disk examination that only parses the databases the live file system currently references will miss entire deleted SQLite database files — including ones containing message content absent from any live table — that unallocated-space carving can still recover.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1220
source_refs:
  - LWCite-1231
updated_at: 2026-08-13
status: complete
---

# Standard infotainment forensic analysis limited to allocated files misses deleted SQLite databases recoverable from unallocated space

## Summary

Running PhotoRec against an NBT EVO infotainment system's unallocated disk space recovered four complete SQLite database files, each containing an SMS `messages` table, that were not present anywhere among the system's live, currently referenced files; running a deleted-record-recovery tool against those carved files then surfaced additional call records for which no live `calls` table existed at all, meaning the corresponding data would have been completely invisible to an examination limited to the actively indexed files.

## Why It Matters

Because deleted SQLite database files persist as intact, individually carvable units on an infotainment system's HDD storage (rather than being immediately overwritten), an examiner who stops after parsing the databases the file system currently lists can significantly undercount the communication evidence actually present on the disk; this is particularly consequential if a factory reset or account switch was performed on the vehicle in an attempt to erase prior user data, since the reset process may only unlink rather than securely wipe the underlying database files.

## Related Mitigations

- [[mitigations/Carve unallocated infotainment disk space for deleted SQLite database files in addition to parsing allocated files]]

## Used By

- [[techniques/Extract and correlate forensic artifacts from a QNX6FS vehicle infotainment hard disk's SQLite databases]]

## References

- [LWCite-1231] Marques, Domingues, Frade and Negrão, 2026, "Forensic analysis of the infotainment system of BMW vehicles", FSI: Digital Investigation 56, 302066.
