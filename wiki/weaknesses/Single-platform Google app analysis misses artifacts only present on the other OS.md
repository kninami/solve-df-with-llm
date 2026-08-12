---
id: DFW-1011
type: weakness
name: Single-platform Google app analysis misses artifacts only present on the other OS
description: Analyzing a Google application on only one of Android or iOS recovers a systematically smaller and different subset of Google Account Information, Device Information, and User Activity History artifacts than the platform's own acquisition rate suggests, because 34 artifact combinations in a 25-app study were recoverable only through cross-platform analysis.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1011
source_refs:
  - DFCite-1006
updated_at: 2026-08-09
status: complete
---

# Single-platform Google app analysis misses artifacts only present on the other OS

## Summary

Independently, Android-only analysis of 25 Google applications acquired 94 of 175 possible (application x artifact-category) combinations (61%), and iOS-only analysis acquired 101 of 175 (65%). Combining both platforms raised the acquisition rate to 109 of 175 (71%), meaning 34 artifact combinations existed only on whichever platform was not examined and would have been permanently missed by a single-OS investigation.

## Why It Matters

An investigator who examines only the suspect's Android phone (or only their iPhone) for a given Google application may report an incomplete account of the user's activity, incorrectly concluding that a category of evidence (e.g., detailed user activity history, device information, or certain saved content) does not exist, when it is simply not retained on the examined platform. Since the two operating systems retain systematically different artifact categories rather than a strict subset relationship, this is not a matter of one platform being generally "better" for forensics but a genuine completeness gap that depends on which device was examined.

## Related Mitigations

- [[mitigations/Acquire and analyze both Android and iOS devices tied to the same Google account]]

## Used By

- [[techniques/Acquire artifacts across Android and iOS builds of the same application]]

## References

- [DFCite-1006] Park et al., 2025, "A comprehensive artifact analysis of Google applications on Android and iOS platforms", FSI: Digital Investigation 55.
