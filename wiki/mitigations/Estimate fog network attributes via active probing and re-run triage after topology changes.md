---
id: DFM-1189
type: mitigation
name: Estimate fog network attributes via active probing and re-run triage after topology changes
source_refs:
  - DFCite-1194
updated_at: 2026-08-13
status: complete
---

# Estimate fog network attributes via active probing and re-run triage after topology changes

## Summary

Estimate the connection-latency and bandwidth inputs a fog-node triage ranking needs by actively probing the network (or by using known network-type/distance characteristics as a proxy) rather than assuming precise values, treat the resulting ranking as an ordering aid rather than a calibrated probability, and re-run the prioritization whenever the fog network's topology or connection quality is known to have changed materially since the event of interest.

## Addresses

- [[weaknesses/Fog-node triage requires network attribute estimates that are hard to obtain and degrade under network dynamics]]

## How To Apply

Where direct measurement of a fog network's connections is possible (e.g. via seized network configuration, provider-supplied topology data, or live probing of accessible portions of the network), use it to populate the latency/bandwidth inputs to the path-based weighting model; where not, fall back to characteristic values for the network type and inter-node distance involved, and document that the resulting ranking is estimate-based rather than measured. Bound the computational cost on large networks by restricting path enumeration to a cutoff near the shortest-path length, since this optimization did not meaningfully harm ranking accuracy in testing. Because the ranking's accuracy degrades as the network's actual state diverges from the state used to compute it, re-run the prioritization using the most current available network-attribute snapshot rather than relying on a ranking computed well before or after the event of interest, and treat the node ordering as a resource-prioritization aid rather than a validated probability of evidence presence when reporting findings.

## References

- [DFCite-1194] Sandvik et al., 2023, "Evidence in the fog - Triage in fog computing systems", FSI: Digital Investigation 44, 301506.
