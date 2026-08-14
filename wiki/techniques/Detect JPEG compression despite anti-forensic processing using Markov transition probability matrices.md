---
id: DFT-2024
type: technique
name: Detect JPEG compression despite anti-forensic processing using Markov transition probability matrices
description: The process of revealing JPEG compression footprints an anti-forensic tool has deliberately removed from an image's DCT-coefficient histogram, by computing second-order statistical features (Markov Transition Probability Matrices over intra- and inter-block DCT-coefficient differences) that remain disturbed even when first-order histogram-based traces have been smoothed away, and classifying the resulting feature vector with an SVM.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2024
  - DFW-2028
aliases:
  - MTPM-based JPEG forensic detector (K_MTPM)
source_refs:
  - DFCite-2024
  - DFCite-2028
updated_at: 2026-08-14
status: partial
---

# Detect JPEG compression despite anti-forensic processing using Markov transition probability matrices

## Summary

JPEG anti-forensic tools work by adding calibrated dithering noise to smooth out the periodic gaps a JPEG compressor leaves in an image's DCT-coefficient histogram, defeating detectors that rely on first-order (histogram-based) statistics. An investigator can still recover reliable evidence of JPEG compression by moving to second-order statistics: modeling how DCT coefficients change relative to their neighbors (within the same 8x8 block and across adjacent blocks) using a Markov random process, since anti-forensic smoothing that hides first-order histogram gaps does not fully erase these higher-order coefficient-correlation disturbances.

## Details

DFCite-2024's three-step scheme first selects a target difference image: the questioned JPEG image is recompressed at a sweep of quality factors (50-95), the pixel-wise difference between the original and each recompressed version is computed, and the recompression whose difference image has the minimum total-sum is chosen as the target (since this quality factor most closely matches the image's true original compression level, if any). Second, the target difference image's DCT is computed, and Markov Transition Probability Matrices are calculated separately for intra-block (within an 8x8 DCT block) and inter-block (same coefficient position across adjacent blocks) coefficient differences, along horizontal, vertical, main-diagonal, and minor-diagonal directions, yielding 8 MTPMs of 81 features each (state range [-4,4]) for a 648-dimensional feature vector. Third, this feature vector is fed to an SVM classifier trained to distinguish JPEG-compressed (including anti-forensically processed) images from genuinely uncompressed or unaltered images. The same MTPM-based second-order feature is also effective for detecting spliced/tampered images, since splicing introduces DCT-coefficient-correlation inconsistencies at spliced boundaries analogous to those left by JPEG anti-forensics.

## Examples

- DFCite-2024's evaluation: 99.004% accuracy on the UCID dataset distinguishing JPEG-compressed/anti-forensically-processed images from uncompressed images, and 98.75%/98.15% accuracy detecting spliced images on the CASIA v1.0 and Columbia datasets respectively, outperforming compared scalar-based (K_Li, K_AR) and SVM-based (K_SPAM, K_SRM) JPEG forensic detectors across replacement rates and anti-forensic schemes tested.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/MTPM-based JPEG anti-forensic detection is comparatively less accurate against explicit DCT-histogram-smoothing schemes]]
- [[weaknesses/CNN-based end-to-end anti-forensic networks defeat both single- and double-JPEG-compression detectors]]

## References

- [DFCite-2024] Kumar et al., "Digital image forensic approach to counter the JPEG anti-forensic attacks", IEEE Access, 2021 — source of the MTPM-based second-order statistical detection scheme and its evaluation results described above.
- [DFCite-2028] Kim et al., 2021, "End-to-end anti-forensics network of single and double JPEG detection", IEEE Access 9 — demonstrates a more advanced CNN-based anti-forensic method that defeats a broad range of both single- and double-JPEG detectors, representing a further evasion threat beyond the explicit-histogram-smoothing schemes this technique was evaluated against.
