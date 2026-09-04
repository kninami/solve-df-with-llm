---
id: LWT-1215
type: technique
name: Classify threatening email content into a forensic taxonomy using an ML and transformer ensemble
description: Automatically triage threatening emails into a forensically grounded multi-class taxonomy (spam, phishing, direct/subtle/workplace/personal-vendetta threats, ransomware, hate speech, propaganda, and related classes) using lexical, stylometric, and header-metadata features fed to classical machine-learning and fine-tuned transformer classifiers, rather than a binary spam/phishing filter.
objective_ids:
  - DFO-1012
weakness_ids:
  - LWW-1231
aliases:
  - Forensically-integrated multi-class email threat detection
  - SET dataset classification
source_refs:
  - LWCite-1242
updated_at: 2026-08-13
status: complete
---

# Classify threatening email content into a forensic taxonomy using an ML and transformer ensemble

## Summary

Conventional automated email filtering distinguishes only spam and generic phishing, leaving nuanced, high-impact threats (workplace misconduct, personal vendettas, veiled/subtle threats, hate speech, extortion) undetected because they lack the bulk or templated indicators those filters rely on. Combining a forensically grounded twelve-class taxonomy with lexical (TF-IDF), stylometric (punctuation/sentence-length/authorship cues), and forensic-metadata (header-anomaly, sender-domain-type) features, then benchmarking classical ML and deep-learning classifiers against them, produces triage-grade multi-class discrimination that a binary spam/phishing filter cannot.

## Details

Each of the twelve taxonomy classes (Spam, Phishing, Direct Threats, Subtle Threats, Workplace Misconduct Threats, Formal Complaint Threats, Anonymous Threats, Ransomware Threats, Hate Speech Threats, Propaganda Mails, Political Threats, Personal Vendetta Threats) is defined by explicit linguistic, behavioral, and technical forensic indicators (e.g., mismatched `From`/`Reply-To` headers, modality-based intent language, sender-domain type) drawn from forensic linguistics and prior casework, rather than by content-based blacklisting alone. Because genuine casework email evidence cannot be shared for privacy/ethics reasons, a privacy-preserving synthetic dataset is built through an archetype-definition, lexicon-curation, template-based-generation, variability/noise-injection, and forensic-metadata-synthesis pipeline, yielding a class-balanced corpus for reproducible benchmarking. Fourteen classifiers spanning linear models, probabilistic (Naive Bayes), ensemble/boosting (Random Forest, XGBoost, LightGBM), and deep architectures (GRU, LSTM, 1D CNN, fine-tuned BERT) are evaluated with macro-averaged precision/recall/F1/AUC and bootstrap confidence intervals; a confusion-matrix and precision-recall analysis is used specifically to surface which class pairs a deployed classifier confuses, since that failure pattern — not overall accuracy — determines whether the tool is safe to use for forensic triage.

## Examples

- On a held-out test set, fine-tuned BERT reached 0.933 accuracy (AUC 0.996), statistically significantly ahead of the strongest classical baselines (Logistic Regression 0.904, SVM 0.900, LightGBM 0.897; paired t-test and McNemar's test both p < 1×10⁻¹⁰), while the classical linear models remained close enough to BERT to be a viable lower-cost deployment option.
- Formal Complaint Threats (1.00 recall) and Ransomware Threats (0.97 F1) were classified near-perfectly due to their rigid, formulaic language, while Anonymous Threats showed reduced precision (0.82) because vague, cautionary phrasing overlaps semantically with Subtle Threats — a forensically meaningful confusion pattern rather than random noise.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Multi-class email threat classifiers confuse semantically overlapping threat categories]]

## References

- [LWCite-1242] Srivastava et al., 2026, "Forensically-integrated machine learning model for multi-class email threat detection using a high-fidelity synthetic dataset", FSI: Digital Investigation 57, 302108.
