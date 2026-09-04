---
id: LWM-2028
type: mitigation
name: Check for CNN-reconstruction blur artifacts and use adversarially-trained detectors when JPEG anti-forensics is suspected
source_refs:
  - LWCite-2028
updated_at: 2026-08-14
status: partial
---

# Check for CNN-reconstruction blur artifacts and use adversarially-trained detectors when JPEG anti-forensics is suspected

## Summary

Do not rely on a single JPEG/DJPEG compression-history detector's negative result as proof an image is unmanipulated; check for the residual visual-quality signature (slight blurring relative to genuinely uncompressed images) that this class of CNN-based anti-forensic reconstruction still leaves, and where feasible use detectors retrained against known CNN-based anti-forensic examples.

## Addresses

- [[weaknesses/CNN-based end-to-end anti-forensic networks defeat both single- and double-JPEG-compression detectors]]

## How To Apply

Where an image's provenance is contested and JPEG anti-forensic processing is suspected, examine fine detail/sharpness against comparably sourced genuine images, since the source paper's own qualitative comparison notes its anti-forensically reconstructed images are "slightly blurry" relative to true originals - a residual artifact not directly targeted by its DCT-histogram/pixel-domain loss functions. Where a detector can be retrained, include CNN-based anti-forensic examples (as published in this and similar papers) in its adversarial training set rather than relying on a detector trained only against earlier dithering-based or hand-crafted anti-forensic methods.

## References

- [LWCite-2028] Kim et al., 2021 — Section IV.B's qualitative comparison notes the proposed method's reconstructed images appear "slightly blurry...in comparison to other methods" despite achieving high undetectability by the tested statistical detectors.
