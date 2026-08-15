---
id: DFW-2028
type: weakness
name: CNN-based end-to-end anti-forensic networks defeat both single- and double-JPEG-compression detectors
description: A single CNN-based anti-forensic network can jointly deceive both single-JPEG and double-JPEG (recompression-history) detectors across DCT-domain and pixel-domain feature spaces, including aligned and non-aligned recompression cases, while producing higher visual quality than earlier single-purpose anti-forensic methods.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2028
source_refs:
  - DFCite-2028
updated_at: 2026-08-14
status: partial
---

# CNN-based end-to-end anti-forensic networks defeat both single- and double-JPEG-compression detectors

## Summary

The source paper trains an EDSR-derived CNN with a combined reconstruction, DCT-histogram-matching, and JPEG-deblocking loss to reconstruct a decompressed JPEG image so that its statistics resemble a genuinely uncompressed image in both the DCT domain (defeating quantization-table/blocking-artifact-based JPEG detectors) and the pixel domain (defeating CNN-based steganalysis-style DJPEG detectors like SRNet). Across six single-JPEG detectors and two DJPEG detectors (including non-aligned recompression cases, which are harder to detect but easier to evade), the method achieved minimum decision error rates close to 0.5 (near-chance) in most tested quality-factor configurations, outperforming both a JPEG-restoration baseline and a prior state-of-the-art anti-forensic method, while degrading visual quality (PSNR/SSIM) less than those alternatives.

## Why It Matters

An investigator relying on JPEG or double-JPEG compression-history detection (whether feature-based or CNN-based) to establish whether an image has been resaved, edited, or manipulated should recognize that this class of anti-forensic tool can defeat a broad range of such detectors simultaneously, at a visual quality high enough to remain plausible as an unmanipulated image, undermining any single detector's negative result as proof of an image's untampered provenance.

## Related Mitigations

- [[mitigations/Check for CNN-reconstruction blur artifacts and use adversarially-trained detectors when JPEG anti-forensics is suspected]]

## Used By

- [[techniques/Detect JPEG compression despite anti-forensic processing using Markov transition probability matrices]]

## References

- [DFCite-2028] Kim et al., 2021 — Tables 1-4 report minimum decision error rates approaching 0.5 across six JPEG detectors and two DJPEG detectors (aligned and non-aligned cases) for the proposed method.
