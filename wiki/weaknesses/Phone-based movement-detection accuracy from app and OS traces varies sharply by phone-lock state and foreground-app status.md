---
id: LWW-2091
type: weakness
name: Phone-based movement-detection accuracy from app and OS traces varies sharply by phone-lock state and foreground-app status
description: The reliability with which WhatsApp logfile connectivity events and iOS `cache_encryptedC.db` motion-state traces indicate genuine phone movement is not constant, but instead depends heavily on whether the phone was locked or unlocked and whether the relevant app was in the foreground or background at the time, and the underlying mechanisms producing some of these traces are not yet fully understood.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - LWM-2092
source_refs:
  - LWCite-2107
updated_at: 2026-08-16
status: complete
---

# Phone-based movement-detection accuracy from app and OS traces varies sharply by phone-lock state and foreground-app status

## Summary

Because iOS restricts background processing and network access differently depending on whether a device is locked and which app currently holds foreground focus, the frequency, completeness, and timing accuracy of both WhatsApp logfile connectivity events and `cache_encryptedC.db` motion-state transitions vary correspondingly, meaning the same underlying physical movement can produce a richer or sparser trace record purely as a function of the phone's lock/foreground state at the time, independent of the movement itself.

## Why It Matters

An investigator treating the absence of a movement-indicating trace as evidence the phone was stationary risks a false conclusion if the phone was, for instance, locked at the time -- since a locked state can suppress the very trace generation the technique depends on, without necessarily suppressing the movement or the app's ability to communicate. Because not every trace-generation mechanism in this domain is fully reverse-engineered, an investigator also cannot assume a currently-unexplained gap or anomaly in the trace record reflects the ground truth rather than a still-undocumented quirk of iOS's own internal state management.

## Related Mitigations

- [[mitigations/Account for phone lock and foreground-app state when interpreting movement-trace gaps, and corroborate with independent evidence]]

## Used By

- [[techniques/Detect periods of phone movement using WhatsApp logfiles and iOS motion-sensor cache traces]]

## References

- [LWCite-2107] van Zandwijk and Boztas, 2021, "The phone reveals your motion: digital traces of walking, driving and other movements on iPhones", FSI: Digital Investigation 37, 301170.
