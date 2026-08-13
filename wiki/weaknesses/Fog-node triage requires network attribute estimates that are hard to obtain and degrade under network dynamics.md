---
id: DFW-1189
type: weakness
name: Fog-node triage requires network attribute estimates that are hard to obtain and degrade under network dynamics
description: Path-based centrality triage of fog computing nodes depends on the investigator being able to assess each connection's latency and bandwidth, the fog system's service-placement weighting, and each node's data volatility, but these attributes are not directly observable after the fact, must be estimated, and the resulting priority ranking degrades when the network's topology or connection quality has changed since the data was processed.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1189
source_refs:
  - DFCite-1194
updated_at: 2026-08-13
status: complete
---

# Fog-node triage requires network attribute estimates that are hard to obtain and degrade under network dynamics

## Summary

The path-based weighting model's inputs — per-connection latency and bandwidth, the fog service-placement algorithm's own weighting behavior, and each candidate node's data volatility (a function of its assumed memory size, encryption, and load) — are not something an investigator can typically read directly off a live or seized fog network; they must be estimated, and validating how sensitive the resulting node ranking is to estimation error was left as future work by the source paper. Separately, path-based computation itself was found to be expensive (over 170 hours for a 1000-node, ~2000-edge network in the reference implementation), and simulated network dynamics (changing connection attributes, edges being added/removed) measurably degraded the ranking's accuracy relative to a static snapshot.

## Why It Matters

An investigator using this triage measure without being able to accurately estimate the underlying network attributes risks prioritizing collection resources based on a ranking that does not reflect the fog system's actual behavior at the time the evidence was generated, particularly if the network has changed (nodes moved, connections degraded, load rebalanced) between the event of interest and the time of investigation. Because the absolute probability values the model produces have not themselves been validated as accurate (only the relative ordering was tested), an investigator should treat the output as a prioritization aid for which node to examine first, not as a calibrated probability to report as a finding.

## Related Mitigations

- [[mitigations/Estimate fog network attributes via active probing and re-run triage after topology changes]]

## Used By

- [[techniques/Prioritize fog computing nodes for evidence collection using graph centrality measures]]

## References

- [DFCite-1194] Sandvik et al., 2023, "Evidence in the fog - Triage in fog computing systems", FSI: Digital Investigation 44, 301506.
