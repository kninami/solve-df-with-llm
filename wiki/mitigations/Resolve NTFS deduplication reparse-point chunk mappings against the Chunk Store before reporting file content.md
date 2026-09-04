---
id: LWM-1144
type: mitigation
name: Resolve NTFS deduplication reparse-point chunk mappings against the Chunk Store before reporting file content
source_refs:
  - LWCite-1141
updated_at: 2026-08-12
status: complete
---

# Resolve NTFS deduplication reparse-point chunk mappings against the Chunk Store before reporting file content

## Summary

Before reporting the content of any file on an NTFS volume with Data Deduplication enabled, check whether its MFT entry carries the deduplication reparse tag (`0x80000013`) and, if so, fully resolve the resident or non-resident `$REPARSE_POINT` mapping against the `System Volume Information\Dedup\ChunkStore` structures rather than treating the reparse-point data as the file's content.

## Addresses

- [[weaknesses/Standard NTFS file readers return only reparse-point stub data for deduplicated files]]

## How To Apply

First identify the Windows Server version in use (resident $REPARSE_POINT on Server 2012; non-resident on Server 2016, 2019, and 2022), since this determines whether the mapping data is read directly from the MFT entry or requires following a data run. Use the `$Reparse:$R` index file to efficiently enumerate deduplicated MFT entries rather than scanning the entire $MFT. For each entry, parse the `FeRp`/`RbRp`/`DdRp` structure chain to obtain the ChunkStore UID and per-stream mapping, then read and hash-verify the referenced chunks from the ChunkStore's `Stream` and `Data` container files before assembling and reporting the reconstructed file content.

## References

- [LWCite-1141] An, Lee and Han, 2023, "Data reconstruction and recovery of deduplicated files having non-resident attributes in NTFS volume", FSI: Digital Investigation 46.
