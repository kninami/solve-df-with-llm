---
id: LWW-1103
type: weakness
name: Synthetic-data-trained blind protocol identification assumes feature independence and has only been validated on one narrow protocol class
description: The Random Forest models are trained under a simplified assumption that extracted protocol features are statistically independent, and the method's effectiveness has so far only been demonstrated on one narrow protocol class (geographic encoding protocols such as GPX and NMEA-derived formats) rather than across the broader range of protocol types blind protocol identification is meant to cover.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1103
source_refs:
  - LWCite-1098
updated_at: 2026-08-10
status: complete
---

# Synthetic-data-trained blind protocol identification assumes feature independence and has only been validated on one narrow protocol class

## Summary

The authors acknowledge directly: "the simplified assumption of feature independence represents a potential limitation," noting that the Random Forest classifier's inherent robustness to complex feature interactions helps mitigate but does not eliminate this issue. The method's real-world validation is also scoped to a single case study on geographic encoding protocols, not the broader diversity of covert or unauthorized protocols an operational BPI system would need to identify.

## Why It Matters

An organization considering this synthetic-dataset-training approach for a broader network-forensics deployment should not assume the demonstrated accuracy generalizes automatically to protocol classes with more feature interdependence, or to significantly different protocol structures than the geographic-encoding case study — both the feature-independence assumption and the narrow validation scope mean additional protocol-specific validation is needed before operational reliance.

## Related Mitigations

- [[mitigations/Validate synthetic-data-trained blind protocol identification per protocol class before operational reliance]]

## Used By

- [[techniques/Identify network protocols blindly using a synthetic-dataset-trained classifier]]

## References

- [LWCite-1098] Abbasi-Azar et al., 2025, "Blind protocol identification using synthetic dataset: A case study on geographic protocols", FSI: Digital Investigation 53.
