---
id: DFT-1161
type: technique
name: Reconstruct firmware RAID virtual disks from Intel and AMD metadata structures
description: Detect that a set of physical disks is configured as a chipset-level (BIOS-managed, driverless-controller) firmware RAID array — Intel Rapid Storage Technology or AMD RAIDXpert2 — by locating and parsing each vendor's Common RAID Disk Data Format-derived metadata, then reconstruct the resulting virtual disk by recovering its five required parameters (physical disk identification, RAID level, disk order, start/end offsets, and stripe size) so it can be mounted and examined as a normal volume.
objective_ids:
  - DFO-1013
weakness_ids:
  - DFW-1166
  - DFW-1167
aliases:
  - X-raid firmware RAID scanning, reconstruction, and recovery
  - Intel RST / AMD RAIDXpert2 virtual disk reconstruction
source_refs:
  - DFCite-1168
updated_at: 2026-08-12
status: complete
---

# Reconstruct firmware RAID virtual disks from Intel and AMD metadata structures

## Summary

Firmware RAID configures a virtual disk through the motherboard's BIOS/chipset rather than a dedicated hardware controller or an OS-level software layer, so it presents no visible controller and leaves no OS-recognizable trace before boot — unlike hardware RAID (visible controller, common in servers) or software RAID (OS-managed, detectable via config files/logs). Both major implementations (Intel RST and AMD RAIDXpert2) base their on-disk metadata on the SNIA Common RAID Disk Data Format (DFF Header, Physical Disk Records, Virtual Disk Records, Configuration Records), stored at a fixed disk offset, which a purpose-built parser can locate and interpret to both detect the RAID configuration and reconstruct the striped virtual disk from the underlying physical disk images.

## Details

Intel RAID metadata is written to the sector immediately preceding each physical disk's last sector; AMD RAID metadata is stored at two fixed byte offsets (0xA00000 and 0xB00000) and additionally includes a DDF Header (Anchor) and Controller Data section absent from Intel's implementation. Reconstructing any virtual disk (deleted or intact) requires recovering five parameters: physical disk identity, RAID level, correct disk order, start/end offsets on each disk, and stripe size. Intel identifies disks only by their storage-device serial number (requiring the investigator to manually map disk images to physical disks during acquisition), while AMD generates and stores its own unique per-disk identifier (GUID) directly in the metadata, enabling more reliable automatic matching. RAID level is inferred from parity structure when not stated explicitly: identical data across disks at the same offset indicates RAID 0, an XOR-consistent parity relationship indicates RAID 5, and paired-identical-data patterns indicate RAID 10; AMD additionally stores an explicit RAID Level Signature plus First/Second Count fields that make level identification deterministic rather than inferred. Disk order can often be recovered from the position of a boot record, present only on the first physical disk of an array. Once all five parameters are recovered, the virtual disk is reconstructed by sequencing stripe-sized blocks across the physical disk images in the correct order, after which it can typically be mounted and examined with standard forensic tools regardless of its underlying file system, since the reconstruction process operates below the file-system layer.

## Examples

- X-raid, a proof-of-concept open-source CLI tool implementing this methodology, offers a Quick Scan mode (checking the known fixed metadata offset) and a Deep Scan mode (a full 16-byte-increment sequential scan of the disk image, as a fallback when improper shutdowns, firmware updates, or filesystem repair operations have shifted or partially overwritten metadata away from its expected location).
- Evaluated across RAID 0, 1, 5, and 10 configurations on both Intel and AMD test systems (using 2-4 physical SSDs per array), X-raid successfully reconstructed every normal (non-deleted) virtual disk configuration tested, with reconstruction times ranging from about 2 to 14 minutes depending on RAID level and array size.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data

## Related Weaknesses

- [[weaknesses/Firmware RAID configuration is undetectable by standard forensic tools and indistinguishable from a standalone disk]]
- [[weaknesses/Guessed stripe size or disk order silently produces a misaligned firmware RAID reconstruction]]

## References

- [DFCite-1168] Yun et al., 2025, "Digital forensic approaches to Intel and AMD firmware RAID systems", FSI: Digital Investigation 54, 301971.
