---
id: LWW-1229
type: weakness
name: Standard IR triage packages omit WMI repository and scheduled-task collection despite both being recoverable non-volatile artifacts
description: Widely used IR triage tools and checklists (Kansa, IR-Rescue, CyLR, NIST SP 800-86) do not include the WMI repository or the scheduled-task directories as default collection targets, so persistence evidence that survives reboot and disk imaging is never acquired even though it is technically recoverable.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1229
source_refs:
  - LWCite-1240
updated_at: 2026-08-13
status: complete
---

# Standard IR triage packages omit WMI repository and scheduled-task collection despite both being recoverable non-volatile artifacts

## Summary

Across 49 confirmed fileless/living-off-the-land intrusions, WMI event-subscription artifacts (`objects.data` in `%SystemRoot%\System32\wbem\Repository\`) were captured in 0.0% of incidents despite WMI persistence appearing in 46.9% of them, and scheduled-task artifacts (`%SystemRoot%\System32\Tasks\` plus the parallel `TaskCache` registry key) were captured in only 2.0% despite 26.5% prevalence. Both artifact classes are non-volatile and survive reboot and standard disk imaging, so the gap is a collection-checklist omission rather than an inherent property of the evidence.

## Why It Matters

WMI `ActiveScriptEventConsumer`/`CommandLineEventConsumer` subscriptions are among the most powerful and least-detected fileless persistence vectors available to an attacker, yet none of the 49 reviewed incident reports referenced WMI-repository forensics at all; NIST SP 800-86's acquisition checklist predates widespread WMI-based persistence and does not list the repository as a collection target, and popular triage packages such as Kansa, IR-Rescue, and CyLR do not include it or the Tasks directory by default. An investigator relying on these standard tools alone will systematically miss persistence mechanisms that are fully recoverable, undermining both incident scoping and any subsequent claim that all persistence vectors were ruled out.

## Related Mitigations

- [[mitigations/Add the WMI repository and scheduled-task directories to standard IR triage collection targets]]

## Used By

- [[techniques/Prioritize fileless malware artifact collection using a technique-to-survival-rate detectability matrix]]

## References

- [LWCite-1240] Paul, 2026, "Forensic visibility gaps in fileless malware incidents: An empirical analysis of artefact survival rates across 49 confirmed intrusions", FSI: Digital Investigation 57, 302112.
