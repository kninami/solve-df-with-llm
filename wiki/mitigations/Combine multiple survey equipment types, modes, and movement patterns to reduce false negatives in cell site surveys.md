---
id: LWM-1114
type: mitigation
name: Combine multiple survey equipment types, modes, and movement patterns to reduce false negatives in cell site surveys
source_refs:
  - LWCite-1108
updated_at: 2026-08-12
status: complete
---

# Combine multiple survey equipment types, modes, and movement patterns to reduce false negatives in cell site surveys

## Summary

Reduce the risk of a false-negative survey result by combining several complementary survey approaches rather than relying on a single static-mode reading with one unit, since no single method is a "perfect" survey and each has different, partially offsetting failure modes.

## Addresses

- [[weaknesses/Static single-location cell-site surveys are susceptible to false negatives that exclude legitimately serving cells]]

## How To Apply

Where feasible, combine: parallel use of multiple mobile-emulator units; both idle and dedicated/connected operating modes; large-scale movement (hundreds of metres, from multiple directions) to and from the location in addition to a static dwell period; and use of a software-controlled radio to reduce the risk of falsely excluding cells due to being locked to a single network's selection algorithm. If a specific cell of interest is not detected, consider a physical visit to the cell mast to confirm it was on-air at the time of the survey. Explicitly document which of these mitigations were and were not used, and disclose the resulting limitations of the survey method when reporting findings, since even this combined approach remains imperfect.

## References

- [LWCite-1108] Tart et al., 2021, "Cell site analysis: use and reliability of survey methods", FSI: Digital Investigation 38.
