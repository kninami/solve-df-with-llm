---
id: DFW-1201
type: weakness
name: Hypervisor-based incremental memory acquisition misses paged-out content stored in pagefile.sys
description: A hypervisor-based memory acquisition system that tracks and transfers only physical RAM pages does not capture data the OS has paged out to disk (Windows' pagefile.sys), so content that existed in memory but was swapped to the page file at the moment of acquisition is absent from the resulting timeline unless the page file is separately and additionally acquired.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1201
source_refs:
  - DFCite-1212
updated_at: 2026-08-13
status: complete
---

# Hypervisor-based incremental memory acquisition misses paged-out content stored in pagefile.sys

## Summary

The FIMAR system's authors state directly that their implementation "did not collect pagefile.sys on Windows OS," and that to obtain paged-out content the thin hypervisor would need to separately capture pagefile.sys in addition to the full and incremental physical-RAM snapshots, since the hypervisor's Extended Page Table change-tracking mechanism only observes writes to physical memory pages, not the OS's own paging activity to disk.

## Why It Matters

Content that has been paged out to disk at the moment of a snapshot — which can include process data, cached file content, or even key material — is invisible to a physical-RAM-only acquisition method, creating a gap in the reconstructed temporal timeline that is easy to overlook precisely because the acquisition otherwise appears comprehensive and continuous. An investigator relying on this class of technique for a complete activity reconstruction should treat the resulting timeline as covering physical RAM only, not the full extent of what was ever resident in the system's working set.

## Related Mitigations

- [[mitigations/Acquire pagefile.sys alongside hypervisor-based incremental memory snapshots to recover paged-out content]]

## Used By

- [[techniques/Acquire incremental memory snapshots using hypervisor-based extended-page-table change tracking]]

## References

- [DFCite-1212] Hirano and Kobayashi, 2023, "FIMAR: Fast incremental memory acquisition and restoration system for temporal-dimension forensic analysis", FSI: Digital Investigation 46, 301603.
