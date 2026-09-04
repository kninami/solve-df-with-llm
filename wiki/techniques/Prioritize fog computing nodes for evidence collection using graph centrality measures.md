---
id: LWT-1182
type: technique
name: Prioritize fog computing nodes for evidence collection using graph centrality measures
description: Rank the candidate nodes of a fog computing network by their estimated probability of containing relevant data-processing evidence, using a path-based graph-centrality measure weighted by network latency, so that limited investigative resources are directed first at the nodes most likely to yield evidence rather than searched exhaustively or arbitrarily.
objective_ids:
  - DFO-1005
weakness_ids:
  - LWW-1189
aliases:
  - Fog node evidence-location triage
  - Path-based internode weighting
source_refs:
  - LWCite-1194
updated_at: 2026-08-13
status: complete
---

# Prioritize fog computing nodes for evidence collection using graph centrality measures

## Summary

In a fog computing deployment, the node that actually processed a given piece of data can be selected dynamically from among many candidate nodes in the network, and each additional candidate location increases the collection and examination burden on an investigator with limited resources. This technique estimates each node's probability of having processed (and therefore possibly still holding) the data of interest by weighting every network path passing through it by the inverse of that path's estimated latency, since fog service-placement algorithms favor low-latency paths.

## Details

For a source (data-generating) node and a set of target (data-consuming) nodes, every non-cyclic path between them is enumerated (with a cutoff at the shortest-path length plus a margin, to bound computation on large networks) and weighted by the inverse of its total latency, itself estimated from per-edge bandwidth, message size, and propagation delay. A candidate fog node's overall weight is the sum of the weights of every enumerated path passing through it; dividing by the total weight across all candidate nodes gives each node's relative probability of having processed the data, letting an investigator rank-order nodes for collection. Compared against five standard graph-centrality measures (Degree, Betweenness, Closeness, Eigenvector, and Harmonic centrality) across three fog network topologies (complete mesh, hierarchical tree, fog-colony) and two generator types (Barabasi-Albert, Erdos-Renyi, Random Lobster), the path-based weighting consistently ranked the true server node closer to the top of the ordered candidate list, particularly for larger networks, and remained robust when network size, topology, or fog architecture varied. It also degrades gracefully rather than catastrophically under simulated network dynamics (changing edge bandwidth/delay, edges being added or removed).

## Examples

- In a five-node example network with a single low-cost path and several higher-cost paths, the internode weighting correctly identified the low-cost-path node as far more likely (62% weighted ratio) to contain the service than nodes only reachable via higher-cost paths (24% and 26%).
- Across ten runs on Barabasi-Albert networks ranging from 50 to 1000 nodes, the path-based measure's advantage over the five standard centrality measures grew more pronounced as network size increased.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Fog-node triage requires network attribute estimates that are hard to obtain and degrade under network dynamics]]

## References

- [LWCite-1194] Sandvik et al., 2023, "Evidence in the fog - Triage in fog computing systems", FSI: Digital Investigation 44, 301506.
