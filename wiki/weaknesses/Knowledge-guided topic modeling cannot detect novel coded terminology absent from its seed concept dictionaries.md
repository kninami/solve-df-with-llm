---
id: DFW-2100
type: weakness
name: Knowledge-guided topic modeling cannot detect novel coded terminology absent from its seed concept dictionaries
description: A topic model seeded with expert-knowledge concept dictionaries is biased toward discovering topics related to the vocabulary an investigator already anticipated, so genuinely novel coded language, newly emerging slang, or case-specific substitute terminology not represented in the seed dictionaries or the model's broader training data can go undetected, even though the underlying unsupervised topic-modeling mechanism does not strictly require an exact keyword match for already-known vocabulary.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2101
source_refs:
  - DFCite-2117
updated_at: 2026-08-16
status: complete
---

# Knowledge-guided topic modeling cannot detect novel coded terminology absent from its seed concept dictionaries

## Summary

Seeding a topic model with expert-knowledge concept dictionaries improves its ability to surface topics matching known vocabulary categories, but this same guidance mechanism means the model's attention is directed toward pre-anticipated concepts; genuinely new coded terminology -- slang a suspect population has recently adopted specifically to evade detection, or terminology specific to a subculture or region the seed dictionaries were not built to cover -- has no equivalent guidance signal and may not be recognized as forming a coherent, investigatively-relevant topic.

## Why It Matters

An investigator relying on a knowledge-guided topic model to triage which messages merit manual review risks a false sense of completeness: the tool's successful identification of anticipated-vocabulary topics does not indicate it has also identified every genuinely relevant topic, particularly ones using coded language the seed dictionaries do not cover. Because coded language specifically evolves to evade detection, and because criminal communication has a documented incentive to adopt exactly this kind of evasive terminology, the failure mode this weakness describes is not a rare edge case but a foreseeable and recurring limitation.

## Related Mitigations

- [[mitigations/Periodically update topic-model seed dictionaries with newly observed coded terminology and manually review low-confidence topic clusters]]

## Used By

- [[techniques/Perform joint semantic analysis of multimodal mobile communication using knowledge-guided topic modeling]]

## References

- [DFCite-2117] "Towards a joint semantic analysis in mobile forensics environments", FSI: Digital Investigation 48, 2024.
