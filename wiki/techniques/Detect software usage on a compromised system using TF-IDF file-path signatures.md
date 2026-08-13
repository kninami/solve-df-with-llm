---
id: DFT-1153
type: technique
name: Detect software usage on a compromised system using TF-IDF file-path signatures
description: Build a per-application signature from the file-path artifacts created or modified when that application runs (via differential analysis of an isolated test system before/after installing and executing it), weight the paths using a TF-IDF scheme, and match a suspect system's file paths against the signature library to triage which applications have actually run on the system under investigation.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1156
aliases:
  - Software Signature Detection Engine
  - SSDE triage
  - TF-IDF file-path software-usage triage
source_refs:
  - DFCite-1157
updated_at: 2026-08-12
status: complete
---

# Detect software usage on a compromised system using TF-IDF file-path signatures

## Summary

Rather than manually reconstructing which applications ran on a compromised system from raw extracted artifacts, this technique automates the process with a Software Signature Detection Engine (SSDE): a signature-construction subsystem builds a TF-IDF-weighted file-path signature for each piece of software from differential file-system snapshots, and a detection subsystem scores a suspect system's own file-path listing against the signature library to flag which software was used, giving an investigator a fast, system-wide triage overview.

## Details

Signature construction runs each candidate application in an isolated environment, captures the file-system state before and after installation/execution, and extracts the set of file paths that changed as that application's raw signature; a TF-IDF weighting scheme (with configurable term-frequency and inverse-document-frequency formula variants, n-gram granularity, and stop-list use) converts the raw path set into a weighted vector signature. Detection computes a similarity score (cosine or simple similarity, again configurable) between the target system's observed file paths and each software's signature vector, and declares the software "present" if the score exceeds a per-software threshold that is itself calibrated during signature construction. The paper explores 8 independent design parameters (path-composition method, n-gram type, stop-list use, TF formula, IDF formula, similarity measure, and threshold size), yielding 576 distinct SSDE model configurations, each with materially different Precision/Recall trade-offs; SSDE models were also benchmarked against a slower doc2vec-based alternative (S3E), showing SSDE achieves higher average Precision with comparable-to-slightly-lower Recall at a small fraction of the computational cost.

## Examples

- Tested against 14 pseudo-real systems from the M57 Patents scenario: about 38% of the 576 SSDE model configurations achieved near-perfect Precision, and about 18% achieved near-perfect Recall, with the standard TF-IDF formula, full-file-path n-grams, cosine similarity, and larger similarity thresholds identified as the parameter values most associated with the strongest-performing models.
- SSDE vs. S3E (prior doc2vec-based work) on the same 14 machines: SSDE averaged 0.607-0.693 Precision vs. S3E's 0.25-0.307, with SSDE's combined train+search time (~127 ms) roughly 18x faster than S3E's (~2271 ms).

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/TF-IDF file-path software-usage signatures cannot achieve high Precision and high Recall simultaneously]]

## References

- [DFCite-1157] Soltani and Hosseini Seno, 2023, "Detecting the software usage on a compromised system: A triage solution for digital forensics", FSI: Digital Investigation 44.
