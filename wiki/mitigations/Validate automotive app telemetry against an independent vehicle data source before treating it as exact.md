---
id: LWM-1164
type: mitigation
name: Validate automotive app telemetry against an independent vehicle data source before treating it as exact
source_refs:
  - LWCite-1166
updated_at: 2026-08-12
status: complete
---

# Validate automotive app telemetry against an independent vehicle data source before treating it as exact

## Summary

Before relying on a recovered speed or timestamp value from an automotive-maintenance app as precise evidence, cross-check it against an independent source — the vehicle's own speedometer/event data recorder, a separately-running navigation app, or an OBD-II scan tool reading — and report a small margin of error rather than the app's value alone.

## Addresses

- [[weaknesses/Automotive maintenance app telemetry lags the vehicle's actual speed and timestamp readings]]

## How To Apply

Where the case turns on a precise speed or exact-time determination, note in the examination report that the specific app's telemetry is known to lag true vehicle state by roughly 1-2 seconds, and where possible obtain a second independent data source for the same trip (vehicle dashboard footage, a separate navigation app, or the vehicle's own event data recorder) to corroborate or bound the recovered value before it is presented as evidence.

## References

- [LWCite-1166] Sumaila and Bahsi, 2022, "Digital forensic analysis of mobile automotive maintenance applications", FSI: Digital Investigation 43, 301440.
