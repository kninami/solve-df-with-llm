---
id: DFT-1187
type: technique
name: Reconstruct file events from Ext4 journal transaction replay
description: Replay Ext4 journal transactions to rebuild file, directory, and directory-entry snapshots, then derive precise event times from transaction commit timestamps and full file paths by tracing parent-directory inode chains, producing a clear, time- and path-annotated timeline of file creation, deletion, renaming, movement, and modification events.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1194
aliases:
  - Simulation of Ext4 Transaction (SET)
  - Ext4 Log Tracker
source_refs:
  - DFCite-1203
updated_at: 2026-08-13
status: complete
---

# Reconstruct file events from Ext4 journal transaction replay

## Summary

The Ext4 file system's journal records metadata changes for file system operations (creation, deletion, renaming, movement) in ordered transactions to support crash recovery, and by systematically replaying these transactions an investigator can reconstruct a detailed file-event timeline even after the events are no longer visible on the live file system. Earlier tools generated file events from the same journal data but omitted event timestamps and full paths, limiting their practical use; replaying transactions to build snapshots and deriving both time and path for each event overcomes this.

## Details

The core technique, termed Simulation of Ext4 Transaction (SET), processes journal transaction block groups sequentially, combining directory-entry and inode block data within each transaction into file/directory snapshots (keyed by inode number) and directory-entry snapshots (keyed by disk block address); only the most recent snapshot per key is retained to bound memory use as more transactions are processed. Event *time* is bounded using an "Event Time Condition": since a transaction's commit block records its completion time, an event generated within that transaction must have occurred strictly after the immediately preceding transaction's commit time and no later than the current transaction's commit time (with a special case using the maximum observed inter-transaction interval to estimate a virtual preceding commit time for the very first transaction, and a preceding/following commit-time window for transactions that end in a revocation block rather than a commit block). Event *paths* are derived by first building a directory-inode-to-name map from the current live file system tree, then tracing each event's parent-directory inode back to the root; if the parent directory no longer exists in the live tree (because it too was deleted), the trace falls back to the maintained set of snapshot data to continue path reconstruction from a deleted ancestor. Comparing directory-entry and inode snapshots across consecutive transactions distinguishes creation, rename, move, and deletion events (which change both a directory entry and its inode) from modification, access, mode/flag-change, timestamp-manipulation, and extended-attribute events (which change only inode data without an accompanying directory-entry change).

## Examples

- The Ext4 Log Tracker tool, implementing this algorithm, was compared against two existing Ext4-journal-based file-event tools (FJTA and exhume_extfs) and produced timelines with explicit event times and full paths that both prior tools lacked, along with additional event types (e.g., rename and move) that exhume_extfs did not identify at all.
- Applied to an intrusion-incident scenario, the technique reconstructed the full sequence of a backdoor rootkit's file creation, movement, and concealment activity from journal data alone, enabling identification of the initial compromise vector.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Ext4 journal-based file event reconstruction misses events whose pre-change state was overwritten]]

## References

- [DFCite-1203] Oh, 2026, "Ext4 Log Tracker: An enhanced approach to file event generation from Ext4 journal", FSI: Digital Investigation 58.
