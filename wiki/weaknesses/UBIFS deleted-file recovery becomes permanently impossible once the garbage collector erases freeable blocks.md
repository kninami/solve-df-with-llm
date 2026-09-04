---
id: LWW-2107
type: weakness
name: UBIFS deleted-file recovery becomes permanently impossible once the garbage collector erases freeable blocks
description: Once UBIFS's garbage collector identifies a logical erase block as containing no live data ("freeable") and erases it -- which happens whenever the journal is committed and the flash device is running low on available space -- any deleted-file content or metadata that block held is permanently and unrecoverably destroyed, and this erasure runs autonomously as part of normal file system operation rather than requiring any deliberate anti-forensic action.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2108
source_refs:
  - LWCite-2126
updated_at: 2026-08-16
status: complete
---

# UBIFS deleted-file recovery becomes permanently impossible once the garbage collector erases freeable blocks

## Summary

UBIFS marks a logical erase block as "freeable" once it contains no data still referenced by the current file-index, and the garbage collector then reclaims freeable blocks (via an unconditional erase, since flash's underlying physical constraints require a full block erase before it can be reused) whenever the journal is committed and the device is running low on free space. Because a deleted file's remaining data typically resides in blocks that eventually become freeable once no longer referenced, the window during which such content remains recoverable is bounded by how soon garbage collection reclaims the relevant block, a process that operates automatically as part of ordinary device use rather than as a deliberate anti-forensic action by a suspect.

## Why It Matters

An investigator who delays acquiring a UBIFS-based device's flash image risks losing recoverable deleted-file evidence to entirely routine, automatic garbage-collection activity that has nothing to do with deliberate evidence destruction -- meaning the same urgency that applies to volatile RAM evidence also applies, to a meaningful degree, to UBIFS flash storage specifically. Because garbage collection frequency depends on how full the device's flash is and how actively it continues to be used after the file was deleted, the actual time window for recovery is device- and usage-dependent and cannot be assumed to match intuitions calibrated on traditional block-based file systems, where deleted data commonly persists far longer absent an explicit overwrite.

## Related Mitigations

- [[mitigations/Acquire a UBIFS flash image as soon as possible and prefer journal-aware analysis before garbage collection erases evidence]]

## Used By

- [[techniques/Recover deleted files from UBIFS flash file systems using journal-based scanning]]

## References

- [LWCite-2126] Deutschmann and Baier, 2024, "Ubi est indicium? On forensic analysis of the UBI file system", FSI: Digital Investigation 48, 301689.
