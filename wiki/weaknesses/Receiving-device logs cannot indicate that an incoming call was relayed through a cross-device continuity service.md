---
id: DFW-1217
type: weakness
name: Receiving-device logs cannot indicate that an incoming call was relayed through a cross-device continuity service
description: Because call control and processing for a cross-device continuity relay is handled entirely by the primary device, the receiving device's own logs are indistinguishable from those of a standard incoming call, so an investigator with only the receiving device cannot determine whether the call was relayed.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1217
source_refs:
  - DFCite-1228
updated_at: 2026-08-13
status: complete
---

# Receiving-device logs cannot indicate that an incoming call was relayed through a cross-device continuity service

## Summary

Testing showed that ADB logcat collected from the receiving device after a Samsung Call & Message Continuity (CMC) relayed call confirmed only that a call was received and accepted; no artifact on the receiving device indicated the caller's device role or that CMC had been used at all, since from the receiving device's perspective the call is structurally identical to a standard call.

## Why It Matters

Investigators who seize only the receiving (victim) party's device in a voice-phishing case will be unable to establish that the call was placed via a covert relay, which limits the applicability of device-level relay-detection findings to cases where at least one device from the criminal organization's side (the primary or secondary device) can also be acquired; relying on the receiving device alone risks a false conclusion that a call originated normally.

## Related Mitigations

- [[mitigations/Correlate system logs from every device role in a suspected cross-device call-relay chain, not just the receiving device]]

## Used By

- [[techniques/Detect CMC-based voice-phishing call relay using Android system log artifacts]]

## References

- [DFCite-1228] Yoo, Park and Kim, 2026, "Forensic analysis of remote call service artifacts for detecting voice phishing via samsung call & message continuity (CMC)", FSI: Digital Investigation 57, 302107.
