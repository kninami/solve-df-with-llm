---
id: DFW-1222
type: weakness
name: Standard file system forensic tools cannot associate a stacked file system's lower files with their corresponding upper files
description: Current forensic file-system analysis tools are equipped to parse a lower file system's own file types but have no functionality to recognize that a group of its files together constitute a separate, distinct stacked upper file system, so an examination that stops at the lower file system entirely overlooks the upper file system's names, hierarchy, and content grouping.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1222
source_refs:
  - DFCite-1234
updated_at: 2026-08-13
status: complete
---

# Standard file system forensic tools cannot associate a stacked file system's lower files with their corresponding upper files

## Summary

Tools such as The Sleuth Kit can analyze the wide variety of lower file system types a stacked file system may be built on, but none provide the ability to associate those lower files with an overlying upper file system, so absent manual, implementation-specific reconstruction, an examiner sees only a collection of individually meaningless lower files (arbitrary chunk/GFID-named files, or an unremarkable directory tree) rather than the actual upper files a user interacted with.

## Why It Matters

Given the growing adoption of stacked-file-system architectures in distributed storage and cloud infrastructure, an examiner who is unaware a lower file system they are analyzing is in fact hosting a stacked upper file system risks treating a collection of opaque lower files as low-value or uninterpretable data, missing the actual upper-level files, their names, and their hierarchical organization that constitute the real evidentiary content — and because reconstruction methods differ significantly by implementation (local vs. distributed, managed vs. unmanaged), a generic approach cannot substitute for identification of the specific stacked file system in use.

## Related Mitigations

- [[mitigations/Extend the file-system forensic workflow with a dedicated stacked-file-system correlation phase linking lower files to their upper file system]]

## Used By

- [[techniques/Analyze a stacked file system by correlating its upper and lower file-system layers]]

## References

- [DFCite-1234] Hilgert, Lambertz and Baier, 2024, "Forensic implications of stacked file systems", DFRWS EU 2024; FSI: Digital Investigation 48, 301678.
