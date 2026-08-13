---
id: DFT-1178
type: technique
name: Adapt an EM side-channel-analysis model to new devices using transfer learning
description: Port a pre-trained Electromagnetic Side-Channel Analysis (EM-SCA) machine learning model to a new but similar device by retraining only its output layer on a small set of traces from the new device, rather than training a fresh model from scratch or applying the original model directly.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1185
aliases:
  - Cross-device portability of EM-SCA
  - Transfer learning for EM-SCA digital forensics
source_refs:
  - DFCite-1188
updated_at: 2026-08-13
status: complete
---

# Adapt an EM side-channel-analysis model to new devices using transfer learning

## Summary

EM-SCA lets an investigator identify a smart device's software activity (e.g. which app was used) non-invasively, by classifying the electromagnetic radiation its System-on-Chip emits during operation. A machine learning model trained on one device's EM traces does not transfer reliably to another device, even an identical make and model, so this technique freezes the pre-trained model's internal layers and retrains only its output layer on a modest number of traces captured from the new target device.

## Details

Traces are captured with a software-defined radio (e.g. HackRF One) and a near-field H-loop antenna positioned over the device's SoC, then converted to frequency-domain windows via Short-Time Fourier Transform for use as classifier input. A baseline Multi-Layer Perceptron trained and tested on the same device reaches near-100% accuracy, but applying that same model directly to a second identical device (or to a new trace sample from the same device captured on a different day) collapses to well under 20% accuracy, because minor differences in antenna placement, ambient EM noise, and even manufacturing variation between "identical" units produce measurably different trace signatures. Retraining only the final (output) layer of the pre-trained model — leaving the earlier layers, which encode general SoC-level EM signal structure, frozen — restores accuracy to 70-98% while requiring far less new training data and time than training a device-specific model from scratch. The specific layer(s) retrained can be varied (output-only, input-only, or top/bottom layer combinations) depending on how much of the original device's learned features remain relevant to the new device.

## Examples

- Applying a model trained on one iPhone 13 directly to two other iPhone 13 units (same make and model) achieved only 10.5% and 22.3% accuracy; retraining just the output layer on each target device raised accuracy to 70-96%.
- Applying transfer learning to a Nordic Semiconductor nRF52-DK IoT development kit produced a similar accuracy recovery over direct cross-device application, extending the result beyond smartphones to resource-constrained IoT hardware.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/A pre-trained EM-SCA model does not generalize to a new device without retraining]]

## References

- [DFCite-1188] Navanesan et al., 2024, "Ensuring cross-device portability of electromagnetic side-channel analysis for digital forensics", FSI: Digital Investigation 48, 301684.
