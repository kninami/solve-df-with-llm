---
id: LWM-1217
type: mitigation
name: Correlate system logs from every device role in a suspected cross-device call-relay chain, not just the receiving device
source_refs:
  - LWCite-1228
updated_at: 2026-08-13
status: complete
---

# Correlate system logs from every device role in a suspected cross-device call-relay chain, not just the receiving device

## Summary

When multiple devices have been seized in a voice-phishing investigation, apply the minimal-indicator artifact framework to ADB logcat data from all of them together, since relay confirmation depends on artifacts that only exist on the primary or secondary device and not on the receiving device.

## Addresses

- [[weaknesses/Receiving-device logs cannot indicate that an incoming call was relayed through a cross-device continuity service]]

## How To Apply

Collect ADB logcat (preferred over dumpstate/logcat for coverage) from every seized device. Prioritize devices whose logs show both a CMC-state indicator and a call-attempt indicator occurring consecutively within a short time window, since this combination suggests involvement in call relaying. Perform a detailed follow-up examination of those prioritized devices for call-delegation-specific artifacts (e.g. `SecondConnectionService` binding, `isLocalInvocation` flags) to determine each device's role (primary vs. secondary) in the relay chain, and extract victim phone numbers and paired-device identifiers to reconstruct the full call flow. Treat a receiving-device-only acquisition as evidence only of call occurrence, not of relay method, and combine device-level findings with network-level packet analysis (e.g. RTP timing/SSRC anomalies) where live capture was possible, since the two approaches are complementary rather than substitutable.

## References

- [LWCite-1228] Yoo, Park and Kim, 2026, "Forensic analysis of remote call service artifacts for detecting voice phishing via samsung call & message continuity (CMC)", FSI: Digital Investigation 57, 302107.
