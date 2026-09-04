---
id: LWT-1233
type: technique
name: Acquire a coherent ARM memory snapshot using stage-2 fault-trapping virtualization
description: Acquire a coherent (non-smeared) memory image from a live ARM Linux system by wrapping the operating system in a thin EL2 hypervisor that temporarily marks all guest memory read-only, catches any write via an ARM stage-2 translation fault, copies the faulting page to a pool before releasing it, and only then lets a standard tool (LiME) scan and transmit the frozen contents — without suspending the operating system.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-1251
aliases:
  - Microvised LiME
  - Memory acquisition microvisor for ARM
source_refs:
  - LWCite-1266
updated_at: 2026-08-13
status: complete
---

# Acquire a coherent ARM memory snapshot using stage-2 fault-trapping virtualization

## Summary

A software-only memory-acquisition tool like LiME scans RAM linearly while the operating system keeps running, so a process that starts and exits entirely during the scan can appear duplicated, or not appear at all, in the resulting image — a form of memory in-coherency known as page smearing. Wrapping the guest OS in a thin ARMv8-a EL2 hypervisor and using the ARM stage-2 (Intermediate Physical Address) memory-translation-fault mechanism to intercept and pool writes before they land lets LiME acquire a memory image that reflects a single consistent point in time, without needing to suspend or hibernate the running system.

## Details

Before acquisition, the hypervisor ("microvisor") sets every stage-2 page-table entry to read-only, so any subsequent guest write traps to the hypervisor as a stage-2 fault; the faulting page's pre-write content is copied into an auxiliary pages pool and its permission is restored to read-write, so it can trap and be pooled at most once per acquisition pass. A modified LiME driver then scans memory linearly as before, but checks the pool first: if a page has already been captured there (because it faulted during the scan), the pooled copy is transmitted instead of the current, possibly-already-modified, live page. Two transmission modes are offered: a linear mode that scans and checks every page each cycle (roughly 6% CPU-time overhead versus unmicrovised LiME, since the microvisor's own memory footprint is small — about 2200 lines of code); and a non-linear mode that instead removes and transmits pages directly from the pool as they accumulate, sleeping briefly between cycles when the pool is empty, trading a longer overall acquisition duration for markedly lower processor utilization (as low as 5% at a 50 ms polling interval) and reduced network/disk I/O — making it suitable for acquisition over constrained channels such as a cellular connection on embedded or mobile ARM devices. Because ARMv8-a's hypervisor MMU can only resolve user-space virtual addresses (not kernel-space ones), the implementation instead maps and handles physical addresses directly, using KVM for ARM as the hypervisor platform, and required porting parts of the Volatility memory-analysis framework to support 64-bit ARM Linux kernels.

## Examples

- Repeatedly running `sleep 1` fifty times in succession should produce process-table snapshots showing exactly one instance of the `sleep` process at any acquisition point; non-microvised LiME reported 27 distinct `sleep` instances in one such test (evidence of in-coherency from processes that existed in memory but were no longer in the live process table by the time LiME transmitted that region), while microvised LiME reported a single consistent instance.
- Measuring stage-2 page faults during idle versus artificially-stressed (via the `stress` tool) system load showed average in-coherency for a 1000-page pool of roughly 0.4% in idle mode versus approximately 50% in the most heavily loaded case tested, showing acquisition run during lower system load produces markedly more coherent snapshots.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/ARM stage-2 fault-trapping memory acquisition aborts under heavy page-fault load, producing no snapshot]]

## References

- [LWCite-1266] Yehuda, Shlingbaum, Gershfeld, Tayouri, and Zaidenberg, 2021, "Hypervisor memory acquisition for ARM", FSI: Digital Investigation 37, 301106.
