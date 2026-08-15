---
id: DFT-2004
type: technique
name: Structure smart-city forensic readiness using a unified process-and-concept metamodel
description: The process of resolving overlap and ambiguity across many existing smart-city/IoT digital forensic readiness frameworks by extracting their common processes and concepts and organizing them into a single high-abstraction metamodel (with UML-style concepts, attributes, operations, and relationships) that practitioners can instantiate for a specific smart-city or smart-home deployment.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-2004
aliases:
  - HADFRM
  - High abstract digital forensic readiness metamodel
source_refs:
  - DFCite-2004
updated_at: 2026-08-14
status: partial
---

# Structure smart-city forensic readiness using a unified process-and-concept metamodel

## Summary

Rather than picking one of many narrow, overlapping, and organization- or device-specific digital forensic readiness (DFR) frameworks for a smart city or smart home, an investigator or system designer uses a model-driven-engineering (MDE) metamodel that has already integrated the common processes and concepts across the existing literature, providing a single, unambiguous structure to instantiate into a concrete readiness plan or isolation/response model for the deployment at hand.

## Details

DFCite-2004 builds HADFRM through a systematic literature review (403 papers screened down to 18 included DFR-for-smart-cities models) followed by MDE-based integration: overlapping processes across the 18 source models (e.g. "Incident Identification," "Incident Response Plan," "Preparation") are merged into five common processes — Incident Response, Data Acquisition, Data Preservation, Data Analysis, and Reporting and Presentation — and 38 redundant concept labels across the sources are consolidated into single canonical concepts (e.g. ForensicExaminer, InterconnectedSystem, IoTDevice, LogFile, CCTVRecord, DigitalEvidence, ChainOfCustody, Timeline). Each concept is defined with an ID, definition, attributes, operations, and UML relationships (association, aggregation, specialization) to other concepts, so that domain practitioners can vertically transform (instantiate) the M2-level metamodel into a case-specific M1/M0 model — demonstrated in the paper by instantiating an "Isolation Model" for a smart-home cybercrime scenario using two governing rules that constrain the instantiated model to be a valid subset of the metamodel.

## Examples

- DFCite-2004's worked example: instantiating the M2-HADFRM's ForensicExaminer and InfectedSystem concepts (with the Isolates relationship) into an M1-Isolation model for a specific smart home ("SmartHome12") and examiner pair ("Lori & Victor").

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/A unified smart-city forensic readiness metamodel has not been validated against a real-world deployment or incident]]

## References

- [DFCite-2004] Alotibi, "A high abstract digital forensic readiness metamodel for securing smart cities", IEEE Access, 2024 — source of the HADFRM metamodel, its literature-integration methodology, and the smart-home isolation-model worked example.
