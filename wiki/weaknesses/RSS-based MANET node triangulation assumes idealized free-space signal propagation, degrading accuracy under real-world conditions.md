---
id: LWW-2112
type: weakness
name: RSS-based MANET node triangulation assumes idealized free-space signal propagation, degrading accuracy under real-world conditions
description: Received-signal-strength-based node triangulation assumes radio signals propagate uniformly according to the inverse square law across all locations and over time, an idealization that real-world obstacles, terrain, and environmental conditions (rain, humidity, dust) violate, degrading location-estimation accuracy in ways the underlying calculation has no way to detect or compensate for on its own.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - LWM-2113
source_refs:
  - LWCite-2132
updated_at: 2026-08-16
status: complete
---

# RSS-based MANET node triangulation assumes idealized free-space signal propagation, degrading accuracy under real-world conditions

## Summary

The inverse-square-law-based distance calculation underlying RSS triangulation assumes a free-space communication environment with no obstacles and consistent transmission power, but real radio propagation is affected by obstacles, terrain, and environmental conditions such as rain, humidity, and dust, none of which the basic calculation accounts for. The technique's own Hello Flood detection mechanism illustrates the practical consequence: because the Plotter can only reliably determine a precise node location where three circles intersect at a single point under a free-space-communication, no-obstacle assumption, any deviation from that assumption -- whether from a genuine environmental factor or a deliberate attack -- produces the same observable symptom (failure to converge), making the two causes difficult to distinguish from the triangulation output alone.

## Why It Matters

An investigator relying on RSS-based location estimates as if they were as precise as GPS-derived coordinates risks overstating the confidence warranted by a technique whose accuracy is known to degrade under conditions the calculation does not model. Because environmental interference and deliberate attack behavior (such as a Hello Flood attacker varying its transmission power) can produce the same triangulation-failure symptom, an investigator must have some independent basis for distinguishing an environmental artifact from genuine anomalous or malicious node behavior before treating a triangulation-convergence failure as evidence of an attack specifically.

## Related Mitigations

- [[mitigations/Corroborate RSS-based MANET location estimates with environmental context and treat single-technique convergence failures as inconclusive alone]]

## Used By

- [[techniques/Track MANET node locations and detect Hello Flood attacks using fog-based RSS triangulation]]

## References

- [LWCite-2132] Ragheb, Safwat, and Azer, 2025, "Unearthing the hidden path of MANET's nodes with signal strength measurements: Forensics challenges, survey and a novel approach for data collection, preservation and examination", FSI: Digital Investigation 53, 301916.
