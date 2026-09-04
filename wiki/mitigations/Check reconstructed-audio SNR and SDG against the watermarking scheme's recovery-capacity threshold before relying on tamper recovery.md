---
id: LWM-2008
type: mitigation
name: Check reconstructed-audio SNR and SDG against the watermarking scheme's recovery-capacity threshold before relying on tamper recovery
source_refs:
  - LWCite-2008
updated_at: 2026-08-14
status: partial
---

# Check reconstructed-audio SNR and SDG against the watermarking scheme's recovery-capacity threshold before relying on tamper recovery

## Summary

Before treating a fragile-watermark-reconstructed audio segment as representative of the original recording, compute or obtain its SNR and subjective-difference-grade against the known recovery-capacity threshold (approximately 3/8 of samples for this scheme), and flag reconstructions beyond that threshold as unreliable.

## Addresses

- [[weaknesses/Fragile-watermark tamper recovery cannot faithfully reconstruct audio beyond roughly 3-8 sample-level tampering]]

## How To Apply

Report the extent of the detected tampering (proportion of frames/samples affected) alongside any reconstructed audio, and treat reconstructions with SNR below about 15 or SDG below about -1.5 (the paper's own intelligibility thresholds) as evidentially unreliable rather than as a faithful recovery of the original expressed content; where possible, corroborate with an independent copy of the recording.

## References

- [LWCite-2008] He et al., 2024 — the paper's own SNR (>15) and SDG (>-1.5) thresholds for judging the reconstructed signal to convey the same meaning as the original are the basis for this check.
