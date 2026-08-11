---
id: DFM-1038
type: mitigation
name: Build a per-camera reference training set before applying defective-pixel timeslot classification
source_refs:
  - DFCite-1028
updated_at: 2026-08-09
status: complete
---

# Build a per-camera reference training set before applying defective-pixel timeslot classification

## Summary

Confirm that a sufficiently large set of images known to have been taken by the specific camera device at known prior time periods is available before relying on defective-pixel timeslot classification, and treat the technique as out of scope when no such device-specific training corpus can be assembled.

## Addresses

- [[weaknesses/Defective-pixel timeslot classification requires prior training images from the specific camera]]

## How To Apply

Where the originating camera device is available or identifiable, collect or request a sufficiently large set of images known to have been captured by that specific unit across distinguishable prior time periods, matching the scale used in validated evaluations (on the order of hundreds of labeled images per timeslot) before training location-based classifiers for that device. Where no such device-specific corpus can be obtained, do not attempt this technique, and instead consider complementary temporal forensic methods such as EXIF metadata analysis (while accounting for its own alterability) or content-based image dating.

## References

- [DFCite-1028] Ahmed et al., 2021, "A machine learning-based approach for picture acquisition timeslot prediction using defective pixels", FSI: Digital Investigation 39.
