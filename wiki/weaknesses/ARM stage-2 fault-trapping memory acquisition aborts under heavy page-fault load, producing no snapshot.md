---
id: LWW-1251
type: weakness
name: ARM stage-2 fault-trapping memory acquisition aborts under heavy page-fault load, producing no snapshot
description: When a live ARM system generates page faults faster than the fixed-size auxiliary pages pool can absorb during a coherent memory acquisition, the microvisor-based technique disables the acquisition and must restart later, meaning no snapshot at all is captured for that attempt under heavy system load.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1252
source_refs:
  - LWCite-1266
updated_at: 2026-08-13
status: complete
---

# ARM stage-2 fault-trapping memory acquisition aborts under heavy page-fault load, producing no snapshot

## Summary

The authors state directly that "in cases where there are too many page faults, it is not possible to create a coherent memory image, because the pages pool is overloaded," and that the current implementation's response is to disable the acquisition and start again later, rather than fall back to a degraded or partial capture. Measured in-coherency for a 1000-page pool rose from roughly 0.4% under idle load to approximately 50% under artificially stressed load, showing the pool-overload condition is a realistic risk on an actively used system, not just an edge case.

## Why It Matters

An investigator relying on this technique against a live, actively-used ARM device (rather than one that can be quiesced first) risks a failed acquisition attempt precisely when the system is under the kind of active load most likely to be forensically interesting — for example, during active malware execution the investigator is trying to capture. Because the tool aborts rather than returning a best-effort partial or lower-coherency image, a failed attempt yields no evidence at all rather than a usable-but-imperfect one, and the investigator must recognize the failure and retry, ideally once load conditions improve.

## Related Mitigations

- [[mitigations/Monitor and dynamically resize the ARM stage-2 acquisition page pool, retrying during lower system load]]

## Used By

- [[techniques/Acquire a coherent ARM memory snapshot using stage-2 fault-trapping virtualization]]

## References

- [LWCite-1266] Yehuda, Shlingbaum, Gershfeld, Tayouri, and Zaidenberg, 2021, "Hypervisor memory acquisition for ARM", FSI: Digital Investigation 37, 301106.
