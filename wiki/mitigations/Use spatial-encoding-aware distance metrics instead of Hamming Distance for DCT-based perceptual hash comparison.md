---
id: DFM-1098
type: mitigation
name: Use spatial-encoding-aware distance metrics instead of Hamming Distance for DCT-based perceptual hash comparison
source_refs:
  - DFCite-1091
updated_at: 2026-08-10
status: complete
---

# Use spatial-encoding-aware distance metrics instead of Hamming Distance for DCT-based perceptual hash comparison

## Summary

When comparing DCT-based perceptual hashes for content matching, use a positional/spatial-encoding-aware distance metric (Normalised Convolution Distance, Hatched Matrix Distance, or 2-D N-gram Cosine Distance) instead of, or alongside, Normalised Hamming Distance, particularly to catch mirrored duplicates of known images.

## Addresses

- [[weaknesses/Hamming-distance perceptual hash comparison ignores positional clustering, letting image mirroring evade DCT-based hash matching]]

## How To Apply

For DCT-based perceptual hash content-matching pipelines (e.g. detecting known illicit images), add a spatially-aware distance metric — no change to the underlying hash-generation algorithm is required. At minimum, explicitly test matching performance against mirrored (horizontally and vertically flipped) variants of known images, since this is the identified worst-case evasion transform under plain Hamming Distance.

## References

- [DFCite-1091] McKeown, 2025, "Beyond Hamming Distance: Exploring spatial encoding in perceptual hashes", FSI: Digital Investigation 52.
