---
id: LWW-1077
type: weakness
name: Android's volatile circular log buffers discard older entries and are lost entirely on power loss
description: Android's logging system (and equivalent kernel-space ring buffers in Android-based in-vehicle infotainment systems) stores log messages in fixed-size volatile circular buffers, so newer entries silently overwrite older ones once a buffer fills, and any buffer content not yet copied elsewhere is permanently erased if the device loses power, regardless of what forensic technique is used to analyze it.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1077
source_refs:
  - LWCite-1067
  - LWCite-1088
  - LWCite-1297
updated_at: 2026-08-14
status: complete
---

# Android's volatile circular log buffers discard older entries and are lost entirely on power loss

## Summary

The IVI ring-buffer study found that Jellybean-based systems maintain seven kernel-space ring buffers and KitKat-based systems maintain five, all volatile and erased when the IVI system is powered off — distinct from separately-stored non-volatile log files (retained for up to a year) that survive a power cycle. The OBD-II/Bluetooth study found the same underlying volatility problem on the phone side: "the Bluetooth HCI snoop logging feature needs to be enabled before the investigated events take place, not during the investigation... The Bluetooth packets cannot be captured without enabling the feature," and separately, "the Android logging system keeps multiple circular buffers for log messages and the Android phone used in our experiment has 256 KB circular buffer sizes. Thus, newer log messages may overwrite the oldest ones when the buffer is full... the log messages in the buffers could be lost if turning off the smartphone." A dedicated Android log-message evidence-extraction study confirms this is a general property of the platform's logging system independent of any specific analysis technique: "the logging system consists of small memory buffers, which are overwritten by the latest log messages," meaning even a highly accurate log-message analysis tool "can only identify and extract digital evidence that corresponds to the recent use (e.g., one week) of the Android device," not the device's full history.

## Why It Matters

First responders, tow operators, or investigators who power down a device (or vehicle, or allow its battery to be disconnected) before a forensic acquisition risk permanently losing log-buffer artifacts that existed only in volatile circular buffers, with no way to distinguish after the fact whether that data ever existed versus was simply lost to a power cycle or buffer wraparound. This limitation applies regardless of how sophisticated the log-analysis tool is: even a tool that perfectly identifies and extracts every type of evidentiary data present in the current buffer contents cannot recover data already overwritten before acquisition, so log-based evidence recovery is inherently bounded to a recent time window whose length depends on the buffer size and the device's log-write volume.

## Related Mitigations

- [[mitigations/Prioritize timely acquisition of volatile Android log data before power loss or circular-buffer overwrite]]

## Used By

- [[techniques/Reconstruct automotive events from Android system logs]]
- [[techniques/Extract evidentiary data from Android log messages using string and taint analysis]]

## References

- [LWCite-1067] Kim et al., 2025, "An effective automotive forensic technique utilizing various logs of Android-based In-vehicle infotainment systems", FSI: Digital Investigation 55.
- [LWCite-1088] Jung et al., 2024, "Automotive digital forensics through data and log analysis of vehicle diagnosis Android apps", FSI: Digital Investigation 49.
- [LWCite-1297] Cheng, Shi, Gong and Guan, 2021, "LogExtractor: Extracting digital evidence from android log messages via string and taint analysis", DFRWS 2021 USA; FSI: Digital Investigation 37, 301193. Confirms the buffer-overwrite limitation applies generally to Android's logging system beyond the automotive context, bounding log-based evidence recovery to roughly the device's most recent week of use.
