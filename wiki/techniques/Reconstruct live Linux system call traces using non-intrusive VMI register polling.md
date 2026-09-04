---
id: LWT-1256
type: technique
name: Reconstruct live Linux system call traces using non-intrusive VMI register polling
description: Recover a running Linux virtual machine's per-process system call trace, with strace-equivalent accuracy, by continuously polling the physical memory addresses of a traced thread's saved kernel-stack registers via virtual machine introspection and inferring each invoked system call from the register values, rather than pausing the VM or placing execution-halting traps on the syscall handler.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1269
aliases:
  - Non-intrusive VMI system call tracing
source_refs:
  - LWCite-1296
updated_at: 2026-08-14
status: complete
---

# Reconstruct live Linux system call traces using non-intrusive VMI register polling

## Summary

Existing live system-call-tracing methods for malware analysis are either intrusive (placing a trap on the kernel's syscall handler, which forces a costly VM exit/re-entry on every single system call and can slow a traced program by roughly two orders of magnitude — both hurting analyst responsiveness and creating a detectable observer effect malware can exploit) or require an in-guest agent (itself detectable and disableable by sophisticated malware); polling the exact physical memory addresses where the Linux kernel stores a traced thread's registers, at a rate faster than the fastest system call completes, recovers the identical trace as an intrusive tracer with negligible performance overhead and no code running inside the monitored VM.

## Details

In the preparation phase, the tool resolves the traced process's `task_struct` (via the standard Volatility-style Intermediate Symbol Table profile and virtual-to-physical translation) to locate its kernel stack, then computes the exact physical address of the `pt_regs` structure at the base of that stack, where the kernel stores every register at every system call invocation. Rather than tracking any single register's raw value, the technique exploits a specific Linux kernel behavior: the `orig_ax` field's paired `ax` field is set to a sentinel value (`-ENOSYS`) immediately before a system call begins and is overwritten with the syscall's actual return value only once it completes, so continuously polling that single register lets a background thread detect exactly when a new system-call frame begins, at which point the `orig_ax` field (which stores the syscall number) can be read reliably. Because register-store operations are not reordered relative to other stores on x86 (total store ordering), observing the sentinel value in `ax` guarantees `orig_ax` already holds the correct value for the system call about to execute, avoiding a race condition that a naive differential-register-value approach would be vulnerable to (e.g. a tight `read()` loop invoking the identical system call with identical arguments repeatedly, which a value-comparison approach could not detect as a "new" call at all). The polling thread runs on a separate CPU core from the guest, and traced entries are buffered and periodically flushed to a trace file by a background thread to avoid adding write latency to the tracing path itself.

## Examples

- Comparing generated traces against a ground-truth `strace` run for three widely-used Linux utilities (lspci, netstat, ps; 959 to 2,299 system calls each) found the non-intrusive method's trace identical to `strace`'s in both content and order across 10 repeated runs of each program, with the same accuracy achieved by the intrusive trap-based method.
- Tracing three real open-source Linux ransomware samples (RAASNet, Ransom0, Ransomware-PoC) with the non-intrusive method added negligible latency over an untraced baseline, while the intrusive trap-based method slowed the same ransomware's execution by roughly two orders of magnitude (RAASNet and Ransom0) to about 15x (Ransomware-PoC); the recovered traces confirmed the malware's file-scanning-and-overwrite behavior via a dominant sequence of File-category system calls, with two of the three samples additionally showing Network/Time/Synchronization calls clustered near the end of execution corresponding to exfiltrating victim data and encryption keys to a command-and-control server.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Non-intrusive VMI system-call tracing cannot reliably capture system call arguments]]

## References

- [LWCite-1296] Nguyen, Orenbach and Atamli, 2022, "Live system call trace reconstruction on Linux", DFRWS 2022 USA; FSI: Digital Investigation 42, 301398.
