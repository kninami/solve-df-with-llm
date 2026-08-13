---
id: DFT-1163
type: technique
name: Classify chat conversations as sexual predatory using supervised machine learning within a digital forensic process model
description: Train supervised text classifiers (e.g. logistic regression, XGBoost, MLP, BiLSTM) on TF-IDF or embedding features to label chat-log conversations as sexual predatory or non-predatory, mapping each machine-learning step explicitly onto the tasks of a Digital Forensic Process Model so the classification output and its supporting features can be presented as admissible investigative findings.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1169
aliases:
  - ML-supported digital forensic process model for online sexual predatory chat detection
source_refs:
  - DFCite-1174
updated_at: 2026-08-12
status: complete
---

# Classify chat conversations as sexual predatory using supervised machine learning within a digital forensic process model

## Summary

Manually reviewing large volumes of chat-log data for online sexual grooming is slow and inconsistent, so this technique trains a supervised text classifier to flag predatory conversations and structures the entire ML pipeline (collect, examine, hypothesize, classify, reduce, evaluate, analyze, reconstruct, interpret) around an established Digital Forensic Investigation process model, so results remain traceable and explainable for court use rather than being a standalone black-box classifier.

## Details

Text is minimally cleaned (HTML character decoding, lemmatization) but not aggressively stripped, since informal artefacts (emphasized misspellings, emoticons, abbreviations like "asl") carry grooming-relevant signal. TF-IDF unigrams/bigrams/trigrams feed logistic regression, XGBoost, and MLP classifiers, while a BiLSTM uses a learned word-embedding input instead. On the PAN-12 dataset (imbalanced: predatory conversations are a small minority), all four models reached ~98% raw accuracy but F1 scores of only 0.577-0.740 once precision/recall are considered together, reflecting the class imbalance. To make individual predictions explainable for the "reconstruct" and "interpret" process tasks, a greedy segment-merging search algorithm iteratively merges the highest-probability lines of a conversation to surface which specific words or phrases drove the model toward a predatory classification, complementing per-word probability tracing via a what-if analysis tool for individual misclassified data points.

## Examples

- The XGBoost and logistic-regression models' top-weighted unigram/bigram/trigram features for the predatory class included "asl" (age/sex/location), "horny", "hi m/f", and "looking for a" — phrases consistent with the established stages of online grooming behavior.
- A conversation was successfully identified as predatory even though it contained little explicit sexual content, consistent with the finding (also reported by the ChatCoder tool) that predators typically rely more on general rapport-building language than overtly sexual language during early grooming.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Predatory-chat classifiers misclassify entire conversations based on a single high-weight ambiguous word]]

## References

- [DFCite-1174] Ngejane et al., 2021, "Digital forensics supported by machine learning for the detection of online sexual predatory chats", FSI: Digital Investigation 36, 301109.
