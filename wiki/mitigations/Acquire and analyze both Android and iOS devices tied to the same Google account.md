---
id: LWM-1011
type: mitigation
name: Acquire and analyze both Android and iOS devices tied to the same Google account
source_refs:
  - LWCite-1006
updated_at: 2026-08-09
status: complete
---

# Acquire and analyze both Android and iOS devices tied to the same Google account

## Summary

When a suspect's Google account is accessible through devices on both operating systems, seize and analyze both rather than treating one as sufficient, since each platform retains a materially different subset of artifacts for the same synchronized applications.

## Addresses

- [[weaknesses/Single-platform Google app analysis misses artifacts only present on the other OS]]

## How To Apply

During scene assessment, identify whether the suspect used a Google account on more than one device or OS family, and prioritize acquiring all such devices rather than the first or most convenient one. During analysis, run the artifact extraction process for each shared application independently on the Android and iOS acquisitions, then merge findings; do not assume that an artifact category absent on one platform indicates the activity did not occur, since it may simply be recorded only on the other platform.

## References

- [LWCite-1006] Park et al., 2025, "A comprehensive artifact analysis of Google applications on Android and iOS platforms", FSI: Digital Investigation 55.
