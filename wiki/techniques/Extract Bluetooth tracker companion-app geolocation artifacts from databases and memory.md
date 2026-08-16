---
id: DFT-1181
type: technique
name: Extract Bluetooth tracker companion-app geolocation artifacts from databases and memory
description: Recover a personal Bluetooth tracker's geolocation history, timestamps, and device identifiers by parsing its companion app's SQLite databases, XML/cache files, and log files across mobile platforms, plus scanning the desktop companion app's live process memory for plaintext geolocation signatures.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1188
aliases:
  - Tile Artifact Parser
  - TAP
  - S.TASER
  - Smart Tag Parser
source_refs:
  - DFCite-1192
  - DFCite-2078
updated_at: 2026-08-16
status: complete
---

# Extract Bluetooth tracker companion-app geolocation artifacts from databases and memory

## Summary

Personal Bluetooth trackers (e.g. Tile) rely on a companion mobile or desktop app to relay a tracked object's location, and that app locally caches days of geolocation history, timestamps, and device/user identifiers even without a paid premium account. Correlating this data across a companion device's SQLite databases (iOS/Android) and, for a desktop client with no persistent local database, its live process memory, reconstructs a timeline of where a tracked object (or the investigation subject carrying it) has been.

## Details

On iOS, an iTunes/Finder backup extraction yields a `TileNetworkDB.sqlite` database whose `ZTILENTITY_PLACEMARK` table stores latitude, longitude, timestamp, and address fields in Apple Cocoa Core Data timestamp format, going back roughly 30 days regardless of premium subscription status; associated log files (`Events_b.log`, `Events_c.log`) additionally record client/user/Tile UUIDs and battery level. On Android, a full device backup/extraction yields comparable but sparser SQLite tables, XML preference files (linked email, UUIDs, tokens, cookies), and cached map-image files. The Windows desktop client stores no equivalent local database; instead, a memory image of the running process is scanned linearly for a known signature to recover plaintext geolocation coordinates, Epoch timestamps, and Tile device names/UUIDs directly from RAM. A companion open-source tool (Tile Artifact Parser, TAP) automates locating and parsing both the SQLite and VMEM sources, correlating recovered points by timestamp and rendering them as an interactive map with path lines between successive coordinates. The same signature-search and correlation methodology generalizes to other Bluetooth-tracker companion apps beyond Tile. For Samsung's SmartTag/SmartTag2 ecosystem, the S.TASER (Smart Tag Parser) tool automates the equivalent extraction from the SmartThings, SmartThings Find, and Samsung Find companion apps: tag identification data (deviceId, model, setupId, label, logId/UUID) and location history are stored across several SQLite databases (`DataLayerData.db`, `DataLayerData_core.db`, `InternalSettings.db`), an activity log (`PersistentLogData.db`), and cache/XML files, with the deviceId acting as the key value linking artifacts across sources; Samsung Find's week-long location history is stored in plaintext, while SmartThings Find's is encrypted client-side (requiring the Android Keystore key, obtainable via dynamic analysis with Frida) but its long-term location history is not removed by an in-app tag-deletion action.

## Examples

- Extraction from an iPhone SE's iTunes backup recovered a full 30-day geolocation history from `ZTILENTITY_PLACEMARK`, plus a Tile firmware binary image stored in the same database.
- A memory image of the Tile Windows desktop client, captured while the app was actively tracking, revealed geolocation coordinates, Epoch timestamps, and Tile UUIDs in plaintext, even though no equivalent data existed in any file on disk for that client.
- TAP's correlation-test suite recovered 100% of embedded valid data points across ten synthetic SQLite databases (0-5,000 points) and ten synthetic 2GB VMEM images, and correctly flagged roughly half of deliberately corrupted/partial data points as such.
- Across five anti-forensics scenarios tested against Samsung SmartTag/SmartTag2 (tag deletion, location-data deletion, account logout, service withdrawal, application synchronization), S.TASER successfully recovered the deviceId (UUID) of every deleted tag from the surviving `DataLayerData_core.db`/`InternalSettings.db`/cache artifacts even after the tag entry itself was removed from `DataLayerData.db`, and cross-referencing `PersistentLogData.db`'s deletion-event logs with cache-derived registration timestamps and model-specific duplicate-logId checks recovered the deleted tag's logId (identifier) in the large majority of cases.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Speed-threshold location-spoofing detection cannot identify gradual or subtle spoofing]]
- [[weaknesses/Re-registering a Bluetooth tracking tag overwrites cached identification data needed to recover its earlier registration]]

## References

- [DFCite-1192] Pace et al., 2023, "Every step you take, I'll be tracking you: Forensic analysis of the tile tracker application", FSI: Digital Investigation 45, 301559.
- [DFCite-2078] Yang, Han, Kim, and Kim, 2025, "Samsung tracking tag application forensics in criminal investigations", FSI: Digital Investigation 52, 301875. Source for the S.TASER tool and the Samsung SmartTag/SmartThings artifact structure, including its five anti-forensics-scenario evaluation.
