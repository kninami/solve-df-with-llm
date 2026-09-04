---
id: LWM-1019
type: mitigation
name: Cross-validate provider-reported location data against independent corroborating evidence
source_refs:
  - LWCite-1013
updated_at: 2026-08-09
status: complete
---

# Cross-validate provider-reported location data against independent corroborating evidence

## Summary

Before treating a provider's ride-history or location record as proof of a suspect's physical movement, compare it against independently sourced evidence — vehicle-side telemetry where available, or other unrelated location/presence data — since user-submitted location data can be fabricated for some providers without any physical presence.

## Addresses

- [[weaknesses/Micromobility ride-history location data can be fabricated via provider APIs]]

## How To Apply

Determine whether the specific provider in question records vehicle-side GPS independently of user-submitted location (as TIER does) and compare the two where available; a mismatch is a strong indicator of fabrication. Where a provider (such as Lime or Voi) lacks this independent check, do not rely on ride-history location data alone — corroborate it with other evidence such as cell-site location information, payment timestamps, witness accounts, or other devices' data before drawing conclusions about a suspect's physical whereabouts from micromobility records.

## References

- [LWCite-1013] Hilgert et al., 2021, "A forensic analysis of micromobility solutions", FSI: Digital Investigation 38.
