---
id: DFT-2008
type: technique
name: Verify and reconstruct tampered encrypted audio using an embedded fragile watermark
description: The process of using a fragile digital watermark embedded into an encrypted audio signal's quantified signal-energy-ratio feature to verify whether audio downloaded from third-party storage is intact, locate which frames were tampered with, and approximately reconstruct their content from watermark-embedded compressed data.
objective_ids:
  - DFO-1010
weakness_ids:
  - DFW-2008
aliases:
  - Signal Energy Ratio (SER) feature watermarking
  - Tamper location and tamper recovery watermarking
source_refs:
  - DFCite-2008
updated_at: 2026-08-14
status: partial
---

# Verify and reconstruct tampered encrypted audio using an embedded fragile watermark

## Summary

For audio that was proactively protected with this scheme before being uploaded to a third-party storage center, an authorized investigator downloading the encrypted, watermarked audio first verifies its authenticity using the embedded watermark; if intact, the audio is decrypted directly, but if any frame has been tampered with, the investigator uses the watermark to identify which frame(s) were attacked and approximately reconstruct their content from compressed data also embedded in the watermark, before decrypting to recover the original audio's meaning.

## Details

DFCite-2008 first encrypts the audio via scrambling and multiplication with logistic-chaotic-map-generated pseudo-random sequences (keyed by initial values k1/k2/k3), then defines a Signal Energy Ratio (SER) feature comparing the encrypted audio to the same chaotic sequence, and embeds two things into that feature per frame: the frame's sequence number (for tamper-location) and a compressed (sub-sampled) version of that frame's data (for tamper-recovery). At verification time, the investigator reconstructs each frame's number from its watermark; a mismatch between an intact neighboring frame's extracted number and its true position identifies the attacked frame's location. The compressed data embedded elsewhere in the watermark is then used to approximately reconstruct the attacked frame's samples (inserting zero-amplitude samples between recovered values), after which standard decryption recovers audio whose expressed meaning matches the original, subject to the scheme's recovery-capacity limit.

## Examples

- DFCite-2008's deletion/substitution/insertion attack tests on 500 WAVE test signals, correctly locating attacked frames and reconstructing signals rated intelligible (SDG > -1.5, SNR > 15) by a 15-listener panel when fewer than 3/8 of samples were altered.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Fragile-watermark tamper recovery cannot faithfully reconstruct audio beyond roughly 3-8 sample-level tampering]]

## References

- [DFCite-2008] He et al., "A novel digital audio encryption and forensics watermarking scheme", IEEE Access, 2024 — source of the SER-feature watermark embedding, tamper-location, and tamper-recovery methods described above.
