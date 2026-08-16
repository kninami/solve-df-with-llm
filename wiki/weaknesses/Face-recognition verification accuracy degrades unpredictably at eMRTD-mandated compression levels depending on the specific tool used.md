---
id: DFW-2089
type: weakness
name: Face-recognition verification accuracy degrades unpredictably at eMRTD-mandated compression levels depending on the specific tool used
description: Current and incoming electronic identity document regulations push stored facial image sizes down toward 10 KB using JPEG2000 compression, but this compression's effect on face-verification accuracy is not uniform across tools -- an open-source library tested showed considerable accuracy worsening and failed operational thresholds at low compression sizes, while a commercial tool showed only negligible variation -- so accuracy cannot be assumed acceptable for a given deployment without tool-specific testing at the actual compression level in use.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-2090
source_refs:
  - DFCite-2105
updated_at: 2026-08-16
status: complete
---

# Face-recognition verification accuracy degrades unpredictably at eMRTD-mandated compression levels depending on the specific tool used

## Summary

Testing two face-recognition tools (an open-source library, DLib, and a commercial SDK, VeriLook) against the same three datasets and the same range of eMRTD-plausible compressed image sizes (32-10 KB) found sharply divergent results: DLib's error-rate indicators (EER, FRR@FAR0.1%, FRR@FAR0.01%) worsened substantially and consistently as image size decreased, failing the commonly-cited FRR@FAR0.1% ≤ 5% operational requirement on two of three datasets even at the largest tested size, while VeriLook's indicators remained close to their uncompressed-image baseline across the entire tested range, comfortably meeting operational thresholds throughout.

## Why It Matters

An identity-verification or border-control deployment that assumes lossy image compression has a small, roughly-uniform effect on face-verification accuracy -- for instance, because a vendor's marketing materials or a general industry expectation suggests compression's impact is negligible -- risks deploying a tool whose real-world accuracy at the actual compression level in use is far worse than assumed, without ever specifically testing for it. Because current regulations already push toward smaller stored image sizes and are trending further in that direction, and because acquisition-pipeline choices (photo size, scan resolution) determine the effective compression ratio at a given target file size, the actual risk profile varies by deployment in ways that generic guidance cannot capture.

## Related Mitigations

- [[mitigations/Benchmark a face-recognition tool's accuracy at the deployment's actual eMRTD compression level rather than assuming compression impact is negligible]]

## Used By

- [[techniques/Assess face-recognition tool accuracy at a specific eMRTD image compression level before relying on it]]

## References

- [DFCite-2105] Calderoni and Magnani, 2022, "The impact of face image compression in future generation electronic identity documents", FSI: Digital Investigation 40, 301345.
