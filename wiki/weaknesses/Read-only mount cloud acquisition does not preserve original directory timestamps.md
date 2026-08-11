---
id: DFW-1021
type: weakness
name: Read-only mount cloud acquisition does not preserve original directory timestamps
description: When cloud storage is acquired via a read-only mount and copy operation, file-level modification timestamps are preserved but directory-level timestamps are not — every copied directory is instead stamped with the time the acquisition command was executed, silently discarding the original directory timestamp metadata.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - DFM-1021
source_refs:
  - DFCite-1014
updated_at: 2026-08-09
status: complete
---

# Read-only mount cloud acquisition does not preserve original directory timestamps

## Summary

This is a documented, acknowledged limitation of the underlying tool rather than a misconfiguration: because the tool only tracks individual objects (files) during sync/copy operations and does not treat directories as objects with their own timestamp metadata, every directory created during acquisition receives the timestamp of the copy operation itself, overwriting whatever creation/modification time the directory had on the remote storage. This also affects metadata-only listing operations, not just full copies.

## Why It Matters

An investigator who examines directory timestamps after acquisition (e.g., to establish when a folder was created or last modified on the cloud account) will see only the acquisition time, not the original value, for every directory in the acquired data — a systematic and easily overlooked data-corruption-on-transfer issue that could lead to incorrect conclusions about file/folder history if the acquisition timestamp is mistaken for original metadata. File-level timestamps remain reliable, so the issue is specific to directories.

## Related Mitigations

- [[mitigations/Record or verify original directory timestamps independently of a mount copy operation]]

## Used By

- [[techniques/Read-only mount-based cloud storage acquisition]]

## References

- [DFCite-1014] Breitinger et al., 2022, "A forensic analysis of rclone and rclone's prospects for digital forensic investigations of cloud storage", FSI: Digital Investigation 43.
