---
id: LWW-1230
type: weakness
name: Fileless PowerShell and memory-resident execution evidence is unrecoverable without prospective logging or early volatile-memory acquisition
description: PowerShell Script Block Logging and volatile in-memory execution artifacts are only ever recoverable if the relevant control was enabled, or the memory was acquired, before or during the intrusion; standard IR sequencing that begins with network isolation and disk imaging structurally forecloses both.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1230
source_refs:
  - LWCite-1240
updated_at: 2026-08-13
status: complete
---

# Fileless PowerShell and memory-resident execution evidence is unrecoverable without prospective logging or early volatile-memory acquisition

## Summary

Across 49 confirmed fileless/living-off-the-land intrusions, PowerShell execution was documented in 77.6% of incidents while PowerShell Script Block Log evidence (EventID 4104) existed in only 30.6%, and memory forensics was never the primary detection method in any of the 49 incidents despite memory being the execution surface for every fileless payload. Unlike an artifact that merely requires the right collection target, Script Block Logging produces nothing at all if Group Policy did not enable it before the intrusion, and volatile memory pages are commonly overwritten within minutes of process termination on a loaded system.

## Why It Matters

The 30.6% Script Block Log survival rate and the 0.0% memory-forensics-as-primary-detection rate reflect two different but equally structural gaps: a deployment gap (the logging control was never turned on for the victim environment) and a sequencing gap (standard IR procedure — network isolation, then log collection, then disk imaging — never captures volatile memory before it is overwritten or the system is shut down). Neither gap can be closed retroactively once the intrusion is underway; an investigator who only discovers the gap during response has already lost the evidence, unlike the WMI/scheduled-task collection-checklist gap where the artifact is still recoverable if collected.

## Related Mitigations

- [[mitigations/Mandate PowerShell Script Block Logging and move memory acquisition ahead of network isolation]]

## Used By

- [[techniques/Prioritize fileless malware artifact collection using a technique-to-survival-rate detectability matrix]]

## References

- [LWCite-1240] Paul, 2026, "Forensic visibility gaps in fileless malware incidents: An empirical analysis of artefact survival rates across 49 confirmed intrusions", FSI: Digital Investigation 57, 302112.
