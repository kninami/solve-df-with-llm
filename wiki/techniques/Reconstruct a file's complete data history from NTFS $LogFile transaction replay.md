---
id: LWT-1278
type: technique
name: Reconstruct a file's complete data history from NTFS $LogFile transaction replay
description: Recover the complete history of every modification made to an NTFS file's data — not just its final state — by replaying the file's own subset of $LogFile transaction records against a per-file virtual MFT entry, recovering the data-run locations, resident data content, and timestamp of the file at each point in time from its creation to its deletion.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1288
aliases:
  - Simulation of MFT Transaction (SMT)
  - NTFS Data Tracker
source_refs:
  - LWCite-1319
updated_at: 2026-08-15
status: complete
---

# Reconstruct a file's complete data history from NTFS $LogFile transaction replay

## Summary

Standard file system analysis of a live NTFS volume, and prior $LogFile-based research, can recover only a file's current metadata (creation time, last-modified time, last-saved data) or, at best, its final on-disk data-run location before deletion. Simulation of MFT Transaction (SMT) instead replays every transaction record belonging to a specific file — in the order they were written to $LogFile — against a per-file virtual MFT entry, recovering the location and content of the file's data, and the time of each change, at every intermediate revision from creation to deletion, not just the final state.

## Details

Each $LogFile record's combined `Target LCN` + `MFT Cluster Index` value identifies which MFT entry the record's operation applies to; records sharing this combined value are grouped as operations on the same file, and a virtual MFT entry is created for that file when its `InitializeFileRecordSegment` (creation) record is encountered, then progressively updated as subsequent records for the same combined value are replayed. Three categories of history are generated: **data-run history** (the trace of the default and Alternate Data Stream `$DATA` attribute's data-run location over time, generated from `InitializeFileRecordSegment`, `CreateAttribute`, and `UpdateMappingPairs` records — useful for recovering file data at any prior revision, including for applications like Notepad++ that write each save to a new disk location under `CREATE_ALWAYS`); **resident data history** (the trace of small, in-MFT-entry file content over time, from `UpdateResidentValue` records on Windows XP and earlier, or from `DeleteAttribute` records' undo data on Vista and later, since post-Vista redo data for this operation is zeroed — particularly useful for tracking a downloaded file's `Zone.Identifier` alternate-data-stream trace even after a user has manually deleted it); and **event time** (derived by correlating each history event against the nearest `UpdateResidentValue` record that updates the file's `$STANDARD_INFORMATION` Modified Time, before or after the event in question). The data-run history additionally requires event filtering, since a single logical file modification can be represented by multiple sequential `UpdateMappingPairs` records, only the last of which reflects the file's actual final data location for that modification (see [[weaknesses/Simulated MFT-transaction data-run history generation can produce spurious intermediate events not representing the file's actual data location]]).

## Examples

- The freeware NTFS Data Tracker tool, built on the SMT technique, groups the data histories of logically-related files (matched by file name and parent-directory file-reference address) to present the combined history of a file across create/delete/recreate cycles under the same name and location.
- Tracking a file's resident-data history recovered a downloaded file's `Zone.Identifier` mark-of-the-web trace even after a user deleted it via Explorer or PowerShell, confirming the file had originated from the internet.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Simulated MFT-transaction data-run history generation can produce spurious intermediate events not representing the file's actual data location]]

## References

- [LWCite-1319] Oh, Lee, and Hwang, 2021, "NTFS Data Tracker: Tracking file data history based on $LogFile", FSI: Digital Investigation 39, 301309.
