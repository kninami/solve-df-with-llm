---
id: DFW-1211
type: weakness
name: Matrix protocol unsigned timestamp and transaction fields can be altered after message-event signing without detection
description: The Matrix message-event `unsigned` JSON object, which holds the `age` and `transaction_id` fields, is deliberately excluded from the event's cryptographic signing process, so its contents can in principle be modified after the event was originally created and signed without invalidating the event or leaving a visible sign of tampering.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1211
source_refs:
  - DFCite-1223
updated_at: 2026-08-13
status: complete
---

# Matrix protocol unsigned timestamp and transaction fields can be altered after message-event signing without detection

## Summary

By protocol design, the `unsigned` object's key-value pairs are excluded from the message-event signing process, meaning they are not covered by the same integrity guarantee that protects the rest of the event; this applies to both the server-updated `age` field and the client-generated `transaction_id` field.

## Why It Matters

Because `age` and `transaction_id` are not part of the signed content, an investigator cannot treat them with the same evidentiary confidence as `origin_server_ts` or the message body itself — a party with the ability to modify stored event data (e.g., someone with server-side access, or manipulated exported data) could alter these fields without the event's signature becoming invalid, so any conclusion drawn from them (such as inferring a client computer's clock accuracy from `transaction_id`) should be corroborated rather than relied upon alone.

## Related Mitigations

- [[mitigations/Treat Matrix unsigned object fields as corroborating evidence only, not as authoritative on their own]]

## Used By

- [[techniques/Determine Matrix message send and download times using origin_server_ts and unsigned age fields]]

## References

- [DFCite-1223] Schipper et al., 2021, "Forensic analysis of Matrix protocol and Riot.im application", FSI: Digital Investigation 36.
