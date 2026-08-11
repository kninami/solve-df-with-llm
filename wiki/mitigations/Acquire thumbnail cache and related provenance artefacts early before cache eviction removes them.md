---
id: DFM-1049
type: mitigation
name: Acquire thumbnail cache and related provenance artefacts early before cache eviction removes them
source_refs:
  - DFCite-1039
updated_at: 2026-08-09
status: complete
---

# Acquire thumbnail cache and related provenance artefacts early before cache eviction removes them

## Summary

Because thumbnail cache entries can be removed by routine cache-cleanup activity over time, prioritize acquiring the thumbnail cache, recent-files history, and Trash metadata as early as possible once a Linux desktop system is identified as relevant to an investigation, and do not treat an empty or absent thumbnail entry as proof a file never existed.

## Addresses

- [[weaknesses/Linux thumbnail cache entries are subject to size-based eviction]]

## How To Apply

When a Linux desktop system is seized or imaged, extract and preserve the thumbnail cache directory, recent-files history file, and Trash metadata directory as part of initial triage, before any further use of the system (which could trigger additional cache activity and evictions) if the system must remain live for any reason. When a suspected deleted file has no corresponding thumbnail entry, explicitly note in the analysis that this could reflect cache eviction rather than the file never having existed, and look for corroboration in the recent-files history or Trash records instead of treating the absence as conclusive.

## References

- [DFCite-1039] Findlay, 2023, "A review of thumbnail images artefacts in the Linux desktop and a methodology to add provenance to deleted files, using the thumbnail images artefact in combination with recent files history, and Trash artefacts", FSI: Digital Investigation 44.
