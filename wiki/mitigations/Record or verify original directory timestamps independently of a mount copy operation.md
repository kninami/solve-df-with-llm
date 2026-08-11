---
id: DFM-1021
type: mitigation
name: Record or verify original directory timestamps independently of a mount copy operation
source_refs:
  - DFCite-1014
updated_at: 2026-08-09
status: complete
---

# Record or verify original directory timestamps independently of a mount copy operation

## Summary

Do not rely on the directory timestamps of files acquired via a read-only mount-and-copy operation as evidence of their original state on the cloud account; capture original directory timestamps through a separate mechanism (a direct API listing call, or the provider's own metadata export) before or during acquisition.

## Addresses

- [[weaknesses/Read-only mount cloud acquisition does not preserve original directory timestamps]]

## How To Apply

Before or alongside a mount-based copy acquisition, separately query the cloud provider's API (e.g., a directory-listing command) or export any metadata report the provider offers, and preserve that output as the authoritative record of original directory timestamps. When reporting findings, note explicitly that directory timestamps in the copied filesystem reflect the acquisition time, not the original cloud timestamp, to prevent a reader from misinterpreting them as original evidence.

## References

- [DFCite-1014] Breitinger et al., 2022, "A forensic analysis of rclone and rclone's prospects for digital forensic investigations of cloud storage", FSI: Digital Investigation 43.
