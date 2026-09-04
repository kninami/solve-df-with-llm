---
id: LWT-1076
type: technique
name: Extract forensic evidence from a drone and its ground control station
description: Perform a full forensic analysis of a small-to-medium commercial drone by systematically extracting and analyzing every component of the unmanned aerial system (UAS) — the drone itself (internal and external memory), its ground control station (GCS, typically a smartphone or tablet), and any removable storage — using industry-standard tools, since attribution and full reconstruction of the drone's use typically require correlating evidence across all components rather than the drone alone.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-1082
aliases:
  - Multi-component drone and ground-control-station forensic extraction framework
source_refs:
  - LWCite-1072
updated_at: 2026-08-10
status: complete
---

# Extract forensic evidence from a drone and its ground control station

## Summary

Prior drone forensic frameworks in the literature were often incomplete: providing controller (GCS) forensic guidance without drone processes, or vice versa, and offering little practical guidance on physical handling or tool reliability. This framework gives investigators a concrete plan of action covering all UAS components, addressing gaps identified in existing frameworks.

## Details

The framework was validated across four drones and four GCS devices (an Apple iPhone and a Samsung smartphone used as controllers, to cover both major smartphone controller operating systems), using industry-standard extraction and analysis tools (Autopsy, Magnet AXIOM, Cellebrite UFED, FTK Imager, iTunes backup extraction). It confirms and extends prior best practices: extracting from the controller whenever possible (since some controllers, e.g. Yuneec Typhoon H, contain an internal file structure accessible without destructive methods like chip-off), using multiple tools rather than relying on one, and maintaining chain of custody and write-blocking wherever compatible hardware exists, while noting that some drones (e.g. certain DJI models) are not detected by physical write blockers and require non-write-blocked extraction methods instead.

## Examples

- Multimedia data was consistently found stored on drones' external memory cards but not their internal memory across all extracted devices, while GCS devices (analyzed via iTunes backup or direct extraction) yielded plist files and application data linking a specific user account to the drone.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Drone-only forensic extraction rarely links the device to a specific controller or suspect without also analyzing the GCS]]

## References

- [LWCite-1072] Thornton and Bagheri Zadeh, 2022, "An investigation into Unmanned Aerial System (UAS) forensics: Data extraction & analysis", FSI: Digital Investigation 41.
