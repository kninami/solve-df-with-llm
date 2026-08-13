---
id: DFM-1218
type: mitigation
name: Flag carved database log records that span file-system cluster boundaries as fragmentation-uncertain
source_refs:
  - DFCite-1229
updated_at: 2026-08-13
status: complete
---

# Flag carved database log records that span file-system cluster boundaries as fragmentation-uncertain

## Summary

When carving unallocated space for transaction log records, compute each candidate record's expected end offset from its declared length and check whether that range crosses a known file-system cluster boundary before trusting its reconstructed content.

## Addresses

- [[weaknesses/MSSQL transaction log record carving fails when a record is fragmented across file-system clusters]]

## How To Apply

After locating a candidate log record via its fixed-length signature, calculate the full record length using the format's own length fields (e.g. `Num Elements`/`RowLog Contents Length`) and compare the resulting byte range against the target volume's cluster size and allocation boundaries. Records that fit entirely within a single cluster can be reconstructed with higher confidence; records whose calculated range crosses into a different, non-adjacent cluster should be reported as fragmentation-uncertain rather than silently reconstructed or silently discarded, so an analyst can decide whether to pursue manual reassembly, cross-check against a live data file, or treat the partial recovery as investigative lead rather than court-ready evidence. Where the volume of candidate signatures is very large relative to the number of records ultimately reconstructable, report both figures (candidates found vs. records fully validated) rather than the candidate count alone.

## References

- [DFCite-1229] Choi and Lee, 2023, "Forensic analysis of SQL server transaction log in unallocated area of file system", DFRWS 2023 APAC; FSI: Digital Investigation 46, 301605.
