---
id: DFM-1211
type: mitigation
name: Treat Matrix unsigned object fields as corroborating evidence only, not as authoritative on their own
source_refs:
  - DFCite-1223
updated_at: 2026-08-13
status: complete
---

# Treat Matrix unsigned object fields as corroborating evidence only, not as authoritative on their own

## Summary

Rely on the signed `origin_server_ts` field as the authoritative send-time for a Matrix message event, and use the unsigned `age`/`transaction_id` fields only as supporting, corroborating detail rather than as an independently trustworthy source.

## Addresses

- [[weaknesses/Matrix protocol unsigned timestamp and transaction fields can be altered after message-event signing without detection]]

## How To Apply

When reconstructing a Matrix conversation timeline, anchor conclusions about when a message was sent to the server on `origin_server_ts`, and independently verify the Matrix homeserver's own clock accuracy where feasible (e.g. by sending a controlled test message and comparing the noted time). Use `age` and `transaction_id` values to corroborate a download time or sender-client inference, but note in the examination report that these fields are not covered by the event's cryptographic signature and could theoretically have been altered after the event was created, particularly where the event data was obtained from a source other than direct client export.

## References

- [DFCite-1223] Schipper et al., 2021, "Forensic analysis of Matrix protocol and Riot.im application", FSI: Digital Investigation 36.
