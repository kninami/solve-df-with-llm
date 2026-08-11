---
id: DFT-1004
type: technique
name: On-device facial recognition presence log analysis
description: Parse locally stored facial-recognition logs and enrollment databases on a smart device that performs face detection/matching entirely on-device, to establish which enrolled or unknown individuals were present, and when, independent of network connectivity.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1004
aliases:
  - Offline Visual ID presence log analysis
source_refs:
  - DFCite-1002
updated_at: 2026-08-09
status: complete
---

# On-device facial recognition presence log analysis

## Summary

Devices whose facial-recognition pipeline runs entirely on-device (no cloud round-trip) continue to log facial detection and recognition events even when disconnected from the network. On Amazon Echo Show devices (Visual ID feature), extracted logs contain a persistent identifier per enrolled individual, timestamps, and periodic torso/hand detection counts, together letting an examiner reconstruct who was in front of the device and when — a pattern generalizable to any on-device biometric recognition system that logs locally.

## Details

During enrollment, the device generates a large feature vector stored in a local database (e.g., SQLite). Each recognition event is logged with a stable per-person identifier that is consistent across devices tied to the same account, letting investigators correlate the same individual's presence across multiple devices. Unenrolled or obscured faces are still logged with a generic placeholder identifier, and periodic detection-count counters are emitted even absent any recognized face, providing a presence baseline independent of successful identification.

## Examples

- Extracted eMMC logs from an Echo Show 15 with WiFi disabled still recorded enrolled-user recognition events with a stable person identifier, timestamps, and profile names, and logged a generic placeholder for an individual with an obscured face.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Obscured or unenrolled faces are logged without individual identification]]

## References

- [DFCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.
