---
id: LWT-1034
type: technique
name: Reason about investigative soundness requirements using an ontology
description: Encode digital forensic standards and guidelines (e.g., ISO/IEC 27037/27041/27042/27043, NIST SP800-86, Interpol guidelines) as a formal description-logic ontology, then use automated reasoning (instance retrieval, classification, conjunctive query answering) to tell an investigator, for a specific evidence source and investigation phase, which soundness requirements (auditability, repeatability, reproducibility, justifiability, sufficiency, reliability) must be satisfied and how.
objective_ids:
  - DFO-1020
weakness_ids:
  - LWW-1035
aliases:
  - Ontology-based investigative soundness requirement reasoning
  - Digital Evidence Admissibility Ontology
  - DEA Ontology
source_refs:
  - LWCite-1025
updated_at: 2026-08-09
status: complete
---

# Reason about investigative soundness requirements using an ontology

## Summary

Because standards and guidelines for sound digital forensic practice exist as multiple separate natural-language documents, an inexperienced investigator can be uncertain how to interpret or apply them together, risking an unsound investigation whose evidence could be disputed in court. A formal SROIQ(D) description-logic ontology unifies concepts from several widely adopted standards and guidelines into a single queryable knowledge base, so that as an investigator specifies each concrete evidence source, medium, datum, or piece of information they are processing, the system automatically retrieves the specific soundness requirements applicable to that item at its current investigation phase.

## Details

The ontology models the standard forensic process (identification, collection, examination, analysis) alongside the operating form each phase transforms data into (potential evidence source, media, data, information), and associates each investigation phase with its own soundness-requirement subconcepts (e.g., IdentificationAuditability, CollectionSufficiency, ExaminationJustifiability, AnalysisReliability). As an investigator concretizes each processing step with real values (e.g., naming a specific virtualized firewall as the potential evidence source), the reasoner performs instance retrieval and classification to surface all applicable soundness-requirement subconcepts and their required supporting actions (e.g., documenting chain of custody, justifying the choice of examination tool, generating and verifying cryptographic hash values) for that specific step.

## Examples

- Applied to a case study reconstructing a data leak using a pfSense firewall's logs and a Squid proxy's access logs (from an ENISA network-forensics exercise), the ontology derived that identification required documenting chain of custody and firewall/PC characteristics, collection required imaging without moving the media and hashing the copy, examination required using and justifying a tool such as Autopsy's Virtual Machine Extractor, and analysis required cross-referencing suspicious IP addresses against a threat-intelligence database such as MISP.

## Related Objectives

- `DFO-1020` Document digital forensic activities

## Related Weaknesses

- [[weaknesses/Description-logic soundness ontology cannot represent uncertain or contradictory compliance guidance]]

## References

- [LWCite-1025] Matijević Gostojić and Vuković, 2023, "A knowledge-based system for supporting the soundness of digital forensic investigations", FSI: Digital Investigation 46.
