---
id: LWM-1083
type: mitigation
name: Supplement ExperDF-Onto with subarea-specific extensions when documenting a subfield-specific DF experiment
source_refs:
  - LWCite-1073
updated_at: 2026-08-10
status: complete
---

# Supplement ExperDF-Onto with subarea-specific extensions when documenting a subfield-specific DF experiment

## Summary

When documenting an experiment specific to a digital forensics subarea, use ExperDF-Onto for the general experimental structure and supplement it with subarea-specific vocabulary or concepts developed separately, rather than assuming the ontology alone fully captures subfield-specific experimental detail.

## Addresses

- [[weaknesses/ExperDF-Onto formalizes only general DF experimentation structure, not subarea-specific experimental concepts]]

## How To Apply

Identify which experimental concepts are specific to the relevant DF subarea before documenting an experiment (e.g. mobile-forensics-specific acquisition variables, or memory-forensics-specific profile variables), and record those separately (in supplementary documentation or a locally-extended ontology) alongside the ExperDF-Onto-formalized general structure, since the published ontology does not yet formalize them.

## References

- [LWCite-1073] Silva et al., 2025, "An ontology for promoting controlled experimentation in digital forensics", FSI: Digital Investigation 52.
