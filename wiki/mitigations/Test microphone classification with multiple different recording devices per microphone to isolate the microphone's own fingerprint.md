---
id: LWM-2106
type: mitigation
name: Test microphone classification with multiple different recording devices per microphone to isolate the microphone's own fingerprint
source_refs:
  - LWCite-2124
updated_at: 2026-08-16
status: complete
---

# Test microphone classification with multiple different recording devices per microphone to isolate the microphone's own fingerprint

## Summary

Before relying on a microphone-classification model's accuracy as evidence it identifies a specific microphone's own acoustic fingerprint, validate it against recordings of the same microphone captured through more than one recording device/chain, to confirm accuracy holds when the recording-device confound is controlled for.

## Addresses

- [[weaknesses/Microphone-classification accuracy can conflate the microphone's own fingerprint with the connected recording device's fingerprint]]

## How To Apply

When constructing or selecting a training/evaluation dataset for microphone classification, prefer a dataset (such as the Audio Forensic Dataset for Digital Multimedia Forensics) where each microphone class was recorded through the same fixed recording device across all classes, isolating the microphone as the sole varying factor. Where the only available dataset pairs each microphone class with a different recording device, treat the resulting accuracy as an upper bound on microphone-specific discriminative power rather than a confirmed microphone fingerprint, and where feasible, supplement the evaluation with additional recordings of at least a subset of the same microphones captured through a second, different recording device to directly test whether classification accuracy holds when the device varies. Document this limitation explicitly when reporting a microphone-classification result derived from a confounded dataset.

## References

- [LWCite-2124] Qamhan, Alotaibi, and Selouani, 2023, "Transformer for authenticating the source microphone in digital audio forensics", FSI: Digital Investigation 45, 301539.
