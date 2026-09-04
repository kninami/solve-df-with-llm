---
id: LWM-1082
type: mitigation
name: Always extract and analyze the GCS alongside the drone to establish device-to-user attribution
source_refs:
  - LWCite-1072
updated_at: 2026-08-10
status: complete
---

# Always extract and analyze the GCS alongside the drone to establish device-to-user attribution

## Summary

Whenever a drone is seized as evidence, also seek out, seize, and forensically extract its associated ground control station (GCS), since device-to-user attribution is much more likely to be established from the GCS than from the drone alone.

## Addresses

- [[weaknesses/Drone-only forensic extraction rarely links the device to a specific controller or suspect without also analyzing the GCS]]

## How To Apply

Treat the GCS (smartphone or tablet) as a required, not optional, component of a UAS forensic examination; where the GCS is unavailable, explicitly document in the report that attribution to a specific individual could not be established from the drone's data alone rather than implying the drone-only extraction was a complete forensic examination of the case.

## References

- [LWCite-1072] Thornton and Bagheri Zadeh, 2022, "An investigation into Unmanned Aerial System (UAS) forensics: Data extraction & analysis", FSI: Digital Investigation 41.
