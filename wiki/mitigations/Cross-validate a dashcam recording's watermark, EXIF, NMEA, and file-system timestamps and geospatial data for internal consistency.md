---
id: DFM-1141
type: mitigation
name: Cross-validate a dashcam recording's watermark, EXIF, NMEA, and file-system timestamps and geospatial data for internal consistency
source_refs:
  - DFCite-1138
updated_at: 2026-08-12
status: complete
---

# Cross-validate a dashcam recording's watermark, EXIF, NMEA, and file-system timestamps and geospatial data for internal consistency

## Summary

Compare a dashcam recording's timestamp, GPS coordinates, and speed data as recorded in each of the locations where it appears — the on-screen watermark, EXIF metadata, the companion NMEA file, and file-system attributes/file naming — and flag any recording where these do not agree with each other or with what is visible in the video content itself.

## Addresses

- [[weaknesses/Dashcam geospatial, temporal, and speed metadata can be forged across a video's watermark and EXIF data]]

## How To Apply

During examination, extract and record every available copy of the recording's temporal, geospatial, and speed data — from the burned-in watermark (requiring manual video review, since no automated watermark-extraction tool exists), EXIF metadata (via Exiftool), the companion NMEA file, and file names/attributes/MAC times from the file system — and explicitly note any inconsistency between them. Check that speed is consistent with the distance between consecutive coordinates and the time elapsed between them, that the coordinates and time plausibly match visible landmarks and lighting/traffic conditions in the video, and that no other collected evidence (cell-site data, other device locations, witness accounts) contradicts the recording's claimed route and time. Treat an internally inconsistent recording, or one whose route/timing cannot be corroborated by independent evidence, with appropriate caution rather than presenting it as reliable on its own.

## References

- [DFCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.
