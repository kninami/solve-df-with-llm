---
id: DFM-1257
type: mitigation
name: Power off and restart, or revert to a clean snapshot, instead of software-rebooting a VM guest when a contamination-free memory dump is required
source_refs:
  - DFCite-1274
updated_at: 2026-08-14
status: complete
---

# Power off and restart, or revert to a clean snapshot, instead of software-rebooting a VM guest when a contamination-free memory dump is required

## Summary

When a memory dump must reflect only the current run's activity — for example between separate malware-sample executions in the same VM — fully power off and power on the guest, or revert it to a snapshot taken before the current run began, rather than performing an in-guest software reboot, since only the software-reboot pathway has been shown to leave substantial pre-reboot memory content recoverable.

## Addresses

- [[weaknesses/Software-rebooting a virtual machine before acquiring a memory dump contaminates the dump with data remnants from before the reboot]]

## How To Apply

Before starting a new analysis run in a reused VM guest, either fully power the guest off and back on through the hypervisor (not merely issue an in-guest reboot command) or revert it to a clean pre-run snapshot, both of which have been experimentally shown to leave no recoverable remnants of prior memory content. Where a software reboot cannot be avoided (e.g. because it is itself part of the scenario being studied), acquire a memory dump immediately before the reboot to separately capture the pre-reboot state, and treat any post-reboot dump as potentially contaminated rather than as reflecting only post-reboot activity, documenting the reboot method used in the case notes.

## References

- [DFCite-1274] Savchenko, Ottmann and Freiling, 2024, "In the time loop: Data remanence in main memory of virtual machines", FSI: Digital Investigation 49, 301758.
