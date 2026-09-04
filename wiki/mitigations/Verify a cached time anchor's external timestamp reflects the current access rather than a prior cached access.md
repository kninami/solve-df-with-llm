---
id: LWM-2130
type: mitigation
name: Verify a cached time anchor's external timestamp reflects the current access rather than a prior cached access
source_refs:
  - LWCite-2149
updated_at: 2026-08-16
status: complete
---

# Verify a cached time anchor's external timestamp reflects the current access rather than a prior cached access

## Summary

Before relying on a browser cache or history record as a time anchor, check whether it represents a reload or reopen of a previously accessed resource — for example by comparing its external timestamp against other records referencing the same URL or resource — since a reload reuses the original external timestamp while recording a new local access time.

## Addresses

- [[weaknesses/Reloading a cached web resource reproduces a stale external timestamp that predates the current access]]

## How To Apply

Group candidate time-anchor records by URL or resource identifier and inspect whether multiple local timestamps map to the same external timestamp value; where they do, treat only the earliest such local/external pair as a genuine anchor for that external time and treat later entries in the group as reloads that cannot validate clock correctness at their own local time. Where feasible, corroborate with browser-specific artifacts (e.g., navigation-type flags) that explicitly distinguish a fresh request from a reload or back/forward navigation.

## References

- [LWCite-2149] Vanini et al., 2024, "Was the clock correct? Exploring timestamp interpretation through time anchors for digital forensic event reconstruction", FSI: Digital Investigation 49.
