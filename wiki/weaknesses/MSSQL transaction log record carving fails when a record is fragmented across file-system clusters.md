---
id: DFW-1218
type: weakness
name: MSSQL transaction log record carving fails when a record is fragmented across file-system clusters
description: Because a deleted transaction log backup file's clusters can be reallocated non-contiguously by the file system, a single log record spanning a cluster boundary may be split across separated, non-adjacent unallocated regions, which signature-based carving of raw unallocated bytes cannot reassemble.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1218
source_refs:
  - DFCite-1229
updated_at: 2026-08-13
status: complete
---

# MSSQL transaction log record carving fails when a record is fragmented across file-system clusters

## Summary

The transaction-log record-carving method's own authors note that reconstruction depends on treating the parity-bit correction bytes as belonging to the log block that contains them and on locating a variable-length record's data contiguously from its signature onward; if the underlying file system (e.g. NTFS, which allocates in clusters) stored the original transaction log backup file fragmented, a single log record can be split across non-adjacent unallocated clusters and the carving method cannot rejoin the pieces.

## Why It Matters

On a large, long-lived production volume, a very large number of byte sequences matched a log-record signature (37 million candidate offsets in one real-world test) but only a small fraction were successfully parsed into complete, reconstructable records, illustrating that cluster fragmentation (compounded by unrelated data occupying intervening unallocated space) sharply limits real-world recovery yield compared to a controlled, less-fragmented test environment; an investigator relying on a raw candidate-offset count as an estimate of recoverable evidence will substantially overstate what can actually be reconstructed.

## Related Mitigations

- [[mitigations/Flag carved database log records that span file-system cluster boundaries as fragmentation-uncertain]]

## Used By

- [[techniques/Carve and reconstruct MSSQL transaction log records from unallocated file-system space]]

## References

- [DFCite-1229] Choi and Lee, 2023, "Forensic analysis of SQL server transaction log in unallocated area of file system", DFRWS 2023 APAC; FSI: Digital Investigation 46, 301605.
