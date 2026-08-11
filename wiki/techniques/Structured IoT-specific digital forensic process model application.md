---
id: DFT-1049
type: technique
name: Structured IoT-specific digital forensic process model application
description: Investigate an IoT-related incident using a formal, phased digital forensic process model (identification, preservation, collection, examination, analysis, presentation) purpose-built or adapted for IoT's distinguishing characteristics — heterogeneous devices and protocols, high data volatility, resource-constrained hardware, and distributed architectures — rather than applying a general-purpose digital forensics process model unchanged.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-1050
  - DFW-1080
aliases: []
source_refs:
  - DFCite-1040
  - DFCite-1070
updated_at: 2026-08-10
status: complete
---

# Structured IoT-specific digital forensic process model application

## Summary

A systematic literature review of 23 IoT-specific digital forensic process models, frameworks, conceptual models, and ontologies published between 2015 and 2024 found that roughly half used a "framework" style (organized, systematic structure for scalability and complexity handling) and nearly half used "concept templates" (semantic descriptions mapping forensic data such as sensor information, communication data, and logs), while methodologies proper (documented step-by-step procedures) were comparatively rare, together reflecting the diversity of approaches taken to adapt general digital forensic process theory to IoT's specific technical constraints.

## Details

Reviewed models varied in which of the six standard forensic phases (identification, preservation, collection, examination, analysis, presentation) they explicitly addressed and treated as critical: across the 23 studies, examination (65.22%) and preservation (60.87%) were most frequently flagged as critical or challenging phases, while identification (26.09%) was least frequently addressed in depth — several works note this is likely because the diversity and volume of IoT devices makes it a genuinely harder problem, not because it is less important. A smaller subset of reviewed models incorporate blockchain architecture (for evidence immutability and traceability) or formal ISO/IEC 27043:2015 alignment, and models varied in whether they addressed data privacy considerations distinct from evidence integrity.

## Examples

- Models reviewed include a fog-based IoT forensics investigation framework using middleware inspired by the 2001 DFRWS process model, an ISO/IEC 27043:2015-aligned generic digital forensic investigation framework for IoT, and a blockchain-based evidence framework using a graphical model to transform raw IoT device data into traceable, security-enhanced forensic information for police investigation.
- SIIFF (Service-Interconnectivity-based IoT Forensics Framework) extends the standard phase set with two additional phases — Identification of Interconnectivity and Integration and Correlation — run iteratively after the interpretation phase: an interconnectivity module examines interpreted evidence for signs that other IoT services or devices were involved, optionally triggers acquisition of new input data about those newly-identified things, and stores discovered relationships (source, target, and connection weight) in a normalized database for correlation with other identifiers (e.g. usernames, IDs, emails) during analysis. Applied to six interconnected-device scenarios on an Android companion-device, this recovered relationships such as an IFTTT automation linking a Twitter post to an Instagram cross-post.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/Most published IoT digital forensic process models lack chain-of-custody support and empirical validation]]
- [[weaknesses/IoT interconnectivity identification finds no relationship when the connected service retains no interconnection traces]]

## References

- [DFCite-1040] Silva et al., 2025, "A review study of digital forensics in IoT: Process models, phases, architectures, and ontologies", FSI: Digital Investigation 53.
- [DFCite-1070] Kim et al., 2022, "An improved IoT forensic model to identify interconnectivity between things", FSI: Digital Investigation 44.
