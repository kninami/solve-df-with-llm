---
id: DFW-1049
type: weakness
name: Linux thumbnail cache entries are subject to size-based eviction
description: A Linux desktop environment's thumbnail cache is not an unbounded, permanent store; cached thumbnails can be automatically purged as the cache grows or ages, so provenance evidence for an older deleted file is not guaranteed to still be present by the time an examination occurs, and the gap between the file's deletion and the examination directly affects how likely the corresponding thumbnail is to have survived.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1049
source_refs:
  - DFCite-1039
updated_at: 2026-08-09
status: complete
---

# Linux thumbnail cache entries are subject to size-based eviction

## Summary

Because the thumbnail cache exists to accelerate file-manager browsing rather than to serve as a permanent evidentiary record, desktop environments implementing the freedesktop.org thumbnail specification apply cleanup policies to bound the cache's size and age, meaning thumbnails for files not recently browsed or thumbnailed can be removed over time independent of any action by the file's owner.

## Why It Matters

An investigator relying on thumbnail-cache-based provenance reconstruction should not assume that the absence of a thumbnail for a given deleted file means the file never existed — it may simply mean the corresponding cache entry was evicted before acquisition. This makes the technique's evidentiary coverage time-sensitive in a way that is not visible from the thumbnail cache's contents alone, since an examiner cannot directly observe what has already been evicted.

## Related Mitigations

- [[mitigations/Acquire thumbnail cache and related provenance artefacts early before cache eviction removes them]]

## Used By

- [[techniques/Reconstruct deleted-file provenance from Linux thumbnail cache and recent-files history]]

## References

- [DFCite-1039] Findlay, 2023, "A review of thumbnail images artefacts in the Linux desktop and a methodology to add provenance to deleted files, using the thumbnail images artefact in combination with recent files history, and Trash artefacts", FSI: Digital Investigation 44.
