---
id: DFM-2121
type: mitigation
name: Provide a guided data-model walkthrough before an analyst uses a relational-graph network-forensic tool operationally
source_refs:
  - DFCite-2140
updated_at: 2026-08-16
status: complete
---

# Provide a guided data-model walkthrough before an analyst uses a relational-graph network-forensic tool operationally

## Summary

Before an analyst relies on a relational-graph network-forensic tool for casework, walk them through the tool's specific node-type data model with a worked example, so they know which node type to check for a given category of information before assuming it is absent.

## Addresses

- [[weaknesses/Analysts unfamiliar with a relational-graph network-forensic tool's data model may look for data in the wrong node type]]

## How To Apply

Provide new users with a short guided tutorial or example case walkthrough that explicitly demonstrates where each major data category (host information, connection/session details, application-layer content) is located within the tool's specific graph data model, before relying on their independent use of the tool for casework. Maintain a quick-reference guide mapping common investigative questions ("where is the HTTP request content for this connection?") to the specific node type/traversal path that answers them, so an analyst mid-investigation can quickly self-correct rather than concluding data is missing. Collect and act on user-reported instances of "expected but couldn't find" data during tool rollout, since these are a direct signal of where the data model's organization diverges from analysts' natural expectations and could be improved or better documented.

## References

- [DFCite-2140] "Using relational graphs for exploratory analysis of network traffic data", FSI: Digital Investigation 48, 2024.
