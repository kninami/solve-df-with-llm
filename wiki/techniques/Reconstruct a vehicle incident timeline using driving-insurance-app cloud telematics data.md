---
id: DFT-1229
type: technique
name: Reconstruct a vehicle incident timeline using driving-insurance-app cloud telematics data
description: Reconstruct a chronological, mapped sequence of a vehicle incident (such as a hit-and-run) by acquiring a driving-insurance usage-based-insurance app's full cloud-stored trip telemetry — GPS coordinates, speed, and discrete driving events like hard braking, acceleration, and distraction — rather than relying on the coarser subset of that data the app's own mobile interface exposes.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1247
aliases:
  - PyShot-style hit-and-run reconstruction from usage-based-insurance cloud data
source_refs:
  - DFCite-1262
updated_at: 2026-08-13
status: complete
---

# Reconstruct a vehicle incident timeline using driving-insurance-app cloud telematics data

## Summary

Usage-based-insurance ("snapshot") apps continuously record a driver's trip data — start/end points, GPS coordinates, speed, and discrete events such as hard braking, acceleration, phone usage, and distraction — to the insurer's cloud, but expose only a partial view of this data through the mobile app's own interface (and, in the case tested, an even sparser view on iOS than Android). Acquiring the full cloud-stored dataset directly, via the technique in [[techniques/Acquire cloud storage data comprehensively using combined open and internal API access]], and mapping the recovered timestamped coordinates and events onto a timeline produces a substantially more complete reconstruction of a vehicle incident than either mobile app interface alone provides.

## Details

Once trip data has been acquired from the insurer's cloud (device/driver IDs, an access token, and per-trip start/end times, GPS coordinates, speed, distance, and a discrete event list with precise timestamps and locations), the events — Start, hard Brake, Acceleration, Speeding, Distraction, phone Usage, and periodic "Valid Period" location samples — are ordered chronologically and plotted on a map to reconstruct the vehicle's path and behavior throughout the incident. This produces both a textual trip timeline (event type, time, and street-level location) and a visual map with color-coded event markers, letting an investigator correlate, for example, a sudden speed drop at a specific coordinate (a braking event) with a subsequent rapid acceleration away from that location (consistent with fleeing the scene). Because the data originates from the insurer's own backend telemetry rather than the local device, this reconstruction remains available even when the responsible vehicle or phone itself is unavailable for direct forensic acquisition, provided the insurer's cloud account can be accessed.

## Examples

- In a simulated hit-and-run case study, a vehicle's cloud-stored telemetry recorded a hard-braking event (a speed change from ~7 mph to 0 mph in a short time frame) at coordinates matching a mannequin's position, followed by a location capture showing the vehicle's position as it fled and a rapid acceleration event (0 to 17 mph) moments later — reconstructing the incident's point of impact, dwell time, and departure speed and direction purely from cloud telemetry, corroborated by photographic and video evidence of the same staged scene.
- A controlled comparison against a dedicated per-second GPS logger showed the insurance app's periodic cloud-stored location and speed samples closely tracked the logger's route and speed trend, including correctly capturing driving actions like speeding, hard braking, and sharp turns, despite reporting speed rounded to the nearest whole number and sampling less frequently than the dedicated logger.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Driving-insurance-app cloud telemetry samples location and speed less frequently than dedicated GPS-tracking equipment]]

## References

- [DFCite-1262] Onik, Spinosa, Asad, and Baggili, 2024, "Hit and run: Forensic vehicle event reconstruction through driver-based cloud data from Progressive's snapshot application", FSI: Digital Investigation 49, 301762.
