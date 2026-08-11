---
id: DFW-1006
type: weakness
name: SQLite B-tree rebalancing causes valid data in freelist pages to be misidentified as deleted
description: When SQLite merges two B-tree pages during rebalancing, the still-valid records copied to the surviving page are placed on the freelist along with genuinely deleted records, causing recovery tools that trust freelist-page membership to report valid, non-deleted data as recovered deleted data.
categories:
  - ASTM_INAC_EX
  - ASTM_MISINT
mitigation_ids:
  - DFM-1006
source_refs:
  - DFCite-1004
updated_at: 2026-08-09
status: complete
---

# SQLite B-tree rebalancing causes valid data in freelist pages to be misidentified as deleted

## Summary

SQLite triggers a page merge when invalidated data occupies more than two-thirds of a page's cells, consolidating the remaining valid data from two pages into one and adding the emptied page(s) to the freelist. A recovery tool that assumes every record found within a freelist page is deleted will incorrectly report records that were valid immediately prior to the merge -- and were simply relocated, not deleted -- as recovered deleted data.

## Why It Matters

This is a structural false-positive source distinct from ordinary deletion: in a documented example, 10 of 20 records in a page were genuinely deleted (records 1-6 and 18-20), but after rebalancing merged the page into the freelist, a naive freelist-based recovery tool reported all 20 records as deleted. Investigators relying on freelist-based recovery without cross-checking against the database's current live contents risk overstating what data was actually removed, which can distort a reconstructed timeline of record deletions.

## Related Mitigations

- [[mitigations/Cross-check SQLite freelist-page records against active table contents]]

## Used By

- [[techniques/SQLite deleted record recovery]]

## References

- [DFCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
