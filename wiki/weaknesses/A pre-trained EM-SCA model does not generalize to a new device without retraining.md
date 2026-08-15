---
id: DFW-1185
type: weakness
name: A pre-trained EM-SCA model does not generalize to a new device without retraining
description: A machine learning model trained on electromagnetic side-channel traces from one device produces near-random results when applied directly to another device, even one of the identical make and model, because small differences in antenna placement, ambient noise, and manufacturing variation between units shift the trace distribution.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1185
source_refs:
  - DFCite-1188
  - DFCite-1271
updated_at: 2026-08-14
status: complete
---

# A pre-trained EM-SCA model does not generalize to a new device without retraining

## Summary

Experiments applying a model trained on one iPhone 13's EM traces to two other iPhone 13 units of the same make and model achieved only 10.5% and 22.3% classification accuracy, and a Principal Component Analysis of the three devices' "idle" traces showed each device's traces form a visibly distinct cluster despite identical hardware specifications. The same failure occurred when testing a model against new trace samples collected from the same device on a different day, indicating the instability is not limited to cross-device variation alone.

## Why It Matters

An investigator who assumes a validated EM-SCA model can be reused as-is across a fleet of the same device model, or reapplied to the same seized device after a delay, risks silently unreliable activity-classification results rather than an obvious failure — the model still produces an output, just an inaccurate one, with no built-in signal that cross-device or cross-time drift has occurred. Treating a single-device-validated model as forensically reliable for other devices without accounting for this drift could support an unsound conclusion about what software activity actually occurred.

## Related Mitigations

- [[mitigations/Retrain only the output layer of a pre-trained EM-SCA model before applying it to a new device]]

## Used By

- [[techniques/Adapt an EM side-channel-analysis model to new devices using transfer learning]]
- [[techniques/Classify IoT device software activity using deep-learning electromagnetic side-channel analysis]]

## References

- [DFCite-1188] Navanesan et al., 2024, "Ensuring cross-device portability of electromagnetic side-channel analysis for digital forensics", FSI: Digital Investigation 48, 301684.
- [DFCite-1271] Han, Kim and Kwon, 2026, "Identifying Internet of Things software activities using deep learning-based electromagnetic side-channel analysis", FSI: Digital Investigation 56, 302072. Confirms that classifier reliability depends on capture and representation choices (frequency- vs. time-domain), consistent with the broader device/session generalization instability documented here.
