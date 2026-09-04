---
id: LWM-1145
type: mitigation
name: Carve for deduplication mapping remnants and cross-reference recovered chunks against the Chunk Store
source_refs:
  - LWCite-1141
updated_at: 2026-08-12
status: complete
---

# Carve for deduplication mapping remnants and cross-reference recovered chunks against the Chunk Store

## Summary

When a deduplicated file has been deleted, extend deleted-file recovery to include carving unallocated space for remnant `delete.log` entries and `FeRp`/`RbRp`/`DdRp` mapping fragments, then reassemble the file from the ChunkStore's still-present chunks rather than searching only for the file's own cluster runs.

## Addresses

- [[weaknesses/Deleted deduplicated NTFS files are not recovered by standard undelete tools]]

## How To Apply

Search unallocated space and the `System Volume Information\Dedup\ChunkStore\<UID>\Stream` directory's `delete.log` for a deletion transaction record matching the target file, and carve for surviving fragments of its `FeRp`/`RbRp`/`DdRp` structures elsewhere on the volume. Use any recovered ChunkStore UID and stream/chunk identifiers to locate the corresponding chunks in the Data and Stream container files, noting that these chunks commonly remain intact even after the referencing file is deleted, as long as another deduplicated file still shares them. Verify each recovered chunk's hash before reassembly, and treat a partial recovery (some chunks located, others already reclaimed because no other file referenced them) as a valid, documented partial-recovery outcome rather than a total failure.

## References

- [LWCite-1141] An, Lee and Han, 2023, "Data reconstruction and recovery of deduplicated files having non-resident attributes in NTFS volume", FSI: Digital Investigation 46.
