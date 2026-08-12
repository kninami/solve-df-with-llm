---
id: DFW-1077
type: weakness
name: Volatile automotive Android log data is lost on power cycle or circular-buffer overwrite
description: Volatile, circular Android log buffers used in automotive forensic reconstruction — kernel-space ring buffers in a vehicle's own Android-based in-vehicle infotainment (IVI) system, and a companion phone's Bluetooth HCI snoop log and main system log buffer when used with an OBD-II scanner — are erased entirely when the device loses power, and are additionally subject to newer entries silently overwriting older ones once the buffer is full; the Bluetooth HCI snoop log specifically must also be manually enabled before the investigated events occur, since it cannot be enabled retroactively.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1077
source_refs:
  - DFCite-1067
  - DFCite-1088
updated_at: 2026-08-10
status: complete
---

# Volatile automotive Android log data is lost on power cycle or circular-buffer overwrite

## Summary

The IVI ring-buffer study found that Jellybean-based systems maintain seven kernel-space ring buffers and KitKat-based systems maintain five, all volatile and erased when the IVI system is powered off — distinct from separately-stored non-volatile log files (retained for up to a year) that survive a power cycle. The OBD-II/Bluetooth study found the same underlying volatility problem on the phone side: "the Bluetooth HCI snoop logging feature needs to be enabled before the investigated events take place, not during the investigation... The Bluetooth packets cannot be captured without enabling the feature," and separately, "the Android logging system keeps multiple circular buffers for log messages and the Android phone used in our experiment has 256 KB circular buffer sizes. Thus, newer log messages may overwrite the oldest ones when the buffer is full... the log messages in the buffers could be lost if turning off the smartphone."

## Why It Matters

First responders, tow operators, or investigators who power down a vehicle (or allow its battery to be disconnected) before a forensic acquisition risk permanently losing IVI interaction artifacts that existed only in volatile ring buffers, with no way to distinguish after the fact whether that data ever existed versus was simply lost to a power cycle. Similarly, if Bluetooth HCI snoop logging was not already enabled on a suspect's phone before the events under investigation, that evidence source is permanently unavailable, and any delay in seizing and imaging an already-logging phone risks the relevant entries being silently overwritten by newer activity or lost entirely if the phone loses power.

## Related Mitigations

- [[mitigations/Prioritize timely acquisition of volatile automotive Android log data before power loss or buffer overwrite]]

## Used By

- [[techniques/Reconstruct automotive events from Android system logs]]

## References

- [DFCite-1067] Kim et al., 2025, "An effective automotive forensic technique utilizing various logs of Android-based In-vehicle infotainment systems", FSI: Digital Investigation 55.
- [DFCite-1088] Jung et al., 2024, "Automotive digital forensics through data and log analysis of vehicle diagnosis Android apps", FSI: Digital Investigation 49.
