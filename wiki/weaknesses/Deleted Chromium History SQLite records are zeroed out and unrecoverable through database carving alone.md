---
id: DFW-2054
type: weakness
name: Deleted Chromium History SQLite records are zeroed out and unrecoverable through database carving alone
description: When a user deletes a browsing history, search term, or download entry in a Chromium-based browser's History SQLite database, the freed unallocated space between remaining table records is zeroed out rather than retained as recoverable slack, so binary carving and keyword searching of the History database file itself cannot recover the deleted content, regardless of the database's write-ahead-log or auto-vacuum settings.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2054
source_refs:
  - DFCite-2055
updated_at: 2026-08-14
status: partial
---

# Deleted Chromium History SQLite records are zeroed out and unrecoverable through database carving alone

## Summary

The source paper's own binary-level analysis found that although "related work indicated that deleted data may be stored within browser artefact data structures," this was not the case for either Brave's or Chrome's History SQLite database: "when records are deleted, the SQLite B-Tree structure is modified so records are moved from node to node... nodes contain unallocated space which may contain deleted or modified data however, analysis failed to identify or recover any of the deleted search terms from the History database." Manual binary review confirmed "the same area of binary zeroed out" both immediately after deletion and after the browser session was closed, ruling out session-closure or a later background process as the cause - the zeroing appears to occur at deletion time itself. Both a text/hex keyword search and a full SQL-file-header carving search for the deleted database also failed to locate any trace.

## Why It Matters

An investigator who expects deleted browsing history, search terms, or download records to remain partially recoverable from within the History database itself (a common assumption based on how SQLite deletion is understood to behave in other contexts) will find this assumption does not hold for Chromium-based browsers' History database specifically, and will need to look elsewhere for evidence that deleted activity occurred, or risk concluding - incorrectly - that no deletion took place or that the deleted content is permanently lost.

## Related Mitigations

- [[mitigations/Correlate Cache and Windows OS artifacts when a Chromium browser's History database yields no deleted-record recovery]]

## Used By

- [[techniques/Recover deleted browser activity by correlating cache, history, and Windows OS artifacts]]

## References

- [DFCite-2055] Berham and Morris, 2022 — Section 5 "Discussion" documents the zeroed-out unallocated space finding and the failed carving/keyword-search attempts against both browsers' History databases.
