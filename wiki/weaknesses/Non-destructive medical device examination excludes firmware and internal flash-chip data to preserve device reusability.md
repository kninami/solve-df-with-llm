---
id: DFW-1173
type: weakness
name: Non-destructive medical device examination excludes firmware and internal flash-chip data to preserve device reusability
description: Deliberately restricting a medical-device forensic examination to non-destructive methods (e.g. imaging a removable SD card) to keep the device usable for future patient care means firmware- and internal-flash-chip-level evidence, which typically requires opening or desoldering the device, is left uncollected.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1173
source_refs:
  - DFCite-1172
updated_at: 2026-08-12
status: complete
---

# Non-destructive medical device examination excludes firmware and internal flash-chip data to preserve device reusability

## Summary

Because opening a medical device to access its onboard flash memory invalidates its warranty and can render it unfit for further patient use, examiners deliberately avoid extracting firmware or internal chip data even when such data might exist and be forensically relevant.

## Why It Matters

A CPAP-machine examination that recovers only removable SD-card data will miss anything stored solely in onboard flash or firmware (which was documented as present, encrypted, and out of scope in the reviewed study), and an investigator who does not explicitly record this scoping decision risks the omission being read later as evidence that no such data exists, rather than as a deliberate, documented trade-off against destroying a device that may still be needed for patient care or regulatory compliance.

## Related Mitigations

- [[mitigations/Pursue destructive medical-device extraction only after non-destructive avenues are exhausted and reuse is not required]]

## Used By

- [[techniques/Apply a three-component device-engineering, forensic, and medical-interpretation methodology to examine a medical device]]

## References

- [DFCite-1172] Schmitt and Butterfield, 2024, "Digital forensics in healthcare: An analysis of data associated with a CPAP machine", FSI: Digital Investigation 48, 301661.
