---
id: LWM-2078
type: mitigation
name: Benchmark image-splicing-localization tools against realistic recompressed social-media imagery before relying on their output
source_refs:
  - LWCite-2085
updated_at: 2026-08-16
status: complete
---

# Benchmark image-splicing-localization tools against realistic recompressed social-media imagery before relying on their output

## Summary

Before relying on a splicing-localization algorithm's output for an image collected from social media, re-validate its detection rate against a dataset built from images actually sourced through and re-downloaded from the relevant social-media platforms (e.g. SMIFD-1000), rather than assuming its published benchmark accuracy on curated datasets will transfer.

## Addresses

- [[weaknesses/Image-splicing localization algorithms trained on curated benchmarks perform poorly on recompressed real-world social-media images]]

## How To Apply

When splicing-localization output will inform a determination about a social-media-sourced image, prefer an algorithm independently benchmarked against realistic, platform-recompressed imagery (of the algorithms compared in SMIFD-1000, CAGI performed best) over one validated only on curated laboratory datasets. Treat a "no manipulation detected" result on a social-media-sourced image with additional caution given the measured recall degradation on this image class, and corroborate with an independent forensic indicator (e.g. metadata inconsistency, reverse image search, or manual visual review) rather than relying on the algorithm's output alone.

## References

- [LWCite-2085] Rana, Hasnat, and Rahaman, 2022, "SMIFD-1000: Social media image forgery detection database", FSI: Digital Investigation 41, 301392.
