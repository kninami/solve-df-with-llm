---
id: DFM-1285
type: mitigation
name: Apply a discrete filter to compensate for anonymity-network node-expiration timeout noise before correlating availability patterns
source_refs:
  - DFCite-1312
updated_at: 2026-08-15
status: complete
---

# Apply a discrete filter to compensate for anonymity-network node-expiration timeout noise before correlating availability patterns

## Summary

Before computing Hamming Distance rankings for availability-correlation deanonymization, apply a discrete filter that treats the samples preceding an observed online-to-offline transition as offline for a window equal to the network's own node-expiration timeout, correcting for the artificial delay the expiration mechanism introduces between a node's actual and observed offline periods.

## Addresses

- [[weaknesses/Availability-correlation deanonymization cannot detect an offline period shorter than the anonymity network's node-expiration timeout]]

## How To Apply

Determine the target anonymity network's node/service expiration timeout (e.g. I2P floodfill nodes default to 60 minutes). Whenever the monitoring infrastructure observes an online-to-offline transition for a candidate node, retroactively mark the preceding samples covering that timeout window as offline before computing Hamming Distance against the target service's availability sequence. Recognize the residual limitation this does not resolve: where the target's true offline periods are shorter than the network's expiration timeout, no transition is ever observed in the first place, and no post-hoc filter can recover the missing signal — in that scenario, either increase monitoring network visibility, or (where within scope and permitted) investigate whether the network's own node software's expiration timeout can be legitimately reduced for the observation.

## References

- [DFCite-1312] Simioni, Gladyshev, Habibnia, and de Souza, 2021, "Monitoring an anonymity network: Toward the deanonymization of hidden services", FSI: Digital Investigation 38, 301135.
