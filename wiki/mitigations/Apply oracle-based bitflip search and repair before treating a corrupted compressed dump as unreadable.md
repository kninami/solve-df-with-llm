---
id: DFM-1024
type: mitigation
name: Apply oracle-based bitflip search and repair before treating a corrupted compressed dump as unreadable
source_refs:
  - DFCite-1016
updated_at: 2026-08-09
status: complete
---

# Apply oracle-based bitflip search and repair before treating a corrupted compressed dump as unreadable

## Summary

Before writing off a corrupted gzip/LZMA-compressed forensic dump as unreadable based on a standard decompression tool's failure, estimate the storage medium's bitflip rate from the fraction of corrupted fragments and attempt a targeted single/double-bitflip repair pass validated by a decompression oracle.

## Addresses

- [[weaknesses/Standard decompression tools discard entire compressed fragments on a single uncorrected bitflip]]

## How To Apply

See [[techniques/Statistical bitflip repair of compressed forensic filesystem images]] for the full method: estimate the bitflip rate from the observed corrupted-fragment count, generate single-bitflip (then, if needed, double-bitflip) repair candidates for each corrupted fragment, and validate each candidate with checksum, decompressed-length, and successful-inflate checks before accepting it as repaired. Where independent file-length metadata (e.g., an inode table) is available, use it to further filter valid candidates. This is worth attempting whenever the corruption is suspected to stem from natural storage bitflips (block/stream compression on flash media) rather than intentional data destruction, which would not exhibit the same sparse, low-rate error pattern.

## References

- [DFCite-1016] Barral et al., 2022, "A forensic analysis of the Google Home: repairing compressed data without error correction", FSI: Digital Investigation 42-43.
