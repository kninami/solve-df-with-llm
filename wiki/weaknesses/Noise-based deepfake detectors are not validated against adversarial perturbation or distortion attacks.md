---
id: LWW-1154
type: weakness
name: Noise-based deepfake detectors are not validated against adversarial perturbation or distortion attacks
description: A deepfake detector that classifies based on extracted forensic noise traces has not been evaluated against deliberate adversarial perturbation or image-distortion attacks targeting the noise signal itself, even though the detector's whole discriminative signal is a noise-domain feature that such attacks are specifically positioned to disrupt.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1154
source_refs:
  - LWCite-1152
updated_at: 2026-08-12
status: complete
---

# Noise-based deepfake detectors are not validated against adversarial perturbation or distortion attacks

## Summary

The authors of a state-of-the-art noise-trace-based deepfake detector explicitly flag as future work the need to "work on defending our model against potential attacks with perturbations and distortions since our approach is noise-based" — acknowledging that, at the time of publication, the model's robustness to deliberate anti-forensic countermeasures targeting its noise-domain feature had not been tested.

## Why It Matters

Because the detector's entire discriminative signal is derived from noise-domain artifacts, an adversary aware of the detection method has a clear, targeted attack surface: adding crafted noise, applying image distortions, or re-compressing content specifically to mask or mimic the expected noise-trace pattern could defeat the classifier in a way that generic robustness testing (e.g., against ordinary re-compression alone) would not reveal. An investigator relying on this detector's output without independent knowledge of whether the specific evidentiary video shows signs of deliberate anti-forensic noise manipulation risks treating a successfully-evaded deepfake as authentic.

## Related Mitigations

- [[mitigations/Test noise-based deepfake detectors against adversarial perturbation and distortion before deployment]]

## Used By

- [[techniques/Detect deepfakes using face-background noise trace comparison]]

## References

- [LWCite-1152] Wang et al., 2022, "Deepfake noise investigation and detection", FSI: Digital Investigation 42.
