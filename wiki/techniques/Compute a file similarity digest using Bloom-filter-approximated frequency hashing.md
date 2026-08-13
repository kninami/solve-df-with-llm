---
id: DFT-1191
type: technique
name: Compute a file similarity digest using Bloom-filter-approximated frequency hashing
description: Generate a compact similarity digest for a file by chunking its content with a rolling hash, weighting each chunk by an approximate cross-corpus document frequency read from a pre-built Bloom filter instead of an exact frequency table, and comparing digests with cosine similarity to determine whether two files are related.
objective_ids:
  - DFO-1007
weakness_ids:
  - DFW-1198
aliases:
  - FbHash-E
  - Bloom-filter-optimized FbHash similarity hashing
source_refs:
  - DFCite-1209
updated_at: 2026-08-13
status: complete
---

# Compute a file similarity digest using Bloom-filter-approximated frequency hashing

## Summary

FbHash-E is a memory- and time-efficient redesign of the FbHash similarity-hashing algorithm: it chunks a file's content using a smaller rolling-hash window than the original, weights each chunk using a TF-IDF-style score, and looks up each chunk's cross-corpus document frequency in a pre-built Bloom filter (whose member document-frequency values were bucketed via k-means clustering) rather than an exact frequency table, producing a fixed-length digest that two files' digests can be compared against via cosine similarity to score their relatedness.

## Details

Reducing the chunk size from 7 to 5 bytes and the rolling-hash width from 56 to 40 bits shrinks both the per-chunk computation cost and the resulting digest size; replacing the exact document-frequency lookup table with a Bloom filter membership/cluster-bucket approximation removes the original algorithm's dominant memory cost, since exact frequency counts for a large reference corpus no longer need to be stored and looked up directly. Reported results found this combination reduced end-to-end hashing runtime to roughly a third of FbHash's, while similarity-score comparisons remained resistant to the known active reduction and emulation attacks that affect other similarity digest algorithms — see [[weaknesses/Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification]] — because the Bloom-filter approximation and TF-IDF weighting scheme do not introduce the specific feature-length or mapping-function weaknesses those attacks exploit.

## Examples

- On a malware-similarity dataset, FbHash-E achieved 87% detection accuracy in roughly 15 seconds of hashing time, versus FbHash's comparable accuracy in roughly 43 seconds, at the cost of a small, systematic upward bias in reported similarity scores that required recalibrating the tool's match threshold from 16 to 28.

## Related Objectives

- `DFO-1007` Reduce data under consideration

## Related Weaknesses

- [[weaknesses/Bloom-filter-approximated similarity hashing systematically inflates similarity scores relative to exact frequency calculation]]

## References

- [DFCite-1209] Singh et al., 2022, "FbHash-E: A time and memory efficient version of FbHash similarity hashing algorithm", FSI: Digital Investigation 41, 301375.
