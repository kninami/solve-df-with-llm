---
id: LWM-2082
type: mitigation
name: Fall back to jailbreaking or a virtualized iOS platform when native ARM-Mac execution fails to install or run a target application
source_refs:
  - LWCite-2095
updated_at: 2026-08-16
status: complete
---

# Fall back to jailbreaking or a virtualized iOS platform when native ARM-Mac execution fails to install or run a target application

## Summary

Before concluding that native ARM-Mac execution of a target iOS application is not viable for a case, attempt the analysis, but treat an install or runtime failure as a signal to fall back to jailbreaking a physical device or using a virtualized iOS platform (e.g. Corellium), rather than as evidence the app is unsuitable for dynamic analysis at all.

## Addresses

- [[weaknesses/Native ARM-Mac execution of iOS applications fails to install or run a substantial proportion of App Store applications]]

## How To Apply

Attempt native ARM-Mac installation and execution first, since it is lower-cost and does not require exploiting a security vulnerability. If the target application refuses to install (commonly due to an iOS-version mismatch) or crashes/hangs on launch, document the specific failure mode and fall back to an alternative dynamic-analysis platform appropriate to the case's resources and time constraints: a jailbroken physical device where a working jailbreak exists for the target iOS version, or a virtualized platform such as Corellium where budget allows and a jailbreak is unavailable. Where none of these options succeed for a given application, document the coverage gap explicitly in the case notes rather than silently omitting the application from analysis.

## References

- [LWCite-2095] Seiden, Webb, and Baggili, 2025, "Tapping .IPAs: An automated analysis of iPhone applications using apple silicon macs", FSI: Digital Investigation 52, 301871.
