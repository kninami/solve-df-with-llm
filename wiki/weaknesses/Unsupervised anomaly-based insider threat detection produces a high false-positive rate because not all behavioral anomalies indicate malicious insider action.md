---
id: DFW-1258
type: weakness
name: Unsupervised anomaly-based insider threat detection produces a high false-positive rate because not all behavioral anomalies indicate malicious insider action
description: Unsupervised anomaly detection flags any behavior sequence that deviates from the learned "normal" profile, but not every deviation is an actual insider threat — a benign role change or unusual-but-legitimate task can appear anomalous, while deliberately concealed malicious behavior can appear normal — producing a high rate of false alarms unless a further correction step distinguishes the two.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1259
source_refs:
  - DFCite-1276
updated_at: 2026-08-14
status: complete
---

# Unsupervised anomaly-based insider threat detection produces a high false-positive rate because not all behavioral anomalies indicate malicious insider action

## Summary

Insider threat detection is not the same problem as anomaly detection: some genuinely malicious insider actions are deliberately disguised to resemble normal behavior (evading detection entirely), while some entirely benign behavior — a sudden role change, an unusual but legitimate one-off task — produces a behavior sequence the model has not seen before and flags as anomalous. Compounding this, the unsupervised data-purification step used to build the "normal" training profile in the first place can itself discard some genuinely normal data as it filters out anomalies, further reducing the training profile's coverage of legitimate behavior variety.

## Why It Matters

An insider threat program that escalates every flagged anomaly to a full investigation risks overwhelming analyst capacity with false alarms drawn from ordinary role changes, project transitions, or one-off legitimate tasks, eroding trust in the detection system and potentially causing analysts to deprioritize genuine alerts (alert fatigue). Because recall (catching all real insider threats) is the more critical metric in this domain — a missed real threat can cause significant organizational damage — a detection scheme cannot simply raise its anomaly threshold to suppress false positives without risking missed genuine threats instead.

## Related Mitigations

- [[mitigations/Apply a secondary graph-based correction step to re-score and filter unsupervised insider-threat anomaly detections before escalating them to investigators]]

## Used By

- [[techniques/Detect behavioral anomalies using unsupervised deep learning]]

## References

- [DFCite-1276] Wei, Chow and Yiu, 2021, "Insider threat prediction based on unsupervised anomaly detection scheme for proactive forensic investigation", FSI: Digital Investigation 38, 301126.
