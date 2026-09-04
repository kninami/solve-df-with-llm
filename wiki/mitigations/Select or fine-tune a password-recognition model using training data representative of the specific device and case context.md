---
id: LWM-1299
type: mitigation
name: Select or fine-tune a password-recognition model using training data representative of the specific device and case context
source_refs:
  - LWCite-1330
updated_at: 2026-08-15
status: complete
---

# Select or fine-tune a password-recognition model using training data representative of the specific device and case context

## Summary

Before relying on a password-recognition ranking model in casework, confirm (or extend) its training data to include a broad, representative mix — dictionary words, leaked credentials, chat text, and general website text — rather than assuming a model trained on a narrow data source will rank correctly on the device's actual mixed text content.

## Addresses

- [[weaknesses/Password-recognition ranking models underrank passwords unlike the specific mix of data they were trained on]]

## How To Apply

Before applying [[techniques/Rank extracted text strings by password likelihood using fine-tuned language models]], confirm the model's training data spans a broad mix of text types (dictionary words, leaked-credential corpora, chat/messaging text, general website text), not just one narrow source. Where the case's specific text sources (e.g. a particular messaging app, a particular language, an unusual note-taking format) are underrepresented in the model's original training data, consider fine-tuning on additional representative samples before relying on the ranking, and document the training data composition used so ranking results can be properly contextualized when reported.

## References

- [LWCite-1330] van Dijk, van de Wetering, Argentini, Gorka, van Luenen, Minnema, Rijgersberg, Ugen, Mann, and Geradts, 2025, "PaSSw0rdVib3s!: AI-assisted password recognition for digital forensic investigations", FSI: Digital Investigation 52, 301870.
