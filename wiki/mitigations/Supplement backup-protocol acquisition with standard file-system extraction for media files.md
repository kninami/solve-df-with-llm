---
id: LWM-1057
type: mitigation
name: Supplement backup-protocol acquisition with standard file-system extraction for media files
source_refs:
  - LWCite-1047
updated_at: 2026-08-09
status: complete
---

# Supplement backup-protocol acquisition with standard file-system extraction for media files

## Summary

Do not rely on a reverse-engineered backup-protocol tool alone for full-device evidence collection; pair it with standard file-system-level extraction to obtain photos, documents, and other media files that fall outside the manufacturer backup protocol's own scope.

## Addresses

- [[weaknesses/Reverse-engineered backup-protocol acquisition does not cover general media files outside the backup data set]]

## How To Apply

When planning acquisition for a device, use the reverse-engineered backup-protocol tool to obtain the structured data categories it covers (contacts, messages, calendar, third-party app data), and separately extract media files (photos, documents) via standard file-system access methods, which typically do not require the special permission the backup protocol itself needs. Document which categories were obtained via which method so the overall evidence collection's completeness can be assessed.

## References

- [LWCite-1047] Park et al., 2022, "A study on data acquisition based on the Huawei smartphone backup protocol", FSI: Digital Investigation 41.
