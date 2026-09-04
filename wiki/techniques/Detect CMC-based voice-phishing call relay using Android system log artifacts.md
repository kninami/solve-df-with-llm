---
id: LWT-1206
type: technique
name: Detect CMC-based voice-phishing call relay using Android system log artifacts
description: Identify that a voice call was covertly relayed through a Samsung Call & Message Continuity (CMC) connection — rather than placed directly by the local dialer — by correlating a minimal, sequential set of device-level dumpstate/logcat and ADB logcat artifacts recorded on the secondary and primary devices involved.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1217
aliases:
  - CMC voice-phishing artifact detection
  - Samsung Call & Message Continuity abuse detection
source_refs:
  - LWCite-1228
updated_at: 2026-08-13
status: complete
---

# Detect CMC-based voice-phishing call relay using Android system log artifacts

## Summary

Voice-phishing organizations increasingly abuse Samsung's Call & Message Continuity (CMC) feature to place calls from an overseas secondary device (SD) through a domestically located, USIM-equipped primary device (PD), so the receiving party sees a legitimate local caller ID. Because this activity leaves no trace distinguishable from a normal call on the receiving device, detection requires collecting and correlating device-level logs from the SD and/or PD rather than relying on network-level packet analysis alone.

## Details

The method classifies candidate log entries by indicator strength: "Strong" indicators (e.g., the `SecondConnectionService`/`ConnectionServiceWrapper` binding on the SD, and the `isLocalInvocation: false` flag together with `SamsungUserCallActivity` launched by the Telecom framework on the PD) appear only during CMC-relayed calls; "Supporting" indicators (e.g., `cmc_activation`/`cmc_call_activation` state transitions) confirm CMC configuration but not relay by themselves; "Insufficient" indicators are generic call-state events observed in both scenarios. An investigator applies these sequentially — call-attempt indicator, connection-verification/delegation indicator, CMC-state indicator, call-success indicator — across whichever of the SD or PD is available, since a single isolated log entry can also appear during benign CMC use. ADB logcat is markedly more informative than dumpstate/logcat: dumpstate/logcat on the PD shows no CMC-specific artifacts at all, and on the SD only reveals RCS-related entries and a `CallLogProvider[mdecservice]` package reference. The technique also generalizes as a first-pass pilot to other remote-control-based spoofing mechanisms: Microsoft's Link to Windows produces `WindowsLink`-tagged ADB logcat entries and Bluetooth audio rerouting to the connecting PC's name, and TeamViewer produces periodic TeamViewer-related ADB logcat entries correlated in time with a network-captured host connection ID, though neither of these secondary vectors was validated as rigorously as the primary CMC analysis.

## Examples

- On the secondary device (SD), the `cmc_activation` field transitioning from `off` to `on` together with a subsequent `ServiceBinder` reference to `com.samsung.android.secondconnection.SecondConnectionService` confirmed that an outgoing call was delegated to the primary device rather than handled locally.
- On the primary device (PD), the ADB logcat entry `isLocalInvocation: false` accompanying the launch of `SamsungUserCallActivity` confirmed that the call was triggered externally by the SD rather than through direct interaction with the PD's own dialer.
- Comparing dumpstate/logcat and ADB logcat coverage across device roles showed that only ADB logcat on the SD or PD reliably exposed CMC-specific artifacts, while dumpstate/logcat only partially exposed them on the SD and not at all on the PD.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Receiving-device logs cannot indicate that an incoming call was relayed through a cross-device continuity service]]

## References

- [LWCite-1228] Yoo, Park and Kim, 2026, "Forensic analysis of remote call service artifacts for detecting voice phishing via samsung call & message continuity (CMC)", FSI: Digital Investigation 57, 302107.
