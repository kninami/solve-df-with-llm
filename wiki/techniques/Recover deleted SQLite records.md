---
id: DFT-1006
type: technique
name: Recover deleted SQLite records
description: Recover deleted records from an SQLite database using one of three complementary approaches — metadata-based (freeblock/freelist pointer traversal), carving-based (residual cell structure scanning), or WAL-based (write-ahead log frame parsing) — each trading off coverage, throughput, and resilience to overwriting differently.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1006
  - DFW-1007
  - DFW-1008
aliases:
  - SQLite deleted record recovery
  - metadata-based SQLite recovery
  - freeblock/freelist recovery
  - carving-based SQLite recovery
  - WAL-based SQLite recovery
source_refs:
  - DFCite-1004
updated_at: 2026-08-09
status: complete
---

# Recover deleted SQLite records

## Summary

SQLite does not erase deleted data immediately; depending on the deletion path and journaling mode, remnants persist in one of three places, each recoverable by a distinct technique: page-local freeblock/freelist pointer structures, residual byte patterns in unallocated page space, or historical page images in the write-ahead log. An examiner typically applies multiple approaches together, since each covers cases the others miss.

## Details

**Metadata-based (freeblock/freelist) recovery** follows SQLite's own bookkeeping: a record-level delete links the freed cell into a page-local freeblock chain, while a table drop or B-tree rebalance returns whole pages to a freelist referenced from the file header. This is the fastest approach (pure pointer traversal) but stops working the moment the pointer metadata itself is overwritten.

**Carving-based recovery** scans raw page bytes for recognizable cell structures (varint size/rowid fields, record-header type codes) without relying on any surviving pointer or even the current schema. This gives it the broadest coverage — it can recover data even after the page header and freeblock pointers referencing it are gone — at the cost of being slower (full byte-level scans) and more prone to false positives from coincidentally record-shaped byte sequences.

**WAL-based recovery** parses the separate `.db-wal` file that SQLite writes in Write-Ahead Logging mode: each modified page is captured as a full-page-image frame before being checkpointed into the main database. Because the WAL is a separate, independently-written file, it can recover data that has been deleted, overwritten, or even wiped via SQLite's `secure_delete` pragma in the main file — the only one of the three approaches that can defeat `secure_delete` — but only for the narrow window before the next checkpoint discards it.

## Examples

- Tools such as SQLite Deleted Records Parser and Undark implement freeblock/freelist traversal.
- FQLite reconstructs complete records from residual cell headers and payloads on a page whose own header had already been overwritten (carving-based).
- Recovering a fully `secure_delete`-wiped record from an uncommitted WAL frame (WAL-based).

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/SQLite B-tree rebalancing causes valid data in freelist pages to be misidentified as deleted]]
- [[weaknesses/SQLite carving misattributes reinserted-table records to the wrong table]]
- [[weaknesses/SQLite WAL checkpoint discards deleted data before recovery]]

## References

- [DFCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
