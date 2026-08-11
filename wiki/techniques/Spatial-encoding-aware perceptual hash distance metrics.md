---
id: DFT-1092
type: technique
name: Spatial-encoding-aware perceptual hash distance metrics
description: Compare two perceptual (semantic/visual) image hashes using a distance metric that accounts for the position and clustering of differing bits — Normalised Convolution Distance (convolving the XOR difference matrix), Hatched Matrix Distance (row/column min-mean summarization), or 2-D N-gram Cosine Distance (sliding-window sub-matrix comparison) — rather than the conventional Normalised Hamming Distance, which only counts how many bits differ while discarding where in the hash those differences fall.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1098
aliases: []
source_refs:
  - DFCite-1091
updated_at: 2026-08-10
status: complete
---

# Spatial-encoding-aware perceptual hash distance metrics

## Summary

Perceptual hashes are almost universally compared using Normalised Hamming Distance, a simple bit-count-difference measure that treats every differing bit as equally significant regardless of its position in the hash. Investigating whether localized/positional changes in an image are actually encoded in the hash's bit layout reveals that they are, and that alternative distance metrics sensitive to this positional structure can recover matching power that Hamming Distance discards.

## Details

Three prototype metrics were evaluated: Normalised Convolution Distance applies a convolutional kernel to the XOR difference matrix between two hashes, producing larger values where differing bits are spatially clustered rather than spread out; Hatched Matrix Distance summarizes row/column-wise minimum and mean values to capture "hatched" weight patterns common in DCT-based hashes; and 2-D N-gram Cosine Distance slides an n×n window across the reshaped hash matrix and computes cosine distance between the resulting flattened n-gram arrays. Tested against pHash, dHash, and wHash (Wavelet Hashing) algorithms, results show measurable improvement over Hamming Distance for certain transform classes, and — notably — the worst-case evasion transform for DCT-based hashes (horizontal/vertical image mirroring) can be completely mitigated using a spatially-aware distance metric, without needing to modify the underlying hash-generation mechanism at all.

## Examples

- For DCT-based perceptual hashes, applying image mirroring (flipping on the x- or y-axis) is a known worst-case transform that defeats Hamming-distance-based matching; using a spatial-encoding-aware distance metric instead fully mitigated this evasion without any change to how the hash itself is generated.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Hamming-distance perceptual hash comparison ignores positional clustering, letting image mirroring evade DCT-based hash matching]]

## References

- [DFCite-1091] McKeown, 2025, "Beyond Hamming Distance: Exploring spatial encoding in perceptual hashes", FSI: Digital Investigation 52.
