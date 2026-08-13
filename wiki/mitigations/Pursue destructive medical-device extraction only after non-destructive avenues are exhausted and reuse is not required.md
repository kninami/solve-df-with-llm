---
id: DFM-1173
type: mitigation
name: Pursue destructive medical-device extraction only after non-destructive avenues are exhausted and reuse is not required
source_refs:
  - DFCite-1172
updated_at: 2026-08-12
status: complete
---

# Pursue destructive medical-device extraction only after non-destructive avenues are exhausted and reuse is not required

## Summary

Weigh the evidentiary value of firmware- or flash-chip-level data against the loss of patient reusability before opening a medical device, and only escalate to a destructive extraction method once non-destructive acquisition (e.g. removable-media imaging) has been exhausted and the device is confirmed not to be needed for further patient care.

## Addresses

- [[weaknesses/Non-destructive medical device examination excludes firmware and internal flash-chip data to preserve device reusability]]

## How To Apply

Document the case-specific justification for any decision to open a medical device or extract its firmware, confirming first (with the relevant clinical or regulatory authority where applicable) that the device is no longer required for patient treatment. Where non-destructive acquisition of removable storage (e.g. an SD card) already answers the investigative question, prefer it over destructive firmware extraction even when the latter might yield additional data.

## References

- [DFCite-1172] Schmitt and Butterfield, 2024, "Digital forensics in healthcare: An analysis of data associated with a CPAP machine", FSI: Digital Investigation 48, 301661.
