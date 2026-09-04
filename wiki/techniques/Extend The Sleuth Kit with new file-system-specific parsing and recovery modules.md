---
id: LWT-2096
type: technique
name: Extend The Sleuth Kit with new file-system-specific parsing and recovery modules
description: Add support for a file system not natively handled by The Sleuth Kit (TSK) -- such as XFS, Btrfs, F2FS, or a vendor-specific format used by embedded devices like Hikvision DVRs -- by implementing new file-system-specific modules against TSK's internal non-specific/file-system-specific architecture, reverse-engineering the target file system's on-disk structures where public documentation is incomplete, and validating the resulting module's metadata and deleted-file recovery accuracy against ground-truth test images.
objective_ids:
  - DFO-1013
  - DFO-1018
weakness_ids:
  - LWW-2101
aliases:
  - Practical TSK file system add-ons
source_refs:
  - LWCite-2118
updated_at: 2026-08-16
status: complete
---

# Extend The Sleuth Kit with new file-system-specific parsing and recovery modules

## Summary

The Sleuth Kit's internal architecture separates a generic ("non-specific") layer, which every supported file system implements a common interface against, from file-system-specific modules that translate a particular file system's on-disk structures into that common interface -- letting TSK's higher-level tools (timeline generation, file listing, metadata extraction) work uniformly across file systems once a new module is added, without needing to modify TSK's core logic. Extending TSK to cover a file system it does not yet support (e.g. XFS, Btrfs, F2FS, or an embedded-device-specific format) means implementing a new module against this architecture, which requires understanding the target file system's structures well enough to correctly parse them, including for cases where public specification documents are incomplete or absent.

## Details

Where official file-system documentation is unavailable or incomplete (as is common for embedded-device-specific or less-widely-documented formats), the target structures must be reverse-engineered empirically: creating known file-system states, examining the resulting raw bytes, and inferring the structure's layout and semantics from the observed patterns, similar in spirit to the differential-analysis reverse-engineering approach used for PLC memory forensics (see [[techniques/Reverse-engineer a PLC's memory dump to extract control-logic, IO states, and logs using differential analysis]]) but applied to file-system on-disk structures instead. Once a module's parsing logic is implemented, it must be validated against ground-truth test images (files and directories created, deleted, and otherwise manipulated in a controlled environment) to measure metadata-extraction accuracy and, particularly, deleted-file recovery rate, since correctly parsing a file system's live structures does not automatically guarantee correct recovery of its deleted-but-not-yet-overwritten content, which often depends on additional file-system-specific knowledge (e.g. how a given file system marks deletion, and what data survives that marking).

## Examples

- New TSK modules were implemented for XFS, Btrfs, and F2FS (three widely-used Linux file systems not previously supported by TSK), plus a vendor-specific file system used by Hikvision DVR/NVR devices, each validated against constructed ground-truth test images for both live-file metadata accuracy and deleted-file recovery rate.
- F2FS's inline-data feature (small files' content stored directly within their inode rather than in separately-addressed data blocks) and its direct-pointer-referenced files posed a specific recovery challenge distinct from files using F2FS's more standard indirect-block addressing, since the new module's initial deleted-file recovery approach was tuned primarily for standard indirect-block-addressed files.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data
- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/New TSK file-system modules recover inline and direct-pointer-referenced files at a much lower rate than standard indirect-block files]]

## References

- [LWCite-2118] "Towards a practical usage for the Sleuth Kit supporting file system add-ons", FSI: Digital Investigation 48, 2024.
