---
id: LWM-1188
type: mitigation
name: Combine multiple spoofing-detection signals rather than a single speed threshold
source_refs:
  - LWCite-1192
updated_at: 2026-08-13
status: complete
---

# Combine multiple spoofing-detection signals rather than a single speed threshold

## Summary

Supplement a single implausible-speed threshold check with additional spoofing indicators — such as unnatural path linearity beyond typical human travel patterns and cross-corroboration against an independent location or activity source — so that gradual or subtle location falsification is not the only class of spoofing a speed-only check can catch.

## Addresses

- [[weaknesses/Speed-threshold location-spoofing detection cannot identify gradual or subtle spoofing]]

## How To Apply

Treat an implausible-speed flag as one signal among several rather than the sole spoofing check. Add a positional-linearity evaluation across a consecutive sequence of location points, comparing observed path shape against a threshold for how straight or artificial a genuine human travel path would plausibly be, since GPS-spoofing tools often move a device along an unnaturally direct or evenly-spaced route. Where available, cross-reference the tracker's reported path against an independent evidence source for the same time window (e.g. cell-site data, a companion device's own native GPS log, or another user's device that encountered the same tracker via its crowd-sourced finding network) to corroborate or contradict the reported locations. Document which spoofing-detection checks were applied and their known blind spots (e.g. gradual drift) in the investigative report, rather than presenting an unflagged location history as verified genuine.

## References

- [LWCite-1192] Pace et al., 2023, "Every step you take, I'll be tracking you: Forensic analysis of the tile tracker application", FSI: Digital Investigation 45, 301559.
