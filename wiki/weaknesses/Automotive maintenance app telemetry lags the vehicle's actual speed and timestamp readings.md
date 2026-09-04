---
id: LWW-1164
type: weakness
name: Automotive maintenance app telemetry lags the vehicle's actual speed and timestamp readings
description: A mobile automotive-maintenance app's logged speed and time values can lag the vehicle's true real-time speed by roughly 1-2 seconds, an ECU-computing-power-dependent relay delay confirmed by cross-referencing the app's data against an independent navigation app and the vehicle's own speedometer, so a value read directly from the app's logs is not an exact, real-time-accurate representation of the vehicle's state at the recorded timestamp.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - LWM-1164
source_refs:
  - LWCite-1166
updated_at: 2026-08-12
status: complete
---

# Automotive maintenance app telemetry lags the vehicle's actual speed and timestamp readings

## Summary

Comparing one app's (GoFar's) logged speed against both a popular navigation app (Waze) and the vehicle's own speedometer, recorded simultaneously during test drives, showed the app's values were mostly consistent but occasionally diverged by 1 km/h at a matched timestamp, and a separate 1-2 second lag was directly observed between an app's (ZUS's) live dashboard speed reading and the maximum speed value later recovered from its log file (39 mph on the dashboard versus 51 mph in the log for the same trip). The device manufacturer attributed this delay to the vehicle's ECU computing power and the rate at which it relays data over the OBD-II/Bluetooth chain.

## Why It Matters

In cases where exact speed at an exact moment matters — for example, establishing whether a vehicle exceeded a speed limit at a specific point on a road, or reconstructing the precise sequence of events in a collision — treating an automotive-maintenance app's logged speed and timestamp as ground truth without accounting for this relay lag risks materially misstating the vehicle's true state at the moment in question, which could affect the outcome of a traffic dispute or insurance claim.

## Related Mitigations

- [[mitigations/Validate automotive app telemetry against an independent vehicle data source before treating it as exact]]

## Used By

- [[techniques/Extract vehicle telemetry from mobile automotive maintenance apps using a tiered acquisition procedure]]

## References

- [LWCite-1166] Sumaila and Bahsi, 2022, "Digital forensic analysis of mobile automotive maintenance applications", FSI: Digital Investigation 43, 301440.
