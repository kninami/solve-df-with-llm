---
id: DFT-1002
type: technique
name: Attribute ICS anomalies to assets using Shapley values
description: Fuse Classification and Regression Trees (CART), Shapley values, and KernelSHAP feature-importance scores to attribute an inferred ICS anomaly to the specific sensors/actuators responsible, for forensic triage prioritization.
objective_ids:
  - DFO-1005
weakness_ids:
  - DFW-1002
aliases:
  - Shapley value ICS asset attribution
source_refs:
  - DFCite-1001
updated_at: 2026-08-09
status: complete
---

# Attribute ICS anomalies to assets using Shapley values

## Summary

After an ICS anomaly is inferred, three independent feature-importance algorithms (CART, Shapley values, and the model-agnostic KernelSHAP) are each applied to the per-asset residual reconstruction error. Their normalized predictions are fused using a relative-support weighting scheme, and an asset is declared "under attack" if its aggregated score falls in the 75th percentile, allowing investigators to prioritize which sensors/actuators to examine first.

## Details

Each algorithm independently ranks ICS assets (sensors/actuators) by their contribution to the anomaly score. CART identifies the most impurity-reducing variable; Shapley values compute a game-theoretic marginal contribution across coalitions of assets; KernelSHAP combines Shapley values with LIME's local linear approximation. A degree-of-belief weight, based on the relative agreement between the three methods' outputs, combines the three predictions into a single per-asset attribution score. This reduces the reliance on any single method's potential misinterpretation and directly supports cyber forensic prioritization by narrowing the assets requiring detailed investigation.

## Examples

- SWaT testbed attack scenario 22: correctly attributed the attack to valve UV401, sensor AIT502, and pump P501, outperforming prior single-method approaches.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Inherent ICS sensor-actuator correlation causes misattribution of attacked assets]]

## References

- [DFCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
