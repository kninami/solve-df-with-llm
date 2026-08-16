---
id: DFW-2128
type: weakness
name: Non-anchoring events lack any artifact that can directly validate system clock correctness at their precise time
description: An event such as a file creation, whose recoverable artifacts contain only a system-clock timestamp and no corresponding external timestamp, cannot itself be checked for clock correctness, forcing an examiner to rely on weaker bounding evidence from unrelated nearby events.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2129
source_refs:
  - DFCite-2149
updated_at: 2026-08-16
status: complete
---

# Non-anchoring events lack any artifact that can directly validate system clock correctness at their precise time

## Summary

Time-anchor validation depends on an artifact that stores both a system-clock timestamp and a genuinely external timestamp. Many forensically significant event types — file creation being the paper's illustrative example — generate no such paired artifact, so there is no direct evidence available for the exact moment the event's own timestamp was recorded. The best an examiner can do is locate the nearest time anchors before and after the event and treat their agreement or disagreement with the local clock as a probabilistic bound rather than a determination for that specific moment.

## Why It Matters

Even when the nearest surrounding time anchors both indicate the clock was correct, the actual event could still have occurred during an undetected period of clock skew between those two anchors, since nothing directly ties the non-anchoring event's own timestamp to an external reference. Treating "no discrepancy found nearby" as equivalent to "the clock was correct for this specific event" overstates the strength of the conclusion, which matters directly for how confidently a finding about event timing can be presented in court.

## Related Mitigations

- [[mitigations/Search holistically for time anomalies to corroborate non-anchoring event clock correctness]]

## Used By

- [[techniques/Validate system clock correctness at event time using paired local-external timestamp anchors]]

## References

- [DFCite-2149] Vanini et al., 2024, "Was the clock correct? Exploring timestamp interpretation through time anchors for digital forensic event reconstruction", FSI: Digital Investigation 49.
