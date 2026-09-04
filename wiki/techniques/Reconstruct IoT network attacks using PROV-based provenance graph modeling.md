---
id: LWT-1294
type: technique
name: Reconstruct IoT network attacks using PROV-based provenance graph modeling
description: Reconstruct and correlate evidence of a link-layer or network-layer attack against an IoT network by modeling the network's activity as a provenance graph — using the W3C PROV data model and PROV-TEMPLATE standard to represent nodes, interactions, and events — built from collected network traffic and provenance logs, then querying the resulting graph to extract an attack subgraph and its correlated forensic artifacts, addressing the correlation challenge that stealthy sub-application-layer attacks often go undetected by device- or platform-centric IoT forensic approaches.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1304
aliases:
  - ProvLink-IoT
  - ProvNet-IoT
  - Link-IoT dataset
source_refs:
  - LWCite-1340
  - LWCite-1341
updated_at: 2026-08-15
status: complete
---

# Reconstruct IoT network attacks using PROV-based provenance graph modeling

## Summary

Most existing IoT provenance-based forensic solutions are device-centric or platform-centric, addressing only application-layer attacks, which lets stealthy attacks at the MAC, network, or other sub-layers alter device behavior without detection. Provenance — the documented origin, history, and lineage of an object, formalized here via the W3C PROV data model — applied to network parameters and traffic captured across an IoT network's protocol stack establishes structured relationships among a series of interactions that exhibit malicious behavior, letting an investigator correlate scattered network artifacts into a coherent, forensically sound reconstruction of an attack.

## Details

**Link-layer (ProvLink-IoT)**: targets the link layer of Low-Power Lossy Networks using the 6TiSCH protocol stack (IEEE 802.15.4e TSCH MAC mode plus the 6top management sublayer). Provenance graphs are generated under both benign and attack scenarios from provenance logs and network traffic collected in a simulated 6TiSCH environment, using PROV-DM and PROV-TEMPLATE to model the relationships. Three link-layer attacks targeting the TSCH and 6top layers were implemented to study their impact and validate the model's forensic analysis capability, and a companion dataset, Link-IoT, was generated from the collected network provenance for reuse in further incident and forensic analysis. The model's performance impact on the IoT network itself was analyzed in terms of provenance growth rate and storage overhead, since provenance collection is itself an ongoing burden on resource-constrained devices. **Network-layer (ProvNet-IoT)**: targets general network-level attacks using information, functional, and event modeling techniques to depict interactions between different nodes at the network layer, using "progressive network provenance" to explain the sequence of events pertaining to various attack scenarios. Provenance graphs generated this way are statistically analyzed to identify recurring patterns and a discriminating feature list, and the graph is queried to extract an attack subgraph correlated with the underlying artifacts to produce forensically sound evidence. ProvNet-IoT was validated against two publicly available labeled IoT datasets with a corpus of different attacks (Edge-IIoT and the IoT Network Intrusion Dataset), rather than a single simulated environment, demonstrating the model's applicability beyond the link-layer-specific 6TiSCH testbed.

## Examples

- Implementing and detecting three distinct link-layer attacks against the TSCH/6top sublayers of a simulated 6TiSCH network validated that ProvLink-IoT's provenance graphs could correlate evidence relevant to sub-application-layer attacks that device-centric approaches would not observe.
- ProvNet-IoT's evaluation against the Edge-IIoT and IoT Network Intrusion datasets — rather than a single custom testbed — demonstrated that querying a generated provenance graph could reliably extract an attack subgraph and correlate it with underlying network artifacts across different, independently-labeled attack corpora.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/IoT network provenance collection imposes growing storage and processing overhead on resource-constrained devices]]

## References

- [LWCite-1340] Sadineni, Pilli, and Battula, 2023, "ProvLink-IoT: A novel provenance model for Link-Layer Forensics in IoT networks", FSI: Digital Investigation 46, 301600.
- [LWCite-1341] Sadineni, Pilli, and Battula, 2022, "ProvNet-IoT: Provenance based network layer forensics in Internet of Things", FSI: Digital Investigation 43, 301441.
