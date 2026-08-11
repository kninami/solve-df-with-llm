---
id: DFM-1033
type: mitigation
name: Cross-reference LLM-identified entities against the source corpus before accepting them as evidence
source_refs:
  - DFCite-1023
updated_at: 2026-08-09
status: complete
---

# Cross-reference LLM-identified entities against the source corpus before accepting them as evidence

## Summary

Before including any entity a language model identified during forensic text triage in an investigative report, verify that it actually appears in the original source corpus, since a plausible-sounding hallucinated entity is otherwise indistinguishable from a genuine extraction.

## Addresses

- [[weaknesses/LLM-assisted forensic text triage hallucinates entities not present in the source evidence]]

## How To Apply

Cross-reference every entity extracted by the language model against the full original text corpus (e.g., via an automated string-matching program) and flag any entity with no match as a likely hallucination requiring exclusion or explicit caveat before it is relied upon. Where feasible, automate this verification step using techniques such as Named Entity Recognition combined with fuzzy string matching, since manual cross-referencing, while faster than the initial manual discovery of entities, is still time-consuming at scale.

## References

- [DFCite-1023] Fayyaz et al., 2024, "A hybrid artificial intelligence framework for enhancing digital forensic investigations of infotainment systems", FSI: Digital Investigation 49.
