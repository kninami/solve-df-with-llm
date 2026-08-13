---
id: DFW-1247
type: weakness
name: Driving-insurance-app cloud telemetry samples location and speed less frequently than dedicated GPS-tracking equipment
description: A usage-based-insurance app's cloud-stored trip data records location and speed periodically ("valid period" samples) at a lower frequency than a dedicated GPS logger, and reports speed rounded to the nearest whole unit, reducing the temporal and positional granularity available for precise incident-timeline reconstruction between recorded events.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1248
source_refs:
  - DFCite-1262
updated_at: 2026-08-13
status: complete
---

# Driving-insurance-app cloud telemetry samples location and speed less frequently than dedicated GPS-tracking equipment

## Summary

A controlled side-by-side comparison against a dedicated per-second GPS logger found that a usage-based-insurance app's cloud-stored telemetry, while tracking the overall route and speed trend closely and correctly capturing discrete driving events (hard brakes, acceleration, sharp turns), samples location and speed only periodically rather than continuously, and rounds reported speed to the nearest whole number (e.g., 7.19 mph recorded as 7 mph).

## Why It Matters

Between two recorded samples or discrete events, an investigator has no direct telemetry evidence of exactly what the vehicle did — its path, speed, and any brief maneuvers in that gap must be interpolated or left unaccounted for, which can matter when reconstructing sub-second or sub-sample-interval details of a fast-moving incident such as a collision or evasive maneuver. Relying on this cloud telemetry alone, without acknowledging its sampling limitations, risks an investigator overstating the precision of a reconstructed timeline or map.

## Related Mitigations

- [[mitigations/Corroborate driving-insurance-app cloud telemetry with a higher-frequency GPS logger or dashcam]]

## Used By

- [[techniques/Reconstruct a vehicle incident timeline using driving-insurance-app cloud telematics data]]

## References

- [DFCite-1262] Onik, Spinosa, Asad, and Baggili, 2024, "Hit and run: Forensic vehicle event reconstruction through driver-based cloud data from Progressive's snapshot application", FSI: Digital Investigation 49, 301762.
