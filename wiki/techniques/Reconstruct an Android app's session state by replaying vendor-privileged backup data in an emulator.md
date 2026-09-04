---
id: LWT-1176
type: technique
name: Reconstruct an Android app's session state by replaying vendor-privileged backup data in an emulator
description: Convert an Android device's vendor-privileged backup or migration package into a standardized application-sandbox file tree, migrate it into a matching app installed in an Android emulator, and repair file permissions so the app launches already logged in, recovering local and cloud-synced application data without the account's credentials or network access to the source device.
objective_ids:
  - DFO-1011
weakness_ids:
  - LWW-1183
aliases:
  - SHARF (Smart Home App Reconstruction Framework)
  - Emulation-based smart home app forensics using vendor privileged Android backup
source_refs:
  - LWCite-1186
updated_at: 2026-08-12
status: complete
---

# Reconstruct an Android app's session state by replaying vendor-privileged backup data in an emulator

## Summary

Most user-relevant smart home data is not stored on the phone; it lives on the vendor's cloud servers and is only fetched and displayed by the app when logged in, so offline extraction from a seized phone alone is often insufficient. Because vendor-customized Android ROMs (e.g., Xiaomi, vivo, OPPO, Huawei/Honor) provide high-privilege backup/migration functions that export a third-party app's full `/data/data/<package_name>/` sandbox — including session tokens and cached databases — this technique replays that exported sandbox inside a forensic-workstation emulator to reconstruct the app in its original logged-in state, without ever needing the account's plaintext credentials or an internet connection to the source device.

## Details

The workflow has three stages. First (data acquisition), the target smartphone's official vendor backup/migration function (e.g., Xiaomi's "Backup & restore"/Mi Mover, vivo's "Mutual Transfer"/EasyShare, OPPO's "Phone Clone", Huawei/Honor's HiSuite or Phone Clone) is used offline to export the target app's data, avoiding any network-driven state change to the source device during acquisition. Second (structure reconstruction and semantic mapping), each vendor's backup encapsulation (extra headers such as "ANDROID BACKUP" or "MIUI BACKUP" wrapped around an internal tar structure) is stripped to a standard tar archive, then its vendor-specific internal directory layout (e.g., single-letter directories `a/`, `f/`, `sp/`, `db/`, `r/`) is mapped onto the Android application-sandbox convention (`files/`, `shared_prefs/`, `databases/`). Third (emulation execution), a version of the target app identical or compatible with the source device's version is installed in an Android emulator to generate a blank sandbox, whose user-data directory is then replaced with the reconstructed backup data before file permissions are repaired (e.g., via `adb shell chmod -R 777`) so the app can read and write its own files under its original identity; the app then launches already logged in and, within a controlled network environment, can be observed interacting with the vendor's live cloud services to recover both locally cached and cloud-synced data. Analysis of directory-level ablation experiments found that the `shared_prefs/` (authentication tokens, session cookies, device identifiers) and `databases/` (device lists, room layouts, scene rules, history) directories together are the critical data subset for reproducing a stable logged-in session; other directories (e.g., `files/`, `cache/`) hold supplementary evidentiary value (logs, cached media) but are not required for login-state continuity.

## Examples

- Validated across more than 20 Android phone models (Xiaomi, vivo, OPPO, Huawei/Honor, spanning Android 9-16) and five mainstream smart home applications, the SHARF prototype tool successfully reconstructed a logged-in emulator instance for each combination, reproducing device lists, room/scene configurations, and historical event logs consistent with the source device, and confirmed via network traffic comparison (using a Fiddler proxy) that the emulator's authenticated HTTP(S) requests and cloud server responses matched those of the original device.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Vendor-privileged Android backup emulation cannot reproduce strong-device-binding sessions for hardware-secured smart home functions]]

## References

- [LWCite-1186] Zhao et al., 2026, "Enhancing smart home forensics: An emulation-based approach utilizing vendor privileged android backup data", FSI: Digital Investigation 57.
