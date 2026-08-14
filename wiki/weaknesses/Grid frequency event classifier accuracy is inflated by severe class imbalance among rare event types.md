---
id: DFW-2046
type: weakness
name: Grid frequency event classifier accuracy is inflated by severe class imbalance among rare event types
description: The reported near-99% overall accuracy of a synchrophasor event classifier is measured against an extremely imbalanced set of event classes, with some event types (long oscillatory events, sustainable frequency excursions, impulsive events) represented by only a handful of examples or none at all, so aggregate accuracy figures do not reflect the classifier's actual reliability at recognizing rare event types.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2046
source_refs:
  - DFCite-2047
updated_at: 2026-08-14
status: partial
---

# Grid frequency event classifier accuracy is inflated by severe class imbalance among rare event types

## Summary

The source paper's own Table 6 event-classification counts for the ISO-NE6 dataset show a Short Oscillatory Event count of 157 against a Long Oscillatory Event count of only 3, a Frequency-Excursion Load/Generator loss count of 8, a Frequency-Excursion sustainable count of 2, and zero Impulsive events - meaning the headline 99.3% XGBoost accuracy is measured on a dataset dominated almost entirely by one event class. The paper itself acknowledges this directly: "accuracy provides a broad view of the model's performance, but it fails to include the distribution of different classes, especially in imbalanced datasets."

## Why It Matters

An investigator or grid operator relying on this classifier's reported accuracy to trust its output for a rare event type (a long oscillatory event, a sustained frequency excursion, or an impulsive event) has little genuine evidence the model performs well on those classes specifically, since they contributed only a handful of training/test examples (or none, in the case of impulsive events) to the overall metric. A misclassified rare-but-consequential event (e.g. mistaking a sustained excursion for a short oscillatory blip) could delay an appropriate grid-operator response.

## Related Mitigations

- [[mitigations/Track per-class precision-recall for rare grid event types and expand their training data before trusting classifications]]

## Used By

- [[techniques/Detect and classify grid frequency events using SPEDA and machine learning]]

## References

- [DFCite-2047] Gopinathan and Shanmugam, 2024 — Table 6 reports the per-class event counts discussed above, and the paper's own "Results" discussion explicitly acknowledges that accuracy alone does not capture class-distribution effects in imbalanced datasets.
