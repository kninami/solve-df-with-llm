---
id: LWW-2101
type: weakness
name: New TSK file-system modules recover inline and direct-pointer-referenced files at a much lower rate than standard indirect-block files
description: A newly implemented file-system-specific module's deleted-file recovery approach, tuned primarily for a file system's standard indirect-block file-addressing structures, recovers files stored via alternative addressing mechanisms -- such as F2FS's inline-data feature or direct-pointer referencing -- at a substantially lower rate, since these alternative structures are not laid out or discoverable the same way as standard indirect-block files.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2102
source_refs:
  - LWCite-2118
updated_at: 2026-08-16
status: complete
---

# New TSK file-system modules recover inline and direct-pointer-referenced files at a much lower rate than standard indirect-block files

## Summary

F2FS's inline-data feature stores a small file's content directly within its inode structure rather than in separately-addressed data blocks, and some files use direct pointer referencing rather than F2FS's more common indirect-block addressing; both cases require different recovery logic than the indirect-block-addressed files a new module's recovery approach is typically developed and validated against first, and testing against ground-truth images confirmed these alternative-addressing files were recovered at a markedly lower rate than standard files.

## Why It Matters

An investigator relying on a new file-system module's overall deleted-file recovery statistics without distinguishing file-storage-addressing type risks understating how much relevant deleted content actually remains unrecoverable for a given case, particularly for small files (which F2FS is more likely to store inline) that could nonetheless be highly relevant, such as short text-based artifacts or configuration snippets. Because a module's initial validation testing may not have proportionally represented inline and direct-pointer-referenced files in its test corpus, the true achievable recovery rate for this file category in a real case may differ further still from any published aggregate figure.

## Related Mitigations

- [[mitigations/Manually carve or separately handle inline and direct-pointer-referenced files a generic file-system recovery module fails to recover]]

## Used By

- [[techniques/Extend The Sleuth Kit with new file-system-specific parsing and recovery modules]]

## References

- [LWCite-2118] "Towards a practical usage for the Sleuth Kit supporting file system add-ons", FSI: Digital Investigation 48, 2024.
