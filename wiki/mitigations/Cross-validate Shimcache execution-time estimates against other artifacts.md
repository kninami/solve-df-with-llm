---
id: LWM-1010
type: mitigation
name: Cross-validate Shimcache execution-time estimates against other artifacts
source_refs:
  - LWCite-1005
updated_at: 2026-08-09
status: complete
---

# Cross-validate Shimcache execution-time estimates against other artifacts

## Summary

Treat any execution-time value derived from Shimcache through an estimation algorithm as provisional, and corroborate it against artifacts that do record genuine timestamps, such as Prefetch last-run times and Windows Event Log entries, before relying on it in a timeline.

## Addresses

- [[weaknesses/Shimcache lacks native file execution timestamps requiring unvalidated estimation]]

## How To Apply

When building an execution timeline from Shimcache-derived estimates, pull the corresponding Prefetch file (if present) and relevant Windows Event Log entries for the same executable and compare their timestamps against the estimated interval. Where Prefetch or Event Log evidence is unavailable (e.g., Prefetch disabled or the executable ran only once outside Prefetch's tracked count), explicitly annotate the timeline entry as estimate-only with its associated uncertainty rather than presenting it as an authoritative execution time.

## References

- [LWCite-1005] Dunsin et al., 2024, "A comprehensive analysis of the role of artificial intelligence and machine learning in modern digital forensics and incident response", FSI: Digital Investigation 48.
