---
id: LWM-1254
type: mitigation
name: Corroborate STUN-derived WhatsApp call IP addresses with independent network or subscriber records before attribution
source_refs:
  - LWCite-1270
updated_at: 2026-08-14
status: complete
---

# Corroborate STUN-derived WhatsApp call IP addresses with independent network or subscriber records before attribution

## Summary

Before attributing a STUN-captured WhatsApp call IP address to a specific individual, confirm through ISP subscriber records and network topology knowledge whether that address is uniquely assigned to the suspect or shared across a carrier-grade NAT pool, household, or VPN service.

## Addresses

- [[weaknesses/WhatsApp call STUN-based IP extraction fails when call participants share a network or connect through carrier-grade NAT]]

## How To Apply

Request subscriber-mapping records from the relevant ISP for the captured IP address and timestamp, and check whether the ISP's allocation is a dedicated address or part of a carrier-grade NAT pool shared across many simultaneous subscribers; if shared, request port-level mapping records where available to narrow attribution to a single subscriber. Cross-check the address against known VPN provider and cloud-hosting IP ranges before treating it as the suspect's residential or mobile connection. Where the STUN capture shows a WhatsApp relay-server address rather than a participant address, note that no useful IP attribution was obtained from this call and rely on other evidence sources instead.

## References

- [LWCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
