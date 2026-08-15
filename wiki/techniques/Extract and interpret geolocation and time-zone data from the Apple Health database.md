---
id: DFT-1242
type: technique
name: Extract and interpret geolocation and time-zone data from the Apple Health database
description: Query the Apple Health database (healthdb_secure.sqlite) directly with SQLite joins across its samples, workouts, metadata, and data_provenances tables to recover workout-associated geolocation coordinates and device time-zone transitions, reconstructing a person's local and international movement history even when no other location source is available.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1260
aliases:
  - Apple Health workout geolocation and time-zone reconstruction
source_refs:
  - DFCite-1279
updated_at: 2026-08-14
status: complete
---

# Extract and interpret geolocation and time-zone data from the Apple Health database

## Summary

Apple Watch and iPhone fitness tracking stores two distinct, exploitable location signals inside the Apple Health database beyond its headline step/heart-rate data: a workout's starting geolocation coordinates (recorded, up to and including iOS 15, as the location's *weather* metadata rather than a dedicated location field, with iOS 16 adding a full route table), and the device's time-zone name at the moment of each recorded sample, which can reveal macro-scale international travel even for periods when no workout was logged at all.

## Details

Before iOS 16, coordinate data is reachable only indirectly: each workout's weather-lookup coordinates are stored as `_HKPrivateWorkoutWeatherLocationCoordinatesLongitude`/`Latitude` metadata keys, joined from the `workouts` table through `metadata_values` and `metadata_keys` — a side effect of the weather API call the Health app makes for each workout, not a deliberately recorded location field, but the only coordinate available for that period. From iOS 16 onward, a new `location_series_data` table stores the full workout route directly, though its `series_identifier` field does not align with any index on the `workout`/`samples` tables and must be joined manually rather than through an automated query. Separately, the `data_provenances` table's `tz_name` field records the device's time-zone (e.g. `Australia/Adelaide`) for any sample type, linked through `objects` and `samples`; because a phone or watch's time zone changes only when its owner (and thus the device) physically crosses a time-zone boundary, a sequence of `tz_name` transitions in step-count samples (data_type 7, chosen because virtually every period has step data even without a workout) reconstructs an itinerary of international or interstate travel independent of whether any workout was recorded. A major iOS 16 database restructure changed table names and relationships (e.g. `workout_events`/`workout_statistics` replacing the earlier `workout_activities` structure), so a query written for one iOS version's schema will not work unmodified against the other.

## Examples

- Joining `samples`, `quantity_samples`, `objects`, and `data_provenances` on shared `data_id`/`ROWID` fields extracted a five-year travel itinerary purely from step-count time-zone transitions, identifying two international trips (Australia to the UK, and Australia to Germany via a Dubai layover) even though the workout table alone showed no international activity during those windows.
- Extracting weather-metadata coordinates for nine "Rowing"-labeled workouts and plotting them in Google Maps placed six of the coordinates at or near cathedrals and churches in the person's home city, and the remaining three at churches in the UK and an airport in Norway — accurate enough to place the person at a specific building, but not always precisely on it (one coordinate landed in the middle of a street).

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Apple Health workout activity-type labels and country-level time-zone entries do not reliably reflect the actual activity or city location]]

## References

- [DFCite-1279] Jennings, Sorell and Espinosa, 2023, "Interpreting the location data extracted from the Apple Health database", DFRWS 2023 EU; FSI: Digital Investigation 44, 301504.
