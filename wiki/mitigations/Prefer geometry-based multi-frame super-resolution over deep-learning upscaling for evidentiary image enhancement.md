---
id: DFM-1301
type: mitigation
name: Prefer geometry-based multi-frame super-resolution over deep-learning upscaling for evidentiary image enhancement
source_refs:
  - DFCite-1332
updated_at: 2026-08-15
status: complete
---

# Prefer geometry-based multi-frame super-resolution over deep-learning upscaling for evidentiary image enhancement

## Summary

For evidentiary license-plate (or similar) enhancement, prefer explainable, geometry-based multi-frame registration and super-resolution methods over deep-learning-based upscaling, since the former's output is directly and verifiably derived from the actual input frames rather than a learned model's generative inference.

## Addresses

- [[weaknesses/Deep-learning-based super-resolution risks fabricating plausible-looking but inaccurate license-plate detail]]

## How To Apply

When enhancement output may be relied on as evidence, use [[techniques/Reconstruct a legible license plate from surveillance video using perspective-registered multi-frame super-resolution]] or a similarly explainable, non-generative multi-frame registration and reconstruction method, rather than a deep-learning super-resolution model, precisely because its output can be traced directly back to the specific input frames rather than to patterns learned from an unrelated training dataset. Where a deep-learning method is used regardless (for example, for investigative leads rather than court presentation), clearly label the output as AI-enhanced/generative and disclose that fine detail may not be faithfully derived from the source footage, and do not treat character-level detail in such output as confirmed without independent corroboration.

## References

- [DFCite-1332] Guarnieri, Fontani, Guzzi, Carrato, and Jerian, 2021, "Perspective registration and multi-frame super-resolution of license plates in surveillance videos", FSI: Digital Investigation 36, 301087.
