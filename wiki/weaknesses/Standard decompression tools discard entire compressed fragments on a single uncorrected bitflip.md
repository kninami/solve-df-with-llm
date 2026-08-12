---
id: DFW-1024
type: weakness
name: Standard decompression tools discard entire compressed fragments on a single uncorrected bitflip
description: Off-the-shelf decompression utilities treat any bitflip-corrupted compressed fragment as entirely unrecoverable and simply fail or skip it, even though most such fragments contain only a single-bit error and the vast majority of their underlying data is intact and could be recovered with targeted repair.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1024
source_refs:
  - DFCite-1016
updated_at: 2026-08-09
status: complete
---

# Standard decompression tools discard entire compressed fragments on a single uncorrected bitflip

## Summary

Standard tooling (e.g., `squashfs-tools`) simply reports a decompression failure for any fragment whose compressed bytes have been altered, with no attempt at partial recovery or error correction, because general-purpose compression tools are not designed to expect or tolerate corrupted input.

## Why It Matters

In a documented case, `squashfs-tools` alone recovered only 8.32% of a corrupted filesystem's total decompressed data (9,806,355 of 117,873,827 bytes), even though the underlying storage medium's actual bitflip rate was low enough that the overwhelming majority of data was, in principle, recoverable with proper handling. An investigator relying solely on standard tooling would significantly under-recover evidence from any storage medium exhibiting even a very low rate of natural bitflip corruption, without any indication that far more data was theoretically recoverable.

## Related Mitigations

- [[mitigations/Apply oracle-based bitflip search and repair before treating a corrupted compressed dump as unreadable]]

## Used By

- [[techniques/Repair compressed forensic filesystem images using statistical bitflip correction]]

## References

- [DFCite-1016] Barral et al., 2022, "A forensic analysis of the Google Home: repairing compressed data without error correction", FSI: Digital Investigation 42-43.
