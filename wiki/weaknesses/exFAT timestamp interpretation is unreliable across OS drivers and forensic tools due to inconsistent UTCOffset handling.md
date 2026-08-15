---
id: DFW-1262
type: weakness
name: exFAT timestamp interpretation is unreliable across OS drivers and forensic tools due to inconsistent UTCOffset handling
description: Four leading digital forensic tools (Autopsy, FTK Imager, X-Ways Forensics, EnCase) each interpret an exFAT volume's UTCOffset-based timestamps differently, and none of them correctly handle every driver-specific storage behavior observed across Windows, MacOS, and Linux, so a tool's displayed timestamp can silently misstate the true UTC time by hours depending on which OS wrote the volume and which tool examined it.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1263
source_refs:
  - DFCite-1283
updated_at: 2026-08-14
status: complete
---

# exFAT timestamp interpretation is unreliable across OS drivers and forensic tools due to inconsistent UTCOffset handling

## Summary

Autopsy assumes the currently-selected timezone in its options tab represents the stored local time and applies an offset transformation on that assumption, producing incorrect results in most tested scenarios; FTK Imager cannot be configured to show anything other than UTC+0 and is therefore only valid for volumes whose UTCOffset fields are actually UTC+0; EnCase assumes an invalid (`0x00`) UTCOffset field means UTC+0, which is incorrect whenever the true stored offset was something else; and X-Ways Forensics interprets timestamps correctly only when every UTCOffset field on a given directory entry is uniformly valid, falling back to unreliable assumptions when fields are mixed valid/invalid.

## Why It Matters

Because none of the four tested tools flags its own interpretation as uncertain — each simply displays a specific date/time value — an investigator using any one tool in isolation has no built-in signal that the displayed timestamp may be off by hours, potentially supporting or undermining an alibi, a sequence-of-events hypothesis, or a cross-device correlation based on an incorrect time. The risk compounds when a volume was used across multiple operating systems (a common scenario for exFAT, given its cross-platform design purpose), since different portions of the same volume's directory entries may follow different, tool-unrecognized storage conventions.

## Related Mitigations

- [[mitigations/Fingerprint the exFAT-writing OS driver and manually verify UTCOffset-based timestamp conversions before relying on a single tool's display]]

## Used By

- [[techniques/Interpret exFAT file timestamps using the UTCOffset field and OS-driver fingerprinting]]

## References

- [DFCite-1283] Nordvik and Axelsson, 2022 (corrigendum 2023), "It is about time — Do exFAT implementations handle timestamps correctly?", FSI: Digital Investigation 42-43, 301476.
