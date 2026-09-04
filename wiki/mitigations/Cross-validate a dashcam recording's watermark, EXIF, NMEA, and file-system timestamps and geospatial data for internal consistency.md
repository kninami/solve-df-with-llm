---
id: LWM-1141
type: mitigation
name: Cross-validate a dashcam recording's watermark, EXIF, NMEA, and file-system timestamps and geospatial data for internal consistency
source_refs:
  - LWCite-1138
  - LWCite-2157
updated_at: 2026-08-17
status: complete
---

# Cross-validate a dashcam recording's watermark, EXIF, NMEA, and file-system timestamps and geospatial data for internal consistency

## Summary

Compare a dashcam recording's timestamp, GPS coordinates, and speed data as recorded in each of the locations where it appears — the on-screen watermark, EXIF metadata, the companion NMEA file, and file-system attributes/file naming — and flag any recording where these do not agree with each other or with what is visible in the video content itself.

## Addresses

- [[weaknesses/Dashcam geospatial, temporal, and speed metadata can be forged across a video's watermark and EXIF data]]

## How To Apply

During examination, extract and record every available copy of the recording's temporal, geospatial, and speed data — from the burned-in watermark (requiring manual video review, since no automated watermark-extraction tool exists), EXIF metadata (via Exiftool), the companion NMEA file, and file names/attributes/MAC times from the file system — and explicitly note any inconsistency between them. Check that speed is consistent with the distance between consecutive coordinates and the time elapsed between them, that the coordinates and time plausibly match visible landmarks and lighting/traffic conditions in the video, and that no other collected evidence (cell-site data, other device locations, witness accounts) contradicts the recording's claimed route and time. Treat an internally inconsistent recording, or one whose route/timing cannot be corroborated by independent evidence, with appropriate caution rather than presenting it as reliable on its own.

A formal version of this check, proposed for a normalized dashcam metadata database populated across filesystem, container, and OS/application sources, defines an expected chronological ordering relationship among a recording's distinct timestamp sources — directory name timestamp (`dn`) ≤ filename timestamp (`fn`) = directory-entry created time (`de_tc`) = system-log timestamp (`sl`) ≤ meta-chunk created/modified times (`mc_tc,tm`) < watermark timestamps (`wt`) = GPS-derived timestamps (`gi`) < directory-entry modified time (`de_tm`). Systematically checking a recording's extracted timestamps against this inequality (rather than only spot-checking individual sources against each other) flags any recording whose timestamp distribution deviates from the expected pattern as a candidate for manipulation, providing the automated metadata-consistency check that earlier guidance identified as a gap.

## References

- [LWCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.
- [LWCite-2157] Lee et al., 2021, "Your car is recording: Metadata-driven dashcam analysis system", FSI: Digital Investigation 38.
