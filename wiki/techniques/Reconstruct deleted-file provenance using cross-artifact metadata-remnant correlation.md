---
id: DFT-1048
type: technique
name: Reconstruct deleted-file provenance using cross-artifact metadata-remnant correlation
description: Establish that a specific file existed on a system, its original path, and an approximate window for when it was accessed or deleted, by systematically searching OS and application artifacts that independently retain file-related metadata (thumbnail caches, recent-files history, Trash records, search-index journals, application logs and registration databases) and cross-correlating whichever of them still hold a matching trace, even after the original file itself is no longer recoverable through ordinary file-system analysis or carving.
objective_ids:
  - DFO-1017
weakness_ids:
  - DFW-1049
  - DFW-1176
aliases:
  - Linux thumbnail-cache and recent-files provenance reconstruction for deleted files
  - Discovering spoliation of evidence through deleted-file traces (macOS)
  - Spoliation trace analysis
source_refs:
  - DFCite-1039
  - DFCite-1176
updated_at: 2026-08-12
status: complete
---

# Reconstruct deleted-file provenance using cross-artifact metadata-remnant correlation

## Summary

Many operating-system and application components independently record a file's path, name, content fragment, or timestamp as a side effect of normal use — separately from the file's own on-disk lifecycle — so a deleted file that is no longer recoverable by carving or file-system analysis can still often be shown to have existed, and roughly when it was deleted, by finding and cross-referencing whichever of these independent metadata remnants survive.

## Details

On Linux desktop environments following the freedesktop.org thumbnail-management specification (GNOME/Nautilus and similar), a cached preview thumbnail persists independently of its originating file and embeds the original path and modification time; correlating it with recent-files history (e.g. a `recently-used.xbel` bookmark file) and Trash metadata (original path and deletion time) gives up to three independent, cross-referencing provenance sources for one deleted file. On macOS, a systematic keyword-driven methodology — performing a defined set of user actions (create, access, modify, copy, up/download, and other operations) on test files, then searching all system and application artifacts for the resulting filenames and content as keywords — identified several previously unanalyzed "spoliation trace" sources beyond the well-known Spotlight `store.db` search index: `parsecd` (a Spotlight-related temp log storing deleted filenames with or without extension), `JournalAttr` (a Spotlight indexing journal storing deleted filename and metadata temporarily during iCloud upload/download), and, for Microsoft Office documents, the `ComRPCDB` SQLite database (embedded-object filename/path plus creation time, including WAL-recoverable deleted entries), the `MicrosoftRegistrationDB` registration database (filename, path, and timestamp for created/downloaded files), and per-application `.plist` preference files (recently-accessed filename and path). This general approach — enumerate candidate metadata-retaining artifacts for the target OS/application stack, classify each as previously studied, known-but-unanalyzed, or genuinely unknown, and search all of them by keyword — is explicitly proposed as OS-agnostic and adaptable beyond the specific artifacts documented for any one platform.

## Examples

- Correlating a Linux thumbnail-cache entry's embedded original-path metadata with a matching Trash record for the same path and a nearby recent-files access timestamp establishes that a specific image file existed at a specific location and was subsequently deleted within a bounded time window.
- On macOS, a deleted Word document's embedded-object metadata recovered from `ComRPCDB` (and its `-wal` file, for entries not yet checkpointed) was cross-referenced against the same filename appearing in `MicrosoftRegistrationDB` and in Spotlight's `JournalAttr`, corroborating that the file existed and had been synced via iCloud before deletion.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/Linux thumbnail cache entries are subject to size-based eviction]]
- [[weaknesses/Failure to systematically enumerate spoliation-trace sources causes deleted-file evidence to be overlooked]]

## References

- [DFCite-1039] Findlay, 2023, "A review of thumbnail images artefacts in the Linux desktop and a methodology to add provenance to deleted files, using the thumbnail images artefact in combination with recent files history, and Trash artefacts", FSI: Digital Investigation 44.
- [DFCite-1176] Joun et al., 2023, "Discovering spoliation of evidence through identifying traces on deleted files in macOS", FSI: Digital Investigation 44, 301502.
