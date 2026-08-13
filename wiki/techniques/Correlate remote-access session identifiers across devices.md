---
id: DFT-1018
type: technique
name: Correlate remote-access session identifiers across devices
description: Establish that two specific devices connected via a remote-access application by matching the persistent application-assigned client identifier that each endpoint's local logs record about the other party, even when only one of the two devices is available for examination.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1018
  - DFW-1151
aliases:
  - Remote-access session cross-device identifier correlation
  - AnyDesk-ID correlation
  - TeamViewer ID correlation
source_refs:
  - DFCite-1012
  - DFCite-1148
updated_at: 2026-08-12
status: complete
---

# Correlate remote-access session identifiers across devices

## Summary

Remote-access applications such as AnyDesk and TeamViewer assign each installation a persistent numeric client ID that is not deleted by default on uninstall. During a session, both the initiating and receiving device log details about the *other* party's client ID (e.g., in connection-trace, chat, and device-configuration log files), so an examiner who only has access to one device's storage can still identify the specific remote party it connected to and, from that party's own logs (if later obtained), corroborate the connection independently.

## Details

Files such as `ad.trace`/`anydesk.trace` (device logs), `user.conf`, `system.conf`, `connection_trace.txt`, and chat `.txt` files each embed the counterpart's client ID alongside timestamps, device make/model, alias, and connection direction (incoming/outgoing). Because this information is mutually and independently recorded by both endpoints, cross-referencing a suspect's device log against a victim's (or vice versa) provides two independent evidentiary records of the same event, strengthening attribution beyond what either device's data would support alone. Thumbnail/wallpaper images, screenshots, and session recordings are likewise stored on both devices, each depicting the *other* party's screen or wallpaper, providing further mutual corroboration.

TeamViewer implements the same mutual-ID-recording pattern across Windows and Android: `rolloutfile.tv13` records the local device's own 10-digit TeamViewer ID, while `Connections.txt` (disk) and each side's `.tvc` configuration file record the counterpart's ID together with the connection's start/end time, direction, and a unique session ID, for both the "Windows controls Android" and "Android controls Windows" connection scenarios. Registry and process-memory artifacts on Windows, and `client.conf`/`connection.txt`/`TVLog.html` on Android, provide further independent copies of the same pairing information.

## Examples

- A Windows PC's `system.conf` file contained the Android device's AnyDesk-ID (`705849768`), while the Android device's own `system.conf` contained the PC's AnyDesk-ID (`1120187527`), independently confirming the pairing from both sides.
- A Windows machine's TeamViewer ID (`1653010513`) and an Android device's TeamViewer ID (`1652949632`) were each independently recoverable from `rolloutfile.tv13` on their own device and from `Connections.txt`/the counterpart's `.tvc` file on the other, confirming the pairing and session timing from both sides.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/AnyDesk-ID becomes unrecoverable if configuration files are deleted without a backup]]
- [[weaknesses/Remote-access application logs fail to record all session actions consistently across platforms]]

## References

- [DFCite-1012] Soni et al., 2024, "A forensic analysis of AnyDesk Remote Access application by using various forensic tools and techniques", FSI: Digital Investigation 48.
- [DFCite-1148] Soni, Kaur and Aziz, 2024, "Decoding digital interactions: An extensive study of TeamViewer's Forensic Artifacts across Windows and android platforms", FSI: Digital Investigation 51. Confirms the same mutual-ID cross-device correlation pattern for TeamViewer across Windows and Android, via `rolloutfile.tv13`, `Connections.txt`, and per-device `.tvc` configuration files.
