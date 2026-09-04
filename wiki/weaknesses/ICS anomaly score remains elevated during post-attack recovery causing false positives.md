---
id: LWW-1001
type: weakness
name: ICS anomaly score remains elevated during post-attack recovery causing false positives
description: BiGAN-based ICS anomaly scoring keeps assigning a high irregularity score during the system-stabilization period after an attack ends, causing the recovery window to be reported as part of the attack.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-1001
source_refs:
  - LWCite-1001
updated_at: 2026-08-09
status: complete
---

# ICS anomaly score remains elevated during post-attack recovery causing false positives

## Summary

After a cyber attack against an ICS asset ends, the physical process (e.g., water tank levels, chemical dosing) requires time -- sometimes hours -- to return to its normal operating range. Because the BiGAN-based fingerprinting model was trained only on stable, attack-free behavior, this instability continues to register as a deviation from the learned fingerprint, so the anomaly-inference method keeps producing a high irregularity score well after the actual attack window has closed.

## Why It Matters

Extra false-positive detections after the true attack window inflate the reported attack duration and reduce precision/F-measure when compared against ground-truth attack logs, which can mislead forensic prioritization by making investigators believe malicious activity is still ongoing when the system is merely recovering. The dataset's own attack-window labels also carry a 20-22 second start delay relative to the actual physical state change, compounding the discrepancy between machine-inferred and logged attack windows.

## Related Mitigations

- [[mitigations/Exclude recovery-period instability from ICS attack detection window]]

## Used By

- [[techniques/Detect behavioral anomalies using unsupervised deep learning]]

## References

- [LWCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
