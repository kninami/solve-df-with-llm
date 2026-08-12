---
id: DFW-1094
type: weakness
name: Multilingual ASR and named-entity extraction in intercepted-call platforms have low accuracy for PERSON entities and unevaluated languages
description: On evaluated languages (English and German), the platform's automatic speech recognition reached only 28.4-35.9% Word Error Rate, and named entity recognition for PERSON entities reached only an F1-score of 15.4-20.6% even after a boosting enhancement — substantially lower than for other entity types such as TIME (78.4-78.8% F1) — and the platform's other supported languages (Dutch, Greek, Lithuanian, Arabic, Spanish, and more) were not included in this evaluation at all.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1094
source_refs:
  - DFCite-1086
updated_at: 2026-08-10
status: complete
---

# Multilingual ASR and named-entity extraction in intercepted-call platforms have low accuracy for PERSON entities and unevaluated languages

## Summary

The paper's own evaluation table reports ASR Word Error Rates of 28.4-28.5% (English) and 35.9% (German), essentially unchanged by a boosting enhancement, and named-entity F1-scores that vary sharply by entity type: PERSON entities scored only 15.4% (20.6% after boosting), while LOCATION scored 44.0-47.9% and TIME scored 78.4-78.8%. The evaluation was explicitly limited to English and German; the paper states other supported languages "were not included in the evaluation."

## Why It Matters

A knowledge graph automatically built from ASR transcripts and named-entity extraction is only as reliable as those underlying components — with roughly a 15-21% F1-score for PERSON entities, a substantial fraction of individuals mentioned in intercepted calls are likely to be missed or misidentified in the resulting network graph, and for languages beyond English and German, the platform's actual accuracy is simply unknown, since it has not been measured. An investigator relying on the platform's automatically constructed speaker/entity network for a non-English/German case, or trusting person-entity edges in the graph without verification, risks building an investigation on an unvalidated or known-unreliable foundation.

## Related Mitigations

- [[mitigations/Manually verify ASR transcripts and PERSON-entity extractions before relying on Autocrime-derived knowledge-graph relationships]]

## Used By

- [[techniques/Analyze organized-crime networks using a multimodal intercepted-call knowledge graph]]

## References

- [DFCite-1086] Madikeri et al., 2025, "Autocrime - open multimodal platform for combating organized crime", FSI: Digital Investigation 54.
