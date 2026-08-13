---
id: DFT-1132
type: technique
name: Correlate a drone pilot to a drone and remote controller using cloud account-binding and flight-log data
description: Reconstruct the reverse-engineered private (internal) API of a drone manufacturer's cloud service and query it to retrieve account-to-device binding records and cloud-synced flight logs, then correlate pilot account, drone, and remote controller identifiers to answer who flew which drone, from where, and when, even when the local app or drone itself has had its data deleted.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1113
aliases:
  - Pilot-drone correlation analysis using DJI cloud forensic data
source_refs:
  - DFCite-1132
updated_at: 2026-08-12
status: complete
---

# Correlate a drone pilot to a drone and remote controller using cloud account-binding and flight-log data

## Summary

Consumer drone manufacturers such as DJI operate a cloud backend that binds a pilot's account to the specific drones and remote controllers registered to it and stores synced flight records. Reverse-engineering the mobile app's private (non-public) API traffic — including bypassing the app's SSL/certificate pinning, request-signing (MAC), anti-replay, and CAPTCHA protections — lets an investigator query this backend directly and recover account-device binding and flight-log evidence that answers the traditional 5W questions (who, what, when, where, and with what device) even when neither the drone nor the pilot's phone holds the data any longer.

## Details

The technique requires intercepting and reconstructing the target app's network traffic against its private cloud API endpoints, which are not publicly documented and are protected against casual interception by mechanisms such as certificate/SSL pinning (bypassed via runtime instrumentation), per-request message authentication codes, replay-protection tokens, and CAPTCHA challenges on certain endpoints. Once reconstructed, authenticated requests to the private API can retrieve which drone serial numbers and remote controller serial numbers are bound to a given pilot account, along with cloud-synced flight session records (start/end time, approximate location, and device identifiers) uploaded automatically by the app during normal operation. Correlating these records establishes device-to-pilot attribution even in scenarios where the physical drone or its controlling phone is unavailable, has been factory reset, or has had its local flight logs deleted, since the cloud copy is created independently of local storage. This complements, rather than replaces, physical/GCS-based drone extraction (see [[techniques/Extract forensic evidence from a drone and its ground control station]]), and shares its core reverse-engineered-private-API acquisition mechanism with [[techniques/Acquire cloud storage data comprehensively using combined open and internal API access]].

## Examples

- Reconstructing DJI's private mobile-app API to retrieve the pilot account bound to a seized drone's serial number, together with a cloud-synced flight log showing the drone's takeoff location and time, corroborating the pilot's presence at a restricted-airspace incident even though the drone's local flight records had been cleared.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Internal-API-based cloud acquisition breaks when a cloud storage provider changes its website or API implementation]]

## References

- [DFCite-1132] Kim et al., 2026, "Correlation analysis of pilots and drones using DJI cloud forensic data", FSI: Digital Investigation 57.
