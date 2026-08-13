---
id: DFT-1155
type: technique
name: Detect communication-based cybercrime using supervised linguistic-semantic classification
description: Score an incoming human-to-human communication message (email, chat, or other SaaS message) against a supervised machine-learning model trained on lexical, syntactic, and semantic features to classify it as benign or as a specific cybercrime type — phishing, fraud, impersonation, or identity theft — producing a calibrated risk score investigators can act on.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1159
aliases:
  - Deterministic linguistic-semantic feature extraction and supervised ML scoring for cybercrime detection
  - DFR-HCI detection function S(X_u)
source_refs:
  - DFCite-1161
updated_at: 2026-08-12
status: complete
---

# Detect communication-based cybercrime using supervised linguistic-semantic classification

## Summary

Modern cybercrime — phishing, business email compromise, impersonation, and financial fraud — increasingly exploits linguistic manipulation (urgency, authority, emotional leverage) rather than technical vulnerabilities. A deterministic feature-extraction pipeline converts each message's text into a reproducible lexical/syntactic/semantic feature vector, which a supervised classifier scores in [0, 1] for cybercrime risk, giving investigators an interpretable, auditable signal rather than a black-box judgment.

## Details

The feature-extraction step is applied deterministically (tokenization, normalization, stop-word removal, then TF-IDF and/or learned embeddings) so the same message always produces the same feature vector, a requirement for forensic replay. On a balanced, five-class (benign, phishing, fraud, identity theft, impersonation) corpus of 5050 messages, a TF-IDF logistic regression baseline achieved accuracy 0.869, macro-F1 0.863, and micro-averaged ROC-AUC 0.978, while deep sequence models (a 1D CNN and a BiLSTM with self-attention) reached higher in-domain performance (CNN: accuracy 0.909, macro-F1 0.905, ROC-AUC 0.991) at the cost of being somewhat less well-calibrated and, for the BiLSTM, considerably more brittle to simple character-level perturbation (macro-F1 dropping from 0.874 to 0.716 under random character drop/swap, versus 0.905 to 0.820 for the CNN). Model decisions were made forensically inspectable via global feature-importance coefficients (e.g. "identity theft", "credit report", and "victim of" driving identity-theft classifications; "click here", "online", and "http" driving phishing classifications) and per-message SHAP/LIME-style local explanations, both of which are exactly replayable because the underlying feature extraction and classifier are deterministic and versioned.

## Examples

- On the supervised in-domain test split, the TF-IDF logistic-regression baseline's per-class F1 ranged from 0.781 (fraud) to 0.935 (identity theft), with phishing and impersonation both above 0.80.
- A representative invoice-fraud message ("Please process the attached invoice urgently before closing today") was correctly scored above the detection threshold, with the linguistic-semantic feature vector surfacing "urgently" and "invoice" as the dominant risk-driving tokens.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Supervised cybercrime-message classifiers collapse against a communication source absent from training data]]

## References

- [DFCite-1161] Omeleze Baror et al., 2026, "DFR–HCI: A forensic-ready microservice architecture for human-to-human communication-based cybercrime detection", FSI: Digital Investigation 58, 302134.
