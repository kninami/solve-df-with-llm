---
id: DFM-2024
type: mitigation
name: Apply a complementary JPEG anti-forensic detector when explicit DCT histogram smoothing is suspected
source_refs:
  - DFCite-2024
updated_at: 2026-08-14
status: partial
---

# Apply a complementary JPEG anti-forensic detector when explicit DCT histogram smoothing is suspected

## Summary

Where an image shows other indicators of processing by an explicit-histogram-smoothing anti-forensic tool (unnatural grainy noise in the spatial domain, a smoothed-looking DCT-coefficient histogram, or known-suspect editing software use), do not rely solely on an MTPM-based (or other single) JPEG anti-forensic detector's negative result; corroborate with a second, differently-designed detection method.

## Addresses

- [[weaknesses/MTPM-based JPEG anti-forensic detection is comparatively less accurate against explicit DCT-histogram-smoothing schemes]]

## How To Apply

Combine MTPM-based detection with an independent double-compression/periodicity-based detector (e.g. checking for non-aligned double-JPEG periodicity artifacts) or a spatial-domain grainy-noise check for dithering artifacts, and treat a negative MTPM result on an image otherwise suspected of anti-forensic processing as inconclusive rather than a confirmed absence of JPEG compression evidence.

## References

- [DFCite-2024] Kumar et al., 2021 — Section III.C's evaluation against aligned/non-aligned double-JPEG-compressed images shows the proposed and NA-DJPG detectors have complementary strengths and weaknesses against different anti-forensic schemes, supporting a combined-detector approach.
