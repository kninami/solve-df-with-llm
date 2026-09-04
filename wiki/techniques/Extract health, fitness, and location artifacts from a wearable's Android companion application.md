---
id: LWT-1291
type: technique
name: Extract health, fitness, and location artifacts from a wearable's Android companion application
description: Recover health metrics (heart rate, blood oxygen, sleep, stress), GPS-tagged activity routes, device-pairing and synchronization history, and cached account/network data from a smartband or fitness-tracker's Android companion application's local SQLite databases and files on a rooted device, and automate the extraction with a purpose-built open-source parsing module, since a paired wearable's post-mortem forensic value depends on data actually synced to and retained by its phone-side companion app.
objective_ids:
  - DFO-1011
weakness_ids:
  - LWW-1301
aliases:
  - Garmin Connect for Android Analyzer (GC4AA)
  - ZL_std / ZL_autopsy (Zepp Life)
source_refs:
  - LWCite-1335
  - LWCite-1336
updated_at: 2026-08-15
status: complete
---

# Extract health, fitness, and location artifacts from a wearable's Android companion application

## Summary

Smartbands and fitness trackers cannot independently store extensive history and typically cannot receive calls or messages, so their forensic value depends almost entirely on their Android companion application, which receives and processes health/activity data over Bluetooth Low Energy and bridges it to the vendor's cloud. Heart-rate and other biometric data recovered from a companion app has already been used to establish time of death or refute an alibi in real murder investigations, making systematic extraction of the app's local SQLite databases and support files — automated with a purpose-built parsing tool — directly case-relevant.

## Details

**Garmin Connect (paired with a Garmin Vivosmart 4 smartband)**: on a rooted Android 11 device, the application's data directory holds multiple SQLite3 databases and support files yielding Daily Summary health metrics, GPS-tagged activity routes, phone-notification content relayed to the band, a `sync_cache.db` recording the smartband's unit ID and BLE-connection timestamps for each synchronization event, network/API response caches, and — recovered from an `app.log` execution log via keyword search for terms like `auth`, `token`, and `password` — cleartext HTTP communication details with Garmin's cloud servers, plus a Firebase-related JSON file containing the account's `access_token` and `refresh_token`. The Garmin Connect for Android Analyzer (GC4AA), a set of Python modules built for the ALEAPP forensic framework, automates parsing of a Vivosmart 4 data-directory dump and produces a report — including graphical presentation of GPS routes and SpO2 reading charts — surfacing more artifact types than prior open-source tooling, including several (Daily Summary, GPS data, Response Cache, Network Logs, Facebook API tokens, Device Synchronization cache, SpO2 charts) not previously documented for this app.

**Zepp Life (formerly Mi Fit, paired with a Xiaomi Mi Band 6)**: on rooted Android 8.1 and 10 devices, the application's private data directory (`/data/data/com.xiaomi.hm.health`, shared with the app's Mi Fit predecessor since Zepp Life is confirmed to be its direct successor retaining the same core database structures — `origin_DB`, `FemaleHealth_ID.db`, `stress_ID.db`, and others) yields GPS coordinates, events and alarms, and biometric data (heart rate, sleep time, fitness activity). Two open-source scripts — `ZL_std`, a Python 3 command-line tool producing high-level views of Zepp Life data, and `ZL_autopsy`, a module integrating the same functionality into the Autopsy forensic platform — automate extraction and correlate the smartphone-side data against the paired Mi Band's own recorded usage.

## Examples

- Cross-referencing Garmin Connect's `gcm_cache.db` against its `cache-database` found records present in one but not the other, establishing that both databases hold independent forensic value and should be examined together rather than treating either as a superset of the other.
- Garmin Connect's `notification-database` was found to only retain recent phone notifications relayed to the band and to have `PRAGMA schema.auto_vacuum` set to `FULL`, meaning deleted notification records cannot be recovered by standard SQLite deleted-record recovery techniques once removed.
- Correlating Zepp Life's phone-side synchronization records against the paired Mi Band 6's own on-device data confirmed which smart-band device had been paired with the examined phone and reconstructed the timeline of synchronization events between them.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Auto-vacuum-enabled wearable companion-app databases permanently destroy deleted notification and activity records]]

## References

- [LWCite-1335] Nunes, Domingues, and Frade, 2023, "Post-mortem digital forensic analysis of the Garmin Connect application for Android", FSI: Digital Investigation 47, 301624.
- [LWCite-1336] Domingues, Francisco, and Frade, 2023, "Post-mortem digital forensics analysis of the Zepp Life android application", FSI: Digital Investigation 45, 301555.
