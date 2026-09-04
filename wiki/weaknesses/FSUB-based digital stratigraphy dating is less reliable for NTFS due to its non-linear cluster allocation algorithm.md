---
id: LWW-1088
type: weakness
name: FSUB-based digital stratigraphy dating is less reliable for NTFS due to its non-linear cluster allocation algorithm
description: While FSUB-based digital stratigraphy dating was demonstrated to the point of practical courtroom applicability for FAT32, and a similar case could likely be constructed for exFAT, NTFS's more complex, non-linear cluster allocation algorithm (and metadata structures located in the middle of the volume rather than only near the start) means the simple "largest written block" FSUB calculation is less reliable for NTFS, requiring further large-scale simulation before conclusions comparable to the FAT32 case can be drawn.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1088
source_refs:
  - LWCite-1080
updated_at: 2026-08-10
status: complete
---

# FSUB-based digital stratigraphy dating is less reliable for NTFS due to its non-linear cluster allocation algorithm

## Summary

The authors state this limitation directly: "for NTFS, the complexity of the allocation algorithm suggests additional larger-scale simulations should be conducted to further understand the consequences of data in non-allocated space on NTFS on removable media. There are likely improvements to the FSUB concept with file systems such as NTFS that do not have a simple linear progression with cluster allocation and have metadata structures in the middle of the volume."

## Why It Matters

An investigator applying the digital-stratigraphy/FSUB technique to an NTFS-formatted recycled storage device should not assume the same confidence level established for FAT32 carries over, since NTFS's allocation behavior can place data in non-allocated space in ways the simple "highest-block-written" FSUB calculation does not correctly characterize as older or newer relative to current file-system activity — a conclusion drawn as if the technique were equally validated across file systems could overstate the strength of a provenance argument in a case involving an NTFS-formatted device.

## Related Mitigations

- [[mitigations/Treat FSUB-based dating conclusions on NTFS as provisional pending further large-scale validation]]

## Used By

- [[techniques/Date non-allocated-space data on recycled storage media using FSUB-based digital stratigraphy]]

## References

- [LWCite-1080] Schneider et al., 2024, "Applying digital stratigraphy to the problem of recycled storage media", FSI: Digital Investigation 49.
