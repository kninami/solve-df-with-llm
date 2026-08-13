---
id: DFT-1228
type: technique
name: Reconstruct floor-ascent and floor-descent events from iPhone Health app altimeter data
description: Determine when and how many floors a suspect's iPhone registered as ascended or descended by extracting timestamped floor-count records from the Health app's databases (barometric altimeter-derived), so that inferred vertical movement can be correlated with a physical scene during event reconstruction.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1246
aliases:
  - Data2activity floor-registration analysis
source_refs:
  - DFCite-1261
updated_at: 2026-08-13
status: complete
---

# Reconstruct floor-ascent and floor-descent events from iPhone Health app altimeter data

## Summary

An iPhone's Health app continuously records a barometric-altimeter-derived count of floors ascended and descended, timestamped and stored in the device's Health databases. Extracting these records lets an investigator infer that a device (and, by extension, its likely carrier) moved vertically at a specific time — for instance, to place a suspect on a particular floor of a building — provided the investigator also understands how the underlying registration actually maps to physical floors.

## Details

The Health app predominantly records floor registrations while walking upstairs and only rarely while walking downstairs, deriving the count from the height difference travelled rather than from a literal count of physical steps or floors: experimentally, a height difference of approximately 3 metres corresponds to the registration of one floor, and across the height differences tested this 3 m-block model matched the number of floors actually registered by the iPhones in 70-80% of cases. Walking speed and phone carrying location (hand, pocket, bag) were found to have only a minor effect on registration accuracy. No floors are registered at all when a subject ascends or descends using an elevator; when using an escalator, floors are registered only while the subject is walking on the escalator, not while standing still on it. These records live alongside other Health app activity data (e.g., step count, walking/running speed — themselves the subject of related iPhone forensic-reconstruction research referred to as "Data2activity") and are recoverable from the device's Health databases using standard mobile forensic extraction and SQLite parsing.

## Examples

- Ascending from ground level to a building's second floor via two intermediate ledges with height differences of roughly 2 m and 3 m registered as only a single floor on the test iPhones, rather than two, because the total height difference — not the number of physical landings — drives the registration.
- Across five different iPhone models tested with seven subjects at varying walking speeds and carrying locations, floor-height differences that were exact multiples of approximately 3 m produced the most reliable floor-count-to-height correspondence.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/iPhone floor-count registrations do not correspond one-to-one with physical floors ascended or descended]]

## References

- [DFCite-1261] van Zandwijk, Lensen, and Boztas, 2023, "Have you been upstairs? On the accuracy of registrations of ascended and descended floors in iPhones", FSI: Digital Investigation 47, 301660.
