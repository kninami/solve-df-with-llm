---
id: DFW-1284
type: weakness
name: Availability-correlation deanonymization cannot detect an offline period shorter than the anonymity network's node-expiration timeout
description: A monitoring infrastructure that observes node availability through a network's own peer-discovery database inherits that database's built-in expiration timeout, so a target's offline period shorter than the timeout produces no observable online-to-offline transition at all, making it indistinguishable from continuous availability and collapsing the Hamming Distance ranking's accuracy for short-downtime targets.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1285
source_refs:
  - DFCite-1312
updated_at: 2026-08-15
status: complete
---

# Availability-correlation deanonymization cannot detect an offline period shorter than the anonymity network's node-expiration timeout

## Summary

Peer-discovery databases such as I2P's `netDB` only remove a node's record after a fixed expiration timeout (60 minutes by default for floodfill nodes) elapses since the node last advertised itself, regardless of how briefly the node was actually offline. When a target's true offline periods are shorter than this timeout (e.g. 30 minutes daily), the node never appears to leave the database at all, so the monitoring infrastructure observes continuous availability and no correction — including the discrete-filter approach that compensates for longer offline periods — can recover the missing downtime signal.

## Why It Matters

An investigator applying availability-correlation deanonymization against a target with short, frequent offline periods will see substantially degraded ranking accuracy (the true delivering node ranking only in the top several percent of candidates rather than first) and may wrongly conclude the technique is inapplicable or that no reliable candidate exists, when in fact the underlying cause is the network's own expiration-timeout granularity rather than a flaw in the correlation approach itself.

## Related Mitigations

- [[mitigations/Apply a discrete filter to compensate for anonymity-network node-expiration timeout noise before correlating availability patterns]]

## Used By

- [[techniques/Deanonymize an anonymity-network hidden service by correlating node and service availability over time]]

## References

- [DFCite-1312] Simioni, Gladyshev, Habibnia, and de Souza, 2021, "Monitoring an anonymity network: Toward the deanonymization of hidden services", FSI: Digital Investigation 38, 301135.
