---
id: DFM-2061
type: mitigation
name: Acquire and analyze Cassandra SSTable tombstone markers before the configured grace period expires
source_refs:
  - DFCite-2061
updated_at: 2026-08-15
status: complete
---

# Acquire and analyze Cassandra SSTable tombstone markers before the configured grace period expires

## Summary

Prioritize acquisition and `sstabledump` analysis of a suspected node's Cassandra tables as soon as possible after identifying a relevant deletion, and check the affected table's `gc_grace_seconds` setting in `cassandra.yaml` to know exactly how much time remains before compaction permanently removes tombstone evidence.

## Addresses

- [[weaknesses/Cassandra tombstones and their deletion evidence are permanently destroyed by compaction after the grace period expires]]

## How To Apply

As soon as a Cassandra data store is identified as potentially relevant evidence, check each in-scope table's `gc_grace_seconds` value in `cassandra.yaml` to establish the remaining recovery window, and prioritize imaging or otherwise capturing that node ahead of any pending compaction (default retention is ten days but is table-configurable, so verify rather than assume). Where possible, take a `nodetool snapshot` and generate an `sstabledump` promptly to preserve `deletion_info` markers and their `marked_deleted`/`local_delete_time` timestamps before they can be reclaimed.

## References

- [DFCite-2061] Bohora, Bothe, Sheth, Chopade & Pachghare, 2021, "Backup and Recovery Mechanisms of Cassandra Database: A Review", JDFSL 15(5). Documents the `gc_grace_seconds` configuration point and the `nodetool`/`sstabledump` acquisition workflow that this mitigation relies on.
