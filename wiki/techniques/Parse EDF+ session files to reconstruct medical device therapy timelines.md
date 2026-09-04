---
id: LWT-1168
type: technique
name: Parse EDF+ session files to reconstruct medical device therapy timelines
description: Parse a medical device's European Data Format Plus (EDF+) session files — a header-plus-fixed-duration-data-record structure used by many clinical monitoring devices — using a domain-specific library to recover patient session signals (e.g. therapy pressure, event flags, usage duration) and reconstruct a timeline of device operation and patient treatment.
objective_ids:
  - DFO-1002
weakness_ids:
  - LWW-1174
aliases:
  - CPAP EDF+ file parsing and OSCAR visualization
source_refs:
  - LWCite-1172
updated_at: 2026-08-12
status: complete
---

# Parse EDF+ session files to reconstruct medical device therapy timelines

## Summary

EDF+ is a documented, header-plus-data-record binary format used by CPAP machines and other clinical monitoring devices to store timestamped physiological session data; because standard forensic tools can display such files only as raw text or hex, a format-aware parser is required to convert them into structured signals that can be reviewed and visualized.

## Details

Each EDF+ file's header records patient identification, recording start date/time, signal count, and per-signal metadata (label, physical/digital min/max, sample count), followed by fixed-duration data records containing the actual measurements. Python libraries `pyedflib` (offers richer signal-analysis capabilities) and `edfrd` (a lower-level reader tolerant of non-standard/device-specific field values) can both parse the header and data records into a readable structure; the open-source clinical tool OSCAR (Open Source CPAP Analysis Reporter) can import an entire forensic image (mounted as a removable drive) and produce a full patient-facing dashboard — device identification, daily and aggregate statistics, event-flag graphs, and machine-setting history — originally built for patient self-monitoring but directly reusable for forensic timeline reconstruction. Because EDF+ generation is device- and configuration-dependent, some fields may be missing or inconsistent depending on how the source device was set up, so scripted parsing code written for one device model may require adjustment for another.

## Examples

- OSCAR's daily-overview graphs correlated recorded therapy pressure against event-annotation data (hypopnea, apnea, obstructive apnea, central apnea) to determine whether the machine responded appropriately to a detected breathing event during a specific sleep session.
- Recovering EDF+ files from unallocated space after a device "factory reset" (documented as only performing a quick FAT32 format) via signature search on the format's known header byte sequence recovered both fully and partially intact prior session records.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Deleted FAT32 directory entries on some medical devices overwrite creation and access date fields with non-standard placeholder values]]

## References

- [LWCite-1172] Schmitt and Butterfield, 2024, "Digital forensics in healthcare: An analysis of data associated with a CPAP machine", FSI: Digital Investigation 48, 301661.
