---
id: LWM-1002
type: mitigation
name: Combine multiple feature-importance algorithms for ICS attack attribution
source_refs:
  - LWCite-1001
updated_at: 2026-08-09
status: complete
---

# Combine multiple feature-importance algorithms for ICS attack attribution

## Summary

Fuse the outputs of several independent feature-importance methods (e.g., CART, Shapley values, KernelSHAP) with a relative-agreement weighting scheme, and require a high-percentile aggregated score before declaring an ICS asset as attacked, rather than trusting any single method's ranking.

## Addresses

- [[weaknesses/Inherent ICS sensor-actuator correlation causes misattribution of attacked assets]]

## How To Apply

Run each candidate attribution algorithm independently on the residual reconstruction error for all assets, then combine the results using a support/agreement-based weighting so that assets which score highly under only one method are down-weighted relative to assets confirmed by multiple methods. Treat assets in the 75th-100th percentile band as requiring manual review rather than automatic inclusion, especially when a correlated but architecturally adjacent asset scores close to the attacked asset.

## References

- [LWCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
