---
id: LWM-1044
type: mitigation
name: Reserve the mutated ensemble detector for high-value files after faster single-model pre-filtering
source_refs:
  - LWCite-1034
updated_at: 2026-08-09
status: complete
---

# Reserve the mutated ensemble detector for high-value files after faster single-model pre-filtering

## Summary

Rather than running the full mutated cross-model ensemble against an entire large corpus, use a faster single-model detector as a first-pass filter to narrow the candidate set, then apply the slower but more accurate ensemble detector only to files that pass the first filter or are otherwise flagged as high-priority.

## Addresses

- [[weaknesses/Mutated cross-model ensemble adversarial detection has substantially higher per-example latency]]

## How To Apply

In a large-scale triage workflow, run an existing faster single-model or dual-model detector across the full corpus first, then apply the mutated ensemble detector selectively to files that the fast filter flags as suspicious, files already otherwise identified as relevant to the investigation, or a representative random sample if adversarial evasion of the fast filter itself is a specific concern. Budget the additional per-file latency into the investigation's timeline explicitly rather than assuming the ensemble method's accuracy gains come at no throughput cost.

## References

- [LWCite-1034] Liu et al., 2021, "A novel adversarial example detection method for malicious PDFs using multiple mutated classifiers", FSI: Digital Investigation 38.
