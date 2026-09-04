---
id: LWM-1168
type: mitigation
name: Supplement keyword search with semantic embedding similarity to capture indirect crime references in LLM message triage
source_refs:
  - LWCite-1173
updated_at: 2026-08-12
status: complete
---

# Supplement keyword search with semantic embedding similarity to capture indirect crime references in LLM message triage

## Summary

Because a keyword-anchored LLM triage pipeline can only judge messages that already contain the search term, augment it with a semantic embedding search over the full message corpus so that crime-relevant messages phrased without the flagged keyword (metaphor, slang, indirect reference) can still be surfaced for review.

## Addresses

- [[weaknesses/Keyword-anchored LLM message triage fails to identify crime-related messages that omit the search keyword]]

## How To Apply

Embed the full message corpus (not just keyword hits) using a sentence/document embedding model, then rank messages by cosine similarity to a small set of representative crime-relevant example messages or phrases. Route both the keyword-matched set and the top semantically-similar-but-keyword-absent messages through the same LLM relevance-classification and majority-vote pipeline, rather than relying on keyword matching alone to decide what gets reviewed.

## References

- [LWCite-1173] Kim et al., 2025, "Digital forensics in law enforcement: A case study of LLM-driven evidence analysis", FSI: Digital Investigation 54, 301939.
