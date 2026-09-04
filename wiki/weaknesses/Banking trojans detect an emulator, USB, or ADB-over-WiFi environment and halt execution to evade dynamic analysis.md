---
id: LWW-1208
type: weakness
name: Banking trojans detect an emulator, USB, or ADB-over-WiFi environment and halt execution to evade dynamic analysis
description: A malware sample configured with anti-analysis "debug" checks tests for indicators of a virtualized or instrumented environment (running in an emulator, ADB-over-WiFi enabled, a USB device connected) at startup and stops operating, or prompts app removal, if any check succeeds, so dynamic analysis performed in a typical sandboxed or emulator-based environment observes none of the malware's actual malicious behavior.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1208
source_refs:
  - LWCite-1219
updated_at: 2026-08-13
status: complete
---

# Banking trojans detect an emulator, USB, or ADB-over-WiFi environment and halt execution to evade dynamic analysis

## Summary

In the analyzed banking trojan, roughly a quarter of samples had this "debug" anti-analysis mode enabled: at first launch the malware checks whether it is running on an emulator, whether ADB over WiFi is enabled, or whether a USB device is connected, and if any of these conditions hold, it stops operating and opens the device's app-settings screen rather than displaying its normal accessibility-permission prompt and beginning malicious activity.

## Why It Matters

An analyst who runs a sample only in a standard emulator or a USB-connected/ADB-debugged device — the default setup for most dynamic-analysis workflows — will see the malware apparently do nothing, and may incorrectly conclude the sample is benign, non-functional, or requires a specific trigger condition that was not identified, rather than recognizing that the analysis environment itself was detected and evaded. This is a distinct blind spot from packing or code obfuscation: the code executes but deliberately withholds its behavior based on the runtime environment.

## Related Mitigations

- [[mitigations/Analyze malware on de-instrumented or physical devices and cross-verify with static analysis when dynamic analysis is evaded]]

## Used By

- [[techniques/Decrypt a banking trojan's C2 communication by extracting its hardcoded encryption keys]]

## References

- [LWCite-1219] Schmutz et al., 2024, "Forensic analysis of hook Android malware", FSI: Digital Investigation 49.
