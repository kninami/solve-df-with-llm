---
id: LWW-2001
type: weakness
name: Facial identification classifiers misattribute identity between look-alikes and identical twins
description: Machine-learning classifiers comparing anthropometric facial features achieve only moderate accuracy (as low as 57-78% in benchmark testing) at distinguishing identical twins and look-alikes, risking both false matches and false non-matches when used as identification evidence.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-2001
source_refs:
  - LWCite-2001
updated_at: 2026-08-14
status: partial
---

# Facial identification classifiers misattribute identity between look-alikes and identical twins

## Summary

Even the best-performing classifier in a landmark-ratio-based facial comparison study (XGBoost, tuned via hyperparameter optimization) reached only 78% accuracy distinguishing "same person" from "different person" image pairs, with several other tested classifiers (Decision Tree, LightGBM, Extra Trees) at or below 58%. Precision/recall figures for the "same" class were markedly weaker than for "different," meaning the system is particularly prone to wrongly rejecting or wrongly confirming a true identity match. Identical twins and look-alikes are the case class the paper explicitly targets and where confusion is most likely.

## Why It Matters

A facial identification result used as investigative or courtroom evidence that misattributes identity — treating a look-alike as the suspect, or an identical twin as an unrelated person — can implicate an innocent individual or fail to implicate the actual suspect. The source paper explicitly cites real cases (e.g. a murder investigation where a suspect's twin was implicated due to facial similarity, and a case where biometric verification was insufficient to resolve a twin-suspect ambiguity) that motivate this concern. Because classifier accuracy varies substantially by algorithm and by dataset, treating any single model's same/different decision as definitive risks an ASTM Inaccuracy (Association) error — attributing evidence to the wrong individual.

## Related Mitigations

- [[mitigations/Corroborate ML-based facial identity comparisons with additional biometric modalities and expert review]]

## Used By

- [[techniques/Identify individuals using facial anthropometric landmark distance ratios]]

## References

- [LWCite-2001] Sanil et al., 2023 — reports 57-78% accuracy across ten classifiers on a same/different facial-pair dataset including look-alikes and identical twins, and documents real investigative cases affected by facial misidentification of twins.
