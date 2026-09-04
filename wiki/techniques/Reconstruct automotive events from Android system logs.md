---
id: LWT-1072
type: technique
name: Reconstruct automotive events from Android system logs
description: Recover vehicle-related events and driver behavior from Android system and application logs in two distinct automotive contexts — the vehicle's own Android-based in-vehicle infotainment (IVI) system's kernel-space ring buffers and non-volatile log files, or an Android phone's OBD-II diagnostic app data cross-referenced with its Bluetooth HCI snoop log and main system log buffer when the phone was used with a Bluetooth OBD-II scanner — reconstructing artifacts and timelines (navigation use, engine start/stop, door access, seat belt use, vehicle velocity, speeding/braking events, refueling) not otherwise supported by mainstream commercial vehicle forensic tools.
objective_ids:
  - DFO-1017
  - DFO-1001
weakness_ids:
  - LWW-1077
aliases:
  - Android system-log-based automotive forensic reconstruction
source_refs:
  - LWCite-1067
  - LWCite-1088
updated_at: 2026-08-10
status: complete
---

# Reconstruct automotive events from Android system logs

## Summary

Both a vehicle's own Android-based infotainment system and a phone used alongside a Bluetooth OBD-II scanner leave forensically rich Android log data documenting vehicle use, but this data source is not supported by at least one popular commercial vehicle forensic tool (Berla's iVe), and the structure of these logging mechanisms was previously not well documented. Systematically acquiring and cross-referencing this log data — either directly from the vehicle's IVI system or indirectly from a companion phone — gives investigators a validated method for reconstructing vehicle-use timelines in accident or criminal investigations.

## Details

**Vehicle-side IVI logs**: applied to five Android-based IVI systems (three Jellybean-based, 2017-2019 model years; two KitKat-based, 2022-2023 model years), all acquired non-invasively. Jellybean-based systems maintain seven kernel-space ring buffers for volatile log data, while KitKat-based systems use five; both versions additionally store seven types of non-volatile log files, with data retained for up to a year. These IVI logging mechanisms differ significantly from those in Android smartphones, particularly in kernel-space ring-buffer structure and behavior.

**Phone-side OBD-II app + Bluetooth + system log correlation**: a phone connected to a vehicle's OBD-II port via a Bluetooth scanner leaves traces in three independently incomplete places — the OBD-II app's own stored records, the phone's Bluetooth HCI snoop log (raw Bluetooth packets exchanged with the scanner), and the Android system's main log buffer. Cross-referencing all three (tested against the Infocar and Torque Pro apps) fills gaps any single source alone would leave and corroborates events across sources — for example, inferring a refueling event (which occurs only while the vehicle, and therefore OBD-II communication, is off) from a gap in Bluetooth communication packets that neither data source logs directly.

## Examples

- Non-volatile IVI log files recovered from a 2022 KIA K5 and 2023 Hyundai Sonata contained artifacts of navigation use, radio listening sessions, engine start/stop events, door access, and seat belt use spanning up to a year of retained history.
- Cross-referencing Bluetooth HCI snoop log gaps against the Infocar app's own data identified a specific refueling window (20:05:08 to 20:09:58) during which the vehicle was turned off, an event not directly logged by either data source alone but inferable from their combination.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system
- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Android's volatile circular log buffers discard older entries and are lost entirely on power loss]]

## References

- [LWCite-1067] Kim et al., 2025, "An effective automotive forensic technique utilizing various logs of Android-based In-vehicle infotainment systems", FSI: Digital Investigation 55.
- [LWCite-1088] Jung et al., 2024, "Automotive digital forensics through data and log analysis of vehicle diagnosis Android apps", FSI: Digital Investigation 49.
