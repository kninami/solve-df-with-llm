---
id: LWT-1245
type: technique
name: Interpret exFAT file timestamps using the UTCOffset field and OS-driver fingerprinting
description: Correctly convert an exFAT directory entry's stored Create/LastModified/LastAccessed timestamp to actual UTC by identifying which operating system's exFAT driver wrote it — since Windows, MacOS, and Linux drivers implement the specification's UTCOffset field differently — using root-directory artifacts (e.g. .fseventsd, System Volume Information) and 10ms-increment field patterns as OS fingerprints.
objective_ids:
  - DFO-1002
weakness_ids:
  - LWW-1262
aliases:
  - exFAT UTCOffset timestamp interpretation
source_refs:
  - LWCite-1283
updated_at: 2026-08-14
status: complete
---

# Interpret exFAT file timestamps using the UTCOffset field and OS-driver fingerprinting

## Summary

The exFAT specification defines a per-timestamp `UTCOffset` field (15-minute increments, an offset-from-local-time bit, plus a validity bit) precisely so a stored local timestamp can be converted to actual UTC, but controlled cross-OS/cross-driver testing shows Windows 10, MacOS, and the Linux native and FUSE exFAT drivers each implement this field differently — some correctly, some incorrectly, and some not at all — so converting a timestamp correctly requires first identifying which driver actually wrote it, not just applying the specification as written.

## Details

Windows 10 follows the specification: it stores the local time (including daylight-saving adjustments) and a valid `UTCOffset`, correctly recoverable to true UTC. MacOS also stores a valid offset but with its sign switched relative to the standard convention, and additionally re-derives the Created timestamp's offset from the current local time whenever a file is opened with certain GUI applications (e.g. TextEdit), silently corrupting a previously-correct Created timestamp if the volume's timezone has since changed. The Linux native exFAT driver always stores timestamps as UTC+0 with a valid offset field regardless of the system's actual local timezone (a compliant but information-losing choice, since the true local time used at creation cannot be recovered from the file alone), while the Linux FUSE exFAT driver leaves the `UTCOffset` field entirely unset (invalid), storing only local time with no offset information at all. Because a mixed-use volume (e.g. connected to both a Windows and a MacOS machine over its lifetime) can carry timestamps written under different conventions on the same directory entry, an investigator should first fingerprint which driver(s) touched the volume — MacOS usage is indicated by `.fseventsd`/`.Spotlight-V100` root-directory folders and use of the `Create10msIncrement` field; Windows usage by a `System Volume Information` folder and use of both the `Create10msIncrement` and `LastModified10msIncrement` fields; Linux FUSE-driver usage by uniformly `0x00` (invalid) `UTCOffset` fields — before deciding how to interpret a given timestamp, rather than applying one fixed conversion rule volume-wide.

## Examples

- MacOS stored a file's Created timestamp as `0xF4` (UTC-3, sign-switched) when the true local timezone was UTC+3, and updated the same file's Last Accessed `UTCOffset` on every mount/unmount cycle, even without any file content change — including changing the sign, which could otherwise be mistaken for a genuine timezone change on the source computer.
- The Linux FUSE exFAT driver stored a file's Created and Last Accessed timestamps identically to how it stored Last Modified when a file was appended to with a bash script (all fields left the local time as-written, `UTCOffset` left invalid at `0x00`), giving no way to recover the actual UTC time the file was created without external corroborating evidence.
- Opening a file manually in MacOS's TextEdit application converted its previously-correct Created `UTCOffset` from the file's original local-time-consistent value to the offset implied by the current local time of the Mac being used to open it, silently corrupting the Created timestamp's UTC-offset field even though no content change was made.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/exFAT timestamp interpretation is unreliable across OS drivers and forensic tools due to inconsistent UTCOffset handling]]

## References

- [LWCite-1283] Nordvik and Axelsson, 2022 (corrigendum 2023), "It is about time — Do exFAT implementations handle timestamps correctly?", FSI: Digital Investigation 42-43, 301476.
