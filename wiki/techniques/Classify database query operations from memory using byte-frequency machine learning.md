---
id: DFT-1144
type: technique
name: Classify database query operations from memory using byte-frequency machine learning
description: Reverse-engineer which type of SQL query operation (index sort, file sort, join, filter, or aggregate) recently ran against a DBMS by extracting an ASCII byte-frequency histogram from the process memory region the DBMS uses for query processing (the sort area) and classifying it with a trained support vector machine.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1147
aliases:
  - SVM-based DBMS query type classification
  - Database memory forensics byte-frequency query classification
source_refs:
  - DFCite-1143
updated_at: 2026-08-12
status: complete
---

# Classify database query operations from memory using byte-frequency machine learning

## Summary

A DBMS process separates two functionally distinct memory regions: the I/O buffer, which caches table/index pages read from disk, and the sort area, a dedicated memory-intensive region used to process data manipulation operations such as sorting, hash-join construction, and grouping. This technique extracts byte-frequency and byte-fraction feature vectors from a memory snapshot's sort area and uses a trained support vector machine (SVM) to predict which of five query operation types produced it, allowing a forensic investigator to reconstruct recent query activity from a single memory snapshot even when audit logs are missing, disabled, or untrusted.

## Details

The technique first isolates the sort area within a DBMS process memory snapshot (a fixed offset range determined for the target DBMS's memory configuration), then builds an ASCII byte-frequency histogram (256-element feature vector) and a "fractions" feature capturing sequences of NULL-padding bytes used to delimit or pad values. An SVM classifier (RBF kernel, hyperparameters selected via grid search) trained on labeled snapshots from a representative query workload predicts one of five operation classes: index sort, file sort, join, filter, or aggregate. Evaluated against MySQL and PostgreSQL populated with the Star Schema Benchmark, the classifier achieved 92% and 90% overall accuracy respectively (macro-averaged F1 of 93%/90%), with perfect or near-perfect recall for index sort, file sort, and join, but weaker performance distinguishing filter from aggregate operations. The approach generalizes across relational DBMSes that maintain a similar sort-area memory architecture, and complements the same research group's memory-cache-pattern approach to full audit-log verification (see [[techniques/Verify database audit logs using memory-cached page access patterns]]), which instead reconstructs which tables and pages were accessed rather than which manipulation operation was performed.

## Examples

- Training an SVM on sort-area byte-frequency histograms collected after running index sort, file sort, join, filter, and aggregate queries against a MySQL 8.0 instance populated with the Star Schema Benchmark (scale 10), then predicting the operation type for an unknown memory snapshot with 92% accuracy.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Byte-frequency query-classification models misclassify database operations with overlapping sort-area patterns]]

## References

- [DFCite-1143] Nissan, Wagner and Aktar, 2023, "Database memory forensics: A machine learning approach to reverse-engineer query activity", FSI: Digital Investigation 44.
