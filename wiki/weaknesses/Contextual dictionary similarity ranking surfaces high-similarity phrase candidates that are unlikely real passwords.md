---
id: DFW-1245
type: weakness
name: Contextual dictionary similarity ranking surfaces high-similarity phrase candidates that are unlikely real passwords
description: Ranking a knowledge-graph-derived candidate dictionary purely by semantic similarity to a seed word can place multi-word phrases or overly literal thematic terms — implausible as real password choices — ahead of more probable single-word or lightly-mangled candidates, which can waste guesses within a time-boxed cracking attempt's limited budget.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1246
source_refs:
  - DFCite-1260
updated_at: 2026-08-13
status: complete
---

# Contextual dictionary similarity ranking surfaces high-similarity phrase candidates that are unlikely real passwords

## Summary

Because the knowledge-graph traversal and embedding-similarity ranking used to compose a contextual password dictionary scores candidates purely on thematic closeness to the seed, terms that are highly relevant to the theme but structurally implausible as passwords (e.g., full article titles or multi-word phrases rather than single words) can rank ahead of candidates a real user would be more likely to have actually chosen.

## Why It Matters

In a time-sensitive, triage-driven investigation, a dictionary attack is typically run against a fixed guess or time budget rather than exhaustively. If the highest-ranked entries in a contextual dictionary are dominated by implausible phrase-level candidates, the guesses actually attempted within that budget skew away from the more probable real-world password structures, reducing the effective hit rate the contextual approach is meant to improve and potentially causing an investigator to conclude — incorrectly — that the target's password is not context-derived at all.

## Related Mitigations

- [[mitigations/Filter or split high-ranked contextual dictionary phrase candidates before a time-boxed cracking attempt]]

## Used By

- [[techniques/Generate a contextual password dictionary using knowledge-graph seed-word traversal and similarity ranking]]

## References

- [DFCite-1260] Kanta, Coisel, and Scanlon, 2023, "Harder, better, faster, stronger: Optimising the performance of context-based password cracking dictionaries", FSI: Digital Investigation 44, 301507.
