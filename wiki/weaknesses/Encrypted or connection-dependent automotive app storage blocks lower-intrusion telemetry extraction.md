---
id: DFW-1163
type: weakness
name: Encrypted or connection-dependent automotive app storage blocks lower-intrusion telemetry extraction
description: An automotive-maintenance app's dashboard can require an active Bluetooth connection to the OBD-II dongle before it will display any data at all, and an app's local log files can be stored in an encrypted format, either of which prevents the least-intrusive manual or logical extraction methods from recovering telemetry that is nonetheless present on the device.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1163
source_refs:
  - DFCite-1166
updated_at: 2026-08-12
status: complete
---

# Encrypted or connection-dependent automotive app storage blocks lower-intrusion telemetry extraction

## Summary

Two distinct causes were observed: first, one tested app's dashboard showed no data whatsoever once the OBD-II dongle lost its Bluetooth connection to the phone, even though the same data remained recoverable via logical extraction of the app's underlying log files — meaning a first responder relying on manual dashboard inspection alone, after the dongle has already been removed from the vehicle, would wrongly conclude no telemetry is available. Second, another tested app encrypted some of its local files (`.brc` extension), which blocked logical extraction from yielding meaningful data for that app, resulting in a markedly lower artifact count for it relative to apps without file-level encryption.

## Why It Matters

A first responder or triage specialist who checks only the app's live dashboard, and finds it blank because the dongle has already been disconnected, may prematurely conclude the vehicle produced no useful telemetry and fail to escalate the device for logical extraction, resulting in an incomplete investigation despite the data being recoverable. Separately, an investigator who does not recognize file-level encryption in an app's data store may misinterpret a low artifact yield as the app simply not collecting much data, rather than as an acquisition failure requiring escalation (e.g. to reverse-engineered decryption or a warrant for cloud-side data).

## Related Mitigations

- [[mitigations/Escalate to logical or physical extraction when live dashboard or plaintext access to automotive app data is blocked]]

## Used By

- [[techniques/Extract vehicle telemetry from mobile automotive maintenance apps using a tiered acquisition procedure]]

## References

- [DFCite-1166] Sumaila and Bahsi, 2022, "Digital forensic analysis of mobile automotive maintenance applications", FSI: Digital Investigation 43, 301440.
