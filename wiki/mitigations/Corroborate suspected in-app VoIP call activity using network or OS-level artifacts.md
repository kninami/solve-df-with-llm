---
id: LWM-1214
type: mitigation
name: Corroborate suspected in-app VoIP call activity using network or OS-level artifacts
source_refs:
  - LWCite-1225
updated_at: 2026-08-13
status: complete
---

# Corroborate suspected in-app VoIP call activity using network or OS-level artifacts

## Summary

Do not conclude from an absent database call log that no in-app VoIP calling occurred; corroborate suspected call activity using network traffic captures, OS-level connection or battery/usage logs, or witness/device-owner statements instead.

## Addresses

- [[weaknesses/VoIP call activity within a messaging app is not recorded in the app's local chat database]]

## How To Apply

Before conducting an examination, test the specific app version's call-logging behavior in a controlled environment to confirm whether it records VoIP call events anywhere on the device. If it does not, and call activity is relevant to the investigation, pursue network-level evidence (packet captures, carrier/ISP records, VPN or router logs showing the relevant IP/port ranges around the time in question) or device/OS-level indicators (screen-on time, battery drain, or microphone/camera usage indicators around the suspected call time) as corroborating sources, and document explicitly in the report that the app's own database contains no call log for this reason rather than because no call occurred.

## References

- [LWCite-1225] Akinbi and Ojie, 2021, "Forensic analysis of open-source XMPP multi-client social networking apps on iOS devices", FSI: Digital Investigation 36.
