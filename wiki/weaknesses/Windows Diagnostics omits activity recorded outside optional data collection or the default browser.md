---
id: LWW-1160
type: weakness
name: Windows Diagnostics omits activity recorded outside optional data collection or the default browser
description: Windows Diagnostics records detailed USB, browser, and wireless-network behavioral events only when the "optional diagnostic data" collection setting is enabled (a setting the user can disable at any time, and which is not the top default choice during Windows setup) and only for the built-in Edge browser, so activity performed with a third-party browser (Chrome, Firefox, Tor) or while optional collection is off leaves no trace in this artifact.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1160
source_refs:
  - LWCite-1163
updated_at: 2026-08-12
status: complete
---

# Windows Diagnostics omits activity recorded outside optional data collection or the default browser

## Summary

Windows Diagnostics offers two collection levels: a "required" tier that records only basic device, quality, and app-compatibility information, and an "optional" tier that additionally records connectivity, configuration, usage, and performance data — the behavioral events (USB attach/detach, browser activity, wireless activity) this artifact is useful for depend entirely on the optional tier being active. Separately, only the built-in Edge browser's activity is recorded; browsing performed in Chrome, Firefox, Tor, or another third-party browser produces no corresponding `EventTranscript.db` events at all.

## Why It Matters

An investigator who finds no relevant USB, browsing, or wireless-network activity in `EventTranscript.db` cannot conclude that no such activity occurred: the absence may simply reflect that optional diagnostic data collection was disabled (either from initial setup or changed later) or that the user's activity was performed in a non-default browser. Treating an empty or sparse EventTranscript.db as evidence of an activity's absence, rather than as an artifact-coverage limitation, risks a materially incomplete reconstruction of user behavior.

## Related Mitigations

- [[mitigations/Corroborate Windows Diagnostics telemetry with independent artifacts and verify its collection settings]]

## Used By

- [[techniques/Reconstruct user activity timelines from Windows Diagnostics telemetry logs]]

## References

- [LWCite-1163] Park and Lee, 2022, "DiagAnalyzer: User behavior analysis and visualization using Windows Diagnostics logs", FSI: Digital Investigation 43, 301450.
