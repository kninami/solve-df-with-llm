---
id: LWT-1088
type: technique
name: Analyze organized-crime networks using a multimodal intercepted-call knowledge graph
description: Process lawfully intercepted telephone conversations and associated non-content data (call metadata, time/spatial positions, social media data) through an integrated pipeline of speaker identification, automatic speech recognition (ASR), and named entity detection, then build multiple knowledge graphs capturing phone and speaker criminal-network interactions, to support cross-border organized-crime investigations that would otherwise be overwhelmed by the volume and diversity of intercepted data.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1094
aliases:
  - Multimodal intercepted-call knowledge-graph platform for organized-crime network analysis
  - Autocrime
  - ROXANNE
source_refs:
  - LWCite-1086
updated_at: 2026-08-10
status: complete
---

# Analyze organized-crime networks using a multimodal intercepted-call knowledge graph

## Summary

Cross-border organized-crime investigations generate large volumes of heterogeneous data (audio/speech, text, video, non-content metadata) that can overwhelm law enforcement agents working with traditional, manual methods. Integrating state-of-the-art speaker identification, ASR, and named-entity detection components into a single pipeline, and using their output to automatically construct knowledge graphs of phone and speaker interactions, gives investigators a structured, queryable view of a criminal network rather than requiring manual review of every intercepted call.

## Details

Developed under the EU H2020 ROXANNE project, the platform (Autocrime) integrates voice activity detection, speaker diarization, ASR, and named entity recognition (NER), evaluated respectively via Detection Error Rate, Diarization Error Rate, Word Error Rate (WER), and F1-score metrics. Six network-analysis technologies build and visualize criminal network graphs from the extracted information, including automatically created edges between speaker nodes based on detected interactions. The platform incorporates Privacy-by-Design principles during development, though the authors note this does not itself guarantee legal compliance — end-users (law enforcement agencies) remain responsible as data controllers for protecting personal data during use. Autocrime is released under the Apache License 2.0 for active law enforcement and recognized academic/R&D partners in EU civil security.

## Examples

- On evaluation datasets, ASR achieved a Word Error Rate of 28.4-28.5% for English and 35.9% for German (with minimal change from a boosting enhancement), while named entity recognition achieved F1-scores of only 15.4-20.6% for PERSON entities (improving to 20.6% with boosting), versus much higher F1-scores (78.4-78.8%) for TIME entities, illustrating substantial variation in extraction reliability by entity type.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Multilingual ASR and named-entity extraction in intercepted-call platforms have low accuracy for PERSON entities and unevaluated languages]]

## References

- [LWCite-1086] Madikeri et al., 2025, "Autocrime - open multimodal platform for combating organized crime", FSI: Digital Investigation 54.
