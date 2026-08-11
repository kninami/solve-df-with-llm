---
id: DFT-1075
type: technique
name: SPARQL-based cross-artifact inconsistency detection over CASE-UCO forensic knowledge graphs
description: Represent a forensic image's extracted artifacts as a CASE/UCO-ontology knowledge graph, then run reusable, schema-consistent SPARQL queries — Indicators of Inconsistency (IoIs) — against that graph to automatically detect contradictions among temporally, structurally, or semantically related artifacts (e.g. a file's recorded deletion time conflicting with its journal entries), surfacing anti-forensic tampering or other events of probative value that would otherwise require exhaustive manual cross-artifact correlation.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1081
aliases:
  - IoI framework
  - Indicator of Inconsistency
source_refs:
  - DFCite-1071
updated_at: 2026-08-10
status: complete
---

# SPARQL-based cross-artifact inconsistency detection over CASE-UCO forensic knowledge graphs

## Summary

Manually correlating heterogeneous artifacts to spot contradictions (a classic sign of anti-forensic tampering or fabricated evidence) does not scale with case volume or investigator expertise. Encoding each contradiction pattern once as a schema-consistent, case-agnostic SPARQL query (an IoI signature) against a standardized CASE/UCO ontology graph of an image's artifacts lets that detection logic be reused across cases and shared between investigators, functioning like a threat-intelligence feed but for contradictory-artifact patterns.

## Details

An investigator encodes forensic knowledge — from prior casework, public incident reports, or structured threat intelligence such as MITRE ATT&CK — as an IoI signature by mapping the relevant artifacts and relationships onto CASE/UCO ontology classes and properties. The proof-of-concept framework was evaluated against five curated anti-forensic scenarios with real artifacts, and the resulting rule set was further validated against independent third-party forensic images to measure false-positive behavior. A proposed community framework organizes this as a Central Repository of peer-reviewed IoI signatures and ontological artifact templates that investigators and tools can push to and pull from, ensuring consistent vocabulary and semantics across participants.

## Examples

- An IoI signature (IOI-002) originally flagged any `$UsnJrnl` write to a Chromium History database as corroborating evidence of tampering; after refinement to require destructive/replacement write semantics (excluding normal Chromium `DataOverwrite` behavior during ordinary browsing), overall specificity across the eight-image test corpus rose from 76% to 100% with no loss of true positives.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/IoI signatures developed on a controlled dataset produce false positives against independent third-party forensic images]]

## References

- [DFCite-1071] Gunestas et al., 2026, "An indicator of inconsistency framework for detecting contradictory digital artifacts", FSI: Digital Investigation 58.
