---
id: LWW-1269
type: weakness
name: Non-intrusive VMI system-call tracing cannot reliably capture system call arguments
description: A polling-based non-intrusive system-call tracer can reliably recover which system call was invoked and when, but cannot reliably recover the call's arguments — pointer-type arguments would require slow, translation-heavy dereferencing that defeats the timing requirements of non-intrusive polling, and the Linux kernel overwrites the last three argument registers with unrelated state before the polling thread can safely read them.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1270
source_refs:
  - LWCite-1296
updated_at: 2026-08-14
status: complete
---

# Non-intrusive VMI system-call tracing cannot reliably capture system call arguments

## Summary

Recovering the content behind a pointer-type system call argument (e.g. the buffer written by a `write()` call) requires virtual-to-physical address translation and a further memory read, both too slow to perform within the tight polling window the technique's timing correctness depends on. Separately, current Linux kernels store the last three system-call argument registers only after the `ax` sentinel field has already been set, meaning by the time the polling thread reliably detects a new system-call frame, those specific argument registers may already have been overwritten with unrelated data, regardless of the argument's type.

## Why It Matters

An investigator relying on this technique to determine which system call a process invoked and in what order gets fully accurate results, but cannot use it alone to recover what data those calls actually operated on (e.g. which file path was opened, or what content was written) — information that can be important for malware behavioral analysis beyond a bare call sequence (e.g. distinguishing which specific files were exfiltrated or encrypted). Because the technique's authors position system-call-sequence-based detection models as not requiring arguments, this limitation may not be apparent to an investigator who assumes argument-level detail is captured whenever a trace file is produced.

## Related Mitigations

- [[mitigations/Selectively apply intrusive trap-based tracing only for system calls whose arguments non-intrusive polling cannot capture]]

## Used By

- [[techniques/Reconstruct live Linux system call traces using non-intrusive VMI register polling]]

## References

- [LWCite-1296] Nguyen, Orenbach and Atamli, 2022, "Live system call trace reconstruction on Linux", DFRWS 2022 USA; FSI: Digital Investigation 42, 301398.
