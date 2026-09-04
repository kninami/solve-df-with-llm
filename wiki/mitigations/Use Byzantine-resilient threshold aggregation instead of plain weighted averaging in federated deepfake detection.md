---
id: LWM-2048
type: mitigation
name: Use Byzantine-resilient threshold aggregation instead of plain weighted averaging in federated deepfake detection
source_refs:
  - LWCite-2049
updated_at: 2026-08-14
status: partial
---

# Use Byzantine-resilient threshold aggregation instead of plain weighted averaging in federated deepfake detection

## Summary

Replace or supplement plain weighted-average threshold aggregation in a multi-organization federated deepfake-detection deployment with a Byzantine-resilient aggregation rule (e.g. coordinate-wise median or trimmed mean), so that a single malicious or compromised client's manipulated threshold submission cannot disproportionately distort the global sparsity pattern shared by the whole federation.

## Addresses

- [[weaknesses/Threshold-averaging aggregation in federated deepfake detection is not robust to adversarial client manipulation]]

## How To Apply

Before deploying this class of federated deepfake-detection scheme across mutually untrusted or loosely trusted organizations, swap the server-side aggregation step from plain averaging to a robust statistic (coordinate-wise median or trimmed mean across submitted threshold vectors) without needing to change the model architecture or client-side local training process, as the source paper's own discussion notes is directly compatible with the existing design. Additionally, monitor for outlier threshold submissions round-over-round as a detection signal for a potentially compromised or malicious participant.

## References

- [LWCite-2049] Al-Fehani et al., 2026 — Section IV.E explicitly identifies coordinate-wise median or trimmed-mean aggregation, drawn from Byzantine-resilient federated learning literature, as a compatible fix that "can be incorporated into TFD without altering the model architecture or local training process."
