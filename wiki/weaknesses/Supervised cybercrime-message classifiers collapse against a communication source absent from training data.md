---
id: LWW-1159
type: weakness
name: Supervised cybercrime-message classifiers collapse against a communication source absent from training data
description: A supervised cybercrime-message classifier that performs strongly on pooled, in-domain data can collapse to near-zero accuracy when applied to messages from an entire communication source domain (e.g. a different corpus of complaints or emails) that was withheld during training, because the model has learned corpus-specific lexical and topic cues rather than source-independent indicators of cybercrime.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1159
source_refs:
  - LWCite-1161
updated_at: 2026-08-12
status: complete
---

# Supervised cybercrime-message classifiers collapse against a communication source absent from training data

## Summary

Two cross-corpus experiments held out an entire source domain during training and tested only on that domain: training on all sources except consumer-complaint narratives and testing on complaints alone, and training on all sources except Enron corporate email and testing on Enron alone. In both scenarios, both a TF-IDF logistic-regression baseline and a CNN collapsed from their in-domain performance (accuracy 0.87-0.91, macro-F1 0.86-0.90) to near-total failure out-of-domain (accuracy 0.000-0.053, macro-F1 0.000-0.039), despite retaining moderate ROC-AUC (0.127-0.365), indicating the models rank messages plausibly but their decision thresholds and learned features do not transfer across communication sources.

## Why It Matters

An investigator relying on a cybercrime classifier's strong published in-domain benchmark score risks a false sense of completeness: the classifier may silently and near-totally fail to flag genuine cybercrime messages in a new SaaS platform, communication channel, or corpus that differs from its training data, resulting in real threats going undetected (an incompleteness defect) rather than a visible error. High reported pooled-corpus accuracy or ROC-AUC does not indicate that a model will generalize to the specific communication source under investigation.

## Related Mitigations

- [[mitigations/Continuously validate and retrain cybercrime classifiers against held-out communication source domains before deployment]]

## Used By

- [[techniques/Detect communication-based cybercrime using supervised linguistic-semantic classification]]

## References

- [LWCite-1161] Omeleze Baror et al., 2026, "DFR–HCI: A forensic-ready microservice architecture for human-to-human communication-based cybercrime detection", FSI: Digital Investigation 58, 302134.
