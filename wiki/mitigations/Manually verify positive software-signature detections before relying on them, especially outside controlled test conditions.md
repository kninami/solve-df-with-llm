---
id: DFM-2021
type: mitigation
name: Manually verify positive software-signature detections before relying on them, especially outside controlled test conditions
source_refs:
  - DFCite-2021
updated_at: 2026-08-14
status: partial
---

# Manually verify positive software-signature detections before relying on them, especially outside controlled test conditions

## Summary

Treat a software signature search engine's positive detection as a triage lead requiring confirmation, not as case-ready evidence, since its measured precision on realistic data is substantially lower than on controlled test machines; manually confirm a small set of the flagged software's most distinctive file paths on the target disk before relying on the detection.

## Addresses

- [[weaknesses/Software signature search engine precision degrades sharply on realistic forensic datasets]]

## How To Apply

Where feasible, select S3E model configurations shown in prior benchmarking to perform best on realistic (not just controlled) datasets, prefer models with a small threshold (associated with better recall-precision balance on M57-like data in the source study), and always follow up a positive detection with a manual check of a handful of the underlying software signature's highest-confidence file paths on the actual target disk before treating the software's presence as established.

## References

- [DFCite-2021] Soltani et al., 2021 — Tables 4-7 identify which specific S3E design-parameter combinations (PV-DM, small/medium threshold, smaller window size) performed best on the realistic M57 dataset specifically, distinct from the best performers on controlled machines.
