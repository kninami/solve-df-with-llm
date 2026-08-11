---
id: DFM-1094
type: mitigation
name: Manually verify ASR transcripts and PERSON-entity extractions before relying on Autocrime-derived knowledge-graph relationships
source_refs:
  - DFCite-1086
updated_at: 2026-08-10
status: complete
---

# Manually verify ASR transcripts and PERSON-entity extractions before relying on Autocrime-derived knowledge-graph relationships

## Summary

Manually verify ASR transcriptions and, especially, PERSON-entity extractions before treating a platform-generated knowledge-graph relationship as established fact, and treat results for languages other than English/German as unvalidated until independently checked.

## Addresses

- [[weaknesses/Multilingual ASR and named-entity extraction in intercepted-call platforms have low accuracy for PERSON entities and unevaluated languages]]

## How To Apply

Before relying on a speaker/entity relationship in the platform's knowledge graph as investigative evidence, have an analyst manually verify the underlying ASR transcript and named-entity extraction, prioritizing PERSON entities given their measured low accuracy. For any language outside the evaluated set (English, German), treat platform output as an unvalidated lead requiring independent confirmation rather than a reliable automated result.

## References

- [DFCite-1086] Madikeri et al., 2025, "Autocrime - open multimodal platform for combating organized crime", FSI: Digital Investigation 54.
