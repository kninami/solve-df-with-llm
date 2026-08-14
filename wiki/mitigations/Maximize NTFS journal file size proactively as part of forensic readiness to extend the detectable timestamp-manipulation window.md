---
id: DFM-2031
type: mitigation
name: Maximize NTFS journal file size proactively as part of forensic readiness to extend the detectable timestamp-manipulation window
source_refs:
  - DFCite-2031
updated_at: 2026-08-14
status: partial
---

# Maximize NTFS journal file size proactively as part of forensic readiness to extend the detectable timestamp-manipulation window

## Summary

As a forensic-readiness measure, proactively configure both $LogFile and $UsnJrnl to their maximum supported size (4GB each) on systems where timestamp-manipulation detection may later be needed, so that a longer history of journal-recorded timestamp changes remains available if an incident is discovered after some delay.

## Addresses

- [[weaknesses/NTFS journal-based timestamp manipulation detection is limited by journal retention capacity]]

## How To Apply

For organizations or systems where forensic readiness is a priority, increase the $LogFile and $UsnJrnl maximum size settings (up to the 4GB NTFS-supported maximum) well before an incident occurs, since retention duration scales with allocated capacity relative to the volume of file operations. For a reactive investigation where journal capacity cannot be changed retroactively, acquire the journals as early as possible once manipulation is suspected, and be prepared to rely on indirect/artifact-based detection methods (e.g. $MFT-based rules) as a fallback for events that have already aged out of the journals.

## References

- [DFCite-2031] Oh et al., 2024 — Section VIII explicitly recommends setting both journal files to their maximum size as a proactive forensic-readiness measure to overcome the retention-capacity limitation.
