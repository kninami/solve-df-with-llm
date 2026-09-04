---
id: LWT-2064
type: technique
name: Detect image LSB steganography using bit-plane cover-image comparison
description: Positively identify and attribute least-significant-bit (LSB) image steganography by locating the suspect image's original, unmodified cover image and visually comparing the two images bit-plane by bit-plane and color channel by color channel, rather than relying solely on statistical steganalysis of the payload image alone.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2064
aliases:
  - CounterSteg-based LSB steganography identification
source_refs:
  - LWCite-2067
updated_at: 2026-08-15
status: complete
---

# Detect image LSB steganography using bit-plane cover-image comparison

## Summary

Given a suspect ("payload") image and a located candidate original ("cover") image of the same pixel dimensions, decompose both images into their individual bit planes (bit 0/LSB through bit 7/MSB) across each color channel (red, green, blue, and alpha) and visually or programmatically diff them. Because most steganographic software concentrates its modifications in the LSB plane, differences confined largely to bit 0 (and sometimes bits 1-2) — while higher bit planes remain identical — constitute a forensic "smoking gun" for LSB steganography that is far more reliable than statistical steganalysis of the payload image in isolation.

## Details

The technique is implemented in the free CounterSteg software, which loads two images and computes a 45-cell grid (5 color/alpha rows x 9 bit-plane columns) of visual difference images plus the percentage of pixels changed per cell, so an examiner can see at a glance which bit planes and color channels were modified and by how much. A genuine steganographic payload is distinguishable from ordinary image processing (contrast, brightness, or gamma adjustment) because standard filters modify pixels broadly across most or all bit planes and colors, whereas steganographic embedding is typically concentrated in the LSB plane (and occasionally one or two bits above it) and, in higher-quality steganography software, deliberately avoids saturated/solid-color regions (e.g., a bright sky) and disperses changes according to per-region noise/variation to evade statistical detection. CounterSteg additionally offers a similar-image search across local and network drives (matching on pixel dimensions and most-significant-bit similarity percentage) specifically to help locate a candidate original cover image when its location is not already known. This complements statistics-only steganalysis approaches and the manipulation-chain-reconstruction technique in [[techniques/Reconstruct an image's manipulation-operator chain using a dual-stream residual network]] by providing a direct, image-pair-based confirmation method rather than a purely statistical or single-image inference.

## Examples

- Comparing a Nikon D90 test photo against copies produced by eight steganographic programs (OpenPuff, Steganography Online, Geocaching Toolbox, OTP-Steg, f5stego.js, DevFarmSteganography, StegoShare, BitCrypt, and OpenStego) classified them into "ugly" (e.g., Steganography Online zeroed the entire LSB plane and embedded data in a visible narrow strip, modifying 100% of that region), "bad" (e.g., OpenPuff modified only the LSB plane but across 12% of all pixels, avoiding saturated regions but still statistically anomalous), and "good"/high-quality (e.g., OpenStego and OTP-Steg compressed the payload to ~1% of pixels, avoided saturated areas, and dispersed changes according to per-channel noise/variation, making them visually and statistically far harder to detect without the cover image).
- With the cover image in hand, even the high-quality software (OpenStego, OTP-Steg) that was designed to defeat statistical steganalysis was made "virtually conclusively" attributable, since the bit-plane comparison directly showed which pixels' LSB values had been altered.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Statistical steganalysis without a located original cover image is unreliable and can be defeated by data-wiping the cover file]]

## References

- [LWCite-2067] Pelosi & Easttom, 2021, "Positive Identification of Least Significant Bit (LSB) Image Steganography Using Cover Image Comparisons", JDFSL 15(6). Source of the CounterSteg bit-plane comparison methodology and its evaluation against eight steganographic programs.
