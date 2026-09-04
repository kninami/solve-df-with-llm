---
id: LWW-1007
type: weakness
name: SQLite carving misattributes reinserted-table records to the wrong table
description: When a table is dropped and a new table with the same schema is later created and populated, carving-based recovery of residual unallocated-area records cannot reliably distinguish which table's data a recovered record originally belonged to, because schema similarity alone is insufficient evidence.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-1007
source_refs:
  - LWCite-1004
updated_at: 2026-08-09
status: complete
---

# SQLite carving misattributes reinserted-table records to the wrong table

## Summary

Carving-based recovery locates residual cell structures in unallocated space by structural signature alone, without reference to schema or metadata. When a dropped table's invalidated records remain in unallocated space and a new table with an identical column structure is subsequently created, carving cannot conclusively determine whether a recovered record belonged to the original (deleted) table or is unrelated residual data, since both would share the same schema shape.

## Why It Matters

In an evaluated case, a "Student List for 2024" table was dropped and a "Student List for 2025" table with the same schema was created; carving-based recovery correctly found 5 residual records but misattributed some of them to the wrong table generation. Reporting deleted records as belonging to the wrong table (or the wrong point in time) can mislead an investigation's event reconstruction, particularly where the distinction between "old deleted data" and "new live data" matters for establishing what existed at a given moment.

## Related Mitigations

- [[mitigations/Verify SQLite recovered records against RowID continuity and table timestamps]]

## Used By

- [[techniques/Recover deleted SQLite records]]

## References

- [LWCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
