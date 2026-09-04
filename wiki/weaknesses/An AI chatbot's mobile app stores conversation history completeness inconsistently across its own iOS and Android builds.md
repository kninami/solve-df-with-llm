---
id: LWW-2110
type: weakness
name: An AI chatbot's mobile app stores conversation history completeness inconsistently across its own iOS and Android builds
description: The same AI chatbot vendor's mobile application can retain drastically different amounts of local conversation content between its iOS and Android builds -- one platform's build may cache full conversation content locally while the other retains essentially none, relying instead on server-side/session state -- so an investigator's expected evidence yield from local extraction depends heavily on which specific platform the target device runs, not only on which app is installed.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2111
source_refs:
  - LWCite-2129
updated_at: 2026-08-16
status: complete
---

# An AI chatbot's mobile app stores conversation history completeness inconsistently across its own iOS and Android builds

## Summary

Examining DeepSeek's mobile apps found the Android build retained essentially no conversation history content in local storage -- the app appears to rely on server-side or in-session state rather than persisting content to disk -- while the iOS build cached full conversation content locally within a `Cache.db` file. Because both builds are nominally "the same app" from the same vendor, an investigator unfamiliar with this platform-specific divergence could reasonably but incorrectly assume both platforms would yield comparable local-extraction results.

## Why It Matters

An investigator who examines an Android device running an AI chatbot app, finds little or no locally cached conversation content, and concludes the app simply does not retain usable evidence risks missing a substantially different, more productive picture that would have applied had the same app been examined on iOS (or vice versa) -- and risks failing to pivot to the platform-appropriate alternative collection method (e.g. network-traffic interception for a platform that stores little locally) in time. This platform-specific divergence is not something a generic "collect from all surfaces" checklist alone reveals; it requires app- and platform-specific validation.

## Related Mitigations

- [[mitigations/Validate an AI chatbot app's local-storage completeness separately per mobile platform before choosing a collection strategy]]

## Used By

- [[techniques/Collect conversational AI artifacts across cloud export, desktop cache, browser cache, and mobile app storage]]

## References

- [LWCite-2129] "Uncovering digital traces of DeepSeek: Cross-platform mobile and network forensics", FSI: Digital Investigation 48, 2024.
