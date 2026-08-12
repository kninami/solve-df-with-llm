---
id: DFW-1002
type: weakness
name: Inherent ICS sensor-actuator correlation causes misattribution of attacked assets
description: Because ICS sensors and actuators are physically and causally interdependent, feature-importance-based attack attribution can assign a high anomaly score to an unaffected asset that merely correlates with the actually attacked one.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1002
source_refs:
  - DFCite-1001
updated_at: 2026-08-09
status: complete
---

# Inherent ICS sensor-actuator correlation causes misattribution of attacked assets

## Summary

ICS assets such as level indicators and pumps are chained together in a physical process, so a malicious change to one asset's readings propagates measurable effects to correlated assets downstream or upstream. Data-driven attribution methods (CART, Shapley values, KernelSHAP) score assets by residual reconstruction error, which can rank a correlated-but-untouched asset above or alongside the actually attacked one.

## Why It Matters

In one evaluated attack scenario, the correctly attacked level indicator (LIT301) was identified with a 100th-percentile score, but a correlated, non-attacked sensor (LIT101) also scored in the 83rd percentile, close enough to risk inclusion in the reported attack points. Misattributing forensic effort to the wrong asset wastes investigative time and can produce an inaccurate account of which physical components were actually compromised, weakening the evidentiary value of the attribution.

## Related Mitigations

- [[mitigations/Combine multiple feature-importance algorithms for ICS attack attribution]]

## Used By

- [[techniques/Attribute ICS anomalies to assets using Shapley values]]

## References

- [DFCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
