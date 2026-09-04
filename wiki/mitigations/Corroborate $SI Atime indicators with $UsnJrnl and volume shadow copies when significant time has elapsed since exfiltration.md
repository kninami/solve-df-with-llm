---
id: LWM-1155
type: mitigation
name: Corroborate $SI Atime indicators with $UsnJrnl and volume shadow copies when significant time has elapsed since exfiltration
source_refs:
  - LWCite-1153
updated_at: 2026-08-12
status: complete
---

# Corroborate $SI Atime indicators with $UsnJrnl and volume shadow copies when significant time has elapsed since exfiltration

## Summary

When examination occurs more than a short time after a suspected Windows PE-based exfiltration event, do not rely on $SI Atime values alone; cross-validate against additional, independently-timestamped artifacts such as $UsnJrnl records and volume shadow copies, and use clustering of multiple partial indicators to narrow down the likely compromise window rather than trusting a single potentially-overwritten timestamp.

## Addresses

- [[weaknesses/NTFS $SI Atime exfiltration indicators become unreliable after continued system use]]

## How To Apply

Classify the examination scenario by elapsed time since the suspected incident (immediate/pre-reboot, first-boot-after-incident, or long-term post-incident) and scale corroboration effort accordingly: for immediate or first-boot analysis, $SI Atime alone may be sufficient given minimal contamination risk; for long-term post-incident analysis, actively pull $UsnJrnl entries and any available volume shadow copies covering the suspected window, and look for clustering patterns across these sources rather than relying on the reliability of any single timestamp. Always pair the Atime evidence with UEFI NVAR boot-order-change analysis where available, since firmware-level boot-sequence-modification traces are comparatively resistant to the same contamination that affects filesystem timestamps.

## References

- [LWCite-1153] Lee, Kim and Jeong, 2026, "Residual forensic indicators of file exfiltration in windows preinstallation environment", FSI: Digital Investigation 56.
