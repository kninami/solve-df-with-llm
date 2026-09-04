---
id: LWT-1274
type: technique
name: Deanonymize an anonymity-network hidden service by correlating node and service availability over time
description: Narrow the set of candidate nodes delivering a hidden service on an anonymity network (such as I2P) down to a small ranked list by continuously sampling every reachable node's online/offline availability alongside the target service's own availability, and ranking nodes by the Hamming Distance between each node's availability bit-sequence and the target service's, on the assumption that the node actually delivering the service will share its downtime pattern.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1284
aliases:
  - I2P monitoring infrastructure deanonymization
  - Availability-correlation deanonymization
source_refs:
  - LWCite-1312
updated_at: 2026-08-15
status: complete
---

# Deanonymize an anonymity-network hidden service by correlating node and service availability over time

## Summary

Anonymity networks encrypt communication content and obscure the ultimate sender/recipient, but they do not hide when a participating node goes on- and offline. Because a hidden service's own downtime is inherently caused by the downtime of whichever node is actually delivering it, recording every network node's availability over time as a bit-sequence and comparing it against the target service's own observed availability bit-sequence via Hamming Distance produces a ranked candidate list — with the true delivering node expected to rank at or near the top — without needing to break the network's traffic encryption or routing anonymity.

## Details

A monitoring infrastructure passively samples the network's distributed peer-to-peer node database (e.g. I2P's `netDB`, populated via `RouterInfo`/`LeaseSet` records) at a fixed interval (e.g. every minute) from multiple vantage points, recording each observed node's availability as a 0/1 bit for each time slot, and does the same for the target hidden service. The Hamming Distance between the target's availability sequence and each candidate node's sequence is computed and used to rank all observed nodes; a genuine match is expected to rank at or near the top of the distance ranking. A key practical complication is that anonymity-network node-discovery protocols apply their own expiration timeout before removing a node's record after it stops advertising availability (I2P's floodfill nodes apply a default 60-minute timeout), which obscures brief offline periods shorter than that timeout and degrades ranking accuracy; a discrete filter — erasing the preceding timeout-length window of samples whenever an online-to-offline transition is observed — compensates for this artifact where the true offline period exceeds the filter window, but cannot recover ranking accuracy for offline periods shorter than the network's own expiration timeout.

## Examples

- In a controlled experiment against the I2P network (achieving only 13-15% network visibility, with roughly 40,000 nodes observed daily), a target node with a synthetic availability pattern of long online periods separated by 60-minute-plus offline periods ranked first by Hamming Distance among all observed nodes, both with and without the discrete filter applied.
- A target node with a shorter 30-minute daily offline period could not be reliably deanonymized (ranking only 50th-58th out of roughly 1,200 unique distance values) because the offline period was shorter than I2P's default 60-minute floodfill expiration timeout, and no filter could compensate since no online-to-offline transition was ever observed by the monitoring infrastructure in the first place.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Availability-correlation deanonymization cannot detect an offline period shorter than the anonymity network's node-expiration timeout]]

## References

- [LWCite-1312] Simioni, Gladyshev, Habibnia, and de Souza, 2021, "Monitoring an anonymity network: Toward the deanonymization of hidden services", FSI: Digital Investigation 38, 301135.
