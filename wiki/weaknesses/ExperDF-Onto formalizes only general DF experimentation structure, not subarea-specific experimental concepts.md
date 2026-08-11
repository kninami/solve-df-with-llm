---
id: DFW-1083
type: weakness
name: ExperDF-Onto formalizes only general DF experimentation structure, not subarea-specific experimental concepts
description: The controlled-experimentation ontology provides a general representation of the digital forensics experimental process and its phases, but the authors state that "the specific understanding of DF subareas is currently not feasible" within the ontology, meaning subfield-specific experimental concepts (e.g. concepts particular to mobile forensics experiments versus memory forensics experiments) are not formally represented.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1083
source_refs:
  - DFCite-1073
updated_at: 2026-08-10
status: complete
---

# ExperDF-Onto formalizes only general DF experimentation structure, not subarea-specific experimental concepts

## Summary

The authors list this as an explicit, acknowledged limitation of the ontology's current scope: it captures general experimental phases and concepts applicable across digital forensics broadly, but does not yet formalize the vocabulary or structure needed to represent experimentation concepts specific to a given DF subarea.

## Why It Matters

A researcher or practitioner in a specific DF subfield (e.g. mobile, memory, or network forensics) who tries to use the ontology to fully document a subarea-specific experimental design may find it captures only the general skeleton of their experiment, leaving subfield-specific decisions, variables, or procedures undocumented in the formal representation and thus not benefiting from the reproducibility and machine-readability the ontology is meant to provide for those details.

## Related Mitigations

- [[mitigations/Supplement ExperDF-Onto with subarea-specific extensions when documenting a subfield-specific DF experiment]]

## Used By

- [[techniques/OWL ontology-based formalization of controlled digital forensics experiments]]

## References

- [DFCite-1073] Silva et al., 2025, "An ontology for promoting controlled experimentation in digital forensics", FSI: Digital Investigation 52.
