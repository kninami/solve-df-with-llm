---
id: DFW-2031
type: weakness
name: NTFS journal-based timestamp manipulation detection is limited by journal retention capacity
description: NTFS journal-based timestamp manipulation detection can only find manipulation events still recorded within the $LogFile's (base 64MB, typically 2-3 hours of data) or $UsnJrnl's (base 32MB, typically 30-40 hours of data) retention window, so manipulation events that occurred further in the past than the journal's actual retained history are undetectable by this technique regardless of how effective the detection algorithm itself is.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2031
source_refs:
  - DFCite-2031
updated_at: 2026-08-14
status: partial
---

# NTFS journal-based timestamp manipulation detection is limited by journal retention capacity

## Summary

The source paper's own discussion states plainly that "NTFS journal-based detection methods have limited detection range due to the default data capacity of NTFS journals," giving $LogFile a base capacity of 64MB (typically 2-3 hours of data) and $UsnJrnl a base capacity of 32MB (typically 30-40 hours of data), with the actual retention period varying by the volume of file operations occurring on the system. Because journal entries are overwritten as new operations occur, once a timestamp-manipulation event's record has aged out of the journal, no amount of algorithmic improvement to the detection method can recover it.

## Why It Matters

An investigator who acquires a system's NTFS journals well after a suspected timestamp-manipulation incident - which is common, since the incident may not be identified as suspicious until much later - may find that the specific manipulation event has already been overwritten in $LogFile (often within hours) and possibly in $UsnJrnl as well (within a day or two on a busy system), even though the manipulated file and its now-falsified timestamps remain on disk. This can leave an investigator unable to directly confirm manipulation occurred, only that the file's current timestamps are suspicious by other (less direct, indirect-type) means.

## Related Mitigations

- [[mitigations/Maximize NTFS journal file size proactively as part of forensic readiness to extend the detectable timestamp-manipulation window]]

## Used By

- [[techniques/Detect NTFS timestamp manipulation using $LogFile and $UsnJrnl journal analysis]]

## References

- [DFCite-2031] Oh et al., 2024 — Section VIII "Discussion" states the base capacities and typical retention windows for $LogFile and $UsnJrnl and identifies this as a limitation of all NTFS journal-based detection methods, including the one proposed in the paper.
