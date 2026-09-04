---
id: LWM-1171
type: mitigation
name: Verify successful entry into a SoC's flash boot mode via current-draw visualization before acquisition
source_refs:
  - LWCite-1177
updated_at: 2026-08-12
status: complete
---

# Verify successful entry into a SoC's flash boot mode via current-draw visualization before acquisition

## Summary

Because there is no general indicator that a system-on-chip has entered the vendor-specific "flash mode" required for firmware dumping, use an oscilloscope or other current-measuring device to visualize the chip's current draw over time and confirm the correct mode was reached before attempting acquisition.

## Addresses

- [[weaknesses/Failure to enter a smart-device SoC's flash boot mode prevents firmware acquisition for some device models]]

## How To Apply

Consult the SoC manufacturer's datasheet for the expected current-draw signature of each boot mode, then connect a current probe or oscilloscope to the power rail while attempting the flash-mode entry sequence (e.g. a specific pin-hold-during-power-on pattern). Compare the observed current-over-time graph against the documented signature; only proceed with the dump once the signature confirms flash mode was reached, and if it cannot be confirmed, document the failed attempt rather than proceeding on an unverified assumption that the mode was entered.

## References

- [LWCite-1177] Eichhorn and Pugliese, 2024, "Do You \"Relay\" Want to Give Me Away? - Forensic Cues of Smart Relays and Their IoT Companion Apps", FSI: Digital Investigation 50, 301810.
