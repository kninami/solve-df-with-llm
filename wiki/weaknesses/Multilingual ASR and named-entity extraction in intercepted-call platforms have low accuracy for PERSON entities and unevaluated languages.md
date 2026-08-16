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
  - DFCite-2091
updated_at: 2026-08-16
status: complete
---

# Multilingual ASR and named-entity extraction in intercepted-call platforms have low accuracy for PERSON entities and unevaluated languages

## Summary

The paper's own evaluation table reports ASR Word Error Rates of 28.4-28.5% (English) and 35.9% (German), essentially unchanged by a boosting enhancement, and named-entity F1-scores that vary sharply by entity type: PERSON entities scored only 15.4% (20.6% after boosting), while LOCATION scored 44.0-47.9% and TIME scored 78.4-78.8%. The evaluation was explicitly limited to English and German; the paper states other supported languages "were not included in the evaluation."

A separate forensic ASR pipeline (built around Mozilla DeepSpeech rather than Autocrime's own ASR component) corroborates that this is not specific to one platform: transcribing recovered voice messages sent between non-native English speakers through common messaging apps produced a Word Error Rate averaging 26.4% (range 17.0%-35.0%) -- more than three times the 7.80% WER measured on clean, native-speaker benchmark audio using the same pipeline -- confirming that ASR accuracy degrades substantially for non-native speakers and informal/low-quality audio generally, not only for the specific languages and platform evaluated by the intercepted-call study above.

## Why It Matters

A knowledge graph automatically built from ASR transcripts and named-entity extraction is only as reliable as those underlying components — with roughly a 15-21% F1-score for PERSON entities, a substantial fraction of individuals mentioned in intercepted calls are likely to be missed or misidentified in the resulting network graph, and for languages beyond English and German, the platform's actual accuracy is simply unknown, since it has not been measured. An investigator relying on the platform's automatically constructed speaker/entity network for a non-English/German case, or trusting person-entity edges in the graph without verification, risks building an investigation on an unvalidated or known-unreliable foundation.

## Related Mitigations

- [[mitigations/Manually verify ASR transcripts and PERSON-entity extractions before relying on Autocrime-derived knowledge-graph relationships]]

## Used By

- [[techniques/Analyze organized-crime networks using a multimodal intercepted-call knowledge graph]]
- [[techniques/Detect and transcribe speech in forensic audio and video evidence using voice activity detection and open-source ASR]]

## References

- [DFCite-1086] Madikeri et al., 2025, "Autocrime - open multimodal platform for combating organized crime", FSI: Digital Investigation 54.
- [DFCite-2091] Negrao and Domingues, 2021, "SpeechToText: An open-source software for automatic detection and transcription of voice recordings in digital forensics", FSI: Digital Investigation 38, 301223. Corroborates ASR accuracy degradation for non-native speakers using an independent, DeepSpeech-based forensic transcription pipeline.
