---
id: DFW-1022
type: weakness
name: Android application cache-clear operation purges recoverable streaming video artifacts
description: Android's built-in per-application "Clear cache" function (accessible via a long-press on the app icon or through system Settings, without root access or any special tooling) reliably and effectively removes recoverable streaming-application cache artifacts, including images, metadata, and cached video fragments, acting as a trivial but powerful anti-forensic step available to any user.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1022
source_refs:
  - DFCite-1015
updated_at: 2026-08-09
status: complete
---

# Android application cache-clear operation purges recoverable streaming video artifacts

## Summary

Testing across six Android streaming applications (Twitch, YouTube Live, Instagram Live, Facebook Live, Reddit, Periscope) found that a standard cache-clear operation left recovered cache directories largely empty; in cases where deleted files were still recoverable from filesystem metadata, an `istat` check on a previously-cached (now empty) file showed the deletion timestamp corresponded exactly to the cache-clear event, confirming the operation as the cause of evidence loss rather than routine app behavior.

## Why It Matters

Because this is a standard, documented Android OS feature requiring no special knowledge, tools, or elevated privileges, any user aware of it can trivially and effectively destroy streaming-engagement evidence after the fact, without needing to root the device or install anti-forensic software. This is in contrast to continued normal app usage, which was found to have comparatively little effect on existing cached evidence (new activity mostly adds to, rather than overwrites, the cache) — cache-clearing is disproportionately more destructive than ordinary use.

## Related Mitigations

- [[mitigations/Prioritize early device acquisition before an application cache-clear can occur]]

## Used By

- [[techniques/Recover streaming application cache artifacts]]

## References

- [DFCite-1015] García Murias et al., 2023, "A forensic analysis of streaming platforms on Android OS", FSI: Digital Investigation 44.
