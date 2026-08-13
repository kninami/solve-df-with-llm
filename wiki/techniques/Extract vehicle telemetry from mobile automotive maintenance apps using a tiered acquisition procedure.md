---
id: DFT-1159
type: technique
name: Extract vehicle telemetry from mobile automotive maintenance apps using a tiered acquisition procedure
description: Recover vehicle telemetry (VIN, GPS coordinates, speed, RPM, acceleration/braking, fuel consumption, trip timestamps) from a mobile automotive-maintenance app that relays OBD-II/CAN-bus data via a Bluetooth-connected dongle, using a non-intrusive-first tiered sequence — manual dashboard inspection, then logical extraction of the app's local database/log/REALM files, then physical extraction if needed — aligned to an on-scene triage decision procedure.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1163
  - DFW-1164
aliases:
  - Automotive maintenance application forensic artifact engineering and triage
source_refs:
  - DFCite-1166
updated_at: 2026-08-12
status: complete
---

# Extract vehicle telemetry from mobile automotive maintenance apps using a tiered acquisition procedure

## Summary

Mobile automotive-maintenance apps (e.g. ZUS Smart Vehicle Health Monitor, Veepeak OBDCheck, GoFar) relay Engine Control Unit data from an OBD-II dongle to a phone over Bluetooth, and store artifacts — VIN, trip GPS coordinates, speed, RPM, acceleration, braking, fuel consumption, and timestamps — useful in traffic, insurance, and criminal investigations. Following the NIST-recommended order of least-to-most-intrusive mobile extraction (manual, then logical, then physical) both minimizes evidence-loss/damage risk and enables non-specialist first responders to complete the earliest, least-intrusive steps on scene.

## Details

**Manual extraction** reads the app's own dashboard: ZUS's dashboard shows live speed, GPS start/end coordinates, engine coolant temperature, and tire pressure, but requires an active Bluetooth connection between dongle and phone to display anything at all; GoFar's and Veepeak's dashboards, by contrast, browse previously-logged trip summaries (distance, average speed, fuel consumption, cost estimate, route map) without needing an active connection. **Logical extraction** (via ADB backup on an unrooted phone, requiring only USB debugging enabled — rooting and physical extraction added no further artifacts in testing) recovers each app's local files: ZUS's log file (GPS position and dongle-connection details), a separate VIN file, and an `ezzy_saver_sp.xml` file (max speed/RPM); Veepeak's connection-detail log (trip start date/time, and vehicle functionality status such as adaptive headlights, parking brake, and keyless ignition — useful for insurance pre-incident state assessment); and GoFar's connection log (phone model, VehicleID, UserID) plus a REALM database file containing VIN, user email/name, GPS route, and average/instant speed sampled every 2 seconds. On-scene triage follows a five-decision flowchart: check whether the dongle is still connected (if yes, manually extract); if not, check whether the dashboard is still accessible (if yes, manually extract); if neither, bag the phone for lab logical/physical extraction; after manual extraction, escalate to the lab if insufficient evidence was obtained.

## Examples

- At a simulated traffic-incident scene, an investigator confirms the OBD-II dongle is still connected, performs manual extraction of the ZUS dashboard's live speed and GPS reading, documents the findings, and only escalates to lab logical extraction if the on-scene evidence proves insufficient.
- Logical extraction of GoFar's REALM file recovered VINs for two different vehicles the app had connected to, plus the associated user's email address and name, providing direct account-to-vehicle attribution.
- Comparing GoFar's GPS/speed/timestamp data against an independent navigation app (Waze) and the vehicle's own dashboard confirmed close but not exact agreement (e.g. 49 km/h logged by GoFar versus 50 km/h recorded by Waze and the speedometer at the same timestamp), validating the general reliability of the recovered telemetry while quantifying its margin of error.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Encrypted or connection-dependent automotive app storage blocks lower-intrusion telemetry extraction]]
- [[weaknesses/Automotive maintenance app telemetry lags the vehicle's actual speed and timestamp readings]]

## References

- [DFCite-1166] Sumaila and Bahsi, 2022, "Digital forensic analysis of mobile automotive maintenance applications", FSI: Digital Investigation 43, 301440.
