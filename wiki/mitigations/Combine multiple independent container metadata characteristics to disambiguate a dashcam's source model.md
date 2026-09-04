---
id: LWM-2137
type: mitigation
name: Combine multiple independent container metadata characteristics to disambiguate a dashcam's source model
source_refs:
  - LWCite-2157
updated_at: 2026-08-17
status: complete
---

# Combine multiple independent container metadata characteristics to disambiguate a dashcam's source model

## Summary

When identifying a dashcam recording's source model from its container file, check the recording's chunk sequence, file/directory naming rule, watermark content and layout, and video decoding parameters (resolution, compression profile) together against a reference signature database, rather than relying on a single characteristic, since candidate models that appear to match on one characteristic are frequently eliminated by the others.

## Addresses

- [[weaknesses/Dashcam source-model identification via a single metadata characteristic is ambiguous across sibling models]]

## How To Apply

Build or consult a reference database recording each known dashcam model's chunk sequence, naming convention, watermark layout, and decoding parameters, and match a recording under examination against all of these dimensions simultaneously rather than stopping once one characteristic appears to match. Where the combined characteristics still yield more than one candidate model, explicitly report the remaining set of consistent candidates rather than asserting a single determination the evidence does not support.

## References

- [LWCite-2157] Lee et al., 2021, "Your car is recording: Metadata-driven dashcam analysis system", FSI: Digital Investigation 38.
