---
id: LWT-1142
type: technique
name: Recover deleted deduplicated NTFS files using chunk-store reconstruction
description: Recover the content of a deleted, deduplicated NTFS file by carving unallocated space for remnants of its $REPARSE_POINT chunk-mapping structures and cross-referencing the recovered chunk identifiers against the Chunk Store, since a deduplicated file's chunks remain allocated (and are not zeroed or reclaimed) as long as any other file still references them, even after the file itself is deleted.
objective_ids:
  - DFO-1013
weakness_ids:
  - LWW-1145
aliases:
  - Deleted deduplicated file recovery
source_refs:
  - LWCite-1141
updated_at: 2026-08-12
status: complete
---

# Recover deleted deduplicated NTFS files using chunk-store reconstruction

## Summary

When a deduplicated NTFS file is deleted, the file system's chunk-sharing model diverges from the behavior a traditional deleted-file-recovery tool expects: the file's MFT entry and cluster runs become available for reuse in the normal way, but each of the file's constituent chunks in the Chunk Store remains allocated for as long as any other still-existing deduplicated file references it, and the deletion is separately logged in a `delete.log` file in the Stream directory rather than by simply marking clusters free.

## Details

Because the original file's `$REPARSE_POINT` mapping structures (and its MFT entry) may themselves be overwritten or reused once the file is deleted, direct reassembly via the live-file method is often not possible. The paper's proposed recovery process instead: (1) carves unallocated space for remnant fragments of the deleted file's `FeRp`/`RbRp`/`DdRp` mapping structures or of its entry in `delete.log`, which records the deletion transaction; (2) uses any recovered ChunkStore UID and stream identifiers to locate the corresponding stream and data container files (`.ccc`/`.cd`) that are still present in the ChunkStore, since those chunks may still be live if referenced elsewhere; and (3) reassembles the file's original content from the recovered chunks using whatever offset/runlist information could be carved or reconstructed. This differs fundamentally from traditional file recovery, where a deleted file's data blocks are recovered directly; here, the data blocks (chunks) are frequently still intact and allocated regardless of the specific file's deletion, but the mapping information that ties them back together in the correct order is what must be recovered.

## Examples

- Carving a `delete.log` entry and remnant reparse-point mapping fragments for a deleted deduplicated file, then reassembling its content from chunks still present (and still referenced by other files) in the ChunkStore's Stream and Data container files.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data

## Related Weaknesses

- [[weaknesses/Deleted deduplicated NTFS files are not recovered by standard undelete tools]]

## References

- [LWCite-1141] An, Lee and Han, 2023, "Data reconstruction and recovery of deduplicated files having non-resident attributes in NTFS volume", FSI: Digital Investigation 46.
