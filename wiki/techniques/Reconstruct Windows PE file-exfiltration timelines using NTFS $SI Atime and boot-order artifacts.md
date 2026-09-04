---
id: LWT-1152
type: technique
name: Reconstruct Windows PE file-exfiltration timelines using NTFS $SI Atime and boot-order artifacts
description: Detect and reconstruct file-exfiltration events carried out from a bypass boot environment such as the Windows Preinstallation Environment (Windows PE) by combining NTFS $STANDARD_INFORMATION Accessed Time ($SI Atime) updates on exfiltrated files with UEFI NVAR firmware evidence of abnormal boot-order modification, since neither endpoint logging nor security-agent telemetry is active while Windows PE is running.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1155
aliases:
  - Windows PE bypass-boot exfiltration detection via $SI Atime
  - NTFS Atime residual indicator analysis for bypass boot environments
source_refs:
  - LWCite-1153
updated_at: 2026-08-12
status: complete
---

# Reconstruct Windows PE file-exfiltration timelines using NTFS $SI Atime and boot-order artifacts

## Summary

When an attacker changes the UEFI boot order to boot into Windows PE from external media, endpoint security agents, logging services, and removable-media control policies never start, leaving conventional file-access evidence sources (Sysmon, Windows Security Log, DLP telemetry) completely silent. This technique instead relies on residual NTFS metadata — specifically, $SI Atime updates that Windows PE still writes during a file copy/access operation — combined with UEFI NVAR firmware traces of the boot-order change itself, to detect the exfiltration and reconstruct its timeline even though no logs were generated.

## Details

Controlled experiments show $SI Atime is updated on file-copy operations performed under Windows PE in over two-thirds of tested cases, subject to the system's `NtfsDisableLastAccessUpdate` configuration (a registry-controlled setting with both user-managed and volume-size-triggered system-managed modes; a preliminary survey of 9 real Windows systems with boot volumes over 128 GB found Atime updates still enabled on 6 of them). Because Windows PE-based exfiltration generates no logs, the methodology defines three detection scenarios by elapsed time since the incident — immediate/pre-reboot (Atime reflects PE activity with minimal contamination), first-boot-after-incident (some values may be overwritten by background processes such as antivirus scans), and long-term post-incident (Atime contamination likelihood increases significantly) — and pairs the Atime evidence with UEFI NVAR variable analysis of boot-sequence-modification records, which are generated pre-OS-initialization and are not easily manipulated or deleted through ordinary user actions, to independently corroborate that an abnormal PE boot actually occurred. Combining both signal types lets an investigator construct a timeline spanning the preparatory boot-order-change phase and the subsequent file-access/exfiltration phase, rather than relying on a single, easily-contaminated timestamp category.

## Examples

- Controlled Windows 11 file-copy experiments from Windows PE to external storage: $SI Atime updated on file read/copy in the majority of tested cases, with update behavior varying by file type (documents vs. others) and by the system's Atime-update configuration mode.
- Robustness experiment (Experiment 2): repeated legitimate system use after the exfiltration event progressively reduced the evidentiary reliability of the original Atime value, motivating the recommendation to corroborate with additional artifacts once meaningful time has elapsed since the event.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/NTFS $SI Atime exfiltration indicators become unreliable after continued system use]]

## References

- [LWCite-1153] Lee, Kim and Jeong, 2026, "Residual forensic indicators of file exfiltration in windows preinstallation environment", FSI: Digital Investigation 56.
