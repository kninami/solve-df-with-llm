---
id: DFT-1170
type: technique
name: Identify a drone's manufacturer and model using RF signal fingerprinting
description: Passively capture a drone's radio frequency transmissions and classify its manufacturer and model from a wavelet-domain RF fingerprint, using machine learning trained on each drone family's distinctive transmission characteristics, without needing physical access to the device.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1177
aliases:
  - RF-based drone detection, identification, and classification
  - DrIfTeR
source_refs:
  - DFCite-1178
updated_at: 2026-08-12
status: complete
---

# Identify a drone's manufacturer and model using RF signal fingerprinting

## Summary

Conventional drone detection methods (radar, vision, acoustic) struggle with small, distant, or visually camouflaged drones, and none of them can determine which manufacturer or model produced a detected drone. Because each drone's radio transmitter has distinct hardware and protocol characteristics, capturing and fingerprinting its RF signal lets an investigator detect, identify the manufacturer of, and classify the specific model of a drone from a distance, without physical access or line of sight.

## Details

The technique first applies wavelet-domain feature extraction and 3-stage wavelet decomposition to preprocess captured RF signals, isolating the distinctive frequency and waveform characteristics of a drone's transmission. Traditional machine learning, deep learning, and ensemble learning models are then evaluated against the extracted features for three progressively finer classification tasks: binary drone detection (is a drone present at all), manufacturer identification, and model-level classification. This complements physical/GCS-based drone forensics (see [[techniques/Extract forensic evidence from a drone and its ground control station]]) by giving an investigator a way to identify a drone's make and model before it is recovered, seized, or brought down — for example, during airspace-incursion or counter-drone incident response, when only its RF emissions are available as evidence.

## Examples

- Evaluated against a benchmark RF dataset covering multiple drone manufacturers and models, the ensemble model achieved effective and accurate detection, manufacturer identification, and model classification, though certain models sharing hardware or transmission modules with others (e.g., the HK-T6A controller and the DJI Phantom 3) were more frequently confused with each other.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/RF fingerprinting misclassifies drone models with overlapping RF signatures due to shared hardware or transmission modules]]

## References

- [DFCite-1178] Choudhary et al., 2025, "DrIfTeR: A Drone Identification Technique using RF signals", FSI: Digital Investigation 54.
