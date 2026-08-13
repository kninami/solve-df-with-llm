---
id: DFW-1168
type: weakness
name: Keyword-anchored LLM message triage fails to identify crime-related messages that omit the search keyword
description: A pipeline that pre-filters messages by keyword match before LLM relevance classification can only ever judge messages containing the search term, so crime-related content phrased indirectly, metaphorically, or in slang without the flagged word is never presented to the model and is silently excluded from the investigation.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1168
source_refs:
  - DFCite-1173
updated_at: 2026-08-12
status: complete
---

# Keyword-anchored LLM message triage fails to identify crime-related messages that omit the search keyword

## Summary

Using a fixed keyword (e.g. "drugs") to pre-select the candidate message set before applying an LLM to judge relevance means the model never sees, and therefore cannot flag, genuinely crime-related messages that describe the same activity without using the flagged term.

## Why It Matters

Investigators relying on this pipeline may reasonably assume that a low or zero LLM-flagged hit rate for a keyword means little relevant material exists, when in fact relevant conversations using code words, slang, or indirect phrasing were never surfaced for review in the first place. This creates a systematic blind spot that grows worse as suspects become more aware that keyword searches are used against them.

## Related Mitigations

- [[mitigations/Supplement keyword search with semantic embedding similarity to capture indirect crime references in LLM message triage]]

## Used By

- [[techniques/Classify keyword-matched message context as crime-relevant using an LLM majority-vote ensemble]]

## References

- [DFCite-1173] Kim et al., 2025, "Digital forensics in law enforcement: A case study of LLM-driven evidence analysis", FSI: Digital Investigation 54, 301939.
