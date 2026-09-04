---
id: LWT-2087
type: technique
name: Assess face-recognition tool accuracy at a specific eMRTD image compression level before relying on it
description: Before relying on a face-recognition/verification tool to compare a subject's live image against the facial image stored in an electronic identity document's chip (eMRTD), measure that specific tool's verification accuracy (equal error rate, false rejection rate at fixed false-acceptance thresholds) at the actual JPEG2000 compression level and image size the document's issuing authority uses, since accuracy degradation from compression varies substantially by tool.
objective_ids:
  - DFO-1008
  - DFO-1004
weakness_ids:
  - LWW-2089
aliases:
  - eMRTD face image compression impact assessment
source_refs:
  - LWCite-2105
updated_at: 2026-08-16
status: complete
---

# Assess face-recognition tool accuracy at a specific eMRTD image compression level before relying on it

## Summary

Electronic machine-readable travel documents (eMRTDs) store a compressed facial image in their chip's DG2 data group, with current and incoming ICAO/ISO regulations progressively lowering the allowed stored image size (down to as little as 10 KB using JPEG2000) as image acquisition resolution and quality standards rise elsewhere in the enrolment pipeline. Because different face-recognition tools respond very differently to this compression, the actual verification accuracy a border-control or identity-verification deployment can expect depends on validating the specific tool in use at the specific compression level and image size the deployment actually stores, rather than assuming compression's effect on accuracy is negligible or uniform across tools.

## Details

The assessment methodology compresses a dataset of face images to a range of target file sizes reflecting plausible eMRTD storage scenarios (e.g. 32, 16, 14, 12, and 10 KB, corresponding to compression ratios that vary sharply by original image resolution and acquisition scenario), then re-runs face verification (both genuine same-subject comparisons and impostor different-subject comparisons) against the compressed images using the candidate face-recognition tool. Standard biometric performance indicators -- Equal Error Rate (EER), and False Rejection Rate at fixed False Acceptance Rate operating points (FRR@FAR0.1%, FRR@FAR0.01%) -- are computed at each compression level and compared against the same indicators measured on the original, uncompressed images, with the relative degradation (ΔP) explicitly quantified rather than assumed. This directly reveals whether a given tool's accuracy remains within an acceptable operational threshold (e.g. the FRR@FAR0.1% ≤ 5% operational requirement commonly cited for identity verification at Automated Border Control gates) at the compression level actually used in production, and at what compression level (if any) accuracy degrades below that threshold.

## Examples

- Testing an open-source face-recognition library (DLib) against three datasets, EER and FRR both increased steadily and substantially as image size decreased from 32 KB to 10 KB, and DLib's FRR@FAR0.1% failed the 5% operational threshold entirely on two of the three datasets (P&S300, P&S600) even before considering compression, meaning further investigation of compression's effect specifically was only meaningful for the dataset (HQ-FRGC) where DLib met the threshold at all.
- Testing a commercial face-recognition SDK (VeriLook) against the same three datasets and compression levels showed only negligible EER/FRR variation across the entire 32-10 KB range, remaining well within the operational FRR@FAR0.1%/0.01% thresholds throughout -- demonstrating that compression's practical impact on verification accuracy is tool-dependent rather than an inherent property of the compression level itself.
- The magnitude of image-size compression ratios varied enormously by acquisition scenario: a 35x45mm photo scanned at 300ppi compressed to a 10 KB target implies a roughly 66:1 compression ratio, while a 1200x1600px live-capture image compressed to the same 10 KB target implies a roughly 563:1 ratio -- meaning the actual compression severity a deployment experiences depends heavily on its specific acquisition pipeline, not on the target file size alone.

## Related Objectives

- `DFO-1008` Establish identities
- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Face-recognition verification accuracy degrades unpredictably at eMRTD-mandated compression levels depending on the specific tool used]]

## References

- [LWCite-2105] Calderoni and Magnani, 2022, "The impact of face image compression in future generation electronic identity documents", FSI: Digital Investigation 40, 301345.
