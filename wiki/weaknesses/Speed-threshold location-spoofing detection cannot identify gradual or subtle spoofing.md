---
id: LWW-1188
type: weakness
name: Speed-threshold location-spoofing detection cannot identify gradual or subtle spoofing
description: A spoofing-detection method that flags only location points whose implied travel speed between consecutive coordinates exceeds an unreasonable threshold (e.g. faster than commercial air travel) will not detect a falsified location that changes gradually or by a small amount, since such changes never trigger the speed threshold.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1188
source_refs:
  - LWCite-1192
updated_at: 2026-08-13
status: complete
---

# Speed-threshold location-spoofing detection cannot identify gradual or subtle spoofing

## Summary

A commercial GPS-spoofing app can inject falsified location data into a Bluetooth tracker's companion app, and a bad actor can use this to hide a tracker's true location or to feed false location data into other users' devices via the tracker's crowd-sourced finding network. A detection method that calculates the implied speed between consecutive recovered location points and flags only those exceeding a maximum-reasonable-travel-speed threshold (e.g. ~650 mph, the top speed of a commercial airliner) will only catch spoofing that produces an abrupt, physically-impossible jump — not spoofing that moves the reported location slowly or by a small, physically-plausible distance.

## Why It Matters

An investigator relying solely on a speed-threshold flag to distinguish genuine from spoofed location evidence may treat unflagged points as trustworthy when a subtle or slowly-drifting spoof would pass through undetected, potentially supporting an incorrect conclusion about where a tracked object or its carrier actually was. Because the underlying tracker vendor (in the source paper's case, Tile) provided no built-in spoofing detection or mitigation of its own at the time of testing, an investigator has no vendor-side signal to fall back on if this proof-of-concept-level detection method is the only check applied.

## Related Mitigations

- [[mitigations/Combine multiple spoofing-detection signals rather than a single speed threshold]]

## Used By

- [[techniques/Extract Bluetooth tracker companion-app geolocation artifacts from databases and memory]]

## References

- [LWCite-1192] Pace et al., 2023, "Every step you take, I'll be tracking you: Forensic analysis of the tile tracker application", FSI: Digital Investigation 45, 301559.
