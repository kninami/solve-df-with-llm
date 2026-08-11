---
id: DFT-1061
type: technique
name: Audio latency and tailing-based smartwatch recording authentication
description: Forensically authenticate an audio file recorded on a smartwatch's built-in voice recorder by measuring device-specific spectral properties (audio latency and tailing at the start/end of the recording, sampling rate/bandwidth), comparing the recording's file structure and metadata atoms against the known-genuine pattern for that device/app, and cross-checking the audio file's internal timestamps against the file system's own timestamps and file-naming convention, to determine whether the file is genuine and, if tampered with, approximately where the tampering occurred.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1066
aliases: []
source_refs:
  - DFCite-1056
updated_at: 2026-08-10
status: complete
---

# Audio latency and tailing-based smartwatch recording authentication

## Summary

Recordings made by a smartwatch's Voice Recorder application exhibit small, consistent artefacts — a fixed audio latency and tailing window at the start and end of the recording, an 8 kHz bandwidth ceiling, and a device/app-specific file structure and timestamp scheme — that differ measurably from a recording made or re-saved by the paired smartphone's own recording app. Comparing a questioned file against this device-specific fingerprint reveals whether it is a genuine, unmodified smartwatch recording, and can localize where editing occurred.

## Details

The method combines three feature classes: (1) spectral analysis to measure audio latency (~0.09 s) and audio tailing (~0.06 s) present in genuine smartwatch recordings, which are lost or altered when a section is trimmed; (2) file-structure analysis, examining container-format atoms (e.g. `moov/trak/tkhd`) to recover the recording start time and last-save time, and checking the file naming convention (`[sequence]_W_[YYMMDD_HHMMSS].m4a` or `Memo_[sequence]_W_[YYMMDD_HHMMSS].m4a`); and (3) timestamp cross-checking between the file name's embedded time, the file's internal atom timestamps, and the device file system's own creation/modification timestamps (accessed via the Smart Development Bridge, SDB, tool on the Tizen-based watch). Genuine files satisfy two criteria: the file system's modification and change times are equal, and the file-name-embedded time is less than or equal to the file structure's internal creation time. Strongest authentication requires access to the source smartwatch itself so file-system-level timestamps can be directly compared; analysis of the audio file alone (without the originating device) provides weaker verification based only on the audio-signal and container-metadata features.

## Examples

- Recordings from five different Galaxy Watch models running Tizen OS were compared against recordings subsequently edited using the default recording app on a paired smartphone; the edited files showed altered audio latency/tailing and file-structure patterns inconsistent with an unmodified smartwatch original.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Audio-file-only smartwatch recording authentication is weaker than authentication backed by the source device]]

## References

- [DFCite-1056] Park et al., 2024, "Advanced forensic method to authenticate audio files from Tizen-based Samsung Galaxy Watches", FSI: Digital Investigation 48.
