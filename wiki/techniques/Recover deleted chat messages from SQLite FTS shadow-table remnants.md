---
id: LWT-1196
type: technique
name: Recover deleted chat messages from SQLite FTS shadow-table remnants
description: Recover a chat message deleted through an application's own delete function by reading the corresponding shadow (content) table that the SQLite Full-Text Search (FTS) extension maintains for the searchable column, since an app's delete-message function commonly clears only the main table's message content while the parallel FTS shadow table, still linked by the same message ID, retains an untouched copy.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1204
aliases:
  - FTS-based deleted-message recovery
  - SQLite FTS shadow-table anti-forensic recovery
source_refs:
  - LWCite-1217
updated_at: 2026-08-13
status: complete
---

# Recover deleted chat messages from SQLite FTS shadow-table remnants

## Summary

When an application enables the SQLite FTS extension to make a column's text searchable, FTS maintains one or more separate shadow tables (named `[table]_content`/`[table]Search_content` depending on FTS version) that store a duplicate copy of the indexed data; if the application's own delete-message function only updates the main table (clearing the visible content and marking a deleted-status flag) without also clearing the corresponding FTS shadow-table row, the original message content remains recoverable from the shadow table by matching the same message/row ID that persists, unmodified, in the main table.

## Details

Standard techniques for recovering deleted SQLite records rely on unused-page analysis or rollback-journal recovery, both of which fail once "secure delete" zeroes freed pages or no journal file is available; this technique instead exploits the application's own indexing infrastructure, which was never designed with deletion in mind. Practically, this requires first identifying which of the application's tables have an associated FTS shadow-table set (visible in the database schema by the presence of `_content`/`Search_content`/`_data`/`_segdir`/`_docsize` companion tables), then, for a row whose main-table content column has been cleared or flagged deleted, querying the shadow-table's row with the matching ID to recover the original text. Because different applications implement their own message-deletion logic differently, the specific columns cleared (and whether a "leave/soft-delete" action deletes anything at all) must be verified per application rather than assumed from one case study.

## Examples

- Cisco Webex (Hur et al., 2023): the "select and delete a message" function clears only the `MESSAGE_DATA` column and sets `MESSAGE_TYPE` to a deleted-status value in the `Message` table of `spark_persistent_store.db`, while the FTS `MessageSearch` and `MessageSearch_content` shadow tables retain the original `MESSAGE_DATA` value under the same, unchanged `MESSAGE_ID`, allowing full recovery of message text believed deleted by both sender and receiver. Webex's separate "leave a chat room or space" function was found to delete only the conversation's title metadata from the `Conversation` table, leaving all of that conversation's individual messages entirely undeleted in the `Message` table regardless of FTS.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/FTS-based deleted-message recovery depends on the target application's database schema retaining undeleted FTS shadow-table remnants]]

## References

- [LWCite-1217] Hur et al., 2023, "Forensic analysis for multi-platform Cisco Webex", FSI: Digital Investigation 47, 301659.
