---
id: LWT-1236
type: technique
name: Identify WhatsApp call participant IP addresses using STUN traffic analysis
description: Capture network traffic during a live WhatsApp voice or video call and extract each participant's public IP address from the unencrypted STUN (Session Traversal Utilities for NAT) protocol messages WhatsApp exchanges while establishing the peer-to-peer call connection.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1253
aliases:
  - WhatsApp call IP extraction via STUN
source_refs:
  - LWCite-1270
updated_at: 2026-08-14
status: complete
---

# Identify WhatsApp call participant IP addresses using STUN traffic analysis

## Summary

WhatsApp voice and video calls attempt a direct peer-to-peer connection and use the STUN protocol to help each participant's device discover its own public-facing IP address and port for that purpose; because STUN messages are not end-to-end encrypted the way call content is, capturing network traffic during an active call and parsing its STUN packets can reveal both call participants' public IP addresses.

## Details

The investigator (or a cooperating network operator) captures packet traffic from a device involved in, or positioned to observe, a live WhatsApp call and filters for STUN protocol traffic, which uses a well-known message format regardless of the surrounding encrypted call payload. Each STUN Binding Request/Response exchange reveals the sending device's observed public IP address and port, giving the investigator the network-level location information needed to correlate a WhatsApp account with a specific internet connection or, via ISP subscriber records, a specific subscriber. The technique only works while a call is actively in progress and requires network-level capture positioning (e.g. a lawful-intercept tap, a monitored WiFi access point, or a cooperating carrier), not merely device-level access to a phone.

## Examples

- Capturing traffic from a monitored network during a live WhatsApp video call revealed STUN Binding messages containing the public IP addresses of both call participants, despite the call's audio/video payload remaining end-to-end encrypted.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/WhatsApp call STUN-based IP extraction fails when call participants share a network or connect through carrier-grade NAT]]

## References

- [LWCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
