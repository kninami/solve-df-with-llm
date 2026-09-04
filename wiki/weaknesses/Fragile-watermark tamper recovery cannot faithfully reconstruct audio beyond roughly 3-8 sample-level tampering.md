---
id: LWW-2008
type: weakness
name: Fragile-watermark tamper recovery cannot faithfully reconstruct audio beyond roughly 3-8 sample-level tampering
description: The scheme's tamper-recovery reconstruction quality degrades as more of an audio signal's samples are deleted, substituted, or inserted, and once tampering exceeds roughly three-eighths of the samples, the reconstructed signal no longer reliably conveys the original audio's expressed meaning.
categories:
  - ASTM_INAC_COR
mitigation_ids:
  - LWM-2008
source_refs:
  - LWCite-2008
updated_at: 2026-08-14
status: partial
---

# Fragile-watermark tamper recovery cannot faithfully reconstruct audio beyond roughly 3-8 sample-level tampering

## Summary

The source paper's own tamper-recovery capability analysis (R_c = L_c/L) reports a recovery capacity of about 3/8, with SNR and subjective-difference-grade (SDG) values dropping as the deleted-sample proportion increases; the paper explicitly states that "when a large number of samples are attacked... it is difficult to reconstruct the expression content of the original audio signal." Because tamper recovery relies on a compressed (sub-sampled) copy of each frame embedded elsewhere in the watermark, more extensive tampering removes proportionally more of the recovery data needed to reconstruct it.

## Why It Matters

If an investigator relies on this scheme's reconstructed signal to determine an audio recording's original content after a substantial deletion, substitution, or insertion attack, the reconstruction may no longer accurately reflect the original expression once the attack exceeds the recovery-capacity threshold, risking a mistaken conclusion about what the original audio actually contained.

## Related Mitigations

- [[mitigations/Check reconstructed-audio SNR and SDG against the watermarking scheme's recovery-capacity threshold before relying on tamper recovery]]

## Used By

- [[techniques/Verify and reconstruct tampered encrypted audio using an embedded fragile watermark]]

## References

- [LWCite-2008] He et al., 2024 — Section V.B reports a ~3/8 recovery capacity (R_c) and shows SNR/SDG degrading with increasing deleted-sample proportion in Table 7 and Figures 12-13.
