---
id: LWW-1232
type: weakness
name: Retrieval-augmented forensic LLM responses cite sources that do not match the retrieved context or propagate errors from it
description: A RAFT-fine-tuned local LLM's response can carry a fabricated or mismatched citation even while being provided the correct retrieved context, and separately can faithfully reproduce a factual error already present in the retrieved source material, so a well-formatted citation does not by itself confirm either that the source exists as cited or that its content is correct.
categories:
  - ASTM_INAC_EX
  - ASTM_MISINT
mitigation_ids:
  - LWM-1232
source_refs:
  - LWCite-1243
updated_at: 2026-08-13
status: complete
---

# Retrieval-augmented forensic LLM responses cite sources that do not match the retrieved context or propagate errors from it

## Summary

Of 2,244 evaluated ForensicLLM responses, 300 carried a citation that matched neither the title nor the author present in the retrieved context — a hallucinated or mismatched citation despite the correct supporting material having been retrieved — and a user-study participant separately reported a response that was "technically incorrect, but it's not really the LLM's fault, as the research paper it cited contained incorrect descriptions of the tooling," showing the model can faithfully propagate an error already present in its source.

## Why It Matters

An investigator relying on the model's citation as a shortcut to source verification (rather than an invitation to independently check it) risks treating a fabricated or content-mismatched reference as a peer-reviewed anchor for a report claim, undermining the admissibility rationale (Daubert-style peer-review and testability criteria) that motivated using a citation-grounded model in the first place. Ten of the 32 user-study participants separately reported being unable to locate a cited paper online at all, compounding the risk that a plausible-looking citation goes unverified in practice.

## Related Mitigations

- [[mitigations/Independently verify LLM-generated forensic citations against the original source before relying on the response]]

## Used By

- [[techniques/Query digital forensic literature and artifacts using a retrieval-augmented fine-tuned local LLM]]

## References

- [LWCite-1243] Sharma et al., 2025, "ForensicLLM: A local large language model for digital forensics", FSI: Digital Investigation 52, 301872.
