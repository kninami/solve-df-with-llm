---
id: DFM-1052
type: mitigation
name: Train or fine-tune anomaly detection models separately per target surveillance environment
source_refs:
  - DFCite-1042
updated_at: 2026-08-09
status: complete
---

# Train or fine-tune anomaly detection models separately per target surveillance environment

## Summary

Do not assume a video behavioral anomaly detector trained on one type of environment generalizes to a materially different one; train or fine-tune a separate model using normal-behavior footage specific to each target deployment environment before relying on its output for that environment.

## Addresses

- [[weaknesses/Video behavioral anomaly definitions are context- and environment-dependent]]

## How To Apply

Before deploying a video anomaly detector to a new surveillance environment, collect a representative sample of that environment's own normal/routine activity and use it to train or fine-tune the model, rather than reusing a model trained on a different environment's normal-behavior distribution unmodified. Where cross-environment evaluation is necessary for research or benchmarking purposes, report results per environment separately (as is standard practice, e.g., evaluating on ATM, pedestrian-walkway, and street/shop datasets independently) rather than implying a single model's performance figure applies universally.

## References

- [DFCite-1042] Khaire and Kumar, 2022, "A semi-supervised deep learning based video anomaly detection framework using RGB-D for surveillance of real-world critical environments", FSI: Digital Investigation 40.
