---
id: LWM-1006
type: mitigation
name: Cross-check SQLite freelist-page records against active table contents
source_refs:
  - LWCite-1004
  - LWCite-1268
updated_at: 2026-08-14
status: complete
---

# Cross-check SQLite freelist-page records against active table contents

## Summary

Before reporting a record recovered from a freelist page as "deleted," compare it against the database's current live table contents; if the record is still present, it was relocated by B-tree rebalancing rather than deleted, and should not be reported as recovered deleted data.

## Addresses

- [[weaknesses/SQLite B-tree rebalancing causes valid data in freelist pages to be misidentified as deleted]]

## How To Apply

After extracting candidate records from freelist pages via freeblock/freelist traversal, run each recovered record's key fields against a full scan of the database's currently active tables. Records that match live rows should be excluded from the "deleted records" findings and instead noted as artifacts of B-tree rebalancing, since only records absent from the live tables represent genuinely deleted data. Where the target table's record layout is known (e.g. from prior schema documentation or reverse engineering), additionally validate each freelist candidate's own field values for structural plausibility — for example, checking that a known boolean/flag field falls within its documented value range — before accepting it as a recovered record; this schema-aware check both filters coincidentally record-shaped garbage bytes and recovers partially-overwritten candidates that pure pointer-membership checks alone would discard.

## References

- [LWCite-1004] Lee et al., 2025, "A comprehensive analysis and evaluation of SQLite deleted Record recovery techniques: A survey", FSI: Digital Investigation 55.
- [LWCite-1268] Wu, Breitinger and Baggili, 2026, "I know where you have been last summer: Extracting privacy-sensitive information via forensic analysis of the Mercedes-Benz NTG5/2 infotainment system", FSI: Digital Investigation 56, 302068. NTGCarver validates freelist candidates against a known "valid" flag field before accepting them, outperforming generic recovery tools on the same table.
