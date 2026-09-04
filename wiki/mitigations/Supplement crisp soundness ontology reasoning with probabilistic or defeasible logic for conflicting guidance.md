---
id: LWM-1035
type: mitigation
name: Supplement crisp soundness ontology reasoning with probabilistic or defeasible logic for conflicting guidance
source_refs:
  - LWCite-1025
updated_at: 2026-08-09
status: complete
---

# Supplement crisp soundness ontology reasoning with probabilistic or defeasible logic for conflicting guidance

## Summary

Where the underlying standards or guidelines encoded in a soundness-requirement ontology are ambiguous or conflict with one another for a given scenario, extend or supplement the crisp description-logic reasoning with a formalism capable of representing uncertainty or defeasible (default, overridable) rules, and surface the conflict to the investigator rather than silently resolving it to a single answer.

## Addresses

- [[weaknesses/Description-logic soundness ontology cannot represent uncertain or contradictory compliance guidance]]

## How To Apply

When extending or maintaining a description-logic soundness ontology, identify axioms sourced from standards known to sometimes diverge in guidance, and model those specific areas using probabilistic logic (to represent degrees of confidence) or defeasible logic (to represent default rules that can be overridden by more specific ones) rather than forcing them into the crisp SROIQ(D) formalism. Where a genuine conflict is detected during reasoning, have the system explicitly report the conflicting sources and their requirements to the investigator for a documented human judgement call, rather than presenting only one derived answer.

## References

- [LWCite-1025] Matijević Gostojić and Vuković, 2023, "A knowledge-based system for supporting the soundness of digital forensic investigations", FSI: Digital Investigation 46.
