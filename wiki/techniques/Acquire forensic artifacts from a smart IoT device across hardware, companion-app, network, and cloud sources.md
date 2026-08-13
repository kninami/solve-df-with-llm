---
id: DFT-1165
type: technique
name: Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources
description: Systematically collect forensic evidence for a smart IoT device across its full multi-source ecosystem — hardware-level extraction from the device itself (UART firmware dump or chip-off), the companion smartphone app's local storage, captured network traffic where applicable, and the vendor's cloud service/API — since no single source alone yields a complete picture of device state and usage history.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1171
  - DFW-1203
aliases:
  - TEASR (Tool for Evidence Acquisition from Smart Relays)
  - Acquire forensic artifacts from a smart-relay IoT device across firmware, companion-app, network, and cloud-API sources
  - Multi-source Echo Show / smart-display forensic acquisition
  - Xiaomi Mi Smart Sensor Set multi-source forensic examination
source_refs:
  - DFCite-1177
  - DFCite-1216
  - DFCite-1232
updated_at: 2026-08-13
status: complete
---

# Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources

## Summary

Smart IoT devices — wall-socket switch actuators, AI speakers with a display, and similar inconspicuous connected devices — are wholly dependent on wireless connectivity and a companion app or cloud service for interaction, so evidence relevant to their usage is scattered across the device's own hardware, the companion app's local storage, network traffic between components, and the vendor's cloud, requiring a coordinated multi-source acquisition rather than examination of the device alone.

## Details

Device-level acquisition method depends on the device's own hardware interfaces: a debug UART interface (read out with a USB-to-UART adapter and chip-specific command-line tools such as `esptool` or `bk7231tools`) suits relay-style SoCs, while a device with no exposed interface may require full teardown and chip-off extraction of its eMMC/BGA flash package using a dedicated flash reader (e.g. Easy JTAG). Companion-app local data is pulled from the app's private storage directory via `adb` (Android) or equivalent on a rooted/jailbroken test device, where log files can reveal a history of user actions with timestamps and device-pairing history. Cloud artifacts are retrieved via each vendor's device/account API once credentials are obtained (often already cached on the companion client, e.g. via a web-view login), yielding device lists, configuration, historical usage logs, and media/content history not necessarily retained on the device itself. Once artifacts from all available sources are acquired, an integrative correlation analysis — matching identifiers such as a device's serial number or CardID across the hardware, companion-client, and cloud artifact sets — recovers information not obtainable from any single source alone, such as linking a specific companion smartphone to the device it controls, or combining Alexa-cloud photo timestamps with companion-app cache images to determine what a device's camera captured and when.

## Examples

- Firmware dumps from four Shelly-brand relays (SoC: ESP32) contained cloud access tokens, cloud credentials, timezone, and GPS coordinates in plaintext JSON fragments.
- The eWeLink companion app's local log file distinguished switching operations triggered via the app from those triggered via the device's physical button, based on small structural differences in the logged entries.
- The Tuya cloud API's device event log endpoint returned `event_from`/`event_id` fields distinguishing device-, client-, third-party-, and cloud-originated switching and online/offline/activation/reset events, though manually-initiated physical-button switches were not captured in this log at all.
- Amazon Echo Show 2nd generation (Youn et al., 2021): chip-off extraction of the device's 153-ball BGA eMMC flash chip recovered the Ext4-formatted `android_data` partition containing account settings, system logs (including wake-word-detection and app-usage events), and a media database with creation timestamps, hashes, and paths of photos/videos taken by the device; the paired Alexa companion smartphone app recovered account credentials (via a Chrome-based Silk-browser password decrypt) and search-keyword/shopping-list history; and the Alexa cloud API, once account credentials were obtained, returned historical conversation logs, connected-device lists, and photo/video history with timestamps. Correlating the device's serial number (found in both the companion app's CardID and the Echo Show's own hardware) confirmed which smartphone controlled which physical device, and combining cloud-recorded search/shopping activity with device-side photo timestamps built a timeline of user behavior for a hypothetical case study.
- Xiaomi Mi Smart Sensor Set (Castelo Gómez et al., 2022): with hardware-level acquisition of the "Mi Control Hub" and its Zigbee window/motion/switch sensors ruled out entirely (JTAG/chip-off attempted but not achievable by the authors, and the hub's earlier remote-acquisition path required a firmware version the device could no longer be downgraded to), the companion-app layer supplied a rooted Android device's `/data/com.xiaomi.smarthome` directory containing paired-device lists, per-device action logs, the hub's MAC address and geolocation, and — in plaintext, unencrypted `shared_prefs` XML — the home WiFi network's SSID/BSSID/password; the network layer supplied both WiFi traffic (hub-to-cloud UDP updates whenever a sensor's state changed, plus periodic ICMP connectivity checks) and sniffed Zigbee traffic (per-device 802.15.4 hardware addresses, and a request/data/acknowledgement packet triplet for every sensor state change), which together substituted for the direct cloud-API access that could not be obtained for this device.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Failure to enter a smart-device SoC's flash boot mode prevents firmware acquisition for some device models]]
- [[weaknesses/Multi-source IoT and smart-device evidence collection is incomplete when the device, companion app, or cloud source is unavailable]]

## References

- [DFCite-1177] Eichhorn and Pugliese, 2024, "Do You \"Relay\" Want to Give Me Away? - Forensic Cues of Smart Relays and Their IoT Companion Apps", FSI: Digital Investigation 50, 301810.
- [DFCite-1216] Youn et al., 2021, "Forensic analysis for AI speaker with display Echo Show 2nd generation as a case study", FSI: Digital Investigation 38, 301130.
- [DFCite-1232] Castelo Gómez et al., 2022, "Forensic analysis of the Xiaomi Mi Smart Sensor Set", FSI: Digital Investigation 42-43, 301451. Demonstrates the network-traffic layer (WiFi and sniffed Zigbee) substituting for cloud-API and hardware acquisition when both are unavailable, and documents plaintext WiFi credentials recoverable from companion-app storage.
