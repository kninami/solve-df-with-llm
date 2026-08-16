---
id: DFW-2105
type: weakness
name: Microphone-classification accuracy can conflate the microphone's own fingerprint with the connected recording device's fingerprint
description: When a microphone-classification dataset's classes are constructed from microphones each connected to a different recording device (mixer, sound card, or other hardware), a classifier's high accuracy cannot be confidently attributed to the microphone's own acoustic fingerprint alone, since the connected recording device may itself introduce a distinguishing electronic signature that the classifier could be learning instead of, or in addition to, the microphone's actual characteristics.
categories:
  - ASTM_INAC_AS
  - ASTM_MISINT
mitigation_ids:
  - DFM-2106
source_refs:
  - DFCite-2124
updated_at: 2026-08-16
status: complete
---

# Microphone-classification accuracy can conflate the microphone's own fingerprint with the connected recording device's fingerprint

## Summary

On the KSU speech database, where the four classification classes each correspond to a specific microphone paired with a specific recording device (e.g. a Nokia-Mobile microphone recorded via a specific sound card, versus a Shure microphone recorded via a Yamaha mixer), the classifier's exceptionally high measured accuracy (99.38%) could not be confidently attributed to the microphones' own acoustic fingerprints in isolation, since each class also varied in which recording device captured it -- the paper's own discussion explicitly acknowledges this: "we cannot confirm that the result was related to the fingerprint of the microphones only because of the possibility that the classification was affected by the recording devices connected to them."

## Why It Matters

An investigator or researcher relying on a microphone-classification result derived from a dataset with this confound risks overstating what the classifier has actually demonstrated: a high accuracy score on such a dataset shows the classifier can distinguish between the specific microphone-plus-device combinations present in the training data, not necessarily that it can identify the microphone alone when it is later connected to a different, previously-unseen recording device -- a scenario very plausible in real casework where the exact recording chain used to capture evidence audio may differ from any training example.

## Related Mitigations

- [[mitigations/Test microphone classification with multiple different recording devices per microphone to isolate the microphone's own fingerprint]]

## Used By

- [[techniques/Identify a recording's source microphone using a spectrogram-based transformer classifier]]

## References

- [DFCite-2124] Qamhan, Alotaibi, and Selouani, 2023, "Transformer for authenticating the source microphone in digital audio forensics", FSI: Digital Investigation 45, 301539.
