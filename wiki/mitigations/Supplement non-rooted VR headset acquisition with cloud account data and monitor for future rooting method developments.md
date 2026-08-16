---
id: DFM-2123
type: mitigation
name: Supplement non-rooted VR headset acquisition with cloud account data and monitor for future rooting method developments
source_refs:
  - DFCite-2145
updated_at: 2026-08-16
status: complete
---

# Supplement non-rooted VR headset acquisition with cloud account data and monitor for future rooting method developments

## Summary

Compensate for a VR headset's currently unrootable Android OS by collecting the associated vendor cloud account's own data export alongside the device-side logical acquisition, and monitor ongoing research for a future rooting method that would enable direct application-database access.

## Addresses

- [[weaknesses/VR headset forensic acquisition cannot access application databases because the device's Android OS cannot currently be rooted]]

## How To Apply

In addition to [[techniques/Acquire and analyze a VR headset's live data, backup, and internal storage using ADB-based forensic acquisition]], always request or download the associated vendor cloud account's self-service data export, since some communication- and activity-related metadata may be recoverable from the account's server-side records even where the on-device database is inaccessible. Document explicitly in casework reporting that database-level artifacts (particularly chat/message content) could not be recovered due to the current lack of an established rooting method for this device class, so the completeness limitation is clear to anyone relying on the acquisition's results. Monitor published forensic research for VR headsets specifically, since a future rooting method (should one be developed, potentially via a JTAG approach adapted to the device's specific chipset) would materially change what this acquisition category can recover, and re-acquire a device if a new method becomes available and the device remains accessible.

## References

- [DFCite-2145] Raymer, MacDermott, and Akinbi, 2023, "Virtual reality forensics: Forensic analysis of Meta Quest 2", FSI: Digital Investigation 47, 301658.
