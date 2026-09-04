---
id: LWW-1098
type: weakness
name: Hamming-distance perceptual hash comparison ignores positional clustering, letting image mirroring evade DCT-based hash matching
description: Normalised Hamming Distance, the conventional way of comparing two perceptual hashes, counts only how many bits differ and discards where those differing bits fall within the hash, even though positional/spatial information is demonstrably encoded in the hash's bit layout — as a result, a horizontal or vertical mirroring transform applied to an image is a worst-case evasion against Hamming-distance-based matching for DCT-based perceptual hashes.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1098
source_refs:
  - LWCite-1091
  - LWCite-1259
updated_at: 2026-08-13
status: complete
---

# Hamming-distance perceptual hash comparison ignores positional clustering, letting image mirroring evade DCT-based hash matching

## Summary

The paper's findings show that "the relative position of bits in the hash does encode useful information" that Hamming Distance simply discards by treating every differing bit identically regardless of location; consequently, "perceived hash weaknesses may actually be deficits in the distance metric being used" rather than deficits in the hash-generation mechanism itself. Mirroring an image (flipping on the x- or y-axis) is specifically identified as a worst-case transform for DCT-based hashes under Hamming Distance comparison. An earlier million-image-scale evaluation of six perceptual hashing algorithms independently reached the same conclusion from the opposite direction: across nearly all tested algorithms, mirroring produced the largest degradation in intra-image Hamming-distance score of the seven content-preserving modifications tested — see [[techniques/Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis]].

## Why It Matters

An investigator or large-scale content-matching provider relying on Hamming Distance to detect previously-encountered images (e.g. known illicit content) can be evaded by a trivial, easily-automated mirroring transform, even though the underlying perceptual hash itself may have adequately captured the image's visual content — meaning the vulnerability is fixable at the comparison-metric layer without needing to redesign or replace the hash algorithm already deployed at scale.

## Related Mitigations

- [[mitigations/Use spatial-encoding-aware distance metrics instead of Hamming Distance for DCT-based perceptual hash comparison]]

## Used By

- [[techniques/Compare perceptual hashes using spatial-encoding-aware distance metrics]]

## References

- [LWCite-1091] McKeown, 2025, "Beyond Hamming Distance: Exploring spatial encoding in perceptual hashes", FSI: Digital Investigation 52.
- [LWCite-1259] McKeown and Buchanan, 2023, "Hamming distributions of popular perceptual hashing techniques", FSI: Digital Investigation 44, 301509. Earlier million-image-scale study independently identifying mirroring as the most destructive content-preserving modification across nearly all tested algorithms.
