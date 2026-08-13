---
id: DFT-1210
type: technique
name: Reconstruct Windows File History backup and restore activity across host and backup storage devices
description: Systematically examine Windows File History artifacts across three stages — identifying usage traces on the host, determining every associated backup storage device via matching configuration/registry identifiers, and extracting the full backed-up-file history from the Catalog.edb database — to reconstruct a user's past file activity and backup/restore behavior.
objective_ids:
  - DFO-1001
  - DFO-1019
weakness_ids:
  - DFW-1221
aliases:
  - EFIC (Extract File History IntelligenCe)
  - Windows File History three-step examination procedure
source_refs:
  - DFCite-1233
updated_at: 2026-08-13
status: complete
---

# Reconstruct Windows File History backup and restore activity across host and backup storage devices

## Summary

Windows File History (FH), a user-enabled backup feature available since Windows 8, records backup configuration, per-file backup metadata, and restore-operation history across both the host system and whichever storage device (local, USB, or network) the user selected for backups, so a full reconstruction of a user's file history requires correlating artifacts from all associated devices rather than examining the host alone.

## Details

The three-step procedure is: (1) identify FH usage traces on the target host via `Config.xml` (backup cycle, retention policy, target folders), the `fhsvc` service startup-type registry value, and the two FH-specific EVTX event logs (`WHC.evtx` for backup start/end, `BackupLog.evtx` for warnings/errors); (2) determine every storage device that has ever served as an FH backup target by matching volume GUIDs recorded in `Config.xml` against the host's `MountedDevices` registry key (MBR disk signatures or GPT partition GUIDs), since the same GUID appearing on both a host image and a separate storage-device image proves the two are linked; (3) extract the full list of backed-up files and their metadata from the `Catalog.edb` Extensible Storage Engine database's `backupset`, `file`, `namespace`, and `string` tables, which together yield each backed-up file's original path, original created/modified timestamps, size, and the timestamp of the specific backup operation that captured it. Because the two Catalog.edb files (`Catalog1.edb`/`Catalog2.edb`) are updated alternately rather than simultaneously, both must be examined to avoid missing the most recently backed-up or deleted file. The technique further supports investigating anti-forensic misuse of FH's user-facing "Clean Up Versions" (deletion) and "Previous Versions" (restore) features, and their impact on artifact completeness differs by underlying backup-storage file system: on NTFS, a deleted backup's created/accessed/modified timestamps survive unchanged (only the MFT entry-modified time updates), while FAT/exFAT preserves all three original timestamps, in both cases meaning deleted backup entries can potentially be recovered via file-system-level data recovery even after Catalog.edb removes their record.

## Examples

- Cross-referencing a `Win10.E01` host image's `Config.xml` against a separate `USBStor.E01` image's partition GUID confirmed the USB device had been used as that host's FH backup storage, even without directly imaging both devices together.
- Extracting a `test10.txt` record from `Catalog.edb`'s linked `string`/`file`/`namespace`/`backupset` tables reconstructed its original path (`C:\Users\windows10\Desktop\`), original creation and modification timestamps, and the exact backup operation timestamp that captured it.
- A HomeGroup-shared network drive's registry key (`FileHistory\HomeGroup\Target`) recorded the friendly name and URL of a network location used as FH backup storage even after the HomeGroup feature itself was removed from later Windows 10 versions, since existing configurations continued to function.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/File History's restore operation lets a user hide a file behind an identically-pathed decoy without altering the visible backup history]]

## References

- [DFCite-1233] Choi, Park and Lee, 2021, "Forensic exploration on windows File History", FSI: Digital Investigation 36, 301134.
