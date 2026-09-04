---
id: LWT-1051
type: technique
name: Map cyber threats and evidence using a domain-specific infrastructure ontology
description: Extend a general-purpose cyber-investigation ontology (built on STIX/UCO/CASE) with a domain-specific profile that models a particular infrastructure type's own components, threats, and cybercrime classifications, so an investigator can quickly determine which components of that infrastructure were affected, what threats and cybercrime types apply, and what evidence and indicators correspond, rather than manually researching and mapping this context for every incident from scratch.
objective_ids:
  - DFO-1012
weakness_ids:
  - LWW-1053
aliases:
  - Domain-specific infrastructure ontology for cyber-threat and evidence mapping
  - SCOPE ontology
  - Smart City Ontological Paradigm Expression
source_refs:
  - LWCite-1043
updated_at: 2026-08-09
status: complete
---

# Map cyber threats and evidence using a domain-specific infrastructure ontology

## Summary

General-purpose cyber-investigation ontologies such as the Unified Cyber Ontology (UCO) and the Cyber-investigation Analysis Standard Expression (CASE) support cross-tool information sharing but lack terminology and structure specific to particular complex infrastructure domains — for example, Smart City Infrastructure (SCI), which spans citizen services, essential services, livelihood support, and resource systems each with their own component technologies. A domain-specific extension ontology fills this gap by defining infrastructure components, domain-specific threats, cybercrime classifications, data indicators, and roles as first-class ontology classes layered on top of the general-purpose ontology, while integrating established attack-technique catalogs (e.g., MITRE ATT&CK and CAPEC) for consistency with existing threat-intelligence tooling.

## Details

The ontology is built via a standard ontology-engineering process (determine domain/scope, consider existing ontologies to extend, enumerate important domain terms, define class hierarchy, define properties, define value facets/cardinality, create instances), implemented in a description-logic-backed editor (e.g., Protégé) using OWL 2 for logical structure and RDF for data representation. Investigators query or annotate the ontology at each stage of an incident — initial triage, TTP (tactics, techniques, procedures) identification, and indicators-of-compromise/containment/recovery — with the domain-specific extension automatically surfacing which infrastructure components, threats, and evidence types are relevant, compared against a baseline of manually extending the general-purpose ontology with no domain context built in.

## Examples

- Applied to a simulated APT ransomware scenario against a fictional smart-district's telecommunications and IoT-connected systems: the domain-specific ontology represented the affected Smart City Infrastructure components, the specific threats and cybercrime types applicable to each (data interference, illegal access, illegal interception, system interference), and the malware IoCs (hashes, malicious domains) collected during the response, integrated with MITRE ATT&CK technique IDs and CAPEC attack patterns for each stage of the attack.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Domain-specific cyber-threat ontologies require continuous manual updates to remain current]]

## References

- [LWCite-1043] Tok et al., 2025, "A Smart City Infrastructure ontology for threats, cybercrime, and digital forensic investigation", FSI: Digital Investigation 52.
