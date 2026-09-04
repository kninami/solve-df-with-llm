---
id: LWW-1194
type: weakness
name: Ext4 journal-based file event reconstruction misses events whose pre-change state was overwritten
description: Because the technique identifies a file event by detecting a change between a snapshot's before-and-after state, an event cannot be generated if the pre-change inode or directory-entry data was never written to the journal, or was already overwritten by the journal's circular reuse of space before analysis began.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1194
source_refs:
  - LWCite-1203
updated_at: 2026-08-13
status: complete
---

# Ext4 journal-based file event reconstruction misses events whose pre-change state was overwritten

## Summary

The Ext4 journal is a fixed-size circular buffer: once recording reaches the end of the allocated journal area, new transactions overwrite the oldest ones. If a file or directory existed before journal recording began, and only a subset of its attributes (e.g., mode or flags) changed during the recorded period without the pre-change inode data happening to also be written to the journal for an unrelated reason, no event can be generated for that change, since the algorithm depends on comparing before-and-after snapshots. This limitation is more pronounced in environments with high file system activity or long system uptime, where journal entries are rapidly overwritten; rename and move events, which specifically depend on comparing prior snapshot state, are especially sensitive to this and show reduced reconstruction accuracy under high-activity conditions.

## Why It Matters

An investigator relying solely on this technique's output for a complete file-activity timeline may underestimate the true scope of file system activity during the recorded period, particularly on systems with heavy I/O load or a long uptime since the journal was last flushed. The gap is not visible from the tool's output alone — a missing event looks identical to an event that never occurred, since no changed-state comparison is possible without the earlier snapshot data.

## Related Mitigations

- [[mitigations/Cross-reference Ext4 journal-derived timelines with the orphan inode list and other system logs]]

## Used By

- [[techniques/Reconstruct file events from Ext4 journal transaction replay]]

## References

- [LWCite-1203] Oh, 2026, "Ext4 Log Tracker: An enhanced approach to file event generation from Ext4 journal", FSI: Digital Investigation 58.
