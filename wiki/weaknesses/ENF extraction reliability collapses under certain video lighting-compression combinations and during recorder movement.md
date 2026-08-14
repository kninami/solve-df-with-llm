---
id: DFW-2029
type: weakness
name: ENF extraction reliability collapses under certain video lighting-compression combinations and during recorder movement
description: ENF signal extraction from video degrades sharply or fails outright under specific illumination-source and compression combinations (e.g. compact fluorescent lighting at low bitrates), and ENF extraction from audio loses correlation with the true reference signal when the recording device is physically moved during capture due to Doppler-like and air-pressure effects.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2029
source_refs:
  - DFCite-2029
updated_at: 2026-08-14
status: partial
---

# ENF extraction reliability collapses under certain video lighting-compression combinations and during recorder movement

## Summary

The source survey reports a controlled study finding that "the best ENF estimation was achieved for video captured under LED lighting, while the ENF signal quality declined dramatically under CFL lighting," and that "compressed videos at low bit rates (e.g., 100Kbps) and Facebook uploads noticeably diminished ENF detection performance on video captured under LED while they resulted in a complete failure in ENF detection and time of recording verification for 2 min and 5 min videos captured under CFL." Separately, a controlled audio experiment found that ENF-signal correlation between a moving recorder and a simultaneously captured reference dropped substantially once the recorder was physically moved (by hand) partway through a recording, with the frequency estimate visibly departing from the reference during the motion phase and only recovering once the recorder was stationary again.

## Why It Matters

An investigator relying on ENF-based verification for video evidence captured under fluorescent lighting and/or heavily compressed (e.g. downloaded from a low-bitrate source or social media re-upload) risks a complete inability to perform the analysis at all for short clips, rather than merely reduced accuracy - and for audio, any period during which the recording device was moved (e.g. a body-worn or handheld recorder) may yield an ENF trace uncorrelated with the true reference signal for that segment, risking a false non-match if this is not accounted for.

## Related Mitigations

- [[mitigations/Check illumination source, compression history, and recorder-motion segments before relying on ENF extraction results]]

## Used By

- [[techniques/Verify a recording's time using electric network frequency correlation]]

## References

- [DFCite-2029] Ngharamike et al., 2023 — Section V.B discusses the LED-vs-CFL and compression-bitrate ENF-detection study, and Section VII.D.2 discusses the recorder-movement/Doppler-effect experiment and its impact on ENF trace quality.
