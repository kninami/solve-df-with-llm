---
id: DFM-1315
type: mitigation
name: Compute and independently store a whole-file hash of a logical image at acquisition time rather than relying on the format's internal checksums alone
source_refs:
  - DFCite-1356
updated_at: 2026-08-15
status: complete
---

# Compute and independently store a whole-file hash of a logical image at acquisition time rather than relying on the format's internal checksums alone

## Summary

At the moment a logical image (L01 or AFF4-L) is created, compute a cryptographic hash of the entire image file and store it independently of the image itself (in a separate chain-of-custody record), rather than relying solely on the format's own internal, individually-recalculable section/file checksums to later demonstrate the image has not been altered.

## Addresses

- [[weaknesses/L01 and AFF4-L logical image formats lack whole-file integrity verification, letting elaborate metadata manipulation evade detection]]

## How To Apply

Immediately after creating an L01 or AFF4-L logical image using [[techniques/Validate a logical forensic image's integrity against L01-AFF4-L metadata manipulation]]'s findings as a guide to the format's limitations, compute a whole-file cryptographic hash (e.g. SHA-256) of the resulting image file and record it in a separately maintained chain-of-custody log, independent of the image file itself. At any later point the image's integrity needs to be verified, recompute the whole-file hash and compare it against the independently stored value, rather than relying on the format's own built-in verification tooling reporting no errors — since that tooling cannot detect an elaborate, internally-consistent metadata manipulation. Where organizational policy allows, prefer a format with genuine whole-file integrity verification (such as E01) for evidence where post-acquisition tamper-evidence is a priority and logical imaging's selective-collection benefit is not essential.

## References

- [DFCite-1356] Im, Park, Joun, Lee, and Park, 2024, "Revisiting logical image formats for future digital forensics: A comprehensive analysis on L01 and AFF4-L", FSI: Digital Investigation 50, 301811.
