---
id: DFM-1248
type: mitigation
name: Corroborate driving-insurance-app cloud telemetry with a higher-frequency GPS logger or dashcam
source_refs:
  - DFCite-1262
updated_at: 2026-08-13
status: complete
---

# Corroborate driving-insurance-app cloud telemetry with a higher-frequency GPS logger or dashcam

## Summary

Where a vehicle-incident reconstruction requires precision finer than a usage-based-insurance app's periodic cloud-stored sampling interval provides, corroborate the recovered timeline with any available higher-frequency positioning source — a dedicated GPS logger, another vehicle telematics system, or dashcam footage — rather than treating the insurance app's telemetry as the sole or most precise available record.

## Addresses

- [[weaknesses/Driving-insurance-app cloud telemetry samples location and speed less frequently than dedicated GPS-tracking equipment]]

## How To Apply

Identify and acquire any additional positioning or video sources available for the same vehicle and time window — other installed telematics devices, dashcam or nearby CCTV footage, or a second insurer's snapshot data if the vehicle is dual-insured — and use these to fill or validate the gaps between the insurance app's periodic samples. When only the insurance app's telemetry is available, explicitly note in any report that reported speeds are rounded and that positions between recorded samples are interpolated rather than directly measured.

## References

- [DFCite-1262] Onik, Spinosa, Asad, and Baggili, 2024, "Hit and run: Forensic vehicle event reconstruction through driver-based cloud data from Progressive's snapshot application", FSI: Digital Investigation 49, 301762.
