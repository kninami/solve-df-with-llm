---
id: DFW-1260
type: weakness
name: Apple Health workout activity-type labels and country-level time-zone entries do not reliably reflect the actual activity or city location
description: An Apple Health workout's recorded activity type can be triggered by a physically similar but unrelated action (mistaking bell-ringing for rowing), and the database's time-zone field records only a country/region-level zone (e.g. "Europe/Berlin") rather than the specific city visited, so both fields require independent corroboration before being treated as literal fact.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1261
source_refs:
  - DFCite-1279
updated_at: 2026-08-14
status: complete
---

# Apple Health workout activity-type labels and country-level time-zone entries do not reliably reflect the actual activity or city location

## Summary

Apple Watch classifies a workout's activity type from motion sensor patterns, so an unrelated action with a similar physical motion can be misclassified — bell-ringing at churches and cathedrals was recorded as nine separate "Rowing" workouts, discovered only by cross-referencing the workouts' weather-metadata coordinates against known bell-ringing tower locations found through OSINT, and confirmed as bell ringing (not rowing) for seven of the nine via a witness account. Separately, the device's `data_provenances.tz_name` field records only a country/region-level time zone identifier (e.g. Germany's zone is recorded as "Europe/Berlin" regardless of which German city was actually visited), so international travel identified via time-zone transitions can only be localized to the country/region, not the specific city, without a supplementary location source.

## Why It Matters

An investigator who treats a workout's activity-type label at face value risks building an incorrect account of what a person was doing at a given time and place — the difference between "rowing" and "ringing bells at a series of churches" is not a minor detail, and only became apparent because the geolocation coordinates happened to cluster suspiciously around religious buildings rather than a body of water. Likewise, an investigator who treats a time-zone transition as proof of visiting a specific city (e.g. concluding a claimed visit to Frankfurt was false because the database says "Berlin") risks a false credibility challenge, since the database's time-zone granularity cannot distinguish cities within the same country/region by design, not because of any tampering or inaccuracy in the underlying data.

## Related Mitigations

- [[mitigations/Corroborate Apple Health activity-type labels and time-zone-derived location claims with independent witness, OSINT, or image evidence]]

## Used By

- [[techniques/Extract and interpret geolocation and time-zone data from the Apple Health database]]

## References

- [DFCite-1279] Jennings, Sorell and Espinosa, 2023, "Interpreting the location data extracted from the Apple Health database", DFRWS 2023 EU; FSI: Digital Investigation 44, 301504.
