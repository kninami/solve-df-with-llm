---
id: LWT-2060
type: technique
name: Recover deleted Cassandra records by inspecting SSTable tombstone markers
description: Identify recently deleted records in an Apache Cassandra NoSQL database by dumping an SSTable and examining its `deletion_info` tombstone markers, which retain the deleted record's key and the timestamps at which deletion was requested and processed, until the configured grace period expires and compaction removes them.
objective_ids:
  - DFO-1018
weakness_ids:
  - LWW-2060
aliases:
  - Cassandra tombstone analysis
source_refs:
  - LWCite-2061
updated_at: 2026-08-15
status: complete
---

# Recover deleted Cassandra records by inspecting SSTable tombstone markers

## Summary

Cassandra does not delete a record immediately; it marks the record with a tombstone (either from an explicit delete command or an expired time-to-live value) and only physically removes it once the tombstone's grace period has expired and compaction runs. An analyst can install `cassandra-tools`, use `nodetool` to create a snapshot, and generate an `sstabledump` to inspect the raw SSTable event log for `deletion_info` markers that indicate a record has been (or is scheduled to be) deleted.

## Details

Two distinct deletion methods each result in a tombstone: (1) an explicit delete command adds a tombstone directly to the targeted record, or (2) a record marked with a time-to-live (TTL) value receives a tombstone once that TTL expires. Either way, the tombstone is written to the SSTable, and only after the grace period (`gc_grace_seconds` in the table's configuration, ten days by default, but configurable per table in `cassandra.yaml`) elapses does compaction physically delete the tombstoned data. The `deletion_info` marker in an `sstabledump` output for a tombstoned partition carries two timestamps: `marked_deleted`, set by the user/application at the time deletion was requested, and `local_delete_time`, set by the Cassandra server at the time it processed the request — together letting an analyst reconstruct both when a deletion was requested and when the node actually recorded it, similarly to how deleted-record recovery is approached for other structured/log-structured stores.

## Examples

- Running `nodetool snapshot` followed by `sstabledump` against a Cassandra table under investigation to locate `deletion_info` markers and recover the `marked_deleted`/`local_delete_time` timestamps for a record a suspect claims was never deleted, or to establish exactly when a deletion occurred.
- Consulting a table's `cassandra.yaml` `gc_grace_seconds` value to determine how much time remains before a given tombstone (and the underlying deleted data it still references) is permanently removed by compaction.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Cassandra tombstones and their deletion evidence are permanently destroyed by compaction after the grace period expires]]

## References

- [LWCite-2061] Bohora, Bothe, Sheth, Chopade & Pachghare, 2021, "Backup and Recovery Mechanisms of Cassandra Database: A Review", JDFSL 15(5). Describes Cassandra's two deletion methods, the tombstone/grace-period/compaction lifecycle, and the `sstabledump`-based `deletion_info` inspection procedure with `marked_deleted` and `local_delete_time` timestamps.
