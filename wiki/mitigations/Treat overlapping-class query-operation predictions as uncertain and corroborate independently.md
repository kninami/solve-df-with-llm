---
id: DFM-1147
type: mitigation
name: Treat overlapping-class query-operation predictions as uncertain and corroborate independently
source_refs:
  - DFCite-1143
updated_at: 2026-08-12
status: complete
---

# Treat overlapping-class query-operation predictions as uncertain and corroborate independently

## Summary

When a byte-frequency query-operation classifier predicts a class known to overlap with another (filter/aggregate, and in some cases join/index sort), report the prediction as an uncertain candidate rather than a confirmed operation type, and corroborate it with an independent artifact such as the accessed table's Object ID/Page ID identified from the I/O buffer.

## Addresses

- [[weaknesses/Byte-frequency query-classification models misclassify database operations with overlapping sort-area patterns]]

## How To Apply

Consult the classifier's confusion matrix for the trained model and DBMS in use to identify which class pairs are prone to confusion before relying on a single prediction. For predictions falling into a known-overlapping class, cross-check the memory snapshot's I/O buffer for the specific table Object ID and Page ID pattern accessed, since identifying which table and pages were involved can help disambiguate a filter from an aggregate operation even when the sort-area signature alone cannot. Where the distinction materially affects a finding's significance, report the classification as a probable range (e.g., "filter or aggregate") rather than a single determined operation type, and note the model's published per-class accuracy alongside the finding.

## References

- [DFCite-1143] Nissan, Wagner and Aktar, 2023, "Database memory forensics: A machine learning approach to reverse-engineer query activity", FSI: Digital Investigation 44.
