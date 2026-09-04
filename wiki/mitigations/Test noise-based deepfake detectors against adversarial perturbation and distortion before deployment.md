---
id: LWM-1154
type: mitigation
name: Test noise-based deepfake detectors against adversarial perturbation and distortion before deployment
source_refs:
  - LWCite-1152
updated_at: 2026-08-12
status: complete
---

# Test noise-based deepfake detectors against adversarial perturbation and distortion before deployment

## Summary

Before relying on a noise-trace-based deepfake detector's verdict in an investigation, deliberately test it against adversarially perturbed and distorted variants of known deepfake content to characterize how much its noise-domain discriminative signal degrades under targeted anti-forensic countermeasures, rather than assuming its published in-distribution benchmark accuracy carries over to adversarial conditions.

## Addresses

- [[weaknesses/Noise-based deepfake detectors are not validated against adversarial perturbation or distortion attacks]]

## How To Apply

Construct or obtain a test set of deepfake videos deliberately perturbed with noise-domain-targeting countermeasures (added synthetic noise, aggressive re-compression, denoising filters) and re-run the detector against it, comparing accuracy/AUC to the clean-content benchmark. Where evidentiary content shows signs of unusual noise processing or re-encoding history inconsistent with its claimed provenance, treat a noise-based detector's "real" verdict with additional skepticism and corroborate with an independent detection method (e.g., a frequency-domain or spatial-artifact-based detector) rather than relying on the noise-based verdict alone.

## References

- [LWCite-1152] Wang et al., 2022, "Deepfake noise investigation and detection", FSI: Digital Investigation 42.
