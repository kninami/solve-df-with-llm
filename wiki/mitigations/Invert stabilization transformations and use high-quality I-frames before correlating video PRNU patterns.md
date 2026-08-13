---
id: DFM-1161
type: mitigation
name: Invert stabilization transformations and use high-quality I-frames before correlating video PRNU patterns
source_refs:
  - DFCite-1164
updated_at: 2026-08-12
status: complete
---

# Invert stabilization transformations and use high-quality I-frames before correlating video PRNU patterns

## Summary

Before correlating a query video's PRNU pattern against a candidate camera's reference pattern, restrict frame selection to intra-coded (I-frame) content where possible, and blindly search over candidate geometric transformation parameters (translation, scale, warp) to realign frames if the video shows signs of stabilization, rather than correlating raw stabilized frames directly.

## Addresses

- [[weaknesses/PRNU video source-camera correlation degrades under stabilization and compression]]

## How To Apply

Extract I-frames specifically (e.g. via ffprobe/ffmpeg) for PRNU estimation, since they are the least-compressed frame type and do not depend on other frames for decoding. If visual inspection or metadata indicates the video was stabilized, treat the transformation as unknown and search over plausible geometric realignment parameters before correlating, rather than assuming pixel-grid correspondence. When a below-threshold PCE/NCC score is obtained, report it with an explicit caveat that video-specific degradation (compression, re-encoding, stabilization) can suppress a genuine match, and where possible corroborate with the source platform's least-compressed available copy of the video rather than a re-encoded social media download.

## References

- [DFCite-1164] Akbari et al., 2022, "Digital forensic analysis for source video identification: A survey", FSI: Digital Investigation 41, 301390.
