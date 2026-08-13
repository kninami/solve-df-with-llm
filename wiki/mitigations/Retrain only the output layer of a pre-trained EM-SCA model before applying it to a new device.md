---
id: DFM-1185
type: mitigation
name: Retrain only the output layer of a pre-trained EM-SCA model before applying it to a new device
source_refs:
  - DFCite-1188
updated_at: 2026-08-13
status: complete
---

# Retrain only the output layer of a pre-trained EM-SCA model before applying it to a new device

## Summary

Before relying on a pre-trained EM-SCA classification model against a new target device (or the same device examined again after a time gap), capture a modest set of new EM traces from that device and retrain only the model's final output layer, keeping the earlier layers frozen, rather than either reusing the original model unmodified or training an entirely new model from scratch.

## Addresses

- [[weaknesses/A pre-trained EM-SCA model does not generalize to a new device without retraining]]

## How To Apply

Capture new EM traces from the specific target device under investigation, using the same acquisition setup (SDR, near-field antenna position, sample rate) as was used to train the original model where possible. Reconstruct the pre-trained model, freeze all layers except the output layer, and retrain that output layer on the newly captured traces for a modest number of epochs. Validate the retrained model against held-out traces from the same target device before relying on its classifications, since which layer(s) are most effective to retrain (output-only, input-only, or a top/bottom split) can depend on how similar the new device's internal EM signal structure is to the original training device. This substantially reduces both the data volume and training time needed compared to training a device-specific model from scratch, while restoring accuracy from near-random (under 20%) to the 70-98% range observed in testing.

## References

- [DFCite-1188] Navanesan et al., 2024, "Ensuring cross-device portability of electromagnetic side-channel analysis for digital forensics", FSI: Digital Investigation 48, 301684.
