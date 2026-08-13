---
id: DFW-1145
type: weakness
name: Deleted deduplicated NTFS files are not recovered by standard undelete tools
description: A deleted-file-recovery tool that assumes a file's data lives in its own cluster runs will fail to recover a deleted deduplicated file, because the file's content is instead split across chunks shared with other files in the Chunk Store, and the mapping information needed to locate and reorder those chunks is not carved by traditional recovery methods.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1145
source_refs:
  - DFCite-1141
updated_at: 2026-08-12
status: complete
---

# Deleted deduplicated NTFS files are not recovered by standard undelete tools

## Summary

Traditional deleted-file recovery techniques assume a one-to-one relationship between a deleted file and the disk sectors that held its content, and either scan for the file's own now-unallocated cluster runs or carve for file-type-specific signatures within unallocated space. Neither approach accounts for deduplication's indirection: a deleted deduplicated file's chunks are stored, shared, and referenced elsewhere in the Chunk Store, so the deleted file's data may still be entirely present and undamaged on disk while remaining completely invisible to a recovery method that never looks there.

## Why It Matters

An examiner running a standard undelete or carving pass against a deduplication-enabled Windows Server volume may report a deleted file as unrecoverable when its content is, in fact, still on disk in full, simply because the recovery tool does not know to carve for and resolve deduplication-specific mapping structures (`delete.log`, `FeRp`/`RbRp`/`DdRp` remnants) rather than the file's own cluster runs.

## Related Mitigations

- [[mitigations/Carve for deduplication mapping remnants and cross-reference recovered chunks against the Chunk Store]]

## Used By

- [[techniques/Recover deleted deduplicated NTFS files using chunk-store reconstruction]]

## References

- [DFCite-1141] An, Lee and Han, 2023, "Data reconstruction and recovery of deduplicated files having non-resident attributes in NTFS volume", FSI: Digital Investigation 46.
