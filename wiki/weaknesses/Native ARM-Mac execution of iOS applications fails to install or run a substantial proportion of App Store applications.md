---
id: LWW-2081
type: weakness
name: Native ARM-Mac execution of iOS applications fails to install or run a substantial proportion of App Store applications
description: Running iOS applications natively on an ARM-based Mac requires downgrading to an older macOS version to preserve automatic IPA decryption, which in turn causes the platform to emulate an outdated iOS version; a majority of contemporary App Store applications specify a minimum iOS version newer than what the platform reports, so they refuse to install, and a further share crash or hang on launch for other environment-mismatch reasons.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2082
source_refs:
  - LWCite-2095
updated_at: 2026-08-16
status: complete
---

# Native ARM-Mac execution of iOS applications fails to install or run a substantial proportion of App Store applications

## Summary

Testing against the top 100 free iPhone apps and top 100 free iPhone games from the US App Store, only 92 of 200 (46%) installed and ran successfully under native ARM-Mac execution. The largest failure category, 61 applications (30.5%), was outright install refusal -- primarily because the platform's necessary older macOS version (11.2.3 or earlier, required to preserve automatic IPA decryption) emulates an iOS version (14.4) older than the minimum many contemporary applications require. A further 16% exhibited a runtime exception error, and smaller proportions failed via hangs, missing libraries, segmentation faults, symbol errors, or generic execution errors.

## Why It Matters

An investigator relying on native ARM-Mac execution as their primary or sole method for dynamically analyzing an iOS application cannot assume the method will actually work for a given app before attempting it; more than half of tested contemporary apps failed to run successfully, meaning coverage gaps are the norm rather than the exception for this methodology as currently constrained by the macOS-downgrade requirement. Treating an install or launch failure as evidence the app has "nothing of forensic interest" rather than as a methodology limitation would be a misinterpretation of what the failure actually indicates.

## Related Mitigations

- [[mitigations/Fall back to jailbreaking or a virtualized iOS platform when native ARM-Mac execution fails to install or run a target application]]

## Used By

- [[techniques/Perform dynamic analysis of iOS applications on ARM-based macOS using differential filesystem snapshotting]]

## References

- [LWCite-2095] Seiden, Webb, and Baggili, 2025, "Tapping .IPAs: An automated analysis of iPhone applications using apple silicon macs", FSI: Digital Investigation 52, 301871.
