---
id: LWT-1224
type: technique
name: Harvest public social media location data using a reverse-engineered internal API
description: Reverse-engineer the internal (non-public) API a social network's web-based map feature uses — by inspecting browser developer-tools network traffic for the POST request and JSON response objects backing a public, location-based content map — to programmatically enumerate and download all publicly-uploaded geotagged photos and videos at a location, turning the platform into a de facto distributed surveillance system supplementing traditional CCTV.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-1241
aliases:
  - Snap Map exploitation for open-source surveillance
  - Distributed surveillance via social network map scraping
source_refs:
  - LWCite-1256
updated_at: 2026-08-13
status: complete
---

# Harvest public social media location data using a reverse-engineered internal API

## Summary

Some social networking sites offer a public, web-accessible map feature that lets any user browse geotagged content other users chose to publish to a public heatmap or map view. Because these map features are typically implemented client-side against an internal API not documented for third-party use, intercepting the browser's own network traffic while manually browsing the map reveals the request format and response structure needed to programmatically enumerate and retrieve the same content at scale, without requiring any special access or an official developer API.

## Details

Using a browser's developer tools (or an intercepting proxy) while manually panning and clicking through the map's public interface reveals the POST requests the client sends and the JSON objects the server returns, including signed media URLs and location metadata for each publicly-uploaded item in the current view. A script that replays these requests across a target geographic area and time window can then download the corresponding media and metadata programmatically, effectively converting a public social-media map feature into a passive surveillance tool that can be pointed at a location of interest to reconstruct a timeline of activity, identify individuals or vehicles present, or corroborate other evidence — supplementing traditional CCTV footage in areas or time windows where none is available.

## Examples

- The technique was demonstrated against Snapchat's "Snap Map" feature to monitor social unrest in Minneapolis-Saint Paul following the death of George Floyd in May-June 2020, harvesting publicly-uploaded Snaps geotagged to the area to reconstruct a timeline and visual record of events as an open-source-intelligence surveillance exercise.
- Harvested Snap media included content usable for facial identification, vehicle license-plate reading, and general activity/location tracking during the monitored period, illustrating the range of investigative value extractable from a single public map feature.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Client-attached geotag metadata on public social media maps can be poisoned with false locations undetected by the platform]]

## References

- [LWCite-1256] Matthews et al., 2021, "Ghost protocol -- Snapchat as a method of surveillance", FSI: Digital Investigation 36, 301112.
