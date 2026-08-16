---
id: DFW-2084
type: weakness
name: Non-invasive sensor spoofing and covert attacks against a single building-automation sensor type leave no distinguishing trace in its own event log
description: A building automation and control system (BACS) or home automation system (HAS) sensor's own event log cannot by itself distinguish a genuine physical event from a non-invasively spoofed one, nor detect that a genuine event was covertly evaded, because the log only records what the sensor itself measured, and a knowledgeable attacker can manipulate what a single sensor type measures without leaving any anomaly visible in that sensor's own records.
categories:
  - ASTM_INAC_EX
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2089
source_refs:
  - DFCite-2104
updated_at: 2026-08-16
status: complete
---

# Non-invasive sensor spoofing and covert attacks against a single building-automation sensor type leave no distinguishing trace in its own event log

## Summary

A PIR sensor spoofed by a thermal-emitting drone logs a presence event indistinguishable in structure from a genuine human-triggered event; a PIR or CO2 sensor evaded by thermal shielding or breath containment logs nothing at all despite genuine physical presence. In both cases, the affected sensor's own event log record (or absence of one) is internally unremarkable -- the log entry format, timestamp, and value are exactly what a genuine event would produce, and no built-in anomaly-detection mechanism in the tested systems flagged either the spoofed or the missing record as suspicious.

## Why It Matters

A crime scene reconstruction (CSR) analysis that relies on a single sensor type's event log as its basis for concluding an individual was, or was not, present at a specific place and time risks drawing an erroneous or misleading conclusion if that sensor was non-invasively spoofed or evaded and no other evidence source contradicts it. Because these attacks require no physical alteration of the sensor and can be conducted with commonly available equipment (a consumer drone, an emergency blanket, an inflatable mattress), an investigator cannot assume such attacks require unusual sophistication or leave physical traces that would independently alert them to tampering.

## Related Mitigations

- [[mitigations/Cross-reference multiple independent sensor types covering the same space before relying on a building-automation event log]]

## Used By

- [[techniques/Detect non-invasive sensor spoofing and covert tampering in building automation event logs using sensor fusion]]

## References

- [DFCite-2104] Bengtsson, Johnny, 2025, "The ghost in the building: Non-invasive spoofing and covert attacks on automated buildings", FSI: Digital Investigation 52, 301880.
