---
id: DFT-2026
type: technique
name: Identify IoT device internal behavior using electromagnetic side-channel analysis
description: The process of non-invasively determining what software activity a live IoT device or smartphone is currently performing by capturing its unintentional electromagnetic radiation with a software-defined radio and near-field antenna, converting the signal to a frequency-domain feature vector, and classifying it with a machine-learning model trained on that device's known behaviors.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-2026
aliases:
  - EM-SCA (electromagnetic side-channel analysis) for IoT forensics
  - EMvidence framework
source_refs:
  - DFCite-2026
updated_at: 2026-08-14
status: partial
---

# Identify IoT device internal behavior using electromagnetic side-channel analysis

## Summary

Most IoT devices store minimal data on-board, are often encrypted, and are only forensically informative while running - so turning a device off to move it to a lab destroys the opportunity to learn what it was doing. An investigator instead places a near-field probe over the device's system-on-chip while it remains powered on at the scene, captures its electromagnetic radiation at the CPU clock frequency using a software-defined radio (no physical tampering or storage access required), and classifies the resulting signal with a machine-learning model trained to recognize that device model's specific internal software activities (e.g. answering a voice command, playing media, being idle, powering on).

## Details

DFCite-2026 acquires EM traces using a HackRF One SDR with an RF Explorer near-field H-loop antenna positioned over each device-under-test's SoC at its known CPU clock frequency, using complex I/Q sampling at the SDR's maximum 20MHz sample rate/bandwidth. Captured time-domain I/Q data is converted to the frequency domain via Short-Time Fourier Transform (2048-sample window, 256-sample/12% overlap), producing a 2048-feature vector per trace that is far more informative for classification than the noisy raw time-domain signal, since frequency-domain conversion separates the information-leaking components from external noise. Per-device multi-layer perceptron, random forest, and CNN classifiers are trained on these STFT feature vectors to distinguish each device's own set of software-activity labels, with MLP the strongest classifier overall (up to 99.96% accuracy on Samsung SmartThings Hub) though CNN or Random Forest occasionally edged it out for specific devices. To make this practical for field investigators without ML expertise, the trained per-device model is packaged as an installable plug-in (a ZIP file bundling the serialized model and a callback-function Python script) for the open-source EMvidence framework, which coordinates EM data acquisition, plug-in-based analysis, and report generation from a central core so that a third-party developer's device-specific expertise can be reused across the wider forensic community without every investigator needing their own copy of every IoT device model.

## Examples

- DFCite-2026's public EM side-channel dataset covering 8 device types (Amazon Echo Show 5/Dot, Google Home, Samsung SmartThings Hub, Apple iPhone 4S, Sony Xperia T, Samsung Galaxy Grand Prime, Nokia 4.2), 2 physical units per type, and 8-10 labeled software-activity classes per device, stored in HDF5 format (~53GB raw, ~12GB compressed).

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/EM side-channel behavior classifiers have unverified portability across different physical units of the same device model]]

## References

- [DFCite-2026] Sayakkara and Le-Khac, "Electromagnetic side-channel analysis for IoT forensics: Challenges, framework, and datasets", IEEE Access, 2021 — source of the EM-SCA acquisition/classification pipeline, the EMvidence plug-in architecture, and the published EM dataset described above.
