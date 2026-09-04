---
id: LWT-1226
type: technique
name: Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis
description: Assess how well a perceptual hashing algorithm discriminates between different images, and how robust it is against content-preserving modifications, by computing the Hamming-distance distribution between unrelated image pairs (inter-score) and between an image and modified variants of itself (intra-score) across a million-image-scale dataset, rather than relying on small-scale or anecdotal testing.
objective_ids:
  - DFO-1004
weakness_ids:
  - LWW-1098
  - LWW-1244
aliases:
  - Million-image-scale perceptual hash inter/intra-score distribution evaluation
  - PHASER (Perceptual Hashing Algorithms Evaluation and Results)
source_refs:
  - LWCite-1259
  - LWCite-1333
updated_at: 2026-08-15
status: complete
---

# Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis

## Summary

Perceptual hashing algorithms (used, for example, in CSAM and copyright-infringement detection) are deployed at web scale, yet their published evaluations are often small-scale or anecdotal. Computing the full distribution of Hamming-distance scores between large numbers of unrelated image pairs and between an image and several content-preserving modified variants of itself reveals, algorithm by algorithm, how tight and well-separated the "same image" and "different image" score distributions actually are, and which modifications most degrade that separation.

## Details

For each perceptual hashing algorithm under test (evaluated: Facebook/Meta's PDQ, Apple's NeuralHash, the popular pHash library, plus BlockHash, ColourHash, and WaveHash), an inter-score distribution is built from the Hamming distances between large numbers of unrelated image pairs (establishing the algorithm's baseline "different image" noise floor), and an intra-score distribution is built from the Hamming distances between each image and seven content-preserving variants of itself (including cropping, compression, resizing, border addition, watermarking, and horizontal/vertical mirroring), all at a million-image scale. An algorithm is judged robust for a given modification when its intra-score distribution for that modification stays well below (i.e., more similar than) its inter-score distribution, with minimal overlap; algorithms whose inter-score distribution itself clusters into large equivalence classes of accidentally-colliding unrelated images are separately flagged as poor discriminators regardless of their intra-score performance. This distribution-based methodology generalizes beyond the six tested algorithms and is a useful pre-deployment check before relying on Hamming-distance thresholds for any content-matching pipeline at scale.

**Open-source modular framework (PHASER)**: the same research group operationalized this inter/intra-score distribution methodology as an open-source, modular Python evaluation framework, letting a forensic specialist freely combine a Perceptual Hashing Algorithm, an Image Transform, and a Distance Algorithm into a "triplet" and explore its behavior on a bespoke dataset with minimal configuration (a provided Jupyter notebook drives the common workflow, and intermediate hashes/distance scores are saved to portable CSV files for external analysis). PHASER explicitly separates inter-distance observations (unrelated-image-pair comparisons, sampled rather than exhaustively computed once dataset size makes the full pairwise count impractical, since inter-comparisons scale with the square of the image count) from intra-distance observations (each image against its own transformed variants), and supports three evaluation modes: Exploratory Analysis (histogram/KDE plots of the inter/intra distributions), Classification Efficacy (ROC/AUC and Equal-Error-Rate plots treating matching as a classification problem), and Performance Optimisation (an optional bit-level analysis that learns a per-bit weight vector reflecting how much each hash bit contributes to correct classification across transform types, for algorithms/distance-metrics that accept a weighting parameter). Because PHASER's triplet architecture treats the hash algorithm, transform, and distance metric as independently swappable components, it surfaces asymmetric algorithm behavior that a fixed evaluation pipeline could miss — for example, a global-feature-based hash can be entirely unaffected by a transform that defeats most other algorithms, simply because that hash's underlying representation does not encode the structural information the transform disrupts.

## Examples

- Across nearly all tested algorithms, horizontal/vertical mirroring produced the largest intra-score degradation of the seven tested modifications — a finding later confirmed and explained mechanistically for DCT-based hashes by [[techniques/Compare perceptual hashes using spatial-encoding-aware distance metrics]], which showed the underlying weakness is in Hamming-distance comparison rather than in the hash generation itself.
- ColourHash and WaveHash were found to have such poor inter-score discrimination — producing large equivalence classes of Hamming-distance-identical, functionally unrelated images at the million-image scale — that the authors recommend discounting them for large-scale deployment, while PDQ showed the tightest, best-separated distributions of the algorithms tested.
- In a PHASER case-study comparison of ColorHash, PDQ, and pHash against a red-border image transform, ColorHash showed almost complete inter/intra distribution overlap (a threshold balancing false-positive and false-negative rates landed both around 70%, unusably poor), PDQ cleanly separated the two distributions, and pHash showed a moderate overlap requiring an explicit false-positive/false-negative trade-off — illustrating the three general behavior patterns an algorithm/transform/distance triplet can exhibit.
- Testing found that Rotate and Mirroring transforms — difficult for most algorithms — had no detrimental effect on ColorHash specifically, because ColorHash's global colour-histogram representation is insensitive to the pixel-structure changes those transforms introduce, a triplet-level insight the modular framework made straightforward to isolate.
- PHASER's bit-weighting Performance Optimisation mode was experimentally explored as a way to improve an existing algorithm's classification performance without altering its underlying hash-generation mechanism, by learning which bits of the hash reliably carry signal across transform types and down-weighting the rest during distance comparison.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Hamming-distance perceptual hash comparison ignores positional clustering, letting image mirroring evade DCT-based hash matching]]
- [[weaknesses/Low-entropy perceptual hash algorithms produce large equivalence classes that falsely match unrelated images]]

## References

- [LWCite-1259] McKeown and Buchanan, 2023, "Hamming distributions of popular perceptual hashing techniques", FSI: Digital Investigation 44, 301509.
- [LWCite-1333] McKeown, Aaby, and Steyven, 2024, "PHASER: Perceptual hashing algorithms evaluation and results - An open source forensic framework", FSI: Digital Investigation 48, 301680.
