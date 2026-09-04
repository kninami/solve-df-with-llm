---
id: LWW-1171
type: weakness
name: Failure to enter a smart-device SoC's flash boot mode prevents firmware acquisition for some device models
description: Entering the vendor-specific "flash mode" required to dump a system-on-chip's firmware over UART requires undocumented, chip-specific pin assignments and timing that are not standardized across manufacturers, so an examiner can be unable to acquire firmware from a device even with physical UART access.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1171
source_refs:
  - LWCite-1177
  - LWCite-1232
updated_at: 2026-08-13
status: complete
---

# Failure to enter a smart-device SoC's flash boot mode prevents firmware acquisition for some device models

## Summary

There is no general, cross-vendor instruction set for placing an embedded SoC into its flash-readable boot mode, and there is often no visible confirmation that the mode was successfully entered, so acquisition attempts can silently fail even after gaining physical debug access.

## Why It Matters

In a controlled multi-device study, firmware could only be successfully dumped from 12 of 16 examined smart relays; for the remaining four, the requirements for a stable entry into flash mode could not be determined even with UART access to the debug interface, meaning firmware-level evidence (Wi-Fi credentials, cloud tokens, device state, timezone/location data) from those devices was simply unobtainable in that examination. A separate examination of the Xiaomi Mi Smart Sensor Set found the same category of failure from a different angle: although the hub's and battery-powered sensors' flash chips were theoretically compatible with JTAG/chip-off per their datasheets, the authors could not successfully perform either technique despite the necessary equipment, and a remote-acquisition path that had worked on an earlier firmware version was permanently closed off once the device's firmware updated, since no downgrade path existed and the vendor's current firmware provided no remote-connection service at all.

## Related Mitigations

- [[mitigations/Verify successful entry into a SoC's flash boot mode via current-draw visualization before acquisition]]

## Used By

- [[techniques/Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources]]

## References

- [LWCite-1177] Eichhorn and Pugliese, 2024, "Do You \"Relay\" Want to Give Me Away? - Forensic Cues of Smart Relays and Their IoT Companion Apps", FSI: Digital Investigation 50, 301810.
- [LWCite-1232] Castelo Gómez et al., 2022, "Forensic analysis of the Xiaomi Mi Smart Sensor Set", FSI: Digital Investigation 42-43, 301451. Reports JTAG/chip-off acquisition failing on both the hub and its battery-powered sensors despite theoretical compatibility, and a firmware update permanently closing a previously working remote-acquisition path.
