---
id: DFT-1172
type: technique
name: Extract and reconstruct a drone's flight path from manufacturer-specific GPS log formats
description: Extract GPS/telemetry flight-log data from a drone's storage, decode the manufacturer-specific log format (which varies in encoding, encryption, and the set of parameters recorded), and plot the resulting coordinates as a reconstructed flight path on a map, to establish takeoff location, route, and timing of a flight.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-1179
aliases:
  - Drone GPS flight log analysis and flight path reconstruction
  - FlyLog Converter Tool workflow
source_refs:
  - DFCite-1181
updated_at: 2026-08-12
status: complete
---

# Extract and reconstruct a drone's flight path from manufacturer-specific GPS log formats

## Summary

A drone's flight logs record its GPS position throughout a flight, but each manufacturer encodes that data differently — some encrypted, some plaintext, with widely varying numbers of logged parameters — so a single generic parser cannot decode every drone's logs. This technique extracts and decodes the manufacturer-specific flight-log format, then plots the recovered coordinates as a flight path over a map, giving an investigator the drone's takeoff location, route, and timing.

## Details

Flight logs were extracted and analyzed from three drone families with structurally different log formats: DJI (a proprietary, encrypted `.DAT` format requiring dedicated decoding), Parrot (plaintext `.txt`/`.json` logs), and Yuneec (plaintext `.csv` logs). Because Parrot's native log format is not directly human-readable or mappable, the authors developed and released an open-source utility, the FlyLog Converter Tool, which parses Parrot's `.txt`/`.json` logs and converts them into an easily analyzable `.csv` format. Once decoded, GPS coordinates (latitude, longitude, altitude) and their associated timestamps are plotted as waypoints on satellite imagery (e.g., in Google Earth Pro) to reconstruct the drone's actual flight path, takeoff/landing points, and route timing. This complements the broader multi-component acquisition procedure in [[techniques/Extract forensic evidence from a drone and its ground control station]] by providing the specific decode-and-visualize step for GPS/flight-log data once it has been extracted from the drone or its storage.

## Examples

- Reconstructing a DJI Phantom 4's flight path from its 268-parameter, 45-entries-per-second flight log produced a substantially more detailed and precise route (takeoff point, path, and landing) than reconstructing a Parrot Bebop 2's 21-parameter, 11-entries-per-second log or a Yuneec Typhoon H's 22-parameter, 19-entries-per-second log, even though all three were successfully mapped as a flight path.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Non-DJI drone flight logs record substantially fewer parameters than DJI logs, reducing available forensic detail]]

## References

- [DFCite-1181] Kumar and Agrawal, 2021, "Drone GPS data analysis for flight path reconstruction: A study on DJI, Parrot & Yuneec make drones", FSI: Digital Investigation 38.
