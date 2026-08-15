---
id: DFW-1215
type: weakness
name: ReFS's circular-buffer journal cannot recover file events older than the buffer's retention window
description: Both ReFS journaling artifacts (the Logfile's Data area and the Change Journal) store transactions in a fixed-size circular buffer in which the oldest transactions are continuously overwritten by new ones, so any file-system event whose transaction record has already been overwritten by the time of acquisition cannot be reconstructed by opcode-replay analysis, regardless of how thorough the parsing methodology is.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1215
source_refs:
  - DFCite-1227
  - DFCite-1269
updated_at: 2026-08-14
status: complete
---

# ReFS's circular-buffer journal cannot recover file events older than the buffer's retention window

## Summary

Unlike NTFS's `$UsnJrnl`, whose deallocated records may sometimes still be carved from disk before being overwritten by an unrelated write, the Change Journal's circular-buffer design means the oldest transaction is constantly and immediately overwritten by the newest, making recovery of an overwritten Change Journal transaction "nearly impossible." The Logfile's Data area uses the same circular-buffer approach for its transaction storage, so the depth of reconstructable history for either artifact is bounded strictly by the buffer's fixed allocated size and the volume's write activity rate.

## Why It Matters

An investigator reconstructing a file-activity timeline from ReFS journaling artifacts alone may underestimate the true historical scope of activity on the volume, since events beyond the buffer's retention window leave no trace and produce no indication in the tool's output that a gap exists — a missing event is indistinguishable from an event that never occurred. This is more severe on volumes with high write activity or a long time since acquisition-worthy events occurred, where the retention window in wall-clock time may be very short.

## Related Mitigations

- [[mitigations/Acquire a ReFS volume promptly and enable the Change Journal in advance when ongoing monitoring is anticipated]]

## Used By

- [[techniques/Reconstruct file-system events from ReFS Logfile transaction-opcode replay]]
- [[techniques/Identify a data-wiping tool from ReFS Logfile deletion opcode patterns]]

## References

- [DFCite-1227] Lee et al., 2021, "Forensic analysis of ReFS journaling", FSI: Digital Investigation 38.
- [DFCite-1269] Kim and Lee, 2026, "Identification of data wiping tools based on deletion patterns in ReFS $Logfile", FSI: Digital Investigation 56, 302069. Notes that a full $Logfile buffer causes reuse (overwriting) of older wiping-related transaction records, and recommends corroborating $Logfile-based wiping-tool findings with other artifacts.
