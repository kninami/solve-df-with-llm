---
id: LWT-1141
type: technique
name: Reassemble deduplicated NTFS files with non-resident reparse-point attributes
description: Reconstruct the original content of a file deduplicated by Windows Server's Data Deduplication feature by parsing its MFT entry's $REPARSE_POINT attribute — resident on Windows Server 2012 but non-resident (spanning a data run) on Windows Server 2016, 2019, and 2022 — to recover the chunk-mapping structures needed to reassemble the file from the Chunk Store.
objective_ids:
  - DFO-1013
weakness_ids:
  - LWW-1144
aliases:
  - NTFS deduplicated file reassembly
  - Windows Server deduplication reparse-point reconstruction
source_refs:
  - LWCite-1141
updated_at: 2026-08-12
status: complete
---

# Reassemble deduplicated NTFS files with non-resident reparse-point attributes

## Summary

The NTFS Data Deduplication feature removes duplicated content by splitting a file into variable-length chunks (identified with the Rabin fingerprint algorithm) and storing each unique chunk once in a `ChunkStore` directory under `System Volume Information\Dedup`; the original file's `$DATA` attribute is replaced with a `$REPARSE_POINT` attribute that records the mapping needed to reassemble the chunks. Prior published methodology covered only Windows Server 2012, where this attribute is resident (stored directly in the MFT entry); from Windows Server 2016 onward it is non-resident, spread across a data run, and requires parsing an additional layer of chained structures to recover the same mapping.

## Details

Reassembly requires identifying the deduplicated file's MFT entry via its `$REPARSE_POINT` attribute (type ID `0x0000000C`, deduplication reparse tag `0x80000013`), then, for the non-resident case, walking the attribute's data run to collect the mapping data spread across one or more clusters. That mapping data is organized as a chain of three structures — a `FeRp` header (recording the original file's creation time, original size, and the ChunkStore UID that identifies which chunk store holds its data), a `RbRp` structure, and a `DdRp` structure (recording, per stream, the stream file's location and a hash of the stream used to validate the reassembly) — which together point into the `ChunkStore\<UID>\Stream` and `\Data` directories' `.ccc`/`.cd` container files where the actual chunk content and per-chunk hashes are stored. The `$Reparse:$R` index file (MFT entry 26) provides an efficient way to enumerate only the MFT entries that have a `$REPARSE_POINT` attribute, avoiding an inefficient full-$MFT scan. Reassembly should verify each recovered chunk against its recorded hash before writing it into the reconstructed output file, since chunks are shared across multiple deduplicated files and an incorrect chunk resolution silently corrupts the reassembled content rather than failing outright.

## Examples

- Recombining a Windows Server 2019 deduplicated file by resolving its non-resident `$REPARSE_POINT` attribute's data run into `FeRp`/`RbRp`/`DdRp` structures, then reading the referenced `.ccc` stream and data container files from the `ChunkStore` to reproduce the original file byte-for-byte.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data

## Related Weaknesses

- [[weaknesses/Standard NTFS file readers return only reparse-point stub data for deduplicated files]]

## References

- [LWCite-1141] An, Lee and Han, 2023, "Data reconstruction and recovery of deduplicated files having non-resident attributes in NTFS volume", FSI: Digital Investigation 46.
