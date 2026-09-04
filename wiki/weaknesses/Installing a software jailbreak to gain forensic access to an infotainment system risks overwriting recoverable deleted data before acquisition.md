---
id: LWW-1257
type: weakness
name: Installing a software jailbreak to gain forensic access to an infotainment system risks overwriting recoverable deleted data before acquisition
description: A software-jailbreak-based extraction method necessarily writes jailbreak, daemon, and SSH-mod files to the target infotainment system's own storage before any evidence is acquired, and because the eMMC's TRIM behavior is not fully known, this write activity risks overwriting previously deleted but still-recoverable data before it can be examined.
categories:
  - ASTM_INAC_ALT
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1258
source_refs:
  - LWCite-1275
updated_at: 2026-08-14
status: complete
---

# Installing a software jailbreak to gain forensic access to an infotainment system risks overwriting recoverable deleted data before acquisition

## Summary

Unlike a hardware write-blocked physical extraction, a USB software jailbreak used to access an infotainment system's file system (e.g. a Ford SYNC 3 APIM) must write jailbreak, daemon-installer, and SSH-mod package files to the target's own eMMC storage before any data can be read out, and because it was not possible in the underlying study to also obtain a bit-for-bit physical dump of the eMMC chip for comparison, the extent to which this write activity overwrites previously deleted data (e.g. via the eMMC's built-in TRIM/garbage-collection function) is unknown.

## Why It Matters

A deleted file's allocated space is only marked available, not immediately erased, so it typically remains recoverable until overwritten by new writes — but if the acquisition method itself is the source of new writes to the target medium, the investigator may unknowingly destroy the very deleted content the analysis is meant to discover, and has no way after the fact to distinguish content that was truly absent before the jailbreak from content the jailbreak's own installation overwrote.

## Related Mitigations

- [[mitigations/Obtain a full physical image of an infotainment system's storage chip before installing any jailbreak or extraction software, when hardware access allows]]

## Used By

- [[techniques/Extract and correlate forensic artifacts from a QNX6FS vehicle infotainment hard disk's SQLite databases]]

## References

- [LWCite-1275] Antonson, Quick and Choo, 2025, "Infotainment system Forensics: Ford SYNC 3 gen 2 infotainment system as a use case", FSI: Digital Investigation 53, 301917.
