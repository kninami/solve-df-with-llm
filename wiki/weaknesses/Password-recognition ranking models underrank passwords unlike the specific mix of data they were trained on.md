---
id: DFW-1297
type: weakness
name: Password-recognition ranking models underrank passwords unlike the specific mix of data they were trained on
description: A password-recognition model's ranking quality depends on how well its training data's variety (dictionary words, leaked credentials, chat text, website text) matches the kind of password and surrounding non-password text actually present on a given device, so a model trained on a narrower mix (e.g. only dictionary words and leaked credentials) will rank a genuine but atypical password lower than a model trained on a broader, more representative mix.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1299
source_refs:
  - DFCite-1330
updated_at: 2026-08-15
status: complete
---

# Password-recognition ranking models underrank passwords unlike the specific mix of data they were trained on

## Summary

The underlying research's central finding on training-data composition is that "expanding the training set beyond dictionary words and leaked credentials is critical" and that "a wide variety of non-password data should be used to ensure the model is able to perform well when confronted with the variety of data that are stored on modern devices" — implying that a model trained on a narrower data mix systematically underperforms specifically because its training distribution does not represent the full variety of real device text.

## Why It Matters

An investigator relying on a password-recognition model trained on a narrow or unrepresentative data mix (for example, only public leaked-credential lists) risks the true password being ranked far down the candidate list, or missed within a practical time budget, even though the model appears to perform well on its own benchmark data. Since a "secure phone" scenario typically allows only a limited number of password attempts before lockout or wipe, ranking accuracy directly determines whether the investigation succeeds, making training-data representativeness a decision with direct case consequences rather than a purely academic concern.

## Related Mitigations

- [[mitigations/Select or fine-tune a password-recognition model using training data representative of the specific device and case context]]

## Used By

- [[techniques/Rank extracted text strings by password likelihood using fine-tuned language models]]

## References

- [DFCite-1330] van Dijk, van de Wetering, Argentini, Gorka, van Luenen, Minnema, Rijgersberg, Ugen, Mann, and Geradts, 2025, "PaSSw0rdVib3s!: AI-assisted password recognition for digital forensic investigations", FSI: Digital Investigation 52, 301870.
