---
id: DFM-1172
type: mitigation
name: Corroborate captured IoT command logs against independent device or cloud state records before attributing an action
source_refs:
  - DFCite-1177
updated_at: 2026-08-12
status: complete
---

# Corroborate captured IoT command logs against independent device or cloud state records before attributing an action

## Summary

Because a replayed IoT command is indistinguishable from a genuine one at the network-capture layer alone, cross-check a captured local switching-action log against an independent evidence source — device-side state history, cloud API event logs, or physical-observation timing — before attributing the action to a specific user-initiated request.

## Addresses

- [[weaknesses/Replay-attack vulnerability in local smart-relay communication undermines reliable attribution of a captured switching action]]

## How To Apply

Where a companion app or device log records a switching event, obtain a second, independently-generated record of the same event (e.g. the vendor cloud API's device event log, or the relay's own onboard state history) and confirm the timestamps and event sequence are mutually consistent before treating the captured network traffic as proof that the user (rather than a replayed packet) triggered the action. Note in the examination report when only a single, replay-vulnerable local-traffic source is available and no independent corroboration could be obtained.

## References

- [DFCite-1177] Eichhorn and Pugliese, 2024, "Do You \"Relay\" Want to Give Me Away? - Forensic Cues of Smart Relays and Their IoT Companion Apps", FSI: Digital Investigation 50, 301810.
