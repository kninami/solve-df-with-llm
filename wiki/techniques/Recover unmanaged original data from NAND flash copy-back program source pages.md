---
id: LWT-2033
type: technique
name: Recover unmanaged original data from NAND flash copy-back program source pages
description: The process of recovering data a user believes was deleted from a NAND flash storage device (SSD, USB stick, SD/CF card, eMMC, UFS) by reading the source page a background copy-back program operation left behind as unmanaged data after copying the original content to a new destination page, since the host-level erase or delete command only affects the destination block, not the original source page.
objective_ids:
  - DFO-1018
weakness_ids:
  - LWW-2033
aliases:
  - Copy-back program unmanaged data recovery
source_refs:
  - LWCite-2033
updated_at: 2026-08-14
status: partial
---

# Recover unmanaged original data from NAND flash copy-back program source pages

## Summary

NAND flash memory periodically runs a background copy-back program operation to relocate data from a deteriorating source page to a fresh destination page, protecting against charge-retention data loss. Once relocated, the data at the destination page becomes the "managed" copy the file system and host operating system track and can erase on request, but the original source page's content becomes "unmanaged data" - it is neither tracked by the block-management layer nor touched by the host's subsequent delete/erase commands - and so it typically remains intact and readable on the flash chip even after the host reports the data successfully deleted.

## Details

LWCite-2033 traces the specific mechanism: NAND controller monitors cell deterioration and triggers a copy-back command that reads the source page (with ECC correction, on- or off-chip), writes it to a destination page in another block, and marks the destination as valid/managed data going forward. If the host later requests deletion of that data, the controller issues an erase command only to the block containing the now-managed destination page; the original source block, no longer referenced by the file system's mapping table, is left untouched. An investigator with chip-level access (e.g. via a forensic NAND reader/programmer after chip-off extraction, or low-level controller access) can therefore locate and read the source page directly to recover content the file system and even the storage controller's own logical view report as deleted, without needing any file-carving or file-system-metadata-based recovery method at all.

## Examples

- LWCite-2033's threat-model walkthrough: a host requests deletion of personal information; the controller erases only the destination block (BLK2) containing the managed copy; the unmanaged original (BLK1's source page) remains readable, and an actor with block-management-level access can read it directly via a standard read command routed to the unmanaged block.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Secure copy-back program firmware overwrites unmanaged source-page data, eliminating this recovery opportunity]]

## References

- [LWCite-2033] Ahn and Lee, "Forensics and anti-forensics of a NAND flash memory: From a copy-back program perspective", IEEE Access, 2021 — source of the copy-back program mechanism and unmanaged-data recovery opportunity described above.
