---
id: DFM-2026
type: mitigation
name: Validate an EM-SCA plug-in's cross-unit portability and account for dynamic clock scaling before relying on its classification
source_refs:
  - DFCite-2026
updated_at: 2026-08-14
status: partial
---

# Validate an EM-SCA plug-in's cross-unit portability and account for dynamic clock scaling before relying on its classification

## Summary

Before treating an EM-SCA plug-in's software-activity classification of a target IoT device as reliable evidence, confirm the plug-in has been validated (or independently spot-checked) against a physical unit different from the one it was trained on, and account for dynamic clock-frequency scaling by monitoring across a frequency range rather than assuming a single fixed information-leaking frequency.

## Addresses

- [[weaknesses/EM side-channel behavior classifiers have unverified portability across different physical units of the same device model]]

## How To Apply

Where feasible, spot-check an EM-SCA plug-in's classification against a known-state reference unit of the same device model available to the investigating lab before relying on it for an unknown target unit in a case. When capturing EM data from a device known to use DVFS or heterogeneous CPU clustering, sweep or monitor a range of frequencies around the nominal clock rate rather than a single fixed value, to reduce the risk of missing the information-leaking signal during workload-driven frequency shifts.

## References

- [DFCite-2026] Sayakkara and Le-Khac, 2021 — Section VII.A's future-work discussion is the basis for both recommendations: validating cross-device portability, and adjusting acquisition to account for DVFS/big.LITTLE-driven frequency dynamics.
