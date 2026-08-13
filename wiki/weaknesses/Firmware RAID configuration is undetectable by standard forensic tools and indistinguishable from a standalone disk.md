---
id: DFW-1166
type: weakness
name: Firmware RAID configuration is undetectable by standard forensic tools and indistinguishable from a standalone disk
description: Firmware (chipset/BIOS-managed) RAID configures storage before OS boot, presents no visible controller card, and gives no OS-level or standard-setup indication that it exists, so widely used forensic tools (EnCase, X-Ways, R-Studio, UFS Explorer) fail to detect it at all, causing an investigator who images and examines one physical disk of an array in isolation to overlook the significant amount of striped or parity-distributed data actually stored across the full array.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1166
source_refs:
  - DFCite-1168
updated_at: 2026-08-12
status: complete
---

# Firmware RAID configuration is undetectable by standard forensic tools and indistinguishable from a standalone disk

## Summary

Comparing hardware, software, and firmware RAID from a digital forensics perspective, firmware RAID scores worst on every dimension relevant to detection: detection feasibility is rated "difficult" (no clear indication), external visibility is rated "indistinguishable from standard setup," and reconstruction difficulty is rated "high" with "no OS trace." Testing five widely used forensic tools against firmware RAID configurations found that EnCase, X-Ways, R-Studio, and UFS Explorer could not detect firmware-level RAID volumes on a live system at all, and only one tool (OSForensics, and only for Intel) could identify a firmware RAID configuration directly from an image file; none of the five could automatically reconstruct a virtual disk without manual parameter entry, and none supported AMD firmware RAID whatsoever.

## Why It Matters

Chipset-level firmware RAID has been accessible on ordinary desktop PCs since Intel's 400-series motherboards in 2020 and AMD's 300-series since 2017, making it now widely deployed on consumer and small-business systems that investigators may not expect to encounter RAID on at all. An investigator who images a single physical disk from a firmware-RAID array without recognizing the configuration will acquire only a fraction of the true data (a striped or parity-distributed portion) and, because the disk appears to standard tools as an ordinary standalone drive, has no built-in prompt to suspect anything is missing — the paper explicitly notes this presents "significant anti-forensic risk" since RAID settings can also be deliberately concealed to hide evidence.

## Related Mitigations

- [[mitigations/Scan for firmware RAID signatures before treating a connected disk as a standalone drive]]

## Used By

- [[techniques/Reconstruct firmware RAID virtual disks from Intel and AMD metadata structures]]

## References

- [DFCite-1168] Yun et al., 2025, "Digital forensic approaches to Intel and AMD firmware RAID systems", FSI: Digital Investigation 54, 301971.
