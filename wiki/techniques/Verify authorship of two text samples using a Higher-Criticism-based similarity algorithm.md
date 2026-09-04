---
id: LWT-1115
type: technique
name: Verify authorship of two text samples using a Higher-Criticism-based similarity algorithm
description: Determine whether two bodies of text (e.g. comments and posts from two social media accounts) were written by the same person by chunking each text into equal-length segments and computing a Higher-Criticism (HC) statistical-testing distance between the chunk sets, an intrinsic authorship-verification method that requires no external reference corpus, complex feature engineering, or topic-specific tuning.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1121
aliases:
  - ChunkedHCs
  - HC-based similarity authorship verification
source_refs:
  - LWCite-1115
updated_at: 2026-08-12
status: complete
---

# Verify authorship of two text samples using a Higher-Criticism-based similarity algorithm

## Summary

Undisclosed or fake social media accounts are used to facilitate cyberbullying, fraud, and other illegal activity, motivating a need to determine whether two accounts' writing was produced by the same person. ChunkedHCs applies the Higher Criticism statistical test — originally developed to detect whether any of a large set of independent hypothesis tests deviates from the global null — to a binomial word-occurrence model between chunked segments of two texts, using the resulting HC statistic as a distance measure between the texts' writing styles.

## Details

The algorithm has three steps: (1) each of the two input texts is split into chunks of identical character length; (2) for each word in the combined vocabulary, a p-value is computed from a binomial model of how symmetrically that word's occurrences are distributed between the two texts' chunk corpora, and the HC statistic is derived as the maximum standardized discrepancy across the sorted p-values; (3) the resulting HC distance is converted into a similarity probability, with a decision threshold tuned per text-length interval on a validation set. Because words influencing the HC statistic are empirically shown to be "author-characteristic" (small p-value, low variance, consistent across topics) rather than "topic-related" (large variance, topic-specific), the method automatically emphasizes stylistic signal over subject-matter overlap without requiring explicit feature selection, and is intrinsic — it needs no corpus of other authors' writing to compare against. Evaluated on Reddit users' comments and posts (informal English text), classification accuracy and F1 both rose steadily with the combined text length used, reaching 0.94 accuracy and an F1 of 0.9381 for text pairs between 29,000 and 30,000 characters.

## Examples

- Applied to pairs of Reddit accounts' combined comment/post text at the 29,000-30,000 character length interval, ChunkedHCs achieved 0.94 accuracy and 0.9381 F1 in distinguishing same-author from different-author account pairs.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/HC-based authorship verification accuracy is unreliable for short text samples]]

## References

- [LWCite-1115] Le et al., 2021, "ChunkedHCs algorithm for authorship verification problems: Reddit case study", FSI: Digital Investigation 37.
