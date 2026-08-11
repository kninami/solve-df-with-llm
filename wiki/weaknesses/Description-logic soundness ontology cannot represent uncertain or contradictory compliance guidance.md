---
id: DFW-1035
type: weakness
name: Description-logic soundness ontology cannot represent uncertain or contradictory compliance guidance
description: The SROIQ(D) description logic underlying the soundness-requirement ontology is a crisp, decidable logic that requires every concept and axiom to be definitively true or false within the knowledge base, so it cannot natively represent situations where source standards or guidelines are ambiguous, provide conflicting guidance, or where compliance itself is a matter of degree rather than a binary fact.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1035
source_refs:
  - DFCite-1025
updated_at: 2026-08-09
status: complete
---

# Description-logic soundness ontology cannot represent uncertain or contradictory compliance guidance

## Summary

The authors explicitly acknowledge this as a limitation of their own approach in the paper's conclusion: "the knowledge base might include uncertain or contradictory statements. To manage these problems, the system could be extended by using different logics, such as probabilistic logic or defeasible logic." Because the five source standards/guidelines (ISO/IEC 27037, 27041, 27042, 27043, and the Interpol guidelines) were independently authored, real disagreement or ambiguity between them on a specific requirement is plausible, but the current ontology's crisp logic offers no native mechanism to flag or reason through such a conflict.

## Why It Matters

An investigator relying on the ontology's automated reasoning to determine which soundness requirements apply might not be alerted if the underlying source guidance was itself ambiguous or contradictory for their specific scenario, potentially receiving an overconfident single answer where the real state of professional guidance is unsettled. This is a structural limitation of the modeling approach rather than an error in the specific axioms currently encoded, and would recur for any similarly-modeled compliance domain, not just digital forensics.

## Related Mitigations

- [[mitigations/Supplement crisp soundness ontology reasoning with probabilistic or defeasible logic for conflicting guidance]]

## Used By

- [[techniques/Ontology-based investigative soundness requirement reasoning]]

## References

- [DFCite-1025] Matijević Gostojić and Vuković, 2023, "A knowledge-based system for supporting the soundness of digital forensic investigations", FSI: Digital Investigation 46.
