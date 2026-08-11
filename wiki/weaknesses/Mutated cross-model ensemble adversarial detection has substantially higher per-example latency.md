---
id: DFW-1044
type: weakness
name: Mutated cross-model ensemble adversarial detection has substantially higher per-example latency
description: Evaluating an input against a large group of mutated classifiers to compute a Prediction Inversion Rate takes substantially longer per example than evaluating it against a single-model detector, constraining how much of a large evidence corpus can practically be triaged with this method within a given time budget.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1044
source_refs:
  - DFCite-1034
updated_at: 2026-08-09
status: complete
---

# Mutated cross-model ensemble adversarial detection has substantially higher per-example latency

## Summary

In the paper's own comparative evaluation, the mutated cross-model ensemble system's average detection time (1.242 seconds per example) was 42-100% higher than each of the three single/pairwise-model detectors it was compared against (0.622-0.875 seconds), a direct consequence of needing to evaluate the query against a large group of models (700 in the reported evaluation) rather than one or two.

## Why It Matters

In a forensic setting where a large volume of PDFs (or similar files) must be triaged under time constraints — such as a large seizure of documents in an active investigation — this latency difference compounds across the full corpus, meaning full-corpus application of the technique may not be practicable within an operational timeframe, even though its detection accuracy is higher. An investigator planning a triage workflow needs to account for this throughput tradeoff rather than assuming the more accurate detector is a drop-in replacement for a faster one at scale.

## Related Mitigations

- [[mitigations/Reserve the mutated ensemble detector for high-value files after faster single-model pre-filtering]]

## Used By

- [[techniques/Mutated cross-model ensemble detection of adversarial classifier evasion]]

## References

- [DFCite-1034] Liu et al., 2021, "A novel adversarial example detection method for malicious PDFs using multiple mutated classifiers", FSI: Digital Investigation 38.
