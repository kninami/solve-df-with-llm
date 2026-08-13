---
id: DFM-1251
type: mitigation
name: Apply Hybrid DN-MobileNet's noise-threshold-gated selective denoising before source-camera CNN classification
source_refs:
  - DFCite-1265
updated_at: 2026-08-13
status: complete
---

# Apply Hybrid DN-MobileNet's noise-threshold-gated selective denoising before source-camera CNN classification

## Summary

Instead of unconditionally denoising every I-frame before source-camera classification, estimate each frame's noise level (e.g., via a Laplacian filter combined with a robust median-absolute-deviation estimator) and only apply the denoising step to frames whose noise exceeds a validation-derived threshold, preserving camera-intrinsic signal in already low-noise frames.

## Addresses

- [[weaknesses/Denoising a video I-frame before source-camera classification removes camera-intrinsic noise signal along with additive noise]]

## How To Apply

Implement the selective-denoising decision as a pre-classification gate: estimate noise level per I-frame, compare against a threshold set near the median noise level observed on a representative validation set, and route only frames above that threshold through the denoiser before classification. Re-derive the threshold when applying the pipeline to a substantially different device population (e.g., moving from an older-device dataset to a newer-device dataset with more advanced built-in noise reduction), since a threshold tuned on one population may over- or under-denoise frames from a population with systematically different baseline noise characteristics.

## References

- [DFCite-1265] Tigga and Sitara, 2026, "Hybrid DN-MobileNet: A study on an effective framework for source camera identification from videos", FSI: Digital Investigation 57, 302090.
