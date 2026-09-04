---
id: LWT-2113
type: technique
name: Explore network traffic forensic data using an interactive multimodal relational graph
description: Support exploratory, hypothesis-driven analysis of captured network traffic by ingesting packet-capture data into a graph database and rendering it as an interactive, multimodal graph -- with distinct node types for hosts, host-level extracted data (e.g. DNS queries, certificates), individual connections, and application-layer data -- letting an analyst visually navigate relationships between hosts, sessions, and application content rather than only running fixed queries or filters over a flat packet list.
objective_ids:
  - DFO-1001
  - DFO-1009
weakness_ids:
  - LWW-2120
aliases:
  - Granef
  - Graneful
source_refs:
  - LWCite-2140
updated_at: 2026-08-16
status: complete
---

# Explore network traffic forensic data using an interactive multimodal relational graph

## Summary

Conventional network forensic tools present captured traffic as a filterable flat list or a fixed set of summary views, which supports answering pre-specified questions but is less suited to open-ended, exploratory analysis where an investigator does not yet know exactly what relationship they are looking for. Representing the same data as a relational graph -- with hosts, host-level extracted data, individual network connections, and application-layer data each as distinct, visually distinguishable node types connected by typed relationship edges -- lets an analyst visually traverse from a host of interest to its connections, from a connection to the application data it carried, and back, following whatever investigative thread emerges during examination.

## Details

Captured packet data is processed and loaded into a graph database, structured around a data model with four primary node types: host nodes (representing distinct network endpoints, e.g. by IP address), host-data nodes (data extracted and attributed to a specific host, such as DNS records or TLS certificate details), connection nodes (representing an individual network session/flow between two hosts), and application-data nodes (payload-level content extracted from a connection, such as HTTP request/response details or file transfers). An interactive web-based user interface (Graneful) renders this graph visually, letting an analyst click through from any node to its directly connected nodes, expand or collapse portions of the graph to manage visual complexity, and apply filters to focus the displayed graph on a specific subset of interest, supporting an iterative, exploratory investigative workflow.

## Examples

- A user study with participants unfamiliar with the tool measured usability via the System Usability Scale (SUS), producing an above-average score (78) indicating participants found the graph-based exploration approach reasonably intuitive despite no prior exposure to the specific tool.
- Participants in the user study were able to use the graph interface to trace relationships between a host and its associated connections and application-layer data to answer investigative scenario questions posed during the study, demonstrating the graph model's practical support for hypothesis-driven traffic analysis.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1009` Create visualizations

## Related Weaknesses

- [[weaknesses/Analysts unfamiliar with a relational-graph network-forensic tool's data model may look for data in the wrong node type]]

## References

- [LWCite-2140] "Using relational graphs for exploratory analysis of network traffic data", FSI: Digital Investigation 48, 2024.
