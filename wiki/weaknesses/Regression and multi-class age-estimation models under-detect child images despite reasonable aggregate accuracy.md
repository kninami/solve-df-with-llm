---
id: DFW-1127
type: weakness
name: Regression and multi-class age-estimation models under-detect child images despite reasonable aggregate accuracy
description: Age-estimation models that predict a specific age or age band, rather than a simple child/adult label, achieve materially worse detection of child images than binary classification, even though their overall accuracy metrics can look reasonable.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-1127
source_refs:
  - DFCite-1122
  - DFCite-2141
updated_at: 2026-08-16
status: complete
---

# Regression and multi-class age-estimation models under-detect child images despite reasonable aggregate accuracy

## Summary

A comparative evaluation of binary, multi-class, and regression age-estimation strategies for indecent-image triage found that regression prediction "works best for the identification of images with ages near 35, yet is not able to detect the child images effectively," and multi-class classification "provides no advantage over binary classification." All three strategies reported overall accuracy above 60%, which could mislead a practitioner who only checks the headline accuracy figure into believing any of the three strategies is fit for identifying child victims.

## Why It Matters

The entire forensic purpose of this technique is to flag images of children, so a strategy that reports acceptable-looking aggregate accuracy while systematically failing on the child sub-population is worse than useless for triage — it can create false confidence that a case has been adequately screened. Because the child class is typically the minority and least-represented class in training data, aggregate accuracy figures are dominated by adult-class performance and can obscure exactly the failure mode that matters most operationally.

A later regression-based approach (Vec2UAge) specifically targeting the underage bracket, built on FaceNet-embedding input and underage-skewed training data rather than raw pixels from adult-skewed datasets, reports a substantially improved test Mean Absolute Error of 2.36 years within the underage 1-18 range and per-age-bin analysis showing its lowest error concentrated around 2, 12, and 14-year-old subjects specifically -- suggesting regression's original weakness relative to binary classification may be substantially narrowed, though not necessarily eliminated, by training data specifically curated and augmented for the underage population rather than being an inherent, unfixable property of regression as a modeling choice.

## Related Mitigations

- [[mitigations/Prefer binary child-adult classification over multi-class or regression models for indecent-image age triage]]

## Used By

- [[techniques/Estimate victim age in indecent images using binary child-adult classification]]
- [[techniques/Estimate underage subject age from facial images using FaceNet-embedding regression]] (a later regression-based approach specifically targeting the underage bracket, reporting substantially improved accuracy within that range)

## References

- [DFCite-1122] Roopak et al., 2023, "Comparison of deep learning classification models for facial image age estimation in digital forensic investigations", FSI: Digital Investigation 47, 301637.
- [DFCite-2141] Anda, Dixon, and Bou-Harb, 2021, "Vec2UAge: Enhancing underage age estimation performance through facial embeddings", FSI: Digital Investigation 36, 301119.
