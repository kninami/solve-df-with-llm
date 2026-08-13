---
id: DFM-1140
type: mitigation
name: Follow the dashcam first-response checklist to isolate radios and disable auto-recording before any acquisition attempt
source_refs:
  - DFCite-1138
updated_at: 2026-08-12
status: complete
---

# Follow the dashcam first-response checklist to isolate radios and disable auto-recording before any acquisition attempt

## Summary

Before any acquisition step, stop active recordings, power down and remove the SD card, then power the dashcam back up (without the SD card) only long enough to isolate every radio component individually, disable auto-power-on and g-sensor recording, and record the device's clock, so that no remote or automatic recording activity can occur before evidence is imaged.

## Addresses

- [[weaknesses/Failure to isolate and disable a dashcam's radio and auto-recording features before acquisition risks remote alteration or overwriting of evidence]]

## How To Apply

At the scene, stop any in-progress recording and power off the dashcam before doing anything else. Remove and secure the SD card first, since this protects the recorded data from any further device activity. Power the dashcam back up without the SD card to safely reach its settings menu, then individually turn off every radio component the specific model supports (Wi-Fi, Bluetooth, GSM/SIM connectivity) rather than assuming a single "airplane mode" switch exists, and disable auto-power-on and g-sensor-triggered recording so the device cannot start a new recording session on its own. Record the dashcam's displayed time against a reference UTC clock at this stage, then power the device back down until logical or physical extraction of the (already-removed) SD card is ready to proceed.

## References

- [DFCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.
