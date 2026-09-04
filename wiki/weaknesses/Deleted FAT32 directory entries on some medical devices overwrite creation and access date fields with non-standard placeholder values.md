---
id: LWW-1174
type: weakness
name: Deleted FAT32 directory entries on some medical devices overwrite creation and access date fields with non-standard placeholder values
description: On at least one medical device's FAT32 implementation, deleting a file overwrites the directory entry's creation-date and last-accessed-date fields with non-standard sentinel values while leaving the corresponding time fields intact, so an examiner who reads the date field at face value obtains an inaccurate date for the deletion event.
categories:
  - ASTM_INAC_COR
  - ASTM_MISINT
mitigation_ids:
  - LWM-1174
source_refs:
  - LWCite-1172
updated_at: 2026-08-12
status: complete
---

# Deleted FAT32 directory entries on some medical devices overwrite creation and access date fields with non-standard placeholder values

## Summary

On the examined CPAP device, a deleted file's directory entry has its creation-date field overwritten with the non-standard value `0x0032` and its last-accessed-date field overwritten with `0x0031`, while the corresponding time fields remain accurate, an undocumented behavior not typical of ordinary FAT32 deletion.

## Why It Matters

An examiner who is unaware of this device-specific quirk and reads the directory-entry date fields as-is will report an incorrect or nonsensical deletion date, potentially undermining a reconstructed treatment timeline; the file's own internal EDF+ header start-date field, and the filename itself (which encodes the recording's original date), remain reliable alternate sources for the correct date.

## Related Mitigations

- [[mitigations/Cross-validate a deleted file's directory-entry date against its own internal format-specific header timestamp]]

## Used By

- [[techniques/Parse EDF+ session files to reconstruct medical device therapy timelines]]

## References

- [LWCite-1172] Schmitt and Butterfield, 2024, "Digital forensics in healthcare: An analysis of data associated with a CPAP machine", FSI: Digital Investigation 48, 301661.
