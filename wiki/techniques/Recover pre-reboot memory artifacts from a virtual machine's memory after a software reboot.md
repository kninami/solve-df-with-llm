---
id: DFT-1240
type: technique
name: Recover pre-reboot memory artifacts from a virtual machine's memory after a software reboot
description: Acquire and analyze a virtual machine's RAM after a guest-initiated software reboot to recover data that was resident in memory before the reboot, exploiting the hypervisor's tendency to reuse the guest's existing address space (and therefore not clear its prior contents) rather than allocating a fresh, zeroed one.
objective_ids:
  - DFO-1006
  - DFO-1019
weakness_ids:
  - DFW-1256
aliases:
  - VM memory remanence across software reboot
source_refs:
  - DFCite-1274
updated_at: 2026-08-14
status: complete
---

# Recover pre-reboot memory artifacts from a virtual machine's memory after a software reboot

## Summary

When a guest operating system inside a virtual machine performs an ordinary software reboot (rather than a full power-off/power-on cycle or a revert to a hypervisor snapshot), experiments with the KVM hypervisor show that on average around 99% of data written into the guest's RAM before the reboot remains recoverable from a memory dump taken afterward, because the hypervisor's underlying guest process is not terminated and its allocated address space is not cleared during the reboot — giving an investigator a way to recover data that existed in a VM's memory before a reboot occurred, including potentially malware or other artifacts from a prior execution.

## Details

The finding is specific to the reboot pathway: powering a VM fully off and back on, or reverting it to a snapshot taken before the data was written, produced no observable remanence at all in the same experimental setup, because both of those paths cause the hypervisor to allocate a new, cleared address space for the guest rather than reusing the old one. Recoverability decreases over time and with further memory activity after the reboot — dropping from over 96% median retrieval within the first hour after reboot to under 20% within roughly 12 hours, and remaining slightly under 20% even after 72 hours, as ordinary system and application memory allocation gradually overwrites the remnant pages. Because the underlying mechanism is a software artifact of how the hypervisor handles guest reboots rather than a hardware capacitor-discharge effect, it is conceptually distinct from (and, unlike) traditional bare-metal RAM data remanence, and its magnitude and presence should not be assumed to carry over to other hypervisors or configurations without separate validation.

## Examples

- Writing 100,000 uniquely timestamped test patterns into a KVM guest's RAM, then software-rebooting the guest and immediately dumping its memory, recovered a median of 97,994 patterns (nearly 98% of what was written) across 125 repeated experimental runs.
- The same experiment repeated with a full power-off/power-on cycle, or with a revert to a snapshot taken before the patterns were written, recovered zero patterns in every run — confirming the remanence effect is specific to the software-reboot pathway.

## Related Objectives

- `DFO-1006` Acquire data
- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Software-rebooting a virtual machine before acquiring a memory dump contaminates the dump with data remnants from before the reboot]]

## References

- [DFCite-1274] Savchenko, Ottmann and Freiling, 2024, "In the time loop: Data remanence in main memory of virtual machines", FSI: Digital Investigation 49, 301758.
