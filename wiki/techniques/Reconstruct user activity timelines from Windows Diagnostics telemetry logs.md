---
id: LWT-1156
type: technique
name: Reconstruct user activity timelines from Windows Diagnostics telemetry logs
description: Parse the EventTranscript.db SQLite database used by the built-in Windows Diagnostics (DiagTrack) service to recover and correlate USB storage device attach/detach events, Edge web-browser activity (launch, tab creation/closure, sites visited), and wireless network scan/connect/disconnect events into a per-device user-behavior timeline.
objective_ids:
  - DFO-1017
  - DFO-1001
weakness_ids:
  - LWW-1160
aliases:
  - EventTranscript.db behavioral log analysis
  - DiagAnalyzer
source_refs:
  - LWCite-1163
updated_at: 2026-08-12
status: complete
---

# Reconstruct user activity timelines from Windows Diagnostics telemetry logs

## Summary

Windows 10 and 11 record detailed diagnostic telemetry — including USB device connection history, built-in Edge browser activity, and wireless network activity — in a SQLite3 database at `%ProgramData%\Microsoft\Diagnosis\EventTranscript\EventTranscript.db`, whose `events_persisted` table stores each event's name, timestamp, logging process, and a JSON-encoded payload. Systematically extracting and correlating these events reconstructs a timestamped user-behavior timeline that is independent of, and complements, conventional Windows and browser artifacts.

## Details

Each event's JSON `payload` field records fields such as the recording process's OS/OS-version, device manufacturer/model, and timezone, alongside event-specific data. USB attach is identifiable from a sequential chain of events beginning with `Microsoft.Windows.Storage.Classpnp.DeviceGuidGenerated` and ending with `Microsoft.Windows.Storage.StorageService.SdCardStatus`, recording device manufacturer, model, serial number, filesystem, and mount volume; detach is marked by `Microsoft.Windows.Storage.Classpnp.DeviceRemoved` followed by a filesystem-specific surprise-removal event. Edge browser activity is tracked through `Aria.<str>.Microsoft.WebBrowser.HistoryJournal.*` events for browser launch/close and tab creation/closure (each closure event records the number of tabs that were open), and through `HJ_BeforeNavigateExtended`/`HJ_HistoryAddUrl`/`HJ_NavigateCompleteExtended`/`HJ_HistoryAddUrlEx` events sharing a common `CorrelationGuid` for each site visited, recording the URL, page title, and connection type. Wireless network activity is tracked via `WlanMSM.WirelessScanResults` (nearby APs' SSID/BSSID), connection-attempt events recording success/failure codes, and `Wlanvc.WlanDisconnect`, with connected/disconnected AP SSID and BSSID optionally cross-referenced against public wardriving databases (e.g. WiGLE-style SSID/BSSID lookup services) to approximate the device's physical location and dwell time at a given point in time.

## Examples

- The DiagAnalyzer tool parses an extracted `EventTranscript.db` and generates an HTML report with three timeline graphs (USB device attach/detach, browser started/tab-created/tab-closed/browser-closed/visit events, and WiFi scan/connect/disconnect events), each event annotated with its extracted metadata on hover.
- Combining the recovered USB attach/detach timestamps with shellbag and link-file artifacts can help establish exactly when a removable storage device was connected during a suspected data-leakage incident.
- Combining recovered wireless AP SSID/BSSID connection events with a public AP-geolocation lookup service can help establish how long a device's user remained in the vicinity of a given public or private wireless network.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system
- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Windows Diagnostics omits activity recorded outside optional data collection or the default browser]]

## References

- [LWCite-1163] Park and Lee, 2022, "DiagAnalyzer: User behavior analysis and visualization using Windows Diagnostics logs", FSI: Digital Investigation 43, 301450.
