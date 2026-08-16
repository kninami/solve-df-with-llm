---
id: DFT-1302
type: technique
name: Validate a logical forensic image's integrity against L01-AFF4-L metadata manipulation
description: Assess whether a logical forensic image in the L01 (EnCase) or AFF4-L (open-source) format has had its metadata tampered with after acquisition, by reverse-engineering each format's internal section structure and per-section integrity-verification elements (checksums, hashes), then systematically testing whether altering, deleting, or adding specific metadata fields is detected by the format's own supporting tools — since, unlike the E01 disk-image format, neither logical-image format provides a single representative whole-file integrity value.
objective_ids:
  - DFO-1010
weakness_ids:
  - DFW-1313
aliases:
  - L01/AFF4-L logical image format integrity analysis
source_refs:
  - DFCite-1356
updated_at: 2026-08-15
status: complete
---

# Validate a logical forensic image's integrity against L01-AFF4-L metadata manipulation

## Summary

Logical imaging — selectively collecting only case-relevant files rather than a full physical image — is increasingly important given growing storage capacities, cloud environments where physical imaging is infeasible, and legal frameworks (the Fourth Amendment, GDPR) that favor minimizing the scope of seized data. But logical image file formats have received comparatively little scrutiny regarding their own integrity guarantees. Reverse-engineering the internal structure of the two most-used logical image formats — L01 (from EnCase) and AFF4-L (the open-source academic proposal, also used in EnCase and Magnet AXIOM Cyber) — and systematically testing metadata manipulation against each format's own verification tooling reveals whether these formats actually protect against post-acquisition tampering of evidence metadata.

## Details

Both formats were analyzed by generating sample logical images (via EnCase for L01, via the pyAFF4 open-source library for AFF4-L) and examining their internal byte structure with a hex viewer, identifying each format's supported metadata fields and internal integrity-verification elements (for L01: per-section Adler-32 checksums covering volume, table, ltree, data, and done sections, plus an MD5 hash over the entire ltree section; for AFF4-L: CRC-32 checksums tied to each file's Local File Header and Central Directory, plus ARN identifiers stored in `information.turtle` and `container.description`). Metadata manipulation was then tested in three categories — changing a value to a different value of the same length, completely deleting an existing value, and adding an arbitrary value to a normally-empty field — using two manipulation depths: "simple" manipulation (altering only the target metadata) and "elaborate" manipulation (also recalculating every checksum, offset, and integrity-verification value that the altered metadata affects, to see whether a technically sophisticated attacker could produce output the format's own supporting tool accepts as valid).

## Examples

- For L01, "elaborate" manipulation — recalculating the section-descriptor checksums, next-section offsets, and any additional in-section integrity elements affected by the change — allowed several metadata fields (including the original file source's MD5/SHA1 hash fields, and Acquisition/Deletion date-time fields) to be freely altered, deleted, or newly populated without EnCase flagging any error, since these elements exist as ordinary, individually-recalculable checksummed fields rather than being covered by any whole-file integrity value.
- For AFF4-L, elaborately manipulating an image's ARN (Address Resolution Name) identifiers at both storage locations (`information.turtle` and `container.description`) and correctly recalculating the corresponding Local File Header and Central Directory CRC-32 values produced a file that the pyAFF4 tool and a standard compression-archive verification program both accepted as intact, despite the underlying data having been substituted.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/L01 and AFF4-L logical image formats lack whole-file integrity verification, letting elaborate metadata manipulation evade detection]]

## References

- [DFCite-1356] Im, Park, Joun, Lee, and Park, 2024, "Revisiting logical image formats for future digital forensics: A comprehensive analysis on L01 and AFF4-L", FSI: Digital Investigation 50, 301811.
