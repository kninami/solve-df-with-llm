---
id: LWW-1004
type: weakness
name: Obscured or unenrolled faces are logged without individual identification
description: When a face is not enrolled in Visual ID or is obscured, the Echo Show's log records only a generic "UNDEF" personId rather than any individually identifying value, so presence is confirmed but the specific person cannot be determined from the log alone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1004
source_refs:
  - LWCite-1002
updated_at: 2026-08-09
status: complete
---

# Obscured or unenrolled faces are logged without individual identification

## Summary

The Visual ID pipeline only assigns a stable, individually identifying `personId` when a face is both enrolled and successfully matched. For any other detected face -- unenrolled individuals, or an enrolled individual whose face is obscured or in poor lighting -- the corresponding log entry records `personId: "UNDEF"`, discarding the opportunity to distinguish which specific unidentified person was present.

## Why It Matters

Presence at a scene can still be inferred from these entries (timestamps, torso/hand detection counts), but the identity of the person cannot be established from Visual ID data alone when the personId is UNDEF. This limits the evidentiary value of the artifact in scenarios such as confirming or ruling out a specific unenrolled suspect, and investigators may over-rely on the presence of a log entry without recognizing that it does not by itself identify who was present.

## Related Mitigations

- [[mitigations/Cross-reference Visual ID UNDEF entries with corroborating device logs]]

## Used By

- [[techniques/Analyze on-device facial recognition presence logs]]

## References

- [LWCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.
