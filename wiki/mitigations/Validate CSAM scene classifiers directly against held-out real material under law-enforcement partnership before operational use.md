---
id: LWM-1267
type: mitigation
name: Validate CSAM scene classifiers directly against held-out real material under law-enforcement partnership before operational use
source_refs:
  - LWCite-1292
updated_at: 2026-08-14
status: complete
---

# Validate CSAM scene classifiers directly against held-out real material under law-enforcement partnership before operational use

## Summary

Before relying on an automated scene classifier for CSAM triage, arrange a controlled evaluation against a sample of real held-out CSAM material through an appropriately authorized law-enforcement partnership, rather than accepting public-benchmark accuracy figures as representative of real-world performance.

## Addresses

- [[weaknesses/Scene classifiers trained on public datasets show a large domain gap and degrade sharply on real CSAM]]

## How To Apply

Arrange with a partner law enforcement agency to run a validated model, without further training, against a random or representative sample of their own held-for-research CSAM material under their access controls, and report both overall and per-category accuracy separately (since the domain gap can vary drastically by category). Where per-category accuracy is found to be substantially lower than the public benchmark result, restrict operational use of that category's predictions to a lower-trust triage signal (e.g. a secondary sort key) rather than a primary classification, and disclose the validated real-material accuracy figures alongside the tool's public-benchmark figures in any report or deployment documentation. Periodically re-validate as the tool or its training data changes, since the domain gap is not necessarily static.

## References

- [LWCite-1292] Valois, Macedo, Ribeiro, dos Santos and Avila, 2025, "Leveraging self-supervised learning for scene classification in child sexual abuse imagery", FSI: Digital Investigation 53, 301918.
