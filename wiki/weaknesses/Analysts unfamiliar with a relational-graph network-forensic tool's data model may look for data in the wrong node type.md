---
id: LWW-2120
type: weakness
name: Analysts unfamiliar with a relational-graph network-forensic tool's data model may look for data in the wrong node type
description: A relational-graph network-forensic tool organizes network traffic data across multiple distinct node types (e.g. host, connection, and application-data nodes), and an analyst unfamiliar with which specific node type a given piece of information is modeled under may search the wrong location within the graph, mistakenly concluding the data is absent or the tool does not support that data type at all.
categories:
  - ASTM_MISINT
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2121
source_refs:
  - LWCite-2140
updated_at: 2026-08-16
status: complete
---

# Analysts unfamiliar with a relational-graph network-forensic tool's data model may look for data in the wrong node type

## Summary

A user study of the relational-graph network-forensic interface found that participants' most significant reported difficulty was unfamiliarity with the underlying data model -- specifically, expecting certain application-layer data to be located directly within a connection node rather than in a separate, linked application-data node -- rather than any usability problem with the graph visualization or navigation mechanics themselves.

## Why It Matters

An investigator who does not find expected data at the node type they initially check risks concluding, incorrectly, that the data was not captured or that the tool lacks a needed capability, when the data is in fact present elsewhere in the graph under a different node type. Because this failure mode stems from a mismatch between the analyst's mental model and the tool's actual data model rather than from any missing capability, it can persist even for an otherwise experienced network forensic analyst who has simply not yet learned this specific tool's particular node-type organization.

## Related Mitigations

- [[mitigations/Provide a guided data-model walkthrough before an analyst uses a relational-graph network-forensic tool operationally]]

## Used By

- [[techniques/Explore network traffic forensic data using an interactive multimodal relational graph]]

## References

- [LWCite-2140] "Using relational graphs for exploratory analysis of network traffic data", FSI: Digital Investigation 48, 2024.
