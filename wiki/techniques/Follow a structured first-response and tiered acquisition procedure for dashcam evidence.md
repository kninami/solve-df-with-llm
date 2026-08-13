---
id: DFT-1137
type: technique
name: Follow a structured first-response and tiered acquisition procedure for dashcam evidence
description: At a crime scene involving a dashcam, follow a fixed first-response sequence — stop active recordings, power off, remove the SD card, power the dashcam back up isolated from its radio network, record its clock against a reference time, and disable auto-power-on and g-sensor recording — before acquiring evidence using the least invasive method sufficient (manual, logical SD/direct extraction, or hex dump/chip-off/micro-read as a last resort).
objective_ids:
  - DFO-1010
weakness_ids:
  - DFW-1140
aliases:
  - Dashcam forensic investigation guidelines (preservation and acquisition)
source_refs:
  - DFCite-1138
updated_at: 2026-08-12
status: complete
---

# Follow a structured first-response and tiered acquisition procedure for dashcam evidence

## Summary

Dashcams support Wi-Fi, Bluetooth, GPS, and GSM connectivity, auto-power-on, and g-sensor/motion-triggered recording, any of which can alter or overwrite evidence if the device is not handled correctly at first contact. This technique adapts the mobile-device tool classification model (manual extraction through logical extraction up to hex dumping/JTAG, chip-off, and micro-read) into a dashcam-specific first-response checklist and acquisition order, so evidence is preserved before the least invasive extraction method available is attempted.

## Details

The first-response sequence is: stop any in-progress recording; power off the dashcam and remove the power cable to prevent further overwriting or corruption; remove the SD card (protecting it from further modification while the device configuration is examined); power the dashcam back up without the SD card to safely inspect configuration settings; record the dashcam's displayed time against a reference UTC time; disable auto-power-on and g-sensor-triggered recording; isolate the dashcam from its radio network (equivalent to a mobile phone's airplane mode — turning off Bluetooth/Wi-Fi/GSM components individually, since dashcams generally lack a single airplane-mode toggle); power the dashcam down; and record identifying features (make/model/serial number) for chain of custody. Triage is of limited value for dashcams specifically because their storage is already small (up to 128 GB) and no known "safe" triage tool exists for them. Acquisition then follows an escalating-invasiveness order: manual extraction (direct interaction via the device's touchscreen/buttons/LCD panel, necessary for configuration settings such as licence-plate entry, warning toggles, and Wi-Fi status that are not otherwise recoverable, and which must be photographed since it modifies the live device state); logical extraction of the SD card (write-blocked, hash-verified imaging, the standard and lowest-risk acquisition path since most dashcams use standard FAT32/exFAT file systems that behave predictably in conventional forensic tools); direct-from-device logical extraction via USB mass-storage mode (used only as a last resort, since mounting the dashcam directly can, in some models, trigger an automatic recording rather than a clean mount); and hex dumping/JTAG, chip-off, or micro-read as the most invasive, highest-skill options for damaged or otherwise inaccessible devices. None of the dashcams examined implemented encryption, so encryption is not a practical barrier for this device class specifically.

## Examples

- Isolating a Nextbase dashcam's Wi-Fi and Bluetooth radios and disabling its auto-power-on and g-sensor settings before connecting external power, so that the device's stored recordings and configuration state remained unchanged while its SD card was separately imaged and hash-verified.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Failure to isolate and disable a dashcam's radio and auto-recording features before acquisition risks remote alteration or overwriting of evidence]]

## References

- [DFCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.
