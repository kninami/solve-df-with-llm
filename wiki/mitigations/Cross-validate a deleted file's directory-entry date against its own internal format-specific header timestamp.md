---
id: DFM-1174
type: mitigation
name: Cross-validate a deleted file's directory-entry date against its own internal format-specific header timestamp
source_refs:
  - DFCite-1172
updated_at: 2026-08-12
status: complete
---

# Cross-validate a deleted file's directory-entry date against its own internal format-specific header timestamp

## Summary

When a recovered deleted file's own internal header carries a format-specific timestamp field (as in EDF/EDF+ session files), use that value rather than the file system's directory-entry date field, which some devices overwrite with a non-standard placeholder on deletion while leaving the time field accurate.

## Addresses

- [[weaknesses/Deleted FAT32 directory entries on some medical devices overwrite creation and access date fields with non-standard placeholder values]]

## How To Apply

Before reporting a date derived from a recovered deleted file's directory entry, check whether the underlying file format embeds its own creation/start date in its header (e.g. an EDF+ file's `startdate` field) and compare the two. If the directory-entry date field contains an implausible or placeholder-looking value (e.g. a two-digit sentinel rather than a real date) while the time field looks accurate, treat the directory-entry date as unreliable for this device family and rely on the internal header value, noting the discrepancy in the examination notes.

## References

- [DFCite-1172] Schmitt and Butterfield, 2024, "Digital forensics in healthcare: An analysis of data associated with a CPAP machine", FSI: Digital Investigation 48, 301661.
