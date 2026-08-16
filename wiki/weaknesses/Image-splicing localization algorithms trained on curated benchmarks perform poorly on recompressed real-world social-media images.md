---
id: DFW-2077
type: weakness
name: Image-splicing localization algorithms trained on curated benchmarks perform poorly on recompressed real-world social-media images
description: Established image-splicing localization algorithms (e.g. ADQ1, BLK, CAGI, CFA, ELA, DCT, NOI5) achieve much lower true-positive detection rates when benchmarked against images that have been through the repeated re-compression, resizing, and platform-specific processing typical of social media, compared to their reported performance on curated, unprocessed benchmark datasets.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2078
source_refs:
  - DFCite-2085
updated_at: 2026-08-16
status: complete
---

# Image-splicing localization algorithms trained on curated benchmarks perform poorly on recompressed real-world social-media images

## Summary

Benchmarking seven established splicing-localization algorithms against SMIFD-1000, a dataset of 1,000 images (500 authentic, 500 spliced) actually sourced from and re-downloaded through Facebook, Twitter, and Instagram (rather than only synthesized under laboratory conditions), showed all algorithms had substantially degraded true-positive rates at low false-positive-rate operating points compared to their typically reported performance on curated benchmark datasets, with CAGI performing best among those tested but still well short of the accuracy expected from published results on cleaner data.

## Why It Matters

Because social-media platforms routinely re-compress and resize uploaded images and may apply additional platform-specific processing, evidence images collected from social media during an investigation are systematically different from the relatively clean images most splicing-localization algorithms were developed and validated against. An investigator who applies an off-the-shelf splicing detector to a social-media-sourced image and receives a negative (no manipulation detected) result risks a false sense of confidence, since the algorithm's real-world recall on this class of image is measurably lower than its published benchmark accuracy would suggest.

## Related Mitigations

- [[mitigations/Benchmark image-splicing-localization tools against realistic recompressed social-media imagery before relying on their output]]

## Used By

- (No technique page derived from this source beyond the reused dataset-construction technique; this weakness documents a limitation of pre-existing splicing-localization algorithms benchmarked by the paper, per the reuse-first ingestion policy.)

## References

- [DFCite-2085] Rana, Hasnat, and Rahaman, 2022, "SMIFD-1000: Social media image forgery detection database", FSI: Digital Investigation 41, 301392.
