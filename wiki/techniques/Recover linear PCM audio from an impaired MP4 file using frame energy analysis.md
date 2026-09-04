---
id: LWT-1175
type: technique
name: Recover linear PCM audio from an impaired MP4 file using frame energy analysis
description: Recover the linear PCM audio signal from an MP4 file whose "moov" atom was never written (e.g., because a dashboard camera's power was abruptly cut during recording), by treating the intact "mdat" atom's bitstream as pseudo audio and using per-frame high-band energy to distinguish true audio frames from video-stream noise.
objective_ids:
  - DFO-1002
weakness_ids:
  - LWW-1182
aliases:
  - Energy-based pseudo-audio recovery
source_refs:
  - LWCite-1185
updated_at: 2026-08-12
status: complete
---

# Recover linear PCM audio from an impaired MP4 file using frame energy analysis

## Summary

A normal MP4 file's "moov" atom provides the decoding metadata needed to separate its audio and video streams, but if a dashboard camera's power is cut mid-recording, only the "ftyp" and "mdat" atoms are written and the moov atom needed to read the interleaved bitstream never gets created. This technique recovers the audio content from such an impaired file by treating the raw mdat bitstream as "pseudo audio" and using frame-based high-band energy to detect which portions actually correspond to the linear PCM audio track rather than to the interleaved video stream.

## Details

The mdat bitstream is read in the two possible byte-alignment offsets implied by the audio format's bytes-per-sample setting (pseudo audio type-1 and type-2, since the true byte alignment relative to the start of mdat is unknown), each converted to the frequency domain via short-time Fourier transform over overlapping frames (frame size 64, hop size 32 in the paper's implementation), and a per-frame high-band energy value is computed for each type. Frames whose averaged high-band energy falls below a threshold (0 dB in the paper) are classified as true audio; audio segments detected from both pseudo-audio types are recombined into the recovered signal, then post-processed with impulse-like noise removal to improve intelligibility. The channel count, sampling rate, and bytes-per-sample parameters needed to interpret the raw PCM bitstream are not present in the impaired file itself and must be obtained in advance from a normally recorded MP4 file produced by the same camera model and settings.

## Examples

- Evaluated on 40 audio clips (20 speech, 20 radio music) recovered from impaired dashcam MP4 files across five iNavi camera models, the proposed method achieved a 0.99 audio recovery ratio and the lowest DTW-based distance to the ground truth (average 3.66 vs. 11.36-40.92 for two conventional recovery tools), and scored approximately 35% higher on a MUSHRA subjective audio-quality test than the conventional methods.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Energy-based PCM audio recovery requires prior knowledge of audio format parameters from an intact reference file]]

## References

- [LWCite-1185] Park et al., 2021, "Energy-based linear PCM audio recovery method of impaired MP4 file stored in dashboard camera memory", FSI: Digital Investigation 39.
