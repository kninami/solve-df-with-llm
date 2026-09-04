---
id: LWT-1238
type: technique
name: Classify IoT device software activity using deep-learning electromagnetic side-channel analysis
description: Non-invasively determine which of several known software routines or algorithms an IoT or embedded device is executing by capturing the electromagnetic emissions its System-on-Chip radiates during operation and classifying them with a deep learning model, most reliably in the frequency domain rather than the raw time domain.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1185
aliases:
  - IoT EM-SCA software-activity classification
  - Deep-learning EM-SCA for embedded device forensics
source_refs:
  - LWCite-1271
updated_at: 2026-08-14
status: complete
---

# Classify IoT device software activity using deep-learning electromagnetic side-channel analysis

## Summary

An IoT device's System-on-Chip radiates electromagnetic emissions whose fine structure varies measurably with the specific code path it is executing, giving an investigator a way to identify what software activity occurred on a device without needing logical or physical access to its storage or an installed monitoring agent — an important capability for constrained IoT hardware that may lack forensic acquisition support entirely.

## Details

Traces are captured with a software-defined radio and a near-field probe positioned over the target device's SoC while it executes a controlled set of candidate routines (in the underlying study, ten different sorting algorithms used as a proxy for distinguishable software activity classes), then converted into classifier input either as raw time-domain amplitude sequences or as frequency-domain representations (e.g. via Short-Time Fourier Transform). Training and evaluating convolutional neural network classifiers on both representations showed frequency-domain features consistently generalize and classify more reliably than time-domain features, because frequency-domain representations are less sensitive to the precise timing alignment of a trace capture. This general capture-and-classify methodology is the foundation that device-to-device model portability work (see [[techniques/Adapt an EM side-channel-analysis model to new devices using transfer learning]]) builds on when adapting a trained classifier to a new target device.

## Examples

- Frequency-domain CNN classifiers distinguished which of ten different sorting algorithms an embedded target was executing with substantially higher and more consistent accuracy than equivalent time-domain classifiers trained on the same captured traces.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/A pre-trained EM-SCA model does not generalize to a new device without retraining]]

## References

- [LWCite-1271] Han, Kim and Kwon, 2026, "Identifying Internet of Things software activities using deep learning-based electromagnetic side-channel analysis", FSI: Digital Investigation 56, 302072.
