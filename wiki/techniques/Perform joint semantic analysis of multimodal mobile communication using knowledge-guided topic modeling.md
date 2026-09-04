---
id: LWT-2095
type: technique
name: Perform joint semantic analysis of multimodal mobile communication using knowledge-guided topic modeling
description: Reduce manual review effort for large volumes of extracted mobile-device communication (text messages, call metadata, and other multimodal artifacts) by jointly applying topic modeling seeded with investigator-curated expert-knowledge concept dictionaries, surfacing which conversations or message clusters relate to investigatively relevant topics (e.g. drugs, weapons, or other case-specific concept categories) rather than requiring an analyst to read every extracted message individually.
objective_ids:
  - DFO-1003
  - DFO-1012
weakness_ids:
  - LWW-2100
aliases:
  - JoSemA
  - Joint semantic analysis in mobile forensics
source_refs:
  - LWCite-2117
updated_at: 2026-08-16
status: complete
---

# Perform joint semantic analysis of multimodal mobile communication using knowledge-guided topic modeling

## Summary

A mobile device extraction can contain thousands of text messages and calls, only a small fraction of which are investigatively relevant, making manual review impractical at scale. Knowledge-guided topic modeling addresses this by combining unsupervised topic discovery (which groups messages by shared word-distribution patterns rather than requiring pre-labeled training data) with investigator-supplied expert-knowledge concept dictionaries (curated lists of terms associated with a case-relevant concept, such as drug slang or weapon references), letting the model surface topically-relevant message clusters an analyst can prioritize for manual review.

## Details

Topics are represented as probability distributions over words rather than single labels, so a topic capturing, for instance, drug-related discussion is characterized by the relative prevalence of a whole cluster of associated terms rather than requiring an exact keyword match -- this is intended to be more robust to the coded language, slang, and substitute terminology criminal communication often uses to evade simple keyword search. Expert-knowledge concept dictionaries let an investigator seed the model with case-specific vocabulary known to be relevant (e.g. a list of drug-related slang terms compiled from prior casework or open-source intelligence) before the topic-modeling process runs, biasing the discovered topics toward investigatively meaningful groupings rather than relying purely on whatever word co-occurrence patterns happen to emerge unsupervised from the dataset. The "joint" aspect combines this semantic text analysis with other available multimodal signal (e.g. call metadata, timing, or contact-relationship information extracted alongside the messages) so that a flagged topic cluster can be considered together with its surrounding communication context rather than in isolation.

## Examples

- Applied to a mobile-forensics-relevant message corpus, the knowledge-guided topic model surfaced clusters of messages associated with investigator-supplied concept dictionaries (e.g. drug-related terminology), letting an analyst prioritize review of those clusters over the full unfiltered message set.

## Related Objectives

- `DFO-1003` Review content for relevance
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Knowledge-guided topic modeling cannot detect novel coded terminology absent from its seed concept dictionaries]]

## References

- [LWCite-2117] "Towards a joint semantic analysis in mobile forensics environments", FSI: Digital Investigation 48, 2024.
