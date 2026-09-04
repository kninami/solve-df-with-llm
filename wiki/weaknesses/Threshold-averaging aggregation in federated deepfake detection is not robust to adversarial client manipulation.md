---
id: LWW-2048
type: weakness
name: Threshold-averaging aggregation in federated deepfake detection is not robust to adversarial client manipulation
description: A federated deepfake-detection scheme that aggregates client-submitted pruning thresholds using plain weighted averaging can have its global sparsity pattern distorted by a single malicious or compromised participating client, since the aggregation method itself provides no protection against a client deliberately submitting misleading threshold values.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - LWM-2048
source_refs:
  - LWCite-2049
updated_at: 2026-08-14
status: partial
---

# Threshold-averaging aggregation in federated deepfake detection is not robust to adversarial client manipulation

## Summary

The source paper's own "Privacy and Security Considerations" section states plainly: "Potential security risks arise if malicious clients manipulate their threshold vectors to distort the global sparsity pattern. Our current implementation aggregates thresholds using weighted averaging, which is effective under benign conditions but not inherently robust to adversarial manipulation." A federated network spanning multiple independent organizations (forensic labs, law enforcement agencies, platforms) inherently has a larger attack surface than a single-organization deployment, and any one compromised or malicious participant could submit threshold values engineered to prune away filters that are actually important for detecting a specific type of deepfake, degrading the shared model's detection capability for all participants.

## Why It Matters

A forensic network relying on this federated scheme to jointly improve deepfake detection is only as trustworthy as its least-trusted participant under the current aggregation design; an adversary with access to (or control of) one participating node - whether an external attacker or a malicious insider at a participating organization - could degrade the shared detector's ability to catch specific forgery types across the entire federation without needing to compromise the central server or any other client's data directly.

## Related Mitigations

- [[mitigations/Use Byzantine-resilient threshold aggregation instead of plain weighted averaging in federated deepfake detection]]

## Used By

- [[techniques/Train federated deepfake detectors across forensic labs using threshold-based sparsity sharing]]

## References

- [LWCite-2049] Al-Fehani et al., 2026 — Section IV.E explicitly identifies this threshold-manipulation vulnerability as a limitation of the current weighted-averaging aggregation implementation.
