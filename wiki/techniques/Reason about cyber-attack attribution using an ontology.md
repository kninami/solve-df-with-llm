---
id: LWT-1046
type: technique
name: Reason about cyber-attack attribution using an ontology
description: Represent cyber-attack entities (threat actors, malware, campaigns, indicators, infrastructure) and their relationships in a formal ontology built on a widely adopted threat-intelligence standard (STIX 2.1), then feed that structured representation into a reasoning-based attribution tool to generate and rank candidate attribution hypotheses for who conducted a specific attack, rather than relying on ad hoc, unstructured investigator judgement.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1047
aliases:
  - Ontology-based cyber-attack attribution reasoning
  - OCAI ontology
source_refs:
  - LWCite-1037
updated_at: 2026-08-09
status: complete
---

# Reason about cyber-attack attribution using an ontology

## Summary

STIX 2.1 is a widely adopted format for structuring and sharing cyber threat intelligence, but it does not itself define formal semantics or reasoning constraints, and existing cyber-investigation ontologies typically cover only a narrow subset of attribution-relevant concepts (e.g., threat actor motivation, course of action taken in response, or the roles of investigating entities). Extending STIX 2.1 with additional classes, relationships, and axioms produces a machine-readable knowledge representation that a reasoning-based attribution tool can query to construct and score attribution hypotheses grounded in both technical and contextual evidence.

## Details

Core STIX Domain Objects (Attack Pattern, Campaign, Identity, Indicator, Intrusion Set, Malware, Threat Actor, Tool, Vulnerability, etc.) are represented as disjoint ontology classes, refined with subclasses drawn from established open vocabularies (e.g., threat-actor sophistication, attack-resource-level, kill-chain phases) and new classes for concepts STIX does not natively capture, such as Impact (physical, economic, psychological, reputational, social/societal) and Course of Action phases (based on the SANS incident-response model: preparation, identification, containment, eradication, recovery, lessons learned). New object properties (e.g., a dedicated `hasAttributionTo` relationship distinct from ambiguous repeated `attributed-to` uses in STIX) and covering/closure axioms enforce logical consistency and prevent invalid inferences. Integrating the ontology's classes and relationships into an existing argumentation-based reasoner lets the reasoner activate a richer, more relevant subset of its reasoning rules and produce ranked attribution hypotheses with associated confidence scores and supporting derivations.

## Examples

- Integrated into the ABR (argumentation-based reasoner) attribution tool and evaluated on the SolarWinds, Belgacom, and Spamhaus attacks: for SolarWinds, the enhanced reasoner produced three ranked hypotheses attributing the attack to CozyBear (highest score, 12) versus two hypotheses for Lazarus Group (highest score, 6), and for Spamhaus, no attribution hypothesis could be generated at all before ontology integration due to missing representational elements, while the enhanced system produced one afterward.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Ontology-based attribution reasoning can produce weakly-differentiated attribution hypotheses]]

## References

- [LWCite-1037] Kaur Gill and Karafili, 2026, "A novel ontology for cyber-attack attribution and investigation", FSI: Digital Investigation 57.
