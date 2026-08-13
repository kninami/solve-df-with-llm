---
id: DFM-1156
type: mitigation
name: Configure software-usage signature detection thresholds to prioritize Recall over Precision in forensic triage
source_refs:
  - DFCite-1157
updated_at: 2026-08-12
status: complete
---

# Configure software-usage signature detection thresholds to prioritize Recall over Precision in forensic triage

## Summary

When configuring TF-IDF file-path software-signature detection for investigative triage, deliberately select design parameters (e.g., smaller similarity thresholds, cosine similarity, standard TF-IDF weighting) that favor Recall over Precision, accepting a higher false-positive rate as the cost of reducing the risk of missing genuine software usage evidence.

## Addresses

- [[weaknesses/TF-IDF file-path software-usage signatures cannot achieve high Precision and high Recall simultaneously]]

## How To Apply

Select an SSDE model configuration from the Recall-favoring end of the parameter space identified during signature construction (smaller thresholds, cosine similarity, standard TF-IDF/logarithmic-TF weighting) rather than defaulting to whichever configuration reports the highest raw accuracy figure. Treat flagged software-usage results as an investigative lead list requiring manual confirmation for any finding that will be relied upon evidentially, since the higher false-positive rate accepted by a Recall-favoring configuration means some flagged applications may not actually have run.

## References

- [DFCite-1157] Soltani and Hosseini Seno, 2023, "Detecting the software usage on a compromised system: A triage solution for digital forensics", FSI: Digital Investigation 44.
