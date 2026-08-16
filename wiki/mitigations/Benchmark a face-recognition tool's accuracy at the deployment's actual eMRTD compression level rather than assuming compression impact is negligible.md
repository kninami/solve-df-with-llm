---
id: DFM-2090
type: mitigation
name: Benchmark a face-recognition tool's accuracy at the deployment's actual eMRTD compression level rather than assuming compression impact is negligible
source_refs:
  - DFCite-2105
updated_at: 2026-08-16
status: complete
---

# Benchmark a face-recognition tool's accuracy at the deployment's actual eMRTD compression level rather than assuming compression impact is negligible

## Summary

Before deploying or relying on a face-recognition tool for eMRTD-based identity verification, benchmark that specific tool's verification accuracy (EER, FRR@FAR0.1%, FRR@FAR0.01%) at the actual compressed image size the deployment's document-issuing process produces, rather than assuming compression's effect on accuracy is small or uniform across tools.

## Addresses

- [[weaknesses/Face-recognition verification accuracy degrades unpredictably at eMRTD-mandated compression levels depending on the specific tool used]]

## How To Apply

Use [[techniques/Assess face-recognition tool accuracy at a specific eMRTD image compression level before relying on it]] to measure the candidate face-recognition tool's error-rate indicators at the actual target compression size (and corresponding compression ratio, which depends on the acquisition pipeline's original photo/scan resolution) the deployment uses, comparing against the operational threshold appropriate to the use case (e.g. FRR@FAR0.1% ≤ 5% for Automated Border Control gates). If the tool fails the threshold at the deployment's actual compression level, either select a different tool empirically shown more robust to compression, or advocate for reserving a larger stored image size within the applicable regulatory range before deploying the system operationally. Re-benchmark whenever the acquisition pipeline's resolution/scanning-quality settings or the applicable compression-size regulation changes, since either change alters the effective compression ratio the tool must handle.

## References

- [DFCite-2105] Calderoni and Magnani, 2022, "The impact of face image compression in future generation electronic identity documents", FSI: Digital Investigation 40, 301345.
