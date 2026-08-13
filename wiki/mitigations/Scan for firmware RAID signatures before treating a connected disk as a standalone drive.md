---
id: DFM-1166
type: mitigation
name: Scan for firmware RAID signatures before treating a connected disk as a standalone drive
source_refs:
  - DFCite-1168
updated_at: 2026-08-12
status: complete
---

# Scan for firmware RAID signatures before treating a connected disk as a standalone drive

## Summary

Before imaging and examining any physical disk from a modern (2017-onward AMD or 2020-onward Intel-chipset) desktop or server system as a standalone drive, check it for firmware RAID metadata — either live (via the vendor driver or a signature-scanning tool) or by scanning the fixed metadata offsets in an acquired disk image.

## Addresses

- [[weaknesses/Firmware RAID configuration is undetectable by standard forensic tools and indistinguishable from a standalone disk]]

## How To Apply

On a live system, use a firmware-RAID-aware detection tool (e.g. one that queries the Intel/AMD RAID driver via S.M.A.R.T. data, as X-raid does) to check whether the storage devices attached are part of a firmware RAID array before proceeding, since this check can be performed without altering system state. On a dead system, physically inspect motherboard/controller connections to enumerate all attached disks, then scan each acquired image at Intel's known offset (last sector - 1) and AMD's known offsets (0xA00000/0xB00000) for RAID metadata signatures — falling back to a full sequential scan if BIOS updates, improper shutdowns, or filesystem repairs may have shifted the metadata's expected location. Only after firmware RAID is confirmed absent should a disk be examined as an ordinary standalone drive.

## References

- [DFCite-1168] Yun et al., 2025, "Digital forensic approaches to Intel and AMD firmware RAID systems", FSI: Digital Investigation 54, 301971.
