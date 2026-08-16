---
id: DFT-2092
type: technique
name: Recover fragmented filesystem metadata using prefix-based generic metadata time carving
description: Recover filesystem metadata records (e.g. NTFS $MFT entries, Ext4 inodes) from a disk image without relying on file signatures, by searching for approximately-equivalent, closely co-located candidate timestamps using a sliding-window byte search that only requires the most-significant bytes (the prefix) of candidate timestamps to match rather than requiring exact equivalence, then verifying each surviving candidate location against a filesystem-specific parser.
objective_ids:
  - DFO-1018
  - DFO-1002
weakness_ids:
  - DFW-2096
aliases:
  - Prefix-based Generic Metadata Time Carving
  - Prefix matching potential timestamp carving
source_refs:
  - DFCite-2113
updated_at: 2026-08-16
status: complete
---

# Recover fragmented filesystem metadata using prefix-based generic metadata time carving

## Summary

Generic Metadata Time Carving (GMTC) recovers filesystem metadata records by searching a disk image for closely co-located, byte-identical candidate timestamps (since filesystem metadata records typically store several timestamps consecutively, and many update simultaneously during a single file operation), then verifying each candidate location with a filesystem-specific parser -- an approach that does not depend on file signatures and so works even where signature-based file carving would fail. This technique extends GMTC's exact-match timestamp equivalence test to an approximate, prefix-based match, substantially increasing the recall of recovered metadata records by also finding records whose co-located timestamps are similar but not byte-identical, with little to no reduction in precision.

## Details

The underlying GMTC search uses a sliding window over the disk image's byte stream: for a chosen timestamp length `m` (4 or 8 bytes) and search-window length `k`, every non-overlapping `m`-byte sequence is treated as a candidate timestamp and compared against every `m`-byte sequence within the following `k`-byte window (the test sequences); if at least `h-1` matches are found, the location is recorded as a potential timestamp. The original method requires each test sequence to exactly equal the candidate timestamp; the prefix-based extension instead requires only the candidate's `p` most-significant bytes (its prefix -- typically the portion of a timestamp least likely to change on a minor update, such as the year and month) to match the same prefix length of each test sequence, computed efficiently via an XOR-and-bit-shift operation on the timestamps' big-endian integer form. Once potential timestamp locations are identified, they are fed to an existing filesystem-specific parser (NTFS or Ext4) that checks the surrounding bytes against known metadata-record structure (e.g. Standard Information Attribute or Filename Attribute header flags for NTFS; inode filetype/extent validity checks for Ext4) to confirm or reject each candidate as an actual metadata record, recovering the record's full metadata (including resident file content and Data Attribute extents/block pointers where present) once confirmed. Reducing the prefix length `p` increases recall (more real records found) at the cost of generating more false-positive candidate timestamps for the filesystem-specific parser to reject, and increases the computational time the parser stage requires accordingly, since the underlying timestamp-carving stage's own time complexity is unaffected by the prefix length.

## Examples

- On a 476 GB real-world NTFS forensic image, exact-match GMTC recovered only 41.6% of $MFT records (Recall), while prefix-based matching with `p=2` recovered 97.2% of $MFT records, and $LogFile record recall hovered around 87% across all tested prefix lengths -- both achieved with 100% precision throughout (no false positives were produced by the filesystem-specific parser at any tested prefix length).
- On a 59.5 GB real-world Ext4 image (a Samsung S8 phone dump), reducing the prefix length from `p=4` to `p=1` increased inode-table recall from 91.0% to 94.2%, again with 100% precision maintained throughout.
- Runtime scaled predictably with prefix length: for the large NTFS image, reducing `p` from 8 to 1 increased the number of potential timestamp locations found by roughly a factor of 4.77 and increased filesystem-parser runtime correspondingly, while the underlying timestamp-carving stage's own runtime stayed effectively constant across all tested prefix lengths, since its time complexity depends only on image size, not prefix length.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats
- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Exact-match generic metadata time carving misses filesystem metadata records with similar but non-identical co-located timestamps]]

## References

- [DFCite-2113] Porter, Nordvik, Toolan, and Axelsson, 2021, "Timestamp prefix carving for filesystem metadata extraction", FSI: Digital Investigation 38, 301266.
