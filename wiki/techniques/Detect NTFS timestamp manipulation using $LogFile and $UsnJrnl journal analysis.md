---
id: LWT-2031
type: technique
name: Detect NTFS timestamp manipulation using $LogFile and $UsnJrnl journal analysis
description: The process of detecting whether a file's NTFS timestamps ($SI Modified/Accessed/Created/MFT-Entry-Modified and $FN timestamps) have been deliberately manipulated to hide malicious activity from timeline analysis, by directly extracting and cross-checking pre- and post-change timestamp values recorded in the $LogFile and $UsnJrnl NTFS journals, while distinguishing genuine manipulation from benign file-system-tunneling side effects.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2031
aliases:
  - $LogFile-1A / $UsnJrnl-1A detection algorithm
  - NTFS Log Tracker
source_refs:
  - LWCite-2031
updated_at: 2026-08-14
status: partial
---

# Detect NTFS timestamp manipulation using $LogFile and $UsnJrnl journal analysis

## Summary

Timestamp manipulation is one of the most common anti-forensic techniques attackers use to hide malicious files from timeline analysis, second only to file deletion. Prior detection methods based on $MFT metadata alone are largely "indirect" (they detect side effects of manipulation, like broken sequence-number continuity, rather than the manipulation event itself) and prone to both false positives and blind spots. An investigator instead analyzes the NTFS $LogFile and $UsnJrnl transaction journals directly: since these journals record the actual before ("Undo") and after ("Redo") values of every timestamp-changing operation, comparing them reveals genuine timestamp manipulation events directly, including which file was affected and when the manipulation occurred.

## Details

LWCite-2031's $LogFile-1A method scans $LogFile records for the specific redo-operation/record-offset/attribute-offset signature that indicates a $STANDARD_INFORMATION timestamp update, extracts the pre- and post-change $SI-M/A/C/E values from the record's Undo/Redo data, and identifies the target file via its Log Sequence Number or MFT cluster-index cross-reference. Crucially, before flagging a $SI-C change as manipulation, the method checks whether the change pattern matches "file system tunneling" - a legitimate NTFS behavior where a deleted/renamed/moved file's creation time is cached and re-applied to a same-named file created within 15 seconds - which caused false positives in all prior $LogFile-based methods. The complementary $UsnJrnl-1A method identifies a "BASIC_INFO_CHANGE immediately followed by CLOSE" record pattern as its detection signature, then compares the target file's actual creation-event time against its $SI-C in $MFT (rather than only comparing $SI-E to the last BASIC_INFO_CHANGE time, as prior $UsnJrnl methods did), letting it additionally detect $SI-E manipulation performed via the SetFileTime() API or PowerShell, which prior $UsnJrnl-based methods could not detect at all.

## Examples

- LWCite-2031's evaluation against 14 real-world APT malware samples (APT17-APT40, Dark Hotel, Kimsuky, Winnti) that manipulate timestamps to hide dropped files: the proposed NTFS Log Tracker v1.9 detected all 14 samples via both $LogFile and $UsnJrnl analysis and additionally identified same-path-timestamp-copying and $FN manipulation patterns in several samples, while prior $UsnJrnl-based methods (Program C) detected none of the 14 samples, since all used SetFileTime()/PowerShell to manipulate $SI-E.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/NTFS journal-based timestamp manipulation detection is limited by journal retention capacity]]

## References

- [LWCite-2031] Oh et al., "Forensic detection of timestamp manipulation for digital forensic investigation", IEEE Access, 2024 — source of the $LogFile-1A/$UsnJrnl-1A detection algorithms, the file-system-tunneling identification method, and the APT malware evaluation results described above.
