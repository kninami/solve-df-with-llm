---
id: DFM-2089
type: mitigation
name: Cross-reference multiple independent sensor types covering the same space before relying on a building-automation event log
source_refs:
  - DFCite-2104
updated_at: 2026-08-16
status: complete
---

# Cross-reference multiple independent sensor types covering the same space before relying on a building-automation event log

## Summary

Before relying on a single building-automation or home-automation sensor's event log to support a crime scene reconstruction conclusion, check whether an independent sensor type covering the same physical space corroborates or contradicts it, and treat a single-sensor-type finding as provisional where no such cross-check is possible.

## Addresses

- [[weaknesses/Non-invasive sensor spoofing and covert attacks against a single building-automation sensor type leave no distinguishing trace in its own event log]]

## How To Apply

Identify all sensor types (PIR, CO2, door/window contacts, glass-break, acoustic, and others) that cover the same physical space as the sensor whose event log is under examination, and use [[techniques/Detect non-invasive sensor spoofing and covert tampering in building automation event logs using sensor fusion]] to check whether their records over the relevant time window are mutually consistent. A presence event recorded by one sensor type with no corresponding corroboration from an independent sensor type covering the same space, or a period with no recorded events despite other evidence suggesting activity occurred, should be flagged as a possible spoofing or evasion attempt rather than accepted at face value. Where only a single sensor type covers the space in question, document this as a limitation on the conclusions that can be drawn from the event log, and seek corroborating evidence (physical, testimonial, or from a different system) before treating the sensor's log as conclusive.

## References

- [DFCite-2104] Bengtsson, Johnny, 2025, "The ghost in the building: Non-invasive spoofing and covert attacks on automated buildings", FSI: Digital Investigation 52, 301880.
