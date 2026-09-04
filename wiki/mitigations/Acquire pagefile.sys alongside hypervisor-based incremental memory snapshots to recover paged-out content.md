---
id: LWM-1201
type: mitigation
name: Acquire pagefile.sys alongside hypervisor-based incremental memory snapshots to recover paged-out content
source_refs:
  - LWCite-1212
updated_at: 2026-08-13
status: complete
---

# Acquire pagefile.sys alongside hypervisor-based incremental memory snapshots to recover paged-out content

## Summary

When using a hypervisor-based incremental memory acquisition system on a Windows target, separately acquire the page file (`pagefile.sys`) alongside the full and incremental physical-RAM snapshots, since paged-out content is invisible to a physical-memory-only acquisition mechanism.

## Addresses

- [[weaknesses/Hypervisor-based incremental memory acquisition misses paged-out content stored in pagefile.sys]]

## How To Apply

Where the acquisition hypervisor supports intercepting storage-device accesses (e.g. via a para-passthrough storage driver) in addition to memory-page access, extend it to also acquire `pagefile.sys` at the same acquisition points as the memory snapshots, so paged-out content can be correlated with the same timeline. Where this capability is not available, treat the resulting memory timeline as a physical-RAM-only reconstruction and note the gap explicitly in reporting, and consider a supplementary, separate acquisition of the page file from disk to check for content relevant to the investigation.

## References

- [LWCite-1212] Hirano and Kobayashi, 2023, "FIMAR: Fast incremental memory acquisition and restoration system for temporal-dimension forensic analysis", FSI: Digital Investigation 46, 301603.
