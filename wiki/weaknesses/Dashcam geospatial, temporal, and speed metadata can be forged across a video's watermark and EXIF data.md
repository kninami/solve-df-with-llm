---
id: DFW-1141
type: weakness
name: Dashcam geospatial, temporal, and speed metadata can be forged across a video's watermark and EXIF data
description: A dashcam recording's geospatial coordinates, timestamp, and speed values, whether burned into the on-screen watermark or embedded as EXIF metadata, are not cryptographically protected, so a technically capable actor can alter them to misrepresent where, when, or how fast a vehicle travelled.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1141
source_refs:
  - DFCite-1138
updated_at: 2026-08-12
status: complete
---

# Dashcam geospatial, temporal, and speed metadata can be forged across a video's watermark and EXIF data

## Summary

None of the dashcams examined encrypt their recordings or metadata, and forging any individual geospatial, temporal, or speed value in a recording's watermark or EXIF data is not technically difficult in isolation. Producing a convincing forged recording is nonetheless nontrivial at scale, since a perpetrator must keep every frame's geospatial, temporal, and speed values mutually consistent with each other and with what is visible in the video itself — for a 3-minute, 30fps clip, this means up to 5,400 timestamp entries and matching speed/position values, extending to roughly 108,000 frames if an hour of footage needs to be forged.

## Why It Matters

An investigator who accepts a dashcam recording's watermark or EXIF-derived route, time, and speed data without any cross-validation risks relying on evidence that has been deliberately altered to place a vehicle at a different location, time, or speed than it actually was. The internal-consistency requirement across many frames raises the bar for a convincing forgery but does not make it impossible, and the paper explicitly identifies this as an open area needing a digital forensic tool capable of automatically checking metadata consistency, since no such tool currently exists.

## Related Mitigations

- [[mitigations/Cross-validate a dashcam recording's watermark, EXIF, NMEA, and file-system timestamps and geospatial data for internal consistency]]

## Used By

- [[techniques/Extract and map dashcam geospatial and temporal evidence using EXIF and NMEA data]]

## References

- [DFCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.
