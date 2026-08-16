---
id: DFW-2060
type: weakness
name: Cassandra tombstones and their deletion evidence are permanently destroyed by compaction after the grace period expires
description: A Cassandra tombstone, and the deletion-timing evidence it carries (marked_deleted/local_delete_time), is only retained for the table's configured grace period (ten days by default); once compaction runs after that period, the tombstone and any recoverable trace of the deletion are permanently removed.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2061
source_refs:
  - DFCite-2061
updated_at: 2026-08-15
status: complete
---

# Cassandra tombstones and their deletion evidence are permanently destroyed by compaction after the grace period expires

## Summary

Cassandra's deletion model is time-bounded by design: a tombstone (from an explicit delete or an expired TTL) is written to the SSTable and retained only until its `gc_grace_seconds` grace period elapses, after which compaction physically deletes it. This is a deliberate storage-reclamation mechanism, not a forensic control, so an investigator who does not acquire and analyze the relevant SSTable within the grace window loses the ability to recover the tombstone marker or its `marked_deleted`/`local_delete_time` timestamps entirely.

## Why It Matters

Because Cassandra otherwise lacks native recovery of missing or deleted data, the tombstone-inspection window is the primary opportunity to establish whether, and precisely when, a record was deleted. A delay in acquiring the affected node — whether due to case triage priorities, legal process, or simply not knowing the relevant table's grace-period configuration — can result in permanent, irrecoverable loss of deletion evidence once compaction runs, with no indication left behind that the tombstone ever existed.

## Related Mitigations

- [[mitigations/Acquire and analyze Cassandra SSTable tombstone markers before the configured grace period expires]]

## Used By

- [[techniques/Recover deleted Cassandra records by inspecting SSTable tombstone markers]]

## References

- [DFCite-2061] Bohora, Bothe, Sheth, Chopade & Pachghare, 2021, "Backup and Recovery Mechanisms of Cassandra Database: A Review", JDFSL 15(5). States the default ten-day grace period, its per-table configurability via `cassandra.yaml`, and that compaction permanently deletes the tombstone once the grace period expires; also notes Cassandra "lacks data recovery of missing/deleted data" natively.
