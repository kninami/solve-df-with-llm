---
id: LWW-2005
type: weakness
name: Rare-event audio anomaly classifiers show inconsistent accuracy across classifier-environment combinations
description: The accuracy, recall, and AUC of a rare-event audio anomaly classifier vary substantially depending on both the chosen classifier and the specific background-noise environment, so a single headline performance figure does not guarantee reliable detection in every deployment setting.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2005
source_refs:
  - LWCite-2005
updated_at: 2026-08-14
status: partial
---

# Rare-event audio anomaly classifiers show inconsistent accuracy across classifier-environment combinations

## Summary

The source paper's own per-scene results (Table 4/5) show meaningful swings across the 15 background environments and 6 classifiers - for example, KNN AUC drops to 0.85 in the Bus scene versus 1.00 for MLP in the same scene, and the paper itself notes the dataset's loud environmental noise "makes event detection more difficult in some environments." No single classifier is uniformly best across every environment, and performance in a specific noisy real-world environment (e.g. a busy street or transit setting) cannot be assumed from an average or best-case reported figure.

## Why It Matters

If an investigator deploys a rare-event audio classifier trained or benchmarked primarily on quieter or different environments to a genuinely noisy scene, a real forensically significant event (a gunshot, scream, or breaking glass) could be missed or misclassified, and the resulting gap in the evidentiary record may not be apparent without independent verification of the audio.

## Related Mitigations

- [[mitigations/Select and validate a rare-event audio classifier against the target deployment environment's own background noise profile]]

## Used By

- [[techniques/Detect rare forensic audio events using MFCC-PCA feature engineering and classifiers]]

## References

- [LWCite-2005] Abbasi et al., 2022 — Tables 4 and 5 report per-scene, per-classifier accuracy/AUC swings, and the paper's own discussion notes loud environmental noise makes detection harder in some environments.
