---
id: DFM-1282
type: mitigation
name: Manually verify or discard shared pages with inconsistent content before finalizing a combined module extraction
source_refs:
  - DFCite-1310
updated_at: 2026-08-15
status: complete
---

# Manually verify or discard shared pages with inconsistent content before finalizing a combined module extraction

## Summary

When a module-aggregation tool reports (or an analyst detects) that shared pages at the same module offset disagree in content across source processes or dumps, manually inspect the disagreeing candidates rather than accepting an automatically-selected page as ground truth, and record which offsets were affected.

## Addresses

- [[weaknesses/Combining shared pages from different memory dumps can silently merge inconsistent module content when pages differ]]

## How To Apply

Enable the anomaly-detection logic that flags a page offset with disagreeing "shared" candidates (rather than silently selecting the most-repeated one), and for any flagged offset manually diff the candidate pages to determine whether the difference reflects an embedded, process-specific value (e.g. a memory address) rather than a genuinely different code path or resource. Document any offsets where the true original content could not be conclusively determined, and where the reconstructed module will be used for hashing or code comparison, treat those specific offsets as lower-confidence rather than the module as a whole.

## References

- [DFCite-1310] Fernández-Álvarez and Rodríguez, 2023, "Module extraction and DLL hijacking detection via single or multiple memory dumps", FSI: Digital Investigation 44, 301505.
