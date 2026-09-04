---
id: LWW-1082
type: weakness
name: Drone-only forensic extraction rarely links the device to a specific controller or suspect without also analyzing the GCS
description: Analyzing only data extracted from the drone itself often provides little to no direct link between the drone and a specific ground control station (GCS) or individual, even though the drone's own logs, location data, multimedia, and configuration files are recoverable, because that establishing link is instead typically found by analyzing the GCS and correlating it back to the drone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1082
source_refs:
  - LWCite-1072
updated_at: 2026-08-10
status: complete
---

# Drone-only forensic extraction rarely links the device to a specific controller or suspect without also analyzing the GCS

## Summary

Across the framework's validation, "it was identified that it is often not possible to find data to link the drone to a GCS and a suspect based on data only extracted from the drone" — despite the drone itself yielding log files with location data, multimedia, and configuration files. When the GCS is also analyzed, a link between the drone and the GCS (and from there to a specific user) is much more likely to be identified, since GCS applications commonly store user account details (username, email) that establish attribution.

## Why It Matters

An investigator who acquires and analyzes only a recovered drone, without also obtaining and analyzing its associated GCS (smartphone or tablet), may be able to fully reconstruct the drone's flight and usage history but still be unable to attribute that use to a specific suspect — a gap that matters directly for prosecutorial admissibility and case outcome, not just completeness of the technical record.

## Related Mitigations

- [[mitigations/Always extract and analyze the GCS alongside the drone to establish device-to-user attribution]]

## Used By

- [[techniques/Extract forensic evidence from a drone and its ground control station]]

## References

- [LWCite-1072] Thornton and Bagheri Zadeh, 2022, "An investigation into Unmanned Aerial System (UAS) forensics: Data extraction & analysis", FSI: Digital Investigation 41.
