---
id: LWW-1244
type: weakness
name: Low-entropy perceptual hash algorithms produce large equivalence classes that falsely match unrelated images
description: Some perceptual hashing algorithms (found in large-scale testing to include ColourHash and WaveHash) have such poor inter-image discrimination that large numbers of genuinely unrelated images collide within the same small Hamming-distance neighborhood, causing a content-matching pipeline built on them to report false positive matches between images that have no real connection.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-1245
source_refs:
  - LWCite-1259
updated_at: 2026-08-13
status: complete
---

# Low-entropy perceptual hash algorithms produce large equivalence classes that falsely match unrelated images

## Summary

A million-image-scale evaluation of six popular perceptual hashing algorithms found that, while some (notably PDQ) produced tight, well-separated inter-score and intra-score distributions, others (ColourHash and WaveHash in particular) collapsed large numbers of unrelated images into the same or nearly the same hash value, meaning their effective discriminative capacity at scale is far lower than a hash's bit length alone would suggest.

## Why It Matters

A content-matching deployment (e.g., detecting known illicit or copyrighted material across a large corpus) that relies on a low-discrimination perceptual hash algorithm without accounting for its collision behavior will generate a large volume of false-positive matches between genuinely unrelated content, wasting investigative review time and, in high-volume automated pipelines, potentially triggering unwarranted action against innocent content. This risk compounds with any given similarity threshold: a threshold loose enough to catch true near-duplicates for a low-discrimination algorithm will also catch many unrelated images purely by chance.

## Related Mitigations

- [[mitigations/Select higher-entropy perceptual hash algorithms validated by large-scale distance-distribution benchmarking]]

## Used By

- [[techniques/Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis]]

## References

- [LWCite-1259] McKeown and Buchanan, 2023, "Hamming distributions of popular perceptual hashing techniques", FSI: Digital Investigation 44, 301509.
