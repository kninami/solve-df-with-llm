---
id: DFW-1167
type: weakness
name: Guessed stripe size or disk order silently produces a misaligned firmware RAID reconstruction
description: When a firmware RAID virtual disk is deleted, Intel's implementation overwrites its metadata entirely, so reconstructing the deleted volume requires the investigator to infer critical parameters — especially stripe size, which is never explicitly recorded and must be guessed from a small set of common values — and an incorrect guess produces a reconstructed virtual disk that is silently misaligned rather than failing visibly.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - DFM-1167
source_refs:
  - DFCite-1168
updated_at: 2026-08-12
status: complete
---

# Guessed stripe size or disk order silently produces a misaligned firmware RAID reconstruction

## Summary

Unlike AMD RAID, which appends a new metadata version rather than overwriting on deletion (retaining a full modification history that makes deleted-volume recovery deterministic via an index-based selection of a prior version), Intel RAID overwrites and erases the metadata of a deleted virtual disk, leaving no explicit record of its stripe size, exact start/end offsets, or (unless a boot record happens to be present) disk order. Recovering a deleted Intel virtual disk therefore requires an investigator to iteratively test candidate values — trying common stripe sizes (e.g. 16, 32, 64, 128 KB) and inferring disk order from parity/XOR consistency checks or boot-record position — rather than reading these parameters directly from metadata.

## Why It Matters

The paper's own evaluation explicitly cautions that "the accuracy of recovered volumes may vary if incorrect parameters — such as stripe size or disk order — are supplied," and that "improper disk ordering may lead to misaligned data reconstruction." A misaligned reconstruction does not necessarily fail to mount or produce an obvious error; it can instead yield a virtual disk whose file system structures partially parse while its file contents are corrupted or shifted, risking an investigator unknowingly working from — and reporting on — data that does not accurately represent the original evidence.

## Related Mitigations

- [[mitigations/Validate a reconstructed firmware RAID virtual disk before treating recovered data as reliable]]

## Used By

- [[techniques/Reconstruct firmware RAID virtual disks from Intel and AMD metadata structures]]

## References

- [DFCite-1168] Yun et al., 2025, "Digital forensic approaches to Intel and AMD firmware RAID systems", FSI: Digital Investigation 54, 301971.
