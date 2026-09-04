---
id: LWM-1116
type: mitigation
name: Cross-validate CGN log subscriber attributions against overlapping-session and data-volume consistency checks before use as sole evidence
source_refs:
  - LWCite-1109
updated_at: 2026-08-12
status: complete
---

# Cross-validate CGN log subscriber attributions against overlapping-session and data-volume consistency checks before use as sole evidence

## Summary

Before treating a CGN/NAT log's subscriber attribution as reliable evidence, check the underlying session records for internal inconsistencies — overlapping session times, missing mandatory fields, colliding port ranges, and technically implausible data-volume/duration combinations — that indicate the log itself may be flawed, and do not rely on a CGN log attribution as the sole basis for identifying a suspect.

## Addresses

- [[weaknesses/CGN and NAT reverse-tracking misattributes subscribers when overlapping port-assignment errors are undetected in deterministic NAT logs]]

## How To Apply

Scan the full set of a subscriber's logged sessions for the relevant time window for overlapping session start/end times, sessions missing required fields (such as cellular network information), and sessions whose reported upload/download volumes are inconsistent with their duration or connection type — any of which is a red flag for erroneous or ambiguous log entries rather than a genuine, uniquely attributable session. Where the ISP uses deterministic NAT, request and independently verify the port-range allocation parameters for the relevant public IP address and time window to rule out port-jumping (overlapping concurrent port assignments to different subscribers). Treat a CGN log attribution as corroborating evidence requiring independent support, not as standalone proof of subscriber identity, particularly in cases carrying severe legal consequences.

## References

- [LWCite-1109] Gözükara, 2021, "Challenges and possible severe legal consequences of application users identification from CNG-Logs", FSI: Digital Investigation 39.
