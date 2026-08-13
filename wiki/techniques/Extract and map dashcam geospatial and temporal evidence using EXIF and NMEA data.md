---
id: DFT-1138
type: technique
name: Extract and map dashcam geospatial and temporal evidence using EXIF and NMEA data
description: Extract GPS coordinates, speed, and timestamp fields from a dashcam recording's EXIF metadata and companion NMEA sentence file (using a tool such as Exiftool), convert the extracted values into a mapping format such as KML or GPX, and plot the result onto Google Maps, Google Earth, or GPXSee to reconstruct the vehicle's travelled route, speed profile, and recording times.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-1141
aliases:
  - Dashcam geospatial evidence extraction workflow
source_refs:
  - DFCite-1138
updated_at: 2026-08-12
status: complete
---

# Extract and map dashcam geospatial and temporal evidence using EXIF and NMEA data

## Summary

A dashcam recording can carry geospatial, temporal, and speed data in as many as six different locations — the file system (file names, directory structure, file attributes), configuration files, NMEA sentence files, EXIF video metadata, an on-screen watermark, and the dashcam's own settings menu — but none of these locations are directly mappable on their own. This technique defines a four-step manual workflow (extraction, parsing, data formatting, and mapping) that turns raw EXIF/NMEA data into a route visualization and a structured, further-analyzable dataset.

## Details

NMEA (National Marine Electronics Association) sentence files record geospatial ($GPRMC/$GPGGA), temporal, and speed data in dashcam-specific companion files (typically sharing the recording's filename with an .nmea extension). EXIF data embedded in the recorded video/image file can be extracted using Exiftool (e.g. `exiftool -ee FILENAME` to display embedded GPS/speed/timestamp data, or `-p kml.fmt`/`-p gpx.fmt` output formats to export directly to KML or GPX). Because no existing digital forensic tool at the time of writing supports extracting and mapping geospatial data from dashcam sources end to end, an investigator must manually extract the raw EXIF/NMEA data, parse and reformat it into KML or GPX, and load the result into a mapping system such as Google Maps, Google Earth, or GPXSee (which additionally synthesizes a speed-versus-time chart alongside the plotted route) to produce a usable route visualization. Recording mode (ignition-initiated, manually initiated normal/emergency, or g-sensor-activated) and temporal data are also recoverable from file/directory naming conventions and file attributes revealed during a logical extraction, complementing the EXIF/NMEA-derived geospatial and speed data.

## Examples

- Running `exiftool -ee -p kml.fmt FILENAME > out.kml` on a Nextbase recording and loading the resulting KML into Google Earth produced a plotted vehicle route within a defined radius of a location of investigative interest, cross-referenced against the corresponding GPXSee-rendered speed-versus-time chart for the same journey.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Dashcam geospatial, temporal, and speed metadata can be forged across a video's watermark and EXIF data]]

## References

- [DFCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.
