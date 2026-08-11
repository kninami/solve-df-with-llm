---
id: DFM-1004
type: mitigation
name: Cross-reference Visual ID UNDEF entries with corroborating device logs
source_refs:
  - DFCite-1002
updated_at: 2026-08-09
status: complete
---

# Cross-reference Visual ID UNDEF entries with corroborating device logs

## Summary

When a Visual ID log entry has `personId: UNDEF`, use surrounding evidence -- torso/hand detection counters, timestamp clustering, session IDs, and other device or network logs -- to narrow down who was present, rather than treating the entry as uninformative.

## Addresses

- [[weaknesses/Obscured or unenrolled faces are logged without individual identification]]

## How To Apply

Extract the full log context around each UNDEF entry, including adjacent detection-count entries (e.g., "Found N torsos or hands"), session identifiers, and Wireshark-captured network activity timestamps, and correlate these against other available evidence (witness statements, video from other cameras, access logs) to build a presence timeline even without a resolved identity. Document that UNDEF confirms an unidentified presence, not the absence of one, when presenting findings.

## References

- [DFCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.
