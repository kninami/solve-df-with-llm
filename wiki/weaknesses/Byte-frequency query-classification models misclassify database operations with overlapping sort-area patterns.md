---
id: DFW-1147
type: weakness
name: Byte-frequency query-classification models misclassify database operations with overlapping sort-area patterns
description: A machine-learning classifier trained on sort-area byte-frequency histograms confuses query operation types whose memory access patterns overlap, most consistently misattributing filter operations as aggregate operations (and vice versa) in both evaluated DBMSes, so its predicted operation type cannot always be trusted at face value.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1147
source_refs:
  - DFCite-1143
updated_at: 2026-08-12
status: complete
---

# Byte-frequency query-classification models misclassify database operations with overlapping sort-area patterns

## Summary

The published evaluation's own confusion matrices show that while index sort, file sort, and join operations are distinguished with high accuracy, filter and aggregate operations produce data points that visibly overlap in feature space for both MySQL and PostgreSQL, and the classifier consistently misattributes some filter operations as aggregate operations and some aggregate operations as filter or join operations because both use an index to generate their result and leave similar overlapping data patterns in the sort area.

## Why It Matters

An investigator who takes a single-model prediction of "aggregate" or "filter" as a confirmed determination of what query ran risks misattributing the activity to the wrong operation type, which matters when the distinction affects the interpreted significance of the finding (for example, whether a user merely filtered a view of data or generated an aggregate summary of it). Because this confusion is a structural property of the two operations' overlapping memory access patterns rather than a fixable training-data gap, it is likely to recur on new datasets and DBMSes with a similar sort-area architecture.

## Related Mitigations

- [[mitigations/Treat overlapping-class query-operation predictions as uncertain and corroborate independently]]

## Used By

- [[techniques/Classify database query operations from memory using byte-frequency machine learning]]

## References

- [DFCite-1143] Nissan, Wagner and Aktar, 2023, "Database memory forensics: A machine learning approach to reverse-engineer query activity", FSI: Digital Investigation 44.
