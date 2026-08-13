---
id: DFW-1177
type: weakness
name: RF fingerprinting misclassifies drone models with overlapping RF signatures due to shared hardware or transmission modules
description: RF-fingerprint-based drone model classification confuses two models whose transmitters share underlying hardware or transmission modules, since their RF signatures overlap closely enough that the classifier cannot reliably distinguish them.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1177
source_refs:
  - DFCite-1178
updated_at: 2026-08-12
status: complete
---

# RF fingerprinting misclassifies drone models with overlapping RF signatures due to shared hardware or transmission modules

## Summary

Evaluating DrIfTeR's model-level classification, the authors observed a concentration of misclassifications between two specific classes — attributed directly to "overlapping RF signature patterns due to shared hardware or transmission modules" between those models, rather than to noise or preprocessing error.

## Why It Matters

An investigator relying on RF fingerprinting to identify a drone's model should treat a classification result as provisional rather than conclusive when the reported model is known to share a transmitter design or hardware components with other models on the market, since the classifier may reliably detect the presence and manufacturer of the drone while still misattributing it to the wrong specific model.

## Related Mitigations

- [[mitigations/Apply finer time-frequency or deep-learning feature extraction to disambiguate RF-fingerprint-confusable drone models]]

## Used By

- [[techniques/Identify a drone's manufacturer and model using RF signal fingerprinting]]

## References

- [DFCite-1178] Choudhary et al., 2025, "DrIfTeR: A Drone Identification Technique using RF signals", FSI: Digital Investigation 54. Attributes concentrated model-level misclassification (e.g., HK-T6A as Phantom 3) to overlapping RF signatures from shared hardware or transmission modules.
