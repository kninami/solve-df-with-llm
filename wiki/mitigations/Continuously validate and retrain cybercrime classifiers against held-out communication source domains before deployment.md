---
id: LWM-1159
type: mitigation
name: Continuously validate and retrain cybercrime classifiers against held-out communication source domains before deployment
source_refs:
  - LWCite-1161
updated_at: 2026-08-12
status: complete
---

# Continuously validate and retrain cybercrime classifiers against held-out communication source domains before deployment

## Summary

Before relying on a supervised cybercrime-message classifier against a new communication channel, platform, or organization's message corpus, run a cross-corpus evaluation that withholds that entire source domain from training and measures accuracy, macro-F1, and ROC-AUC on it specifically, rather than trusting a pooled in-domain benchmark score.

## Addresses

- [[weaknesses/Supervised cybercrime-message classifiers collapse against a communication source absent from training data]]

## How To Apply

Maintain a held-out set of source domains distinct from the training pool and periodically re-run cross-corpus (leave-one-source-out) evaluation whenever the classifier is applied to a new deployment context. If cross-corpus accuracy is materially lower than in-domain accuracy, retrain or fine-tune on labeled examples from the target domain before relying on the classifier's output as investigative evidence, and treat any single risk score as a probabilistic indicator to be corroborated with other evidence rather than as a standalone determination of cybercrime.

## References

- [LWCite-1161] Omeleze Baror et al., 2026, "DFR–HCI: A forensic-ready microservice architecture for human-to-human communication-based cybercrime detection", FSI: Digital Investigation 58, 302134.
