---
id: LWW-1019
type: weakness
name: Micromobility ride-history location data can be fabricated via provider APIs
description: For providers whose applications send user-device GPS data directly to the provider's API without independent verification against the vehicle's own GPS, an attacker with knowledge of the provider's API (not just the suspect's device) can inject arbitrary fabricated location data into what appears to be an authentic ride record.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-1019
source_refs:
  - LWCite-1013
updated_at: 2026-08-09
status: complete
---

# Micromobility ride-history location data can be fabricated via provider APIs

## Summary

For Lime and Voi, once a ride is started using a legitimately obtained vehicle identifier, the applications' APIs accept arbitrary GPS coordinates submitted directly by the client, with no independent verification against the vehicle's own onboard GPS. This makes it possible to construct a completely fabricated ride — including implausible routes spanning entire continents — that is stored in the provider's systems indistinguishably from a genuine ride. TIER, by contrast, records both the user-submitted location and the vehicle's own GPS location, allowing mismatches between the two to reveal spoofing; Nextbike does not rely on user-submitted GPS at all.

## Why It Matters

Ride-history data is one of the most forensically valuable artefact types for micromobility applications, directly bearing on a suspect's claimed or inferred physical location and movement. For providers lacking independent vehicle-side verification, this data's evidentiary reliability cannot be assumed at face value — an investigator (or, more concerningly, a suspect who has this technical knowledge and wishes to construct a false alibi) could produce ride records that pass a superficial review but do not reflect real movement.

## Related Mitigations

- [[mitigations/Cross-validate provider-reported location data against independent corroborating evidence]]

## Used By

- [[techniques/Access a cloud account using captured credentials]]

## References

- [LWCite-1013] Hilgert et al., 2021, "A forensic analysis of micromobility solutions", FSI: Digital Investigation 38.
