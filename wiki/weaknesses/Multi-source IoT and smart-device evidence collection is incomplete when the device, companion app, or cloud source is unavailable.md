---
id: DFW-1203
type: weakness
name: Multi-source IoT and smart-device evidence collection is incomplete when the device, companion app, or cloud source is unavailable
description: A multi-source IoT/smart-device acquisition methodology depends on hardware, companion-app, and cloud sources all being available and analyzable; if the device was not seized, the companion smartphone's data was wiped, or the cloud account's data was deleted, the corresponding source contributes nothing and only the remaining source(s) can be analyzed, individually rather than through cross-source correlation.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1203
source_refs:
  - DFCite-1216
  - DFCite-1232
updated_at: 2026-08-13
status: complete
---

# Multi-source IoT and smart-device evidence collection is incomplete when the device, companion app, or cloud source is unavailable

## Summary

The multi-source acquisition-and-correlation methodology's own authors note that "it might not be possible to obtain data from all three sources; for example, if the smart display device was not seized, data were wiped from the smartphone, all data were deleted in the cloud, and so on. In this case, the investigator can analyze each artifact separately," meaning the cross-source correlation analysis that recovers the technique's most valuable findings (e.g. linking a specific companion device to a specific physical device, or building an integrated behavior timeline) is only possible when at least two of the three sources remain available and mutually consistent.

## Why It Matters

An investigator who plans an investigation assuming full three-source coverage may find that a missing source (a device never recovered from the scene, a smartphone that has been wiped or replaced, or a cloud account whose data retention period has lapsed) forecloses not just that source's own artifacts but also the correlation-derived findings that depend on combining it with the others, reducing both the completeness and the corroborative strength of the resulting evidence. Recognizing this dependency early lets an investigator prioritize which sources to secure most urgently (e.g. seizing the physical device before evidence of it can be lost) rather than assuming any one source alone will be sufficient.

## Related Mitigations

- [[mitigations/Cross-correlate whichever IoT evidence sources remain available when one of device, companion app, or cloud is missing]]

## Used By

- [[techniques/Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources]]

## References

- [DFCite-1216] Youn et al., 2021, "Forensic analysis for AI speaker with display Echo Show 2nd generation as a case study", FSI: Digital Investigation 38, 301130.
- [DFCite-1232] Castelo Gómez et al., 2022, "Forensic analysis of the Xiaomi Mi Smart Sensor Set", FSI: Digital Investigation 42-43, 301451. Illustrates the same dependency from the opposite direction: with hardware and direct cloud-API acquisition both unobtainable, only the companion-app and network-traffic sources remained, and the investigators could not confirm whether the sensors themselves retain any local data since analysis of the sensors' own storage was never achieved.
