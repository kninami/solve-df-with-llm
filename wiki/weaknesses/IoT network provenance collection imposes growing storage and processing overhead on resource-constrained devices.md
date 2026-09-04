---
id: LWW-1304
type: weakness
name: IoT network provenance collection imposes growing storage and processing overhead on resource-constrained devices
description: Continuously logging provenance data for every node interaction across an IoT network causes the provenance store to grow over time and consumes processing resources on devices that are already constrained in memory, storage, and battery, creating a trade-off between forensic readiness (more complete provenance) and the resource budget available for a device's primary function.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1306
source_refs:
  - LWCite-1340
updated_at: 2026-08-15
status: complete
---

# IoT network provenance collection imposes growing storage and processing overhead on resource-constrained devices

## Summary

ProvLink-IoT's own evaluation explicitly analyzes the model's "performance impact on IoT network... in terms of provenance growth rate and storage overhead," acknowledging that provenance collection is not a free forensic-readiness measure but an ongoing resource cost imposed on devices that, by definition, are resource-constrained (limited memory, processing power, and often battery life).

## Why It Matters

An investigator or system designer deploying continuous provenance-based forensic readiness across an IoT deployment must budget for this overhead, since a naive full-fidelity provenance-logging configuration can itself degrade device performance, exhaust limited storage (potentially causing older provenance data to be overwritten or discarded before an incident is investigated), or drain battery on battery-powered nodes. Underestimating this cost risks either a deployment that becomes operationally unacceptable to stakeholders or one that quietly reduces logging fidelity/retention to cope, undermining the completeness of the provenance record available when an actual incident occurs.

## Related Mitigations

- [[mitigations/Tune IoT provenance logging granularity and retention to the device's resource budget]]

## Used By

- [[techniques/Reconstruct IoT network attacks using PROV-based provenance graph modeling]]

## References

- [LWCite-1340] Sadineni, Pilli, and Battula, 2023, "ProvLink-IoT: A novel provenance model for Link-Layer Forensics in IoT networks", FSI: Digital Investigation 46, 301600.
