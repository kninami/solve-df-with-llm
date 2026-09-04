---
id: LWW-1144
type: weakness
name: Standard NTFS file readers return only reparse-point stub data for deduplicated files
description: A file system reader or forensic tool that does not specifically handle the NTFS deduplication reparse tag will read only the small $REPARSE_POINT chunk-mapping structure in place of a deduplicated file's original content, missing the file's actual data unless it separately resolves the mapping against the Chunk Store.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1144
source_refs:
  - LWCite-1141
updated_at: 2026-08-12
status: complete
---

# Standard NTFS file readers return only reparse-point stub data for deduplicated files

## Summary

Once Windows Server's Data Deduplication feature processes a file, its `$DATA` attribute is deleted from the MFT entry and replaced with a `$REPARSE_POINT` attribute; a tool that is unaware of the deduplication reparse tag and simply reads the file's attribute list will retrieve this small mapping structure rather than the file's actual content, and analysis results produced this way have a structural limitation the tool itself will not flag.

## Why It Matters

Because the mapping structure's location and format changed between Windows Server 2012 (resident attribute) and Windows Server 2016/2019/2022 (non-resident attribute spanning a data run), a tool or examiner familiar only with the older, simpler resident-attribute case will fail on the newer, more common server versions, and may not realize the returned data is incomplete rather than representative of the file's true content — silently understating the evidence recovered from a deduplication-enabled volume.

## Related Mitigations

- [[mitigations/Resolve NTFS deduplication reparse-point chunk mappings against the Chunk Store before reporting file content]]

## Used By

- [[techniques/Reassemble deduplicated NTFS files with non-resident reparse-point attributes]]

## References

- [LWCite-1141] An, Lee and Han, 2023, "Data reconstruction and recovery of deduplicated files having non-resident attributes in NTFS volume", FSI: Digital Investigation 46.
