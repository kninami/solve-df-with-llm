---
id: DFW-1313
type: weakness
name: L01 and AFF4-L logical image formats lack whole-file integrity verification, letting elaborate metadata manipulation evade detection
description: Neither the L01 nor the AFF4-L logical image format provides a single representative hash or checksum covering the entire image file the way E01 does, and because each format's internal, per-section or per-file integrity elements are individually recalculable, an attacker who elaborately manipulates metadata — recalculating every affected checksum, offset, and hash — can produce a modified image that the format's own supporting tools (EnCase for L01, pyAFF4 and standard archive tools for AFF4-L) verify and accept as intact.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1315
source_refs:
  - DFCite-1356
updated_at: 2026-08-15
status: complete
---

# L01 and AFF4-L logical image formats lack whole-file integrity verification, letting elaborate metadata manipulation evade detection

## Summary

Because L01's and AFF4-L's integrity mechanisms are structured as independent, locally-scoped checksums covering individual sections or files rather than a single value covering the entire image, an attacker with knowledge of the format internals can alter metadata (original-file hash values, acquisition/deletion timestamps, source identifiers) and then correctly recompute every checksum and offset the alteration affects, producing a file that passes the format's own built-in verification with no error reported — a fundamentally different, weaker guarantee than E01's whole-file hash, which cannot be locally patched around in the same way.

## Why It Matters

An investigator or opposing party who relies on a logical image passing its native tool's built-in verification as proof the image has not been tampered with since acquisition may be relying on a false assurance, since this research demonstrates that elaborate metadata manipulation of exactly the fields most relevant to establishing originality and chain of custody (original-file hashes, acquisition and deletion timestamps) can be made undetectable by the format's own tooling. This directly undermines the evidentiary purpose of a logical image format — establishing that collected evidence has not been altered after collection — for any case where L01 or AFF4-L integrity was the sole basis for that assurance.

## Related Mitigations

- [[mitigations/Compute and independently store a whole-file hash of a logical image at acquisition time rather than relying on the format's internal checksums alone]]

## Used By

- [[techniques/Validate a logical forensic image's integrity against L01-AFF4-L metadata manipulation]]

## References

- [DFCite-1356] Im, Park, Joun, Lee, and Park, 2024, "Revisiting logical image formats for future digital forensics: A comprehensive analysis on L01 and AFF4-L", FSI: Digital Investigation 50, 301811.
