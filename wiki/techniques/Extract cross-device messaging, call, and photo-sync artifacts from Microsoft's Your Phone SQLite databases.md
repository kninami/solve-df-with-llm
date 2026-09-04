---
id: LWT-1269
type: technique
name: Extract cross-device messaging, call, and photo-sync artifacts from Microsoft's Your Phone SQLite databases
description: Recover SMS/MMS/RCS messages, call logs, contacts, notifications, and synced photo metadata from Microsoft's Your Phone environment — the Android Your Phone Companion app and its paired Windows 10 Your Phone app — by parsing the SQLite3 databases and registry hive each side maintains, giving an investigator access to a linked smartphone's data through the paired Windows machine even when the phone itself is unavailable.
objective_ids:
  - DFO-1011
weakness_ids:
  - LWW-1280
aliases:
  - Your Phone Analyzer (YPA)
  - Windows 10 Your Phone / Your Phone Companion forensic artifact extraction
source_refs:
  - LWCite-1308
updated_at: 2026-08-15
status: complete
---

# Extract cross-device messaging, call, and photo-sync artifacts from Microsoft's Your Phone SQLite databases

## Summary

Microsoft's Your Phone links an Android smartphone to a Windows 10 machine, mirroring SMS/MMS/RCS messages, call logs, contacts, notifications, and recent photos through eight SQLite3 databases on the Windows side and a smaller set of SQLite3 databases and shared-preferences XML files on the Android side. Because this data is routed through the Windows machine, examining Your Phone's local artifacts on a Windows device recovers a working copy of the linked phone's communications and photos even when the phone itself is inaccessible, encrypted, locked, or physically unavailable.

## Details

On Windows, Your Phone's per-user data lives under `%LOCALAPPDATA%\Packages\Microsoft.YourPhone_8wekyb3d8bbwe`, with configuration held in a `settings.dat` registry hive (device pairing GUID, cloud-account identifier, permission flags, a JSON `UsageSummary` blob identifying the linked phone's manufacturer/model/OS version) and the forensically significant content in eight SQLite3 databases under `LocalCache\Indexed\<device-GUID>\System\Database`: `calling.db` (`call_history` table — phone number, duration, start/last-updated filetime64 timestamps, call type, and a SIM-identifying ICCID in the `phone_account_id` field for multi-SIM devices), `contacts.db` (contacts plus FTS full-text-search tables), `phone.db` (SMS/MMS/RCS messages), `photos.db` (synced photo metadata; only the most recent items keep a locally cached full-resolution or downsized copy, with older items retaining only a thumbnail), and `notifications.db` (notification alerts, including a JSON payload identifying the originating app). On Android, Your Phone Companion's public data directory (`/storage/emulated/0/Android/data/com.microsoft.appmanager/`, accessible without root) holds mostly low-value SDK/telemetry databases, while its root-only private data directory holds the forensically useful `RemoteAppStore.xml.xml` (paired Windows device names, app versions, pairing timestamps) and `mmxauth.xml` (the pairing between the device's `StableUserID` and the Microsoft cloud-account email address used for the pairing).

## Examples

- Recovering the last 30 days of call history (caller, duration, timestamp, call status) and up to one month of SMS/MMS from `calling.db` and `phone.db` on a Windows machine when the paired Android phone itself could not be examined.
- Recovering up to 2,000 recently synced photos/screenshots from `photos.db`, noting that photos larger than 1.5 MiB are stored locally only as a downsized copy with partial EXIF metadata (only Camera Model Name and Maker fields retained).
- Identifying every Windows 10 device paired to a given smartphone, and the Microsoft cloud-account email address used for pairing, from the Android app's private `RemoteAppStore.xml.xml` and `mmxauth.xml` files.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Your Phone deletes a notification record from its local database as soon as it is acknowledged on the phone]]

## References

- [LWCite-1308] Domingues, Andrade, and Frade, 2021, "Microsoft's Your Phone environment from a digital forensic perspective", FSI: Digital Investigation 38, 301177.
