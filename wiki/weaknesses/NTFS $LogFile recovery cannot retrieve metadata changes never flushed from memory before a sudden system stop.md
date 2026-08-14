---
id: DFW-2032
type: weakness
name: NTFS $LogFile recovery cannot retrieve metadata changes never flushed from memory before a sudden system stop
description: Record-level $LogFile recovery can only reconstruct metadata operations that were actually written to disk before a system stopped; file-system changes that were still cached in memory and never flushed to $LogFile at the moment of a sudden shutdown are absent from the journal entirely and cannot be recovered by any $LogFile-based method, however effective.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2032
source_refs:
  - DFCite-2032
updated_at: 2026-08-14
status: partial
---

# NTFS $LogFile recovery cannot retrieve metadata changes never flushed from memory before a sudden system stop

## Summary

The source paper's own MV Sewol ferry case study demonstrates this limitation directly: after fully recovering the ferry's $LogFile data, investigators confirmed that only data runs through the 80th entry (corresponding to the 08:32 recording) had been saved to $MFT and $LogFile on disk; "as the system suddenly stopped, the last data runs of 201404160832.vdo in memory were not saved to disk," and no trace of the two subsequent 08:33/08:34 recording files exists in $LogFile at all - not because the files were deleted, but because "their metadata were not saved to $MFT due to the sudden termination of the system." No amount of record-carving sophistication can recover data that was never written to the journal in the first place.

## Why It Matters

An investigator recovering $LogFile data after a sudden system stop (crash, power loss, physical destruction mid-operation) must recognize that a gap in the recovered journal - such as the absence of expected recent file activity - may reflect data that was genuinely lost from volatile memory before it could be flushed to disk, rather than evidence that the activity never occurred or was deliberately deleted. Misinterpreting this gap as an absence-of-evidence finding (e.g. concluding a video was never recorded) rather than a memory-flush timing artifact could materially affect the investigation's conclusions, as it nearly did in the cited case.

## Related Mitigations

- [[mitigations/Corroborate a $LogFile recovery gap immediately preceding a system stop with independent evidence before concluding data never existed]]

## Used By

- [[techniques/Recover damaged NTFS $LogFile data using record-level carving]]

## References

- [DFCite-2032] Oh et al., 2022 — Section VII "Case Study" documents the MV Sewol ferry example where the last data runs before the sudden shutdown were never flushed to $LogFile/$MFT, and explicitly distinguishes this from a deletion scenario.
