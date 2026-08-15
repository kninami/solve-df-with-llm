---
id: DFM-1256
type: mitigation
name: Send content-blocking and takedown requests to every area of a decentralized storage service's ecosystem, not just its official gateway
source_refs:
  - DFCite-1272
updated_at: 2026-08-14
status: complete
---

# Send content-blocking and takedown requests to every area of a decentralized storage service's ecosystem, not just its official gateway

## Summary

Systematically send content-blocking or takedown requests to every party capable of continuing to distribute a piece of decentralized storage content — the official gateway, any identified third-party gateways, known pinning services, the hosting node's ISP, and cloud hosting providers where applicable — rather than assuming a single request stops distribution.

## Addresses

- [[weaknesses/Decentralized storage content persists and continues to propagate across peer and gateway areas even after a takedown request to a single service area]]

## How To Apply

During investigation, enumerate every gateway, pinning service, and hosting provider through which the target content identifier or node has been observed being served, using the same node/peer/gateway/internet-area identification methods used to find the content in the first place. Send a block or takedown request to each identified party separately, and periodically re-check whether the content identifier remains accessible through any of them after the requests are sent, since response time and compliance vary significantly by provider. Document each provider's response (or lack of one) as part of the case record, since incomplete removal across the ecosystem may itself be relevant to ongoing monitoring or follow-up legal action.

## References

- [DFCite-1272] Son, Kim, Jung, Bang and Park, 2023, "IF-DSS: A forensic investigation framework for decentralized storage services", DFRWS 2023 APAC; FSI: Digital Investigation 46, 301611.
