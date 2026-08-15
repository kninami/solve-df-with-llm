---
id: DFM-2029
type: mitigation
name: Check illumination source, compression history, and recorder-motion segments before relying on ENF extraction results
source_refs:
  - DFCite-2029
updated_at: 2026-08-14
status: partial
---

# Check illumination source, compression history, and recorder-motion segments before relying on ENF extraction results

## Summary

Before performing ENF-based analysis on video, first establish the recording's illumination source (LED versus CFL/incandescent) and compression/upload history, and for audio, review the recording for indications of device movement, since each factor can range from moderately degrading to completely defeating ENF extraction.

## Addresses

- [[weaknesses/ENF extraction reliability collapses under certain video lighting-compression combinations and during recorder movement]]

## How To Apply

For video evidence, check metadata or scene content for the likely illumination type and any known re-compression/social-media re-upload history before committing to an ENF-based time-of-recording or tampering analysis; if CFL lighting and low-bitrate compression are both present, treat the clip as a poor ENF candidate, especially if short, and consider an alternative authentication method. For audio, segment the recording and flag periods of likely recorder movement (e.g. via accompanying video, witness statement, or acoustic cues) for separate, lower-confidence treatment rather than analyzing the full recording as a single uniform-confidence ENF trace.

## References

- [DFCite-2029] Ngharamike et al., 2023 — Sections V.B and VII.D.2's documented lighting/compression and recorder-movement experiments provide the basis for pre-screening a recording's ENF suitability before analysis.
