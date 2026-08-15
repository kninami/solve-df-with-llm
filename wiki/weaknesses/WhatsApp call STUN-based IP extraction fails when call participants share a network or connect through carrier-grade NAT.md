---
id: DFW-1253
type: weakness
name: WhatsApp call STUN-based IP extraction fails when call participants share a network or connect through carrier-grade NAT
description: STUN-derived IP addresses only reflect the public-facing address a device's network path presents, so the technique cannot distinguish individual subscribers behind carrier-grade NAT or a shared WiFi/VPN gateway, and produces no useful attribution at all if WhatsApp instead relays the call through its own relay servers rather than establishing a direct peer-to-peer path.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-1254
source_refs:
  - DFCite-1270
updated_at: 2026-08-14
status: complete
---

# WhatsApp call STUN-based IP extraction fails when call participants share a network or connect through carrier-grade NAT

## Summary

A STUN-derived public IP address identifies a network egress point, not an individual person or device: many mobile subscribers behind the same carrier's carrier-grade NAT, or many devices behind the same home/office router or VPN exit, can present an identical public IP address, and if WhatsApp's call-establishment logic falls back to relaying the call through its own servers instead of a direct peer-to-peer path, the STUN exchange may not expose either participant's true address at all.

## Why It Matters

An investigator treating a STUN-captured IP address as uniquely identifying a suspect risks misattributing a call to the wrong individual within a shared-NAT population, or wasting investigative effort chasing an address that turns out to belong to a VPN provider or WhatsApp's own relay infrastructure rather than the suspect's actual connection. The failure mode is silent — the capture and parsing succeed and produce a plausible-looking IP address either way, giving no direct signal that the result is unreliable.

## Related Mitigations

- [[mitigations/Corroborate STUN-derived WhatsApp call IP addresses with independent network or subscriber records before attribution]]

## Used By

- [[techniques/Identify WhatsApp call participant IP addresses using STUN traffic analysis]]

## References

- [DFCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
