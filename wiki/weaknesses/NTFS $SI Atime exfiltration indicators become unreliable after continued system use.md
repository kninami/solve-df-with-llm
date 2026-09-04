---
id: LWW-1155
type: weakness
name: NTFS $SI Atime exfiltration indicators become unreliable after continued system use
description: The $STANDARD_INFORMATION Accessed Time evidence used to detect Windows PE-based file exfiltration is progressively overwritten by ordinary subsequent system activity (standard-OS boot processes, background scans, routine file access), so the longer the delay between the exfiltration event and examination, the less reliable the Atime value is as evidence of when the exfiltration actually occurred.
categories:
  - ASTM_MISINT
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1155
source_refs:
  - LWCite-1153
updated_at: 2026-08-12
status: complete
---

# NTFS $SI Atime exfiltration indicators become unreliable after continued system use

## Summary

The study's own three-scenario framework acknowledges that reliability decreases with elapsed time since the incident: analysis performed immediately post-event, pre-reboot yields Atime values reflecting the PE activity with minimal contamination; analysis at the first standard-OS boot may already show some values overwritten by background processes such as antivirus scans; and long-term post-incident analysis (days to weeks later) sees a significantly increased likelihood of Atime contamination, reducing reliability. Repeated legitimate system use after the exfiltration event was empirically shown to progressively diminish the evidentiary value of the original Atime value.

## Why It Matters

An investigator examining a system some time after a suspected Windows PE-based exfiltration event cannot assume an observed $SI Atime value still reflects the original exfiltration-time file access, since ordinary subsequent use of the system (a routine reboot, an antivirus scan, or simple continued file interaction) can silently overwrite it. Treating a stale or already-overwritten Atime value as direct proof of exfiltration timing risks an inaccurate or unsupportable timeline, particularly in cases examined well after the fact rather than immediately following incident detection.

## Related Mitigations

- [[mitigations/Corroborate $SI Atime indicators with $UsnJrnl and volume shadow copies when significant time has elapsed since exfiltration]]

## Used By

- [[techniques/Reconstruct Windows PE file-exfiltration timelines using NTFS $SI Atime and boot-order artifacts]]

## References

- [LWCite-1153] Lee, Kim and Jeong, 2026, "Residual forensic indicators of file exfiltration in windows preinstallation environment", FSI: Digital Investigation 56.
