---
id: DFT-2089
type: technique
name: Reconstruct a device provenance timeline from Apple Health database synchronization records
description: Parse an iPhone's Apple Health SQLite database's `data_provenances` table to build a timeline of every distinct device and firmware version that has ever synced health data into the health record tied to a single Apple ID, letting an investigator attribute specific health data points to the device that generated them, cross-validate a device's claimed usage period, and discover the existence of other devices (e.g. an Apple Watch, or a second iPhone) linked to a suspect's account that may not otherwise be known to the investigation.
objective_ids:
  - DFO-1001
  - DFO-1008
weakness_ids:
  - DFW-2092
aliases:
  - Apple Health data_provenances timeline reconstruction
source_refs:
  - DFCite-2108
updated_at: 2026-08-16
status: complete
---

# Reconstruct a device provenance timeline from Apple Health database synchronization records

## Summary

Apple Health aggregates health and activity data from every device (iPhone, Apple Watch, and third-party integrations) linked to a single Apple ID into one unified health record, and internally tracks which specific device and software version generated each data point via a `data_provenances` table. Because this table records the full history of every device that has ever synced data into the account -- not just the device the record is currently being examined on -- it can reveal devices an investigator did not know to look for, and can establish exactly when a given device was first and last active within the health record.

## Details

The `data_provenances` table stores, for each provenance entry, a device identifier, the originating source application/bundle name, the software (firmware/OS) version at the time of sync, and timestamps establishing when that provenance was created and last updated in the health database. Cross-referencing every distinct provenance entry's associated device identifier against the timestamps of the individual health data records (steps, distance, heart rate, and others) that cite it as their source builds a timeline of which physical devices contributed data to the account and over what date ranges, without needing physical access to those other devices at all -- the health database on any one synced device (or an iCloud/iTunes backup of it) already contains this cross-device provenance history. This supports several distinct investigative uses: confirming that a specific device was in active use (via health data) during a period relevant to a case; discovering the existence of a second device (e.g. a suspect's Apple Watch, or a previously unknown second iPhone) that had not otherwise surfaced during the investigation; and cross-validating a device's claimed acquisition/first-use date against independent metadata such as photo EXIF timestamps.

## Examples

- Reconstructing the provenance timeline of a real iPhone/Apple Watch pair's shared Health record recovered the exact date range each device contributed data, correctly identifying the watch's first-sync date as closely matching its known purchase date.
- Cross-referencing a device's earliest `data_provenances` timestamp against the EXIF creation-date metadata of the earliest photos taken on that same device provided independent corroboration of the device's actual first-use date, useful for verifying or challenging a claimed acquisition or setup date.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Apple Health provenance timestamps for some data types are delayed by up to a year from the underlying activity]]

## References

- [DFCite-2108] "The provenance of Apple Health data: A timeline of update history", FSI: Digital Investigation 48, 2024.
