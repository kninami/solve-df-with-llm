---
id: DFW-1179
type: weakness
name: Non-DJI drone flight logs record substantially fewer parameters than DJI logs, reducing available forensic detail
description: Parrot and Yuneec drones log far fewer flight parameters and log entries per second than DJI drones, so a flight path reconstructed from a non-DJI drone's log is inherently less precise and less detailed than one reconstructed from a comparable DJI log.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1179
source_refs:
  - DFCite-1181
updated_at: 2026-08-12
status: complete
---

# Non-DJI drone flight logs record substantially fewer parameters than DJI logs, reducing available forensic detail

## Summary

Comparing the three tested drone families' flight logs, the DJI Phantom 4 recorded 268 parameters at 45 log entries per second, while the Parrot Bebop 2 recorded only 21 parameters at 11 entries per second and the Yuneec Typhoon H recorded 22 parameters at 19 entries per second. As the authors note, "the higher the number of log entries per second, [the] more precise and accurate would be the flight log data," meaning Parrot and Yuneec logs inherently support a coarser, less precise flight-path reconstruction than an equivalent DJI log, independent of any tool or analyst error.

## Why It Matters

An investigator reconstructing a flight path from a Parrot or Yuneec drone's flight log should not assume it carries the same reconstructive precision as a DJI log from a comparable flight; a lower-frequency, fewer-parameter log can produce a materially coarser account of the drone's route and timing, which matters when the flight path's precision is itself contested or evidentially significant (e.g., proximity to a restricted boundary or another aircraft).

## Related Mitigations

- [[mitigations/Supplement lower-parameter GPS flight logs with GCS, mobile-app, and media metadata]]

## Used By

- [[techniques/Extract and reconstruct a drone's flight path from manufacturer-specific GPS log formats]]

## References

- [DFCite-1181] Kumar and Agrawal, 2021, "Drone GPS data analysis for flight path reconstruction: A study on DJI, Parrot & Yuneec make drones", FSI: Digital Investigation 38. Reports the parameter counts and per-second log entry rates (268/45 for DJI vs. 21/11 for Parrot and 22/19 for Yuneec) underlying this weakness.
