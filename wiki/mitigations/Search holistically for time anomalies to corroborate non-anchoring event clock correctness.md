---
id: LWM-2129
type: mitigation
name: Search holistically for time anomalies to corroborate non-anchoring event clock correctness
source_refs:
  - LWCite-2149
updated_at: 2026-08-16
status: complete
---

# Search holistically for time anomalies to corroborate non-anchoring event clock correctness

## Summary

When a reconstructed event has no artifact of its own that pairs a local and an external timestamp, complement the nearest bounding time anchors with a broad search for time anomalies — explicit system-time-change log entries, out-of-order record sequences, and deviations from expected periodic synchronization intervals — and express the resulting confidence on a graded evidentiary scale rather than as a binary correct/skewed conclusion.

## Addresses

- [[weaknesses/Non-anchoring events lack any artifact that can directly validate system clock correctness at their precise time]]

## How To Apply

Identify the nearest time anchors before and after the non-anchoring event of interest, then separately search event logs (e.g., Windows Security event ID 4616, or platform-equivalent manual time-change records), database record ordering, and periodic synchronization settings for anomalies in that window. Absence of anomalies alongside agreeing bounding anchors increases confidence (e.g., toward Casey's C-Scale C4); presence of an anomaly alongside a disagreeing anchor should be treated as strong evidence of skew (e.g., C4.5), while a single bounding anchor alone without an anomaly search should be treated as weak evidence (C3) and reported as such.

## References

- [LWCite-2149] Vanini et al., 2024, "Was the clock correct? Exploring timestamp interpretation through time anchors for digital forensic event reconstruction", FSI: Digital Investigation 49.
