---
id: LWW-1266
type: weakness
name: Scene classifiers trained on public datasets show a large domain gap and degrade sharply on real CSAM
description: An indoor scene classifier's accuracy on public benchmark datasets does not predict its accuracy on real child sexual abuse material, because CSAM systematically differs from staged public scene photography in ways the model was never exposed to during training — most significantly, the near-universal presence of a child in the frame, which public scene datasets rarely depict.
categories:
  - ASTM_MISINT
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1267
source_refs:
  - LWCite-1292
updated_at: 2026-08-14
status: complete
---

# Scene classifiers trained on public datasets show a large domain gap and degrade sharply on real CSAM

## Summary

A self-supervised indoor-scene classifier reached 71.6% balanced accuracy on its public benchmark validation set but only 36.7% balanced accuracy on real CSAM evaluated under law-enforcement partnership, with entire scene categories ("child's room," "living room") frequently confused with each other and with "dressing room." Because public scene datasets are typically staged photography of empty or adult-occupied rooms, while CSAM by definition depicts a child present in essentially every image, a model trained only on the former learns visual cues (object arrangement, lighting, color palette) that are systematically different from — and in some categories actively misleading for — real target material.

## Why It Matters

An investigator or tool developer who evaluates a scene classifier's suitability for CSAM triage using only public benchmark accuracy figures risks substantially overestimating its real-world performance, since the gap identified here (35 percentage points) is large enough to change a tool from broadly reliable to only marginally useful for many scene categories. Because access to real CSAM for validation is itself tightly restricted, this domain gap can persist undetected until a tool is already in operational use, unless a dedicated, access-controlled validation step against real material is built into the tool's development and deployment process.

## Related Mitigations

- [[mitigations/Validate CSAM scene classifiers directly against held-out real material under law-enforcement partnership before operational use]]

## Used By

- [[techniques/Classify indoor scenes in CSAM triage using self-supervised pretraining]]

## References

- [LWCite-1292] Valois, Macedo, Ribeiro, dos Santos and Avila, 2025, "Leveraging self-supervised learning for scene classification in child sexual abuse imagery", FSI: Digital Investigation 53, 301918.
