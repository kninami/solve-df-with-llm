---
id: LWW-1256
type: weakness
name: Software-rebooting a virtual machine before acquiring a memory dump contaminates the dump with data remnants from before the reboot
description: Because a KVM guest's address space is typically reused rather than cleared across a software reboot, an examiner who reboots a virtual machine between analysis steps (e.g. to unfreeze it, or between separate malware-sample runs) risks a subsequent memory dump containing substantial data remnants from before the reboot, mixed in with data from the current run.
categories:
  - ASTM_INAC_EX
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-1257
source_refs:
  - LWCite-1274
updated_at: 2026-08-14
status: complete
---

# Software-rebooting a virtual machine before acquiring a memory dump contaminates the dump with data remnants from before the reboot

## Summary

Experiments show that on average around 99% of data written into a KVM guest's RAM before a software reboot remains recoverable in a memory dump taken shortly afterward, so a memory analysis that assumes a rebooted VM's memory reflects only activity since the reboot may in fact be examining a mixture of current and pre-reboot data, with no built-in indicator distinguishing the two.

## Why It Matters

This is particularly consequential in malware analysis and repeated-sample-testing workflows, where an examiner may reboot the same VM between separate analysis runs expecting a clean slate: artifacts (strings, process structures, injected code) from a prior sample's execution can persist into a subsequent run's memory dump and be misattributed to the current sample, or a single dump taken after reboot may contain the residue of multiple prior, unrelated activities without any indication that this occurred. Because the effect gradually fades but does not disappear cleanly, there is no fixed elapsed-time threshold after which contamination can be safely assumed absent.

## Related Mitigations

- [[mitigations/Power off and restart, or revert to a clean snapshot, instead of software-rebooting a VM guest when a contamination-free memory dump is required]]

## Used By

- [[techniques/Recover pre-reboot memory artifacts from a virtual machine's memory after a software reboot]]

## References

- [LWCite-1274] Savchenko, Ottmann and Freiling, 2024, "In the time loop: Data remanence in main memory of virtual machines", FSI: Digital Investigation 49, 301758.
