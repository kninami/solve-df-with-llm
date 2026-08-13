---
id: DFT-1209
type: technique
name: Extract and correlate forensic artifacts from a QNX6FS vehicle infotainment hard disk's SQLite databases
description: Mount a QNX-based in-vehicle infotainment system's hard disk image via a Linux QNX6 kernel module, then parse its known partition layout and per-partition SQLite databases to extract contacts, call logs, text messages, and paired-device identifiers (Bluetooth address, IMEI, IMSI), carving unallocated disk space for additional SQLite database files the system no longer references.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1220
aliases:
  - BMW CIC/NBT EVO infotainment forensic analysis
source_refs:
  - DFCite-1231
updated_at: 2026-08-13
status: complete
---

# Extract and correlate forensic artifacts from a QNX6FS vehicle infotainment hard disk's SQLite databases

## Summary

In-vehicle infotainment (IVI) systems built on the QNX real-time operating system store their forensically relevant data — synced contacts, call logs, SMS messages, and paired smartphone identifiers — as SQLite 3 databases within a documented QNX6FS partition layout, which mainstream forensic suites cannot mount natively but can access via an existing Linux kernel module, after which standard SQLite parsing and unallocated-space carving recover both live and deleted content.

## Details

Because Autopsy and similar tools lack native QNX6FS support, the target partition (identified via `fdisk`/`losetup` from a raw disk image) is mounted read-only using the QNX6 kernel module available in mainstream Linux distributions, exposing its files to any standard file browser or forensic ingest tool. The relevant SQLite databases follow a consistent naming and location convention across generations of the same vendor's system (e.g. `contactbook_<date>.db` for synced contacts, `mme`/`mme_custom` for paired-device sync history including Bluetooth addresses and connected-device names, and `pim01.db`/`pm8*.a` files for personal-information-management and per-device call-history tables), and the tables within them can be joined on shared identifiers (e.g. a `Contact_ID` primary/foreign key, or a `DEVICE_ID` linking a `pim01.db` session record to its corresponding `pm8000XXX.a` call-history database) to build a complete per-device picture. Beyond the files the system's own directory index still references, running a file-carving tool such as PhotoRec against the disk's unallocated space recovers additional deleted SQLite database files (identified by the `SQLite format 3` file-header signature) that the live file system no longer lists — these carved files can then themselves be processed with a dedicated SQLite-deleted-record recovery tool (see [[techniques/Recover deleted SQLite records]]) to expose records the carved copy's own visible tables do not show. Custom forensic-tool ingest modules (e.g. for Autopsy) can automate discovery of the known file paths and database schemas once the partition is mounted.

## Examples

- Mounting a 2017 BMW 5 Series NBT EVO system's `vol2` partition exposed `contactbook_20120928.db`, `pim01.db`, and multiple `pm8*.a` device-specific call-history databases, from which 637 contacts, 658 phone numbers, and 460 call log entries were extracted for that vehicle alone.
- Running PhotoRec against a 2017 BMW 7 Series NBT EVO disk's unallocated space recovered four additional SQLite database files containing a `messages` table of SMS content not present anywhere in the system's actively referenced files, each showing far more records after processing with a deleted-record-recovery tool (e.g. one file's visible 65 messages became 205 after recovery, alongside 824 recovered call records with no corresponding live `calls` table at all).
- Joining the `DEVICE_PROP` table's Bluetooth address to the `CE_DEVICE_INFO` table's IMEI/IMSI fields for the same `DEVICE_ID` allowed a specific call-history database (`pm8000096.a`) to be attributed to a specific paired smartphone even without direct access to that phone.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Standard infotainment forensic analysis limited to allocated files misses deleted SQLite databases recoverable from unallocated space]]

## References

- [DFCite-1231] Marques, Domingues, Frade and Negrão, 2026, "Forensic analysis of the infotainment system of BMW vehicles", FSI: Digital Investigation 56, 302066.
