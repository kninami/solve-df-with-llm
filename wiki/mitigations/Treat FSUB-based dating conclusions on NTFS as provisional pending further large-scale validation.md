---
id: LWM-1088
type: mitigation
name: Treat FSUB-based dating conclusions on NTFS as provisional pending further large-scale validation
source_refs:
  - LWCite-1080
updated_at: 2026-08-10
status: complete
---

# Treat FSUB-based dating conclusions on NTFS as provisional pending further large-scale validation

## Summary

When applying FSUB-based digital stratigraphy dating to an NTFS-formatted device, explicitly caveat the resulting provenance argument as less validated than the equivalent FAT32 case, and where the conclusion is significant to a case, seek additional corroborating evidence rather than relying on the FSUB calculation alone.

## Addresses

- [[weaknesses/FSUB-based digital stratigraphy dating is less reliable for NTFS due to its non-linear cluster allocation algorithm]]

## How To Apply

When reporting an FSUB-based dating conclusion for data recovered from an NTFS volume, state explicitly that the underlying method has been demonstrated to courtroom-applicable confidence for FAT32 but not yet to the same degree for NTFS, given its non-linear cluster allocation and mid-volume metadata structures. Where possible, corroborate the conclusion with independent evidence (e.g. metadata-linked carved files, as suggested in the paper as a way to establish FSUB from a carved file's internal metadata) rather than relying solely on the basic largest-written-block FSUB calculation for NTFS.

## References

- [LWCite-1080] Schneider et al., 2024, "Applying digital stratigraphy to the problem of recycled storage media", FSI: Digital Investigation 49.
