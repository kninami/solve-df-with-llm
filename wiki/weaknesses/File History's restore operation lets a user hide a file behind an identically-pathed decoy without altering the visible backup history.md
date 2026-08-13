---
id: DFW-1221
type: weakness
name: File History's restore operation lets a user hide a file behind an identically-pathed decoy without altering the visible backup history
description: Because File History's Previous-Versions restore feature matches a file to its backups purely by full path, a user can back up a sensitive file, delete it, create an innocuous file at the same path, back that up too, and then deliberately restore the original sensitive version — leaving the decoy visible in the file system while the sensitive content sits, unindicated, in the same backup slot.
categories:
  - ASTM_INAC_AS
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1221
source_refs:
  - DFCite-1233
updated_at: 2026-08-13
status: complete
---

# File History's restore operation lets a user hide a file behind an identically-pathed decoy without altering the visible backup history

## Summary

Because File History's Previous Versions feature determines which backups belong to a given file solely by matching the file's current full path, restoring an older backed-up version over a newer file that happens to share the same name and location succeeds silently, with the restored (original) file's `Catalog.edb` record reusing the same `fileRecordId` as the decoy file it replaces, distinguished only by a different `fileCreated` value in the `namespace` table.

## Why It Matters

An investigator who only inspects the currently visible file at a given path, or who inspects `Catalog.edb` without checking for multiple `namespace` records sharing the same `childId`/`parentId` pair but different `fileCreated` timestamps, can be misled into believing the visible decoy file is the only content that was ever backed up at that location, missing the deliberately hidden original file's existence and content entirely — a misattribution of what is present at that path versus what the backup history actually recorded there.

## Related Mitigations

- [[mitigations/Compare backup-catalog records sharing the same file identity for mismatched creation timestamps to detect restore-based file hiding]]

## Used By

- [[techniques/Reconstruct Windows File History backup and restore activity across host and backup storage devices]]

## References

- [DFCite-1233] Choi, Park and Lee, 2021, "Forensic exploration on windows File History", FSI: Digital Investigation 36, 301134.
