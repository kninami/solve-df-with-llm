---
id: DFW-1246
type: weakness
name: iPhone floor-count registrations do not correspond one-to-one with physical floors ascended or descended
description: The Health app's floor-ascent and floor-descent counts are derived from total barometric height difference travelled (approximately 3 metres per registered floor) rather than from the actual number of physical floors or landings crossed, so naively treating a registered floor count as the literal number of physical floors involved can misrepresent what really happened.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1247
source_refs:
  - DFCite-1261
updated_at: 2026-08-13
status: complete
---

# iPhone floor-count registrations do not correspond one-to-one with physical floors ascended or descended

## Summary

Because floor registration is triggered by accumulated height difference rather than by counting discrete physical floors, two physical floors connected by unusually short flights (whose combined height difference is under roughly 3 m) can register as only one floor, while an unusually tall single floor can register as more than one — and no floors are registered at all when a device travels by elevator, or while standing still on an escalator. The recorded count is accurate as a measurement of what the device's altimeter detected, but does not always mean what an investigator might assume it means.

## Why It Matters

An investigator using an iPhone's registered floor count as evidence that a suspect was on a specific physical floor of a building risks a mismatched or overstated conclusion if the building's actual floor-to-floor height differences are not first established — a discrepancy that becomes especially significant when placing someone at a specific level matters to the case (e.g., which floor of a building an incident occurred on). The registration also silently omits movement by elevator, and only partially reflects movement by escalator, which could lead an investigator to wrongly conclude no vertical movement occurred at all during those transitions.

## Related Mitigations

- [[mitigations/Obtain on-site floor-height measurements before interpreting iPhone floor-count registrations]]

## Used By

- [[techniques/Reconstruct floor-ascent and floor-descent events from iPhone Health app altimeter data]]

## References

- [DFCite-1261] van Zandwijk, Lensen, and Boztas, 2023, "Have you been upstairs? On the accuracy of registrations of ascended and descended floors in iPhones", FSI: Digital Investigation 47, 301660.
