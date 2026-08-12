---
id: DFT-1077
type: technique
name: Formalize controlled digital forensics experiments using an OWL ontology
description: Formally document a controlled digital forensics experiment (e.g. testing a new forensic tool or technique) using an OWL-coded ontology (ExperDF-Onto) that defines the standard concepts and terms involved — experimental design, variables, procedures, decision-making rationale, limitations, and threats to validity — so that the experiment's process is captured in a structured, machine-readable, and reproducible form rather than an informal narrative description.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1083
aliases:
  - OWL ontology-based formalization of controlled digital forensics experiments
  - ExperDF-Onto
source_refs:
  - DFCite-1073
updated_at: 2026-08-10
status: complete
---

# Formalize controlled digital forensics experiments using an OWL ontology

## Summary

Digital forensics research often lacks formalization of the controlled experimental process itself, producing findings that are less transparent, reproducible, and reliable than in more mature empirical disciplines, and existing published DF experiments frequently omit detailed descriptions of the decision-making procedures behind their design. An ontology that formalizes the concepts and terms used in DF-controlled experiments gives researchers and practitioners a common, structured vocabulary for documenting experiments, improving formality, reproducibility, and eventual technology transfer to industry.

## Details

The ontology's conceptual model, represented as UML class diagrams and coded in OWL, was built on an existing conceptual model for DF-controlled experiments and evaluated by researchers and experts in DF experimentation, whose feedback (gathered via a questionnaire and review of ontology artifacts) confirmed the ontology's capability to formalize DF experimental concepts and led to refinements before the final published version. Practitioners are intended to benefit by adopting the ontology's formal experimental procedures when testing, assessing, or acquiring DF-related technology, not only academic researchers.

## Examples

- Expert questionnaire feedback surfaced minor inconsistencies in the ontology's structure that were resolved in the version presented in the paper, demonstrating the evaluation process's value even without full hands-on ontology use by the participating experts.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/ExperDF-Onto formalizes only general DF experimentation structure, not subarea-specific experimental concepts]]

## References

- [DFCite-1073] Silva et al., 2025, "An ontology for promoting controlled experimentation in digital forensics", FSI: Digital Investigation 52.
