---
id: DFW-1108
type: weakness
name: Metadata, quantization-table, and compression-statistic authenticity checks fail to detect firmware-reprocessed tampered images
description: Standard image-authenticity checks that examine Exif/metadata consistency, JPEG quantization table compatibility, and DCT compression statistics conclude that a tampered image is a genuine, unaltered native capture whenever the tampered content has been reprocessed through the claimed source camera's own firmware, because the resulting traces are genuinely, not merely simulated, native to that camera.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1108
source_refs:
  - DFCite-1102
updated_at: 2026-08-12
status: complete
---

# Metadata, quantization-table, and compression-statistic authenticity checks fail to detect firmware-reprocessed tampered images

## Summary

In the paper's worked case study, the standard forensic checks (metadata analysis, codec/format analysis, and DCT signal analysis) correctly flagged the original tampered image as suspect on all three markers. After the same image was processed through Camera Obscura, every one of those markers instead read as fully consistent with a native Canon EOS M capture — not because the checks were run incorrectly, but because the underlying traces were, in fact, genuinely produced by that camera's real firmware.

## Why It Matters

An investigator who relies on metadata, quantization-table, or compression-statistic consistency as the basis for concluding an image is an unaltered native capture can be confidently and correctly misled when the image was reprocessed through firmware-level counter-forensics, since these checks by design cannot distinguish "genuinely produced by the native pipeline" from "genuinely re-produced by the native pipeline after tampering" — the same underlying camera hardware and firmware generated both.

## Related Mitigations

- [[mitigations/Cross-validate metadata-consistent images against physical-scene coherence and sensor noise checks]]

## Used By

- [[techniques/Reinject a tampered image into camera firmware to forge native processing traces]]

## References

- [DFCite-1102] Baracchi et al., 2021, "Camera Obscura: Exploiting in-camera processing for image counter forensics", FSI: Digital Investigation 38.
