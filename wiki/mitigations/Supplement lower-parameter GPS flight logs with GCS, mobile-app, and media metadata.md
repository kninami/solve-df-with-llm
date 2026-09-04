---
id: LWM-1179
type: mitigation
name: Supplement lower-parameter GPS flight logs with GCS, mobile-app, and media metadata
source_refs:
  - LWCite-1181
updated_at: 2026-08-12
status: complete
---

# Supplement lower-parameter GPS flight logs with GCS, mobile-app, and media metadata

## Summary

When reconstructing a flight path from a drone whose native flight log records comparatively few parameters (e.g., Parrot or Yuneec), corroborate and enrich the reconstruction using the drone's ground control station, its companion mobile app's own logs, and geotagged media (photo/video EXIF) captured during the flight, rather than relying on the sparse flight log alone.

## Addresses

- [[weaknesses/Non-DJI drone flight logs record substantially fewer parameters than DJI logs, reducing available forensic detail]]

## How To Apply

Extract the GCS/mobile-app companion data alongside the drone's own flight log (see [[techniques/Extract forensic evidence from a drone and its ground control station]]), and cross-reference any GPS-tagged media timestamps and coordinates against the flight-log waypoints to fill gaps or corroborate precision where the native log's parameter count and sampling rate are limited; note in the report where reconstruction precision is constrained by the drone's native logging density.

## References

- [LWCite-1181] Kumar and Agrawal, 2021, "Drone GPS data analysis for flight path reconstruction: A study on DJI, Parrot & Yuneec make drones", FSI: Digital Investigation 38. Establishes the parameter-richness gap between DJI and non-DJI flight logs that motivates supplementing with other evidence sources.
