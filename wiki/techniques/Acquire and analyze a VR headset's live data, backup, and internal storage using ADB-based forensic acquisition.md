---
id: DFT-2116
type: technique
name: Acquire and analyze a VR headset's live data, backup, and internal storage using ADB-based forensic acquisition
description: Forensically acquire an Android-based virtual reality headset (e.g. Meta Quest 2) by enabling Developer Mode and USB debugging through its companion mobile app, then using Android Debug Bridge (ADB) to pull a live-system dumpsys data snapshot, an application-backup archive, and the device's internal SD-card-equivalent storage, recovering device/account information, installed-application details, and user-activity artifacts without requiring root access.
objective_ids:
  - DFO-1006
  - DFO-1011
weakness_ids:
  - DFW-2122
aliases:
  - Meta Quest 2 forensic acquisition
source_refs:
  - DFCite-2145
updated_at: 2026-08-16
status: complete
---

# Acquire and analyze a VR headset's live data, backup, and internal storage using ADB-based forensic acquisition

## Summary

Virtual reality headsets are an emerging evidence source as VR-mediated crimes (harassment, grooming, virtual assault) increase, but forensic acquisition methodology for this device class is still nascent. An Android-based headset such as the Meta Quest 2 can be forensically acquired without root access by enabling Developer Mode via its companion mobile app and using ADB over USB to collect a live-system data dump, a full application-backup archive, and the device's internal storage partition -- collectively recovering device/account details, installed-application metadata, and user-generated content.

## Details

Because ADB is disabled by default, Developer Mode must first be enabled by upgrading the headset's primary Meta account to a developer account via the vendor's own developer website, then toggling Developer Mode and USB debugging through the paired companion mobile app's device-settings menu; the headset's proximity sensor should be covered (e.g. with tape) during acquisition, since some devices interrupt or fail the process if the sensor detects the headset is not being worn and lets the display go idle. Once connected via USB-C to a forensic workstation with ADB access enabled, a certified forensic acquisition tool triggers a live-system `dumpsys` collection (yielding individual text files covering user accounts, installed applications and their versions/permissions, Bluetooth pairing history, device hardware/OS/locale/timezone properties, network SSIDs, and per-application usage statistics) and an application-backup archive (containing per-application configuration files, database file paths, and progress/state data useful for reconstructing a timeline of application use). The device's internal storage (accessed as a directly browsable filesystem, since the headset otherwise functions like a standard SD card once connected) is separately imaged, recovering user-downloaded files of any type (including formats the headset's own apps do not natively support), screenshot and screen-recording captures, and per-installed-application data directories mirroring the live-data findings with additional application-specific artifacts (e.g. game save/progress files). A complementary cloud-data collection path, downloading the account's own data export via the vendor's privacy-center self-service feature, recovers personal account details (name, email, date of birth), device serial number and login history, and a record of installed/recently-viewed applications directly from the vendor's servers.

## Examples

- Acquiring a test Meta Quest 2 headset recovered the installed-application version and first-install/last-update timestamps for each of five test-installed VR applications directly from live-data text files, letting an examiner build an application-installation timeline without needing database-level access.
- Internal storage acquisition recovered user-downloaded files (images, a PDF, videos, and audio files) stored in the device's `Download` directory, along with each file's modification timestamp, size, and MD5 hash -- none of which the headset's own applications natively support opening, illustrating that the headset's internal storage functions as general-purpose file storage independent of its VR application ecosystem.
- The vendor cloud account's downloadable data export recovered a `data.json`/`index.html` file pair containing the account holder's name, email, date of birth, device serial number, and login history, corroborating and extending the device-side live-data findings with account-level identity information not present on the headset itself.

## Related Objectives

- `DFO-1006` Acquire data
- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/VR headset forensic acquisition cannot access application databases because the device's Android OS cannot currently be rooted]]

## References

- [DFCite-2145] Raymer, MacDermott, and Akinbi, 2023, "Virtual reality forensics: Forensic analysis of Meta Quest 2", FSI: Digital Investigation 47, 301658.
