---
id: DFT-1048
type: technique
name: Reconstruct deleted-file provenance from Linux thumbnail cache and recent-files history
description: Establish that a specific file existed on a Linux desktop system, its original file path, and an approximate window for when it was last accessed or deleted, by correlating the desktop environment's thumbnail image cache with its recent-files history (e.g., a `recently-used.xbel` bookmark file) and Trash metadata, even after the original file itself is no longer recoverable through ordinary file-system analysis or carving.
objective_ids:
  - DFO-1017
weakness_ids:
  - DFW-1049
aliases:
  - Linux thumbnail-cache and recent-files provenance reconstruction for deleted files
source_refs:
  - DFCite-1039
updated_at: 2026-08-09
status: complete
---

# Reconstruct deleted-file provenance from Linux thumbnail cache and recent-files history

## Summary

Linux desktop environments following the freedesktop.org thumbnail-management specification (used by GNOME/Nautilus and similar desktops) generate and cache a small preview image whenever a supported file (image, video, document) is browsed in a file manager, storing it independently of the original file's own lifecycle in a user-level cache directory. Because this cached thumbnail can persist even after its originating file is deleted and its filesystem metadata is gone, it becomes a standalone evidentiary artefact of the file having once existed, which can be cross-referenced against recent-files history and Trash records to build a fuller provenance picture.

## Details

The thumbnail cache stores each thumbnail keyed by a value derived from the original file's URI, alongside embedded metadata (such as the original file's path and modification time) inside the thumbnail image itself, letting an examiner recover the original file's location and rough timing even without the file. Correlating this with the desktop's recent-files history (which records recently opened file paths and access timestamps) and Trash artefacts (which record original path and deletion time for files deleted via the desktop environment's Trash, as opposed to a direct unlink) provides up to three independent, cross-referencing sources of provenance for a single deleted file, increasing confidence in the reconstructed timeline where multiple sources agree.

## Examples

- Correlating a thumbnail cache entry's embedded original-path metadata with a matching Trash record for the same path and a nearby recent-files access timestamp to establish that a specific image file existed at a specific location and was subsequently deleted within a bounded time window.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/Linux thumbnail cache entries are subject to size-based eviction]]

## References

- [DFCite-1039] Findlay, 2023, "A review of thumbnail images artefacts in the Linux desktop and a methodology to add provenance to deleted files, using the thumbnail images artefact in combination with recent files history, and Trash artefacts", FSI: Digital Investigation 44.
