---
id: DFT-1226
type: technique
name: Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis
description: Assess how well a perceptual hashing algorithm discriminates between different images, and how robust it is against content-preserving modifications, by computing the Hamming-distance distribution between unrelated image pairs (inter-score) and between an image and modified variants of itself (intra-score) across a million-image-scale dataset, rather than relying on small-scale or anecdotal testing.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1098
  - DFW-1244
aliases:
  - Million-image-scale perceptual hash inter/intra-score distribution evaluation
source_refs:
  - DFCite-1259
updated_at: 2026-08-13
status: complete
---

# Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis

## Summary

Perceptual hashing algorithms (used, for example, in CSAM and copyright-infringement detection) are deployed at web scale, yet their published evaluations are often small-scale or anecdotal. Computing the full distribution of Hamming-distance scores between large numbers of unrelated image pairs and between an image and several content-preserving modified variants of itself reveals, algorithm by algorithm, how tight and well-separated the "same image" and "different image" score distributions actually are, and which modifications most degrade that separation.

## Details

For each perceptual hashing algorithm under test (evaluated: Facebook/Meta's PDQ, Apple's NeuralHash, the popular pHash library, plus BlockHash, ColourHash, and WaveHash), an inter-score distribution is built from the Hamming distances between large numbers of unrelated image pairs (establishing the algorithm's baseline "different image" noise floor), and an intra-score distribution is built from the Hamming distances between each image and seven content-preserving variants of itself (including cropping, compression, resizing, border addition, watermarking, and horizontal/vertical mirroring), all at a million-image scale. An algorithm is judged robust for a given modification when its intra-score distribution for that modification stays well below (i.e., more similar than) its inter-score distribution, with minimal overlap; algorithms whose inter-score distribution itself clusters into large equivalence classes of accidentally-colliding unrelated images are separately flagged as poor discriminators regardless of their intra-score performance. This distribution-based methodology generalizes beyond the six tested algorithms and is a useful pre-deployment check before relying on Hamming-distance thresholds for any content-matching pipeline at scale.

## Examples

- Across nearly all tested algorithms, horizontal/vertical mirroring produced the largest intra-score degradation of the seven tested modifications — a finding later confirmed and explained mechanistically for DCT-based hashes by [[techniques/Compare perceptual hashes using spatial-encoding-aware distance metrics]], which showed the underlying weakness is in Hamming-distance comparison rather than in the hash generation itself.
- ColourHash and WaveHash were found to have such poor inter-score discrimination — producing large equivalence classes of Hamming-distance-identical, functionally unrelated images at the million-image scale — that the authors recommend discounting them for large-scale deployment, while PDQ showed the tightest, best-separated distributions of the algorithms tested.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Hamming-distance perceptual hash comparison ignores positional clustering, letting image mirroring evade DCT-based hash matching]]
- [[weaknesses/Low-entropy perceptual hash algorithms produce large equivalence classes that falsely match unrelated images]]

## References

- [DFCite-1259] McKeown and Buchanan, 2023, "Hamming distributions of popular perceptual hashing techniques", FSI: Digital Investigation 44, 301509.
