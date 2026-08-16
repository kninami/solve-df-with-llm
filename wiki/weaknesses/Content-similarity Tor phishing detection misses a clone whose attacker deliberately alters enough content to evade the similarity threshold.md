---
id: DFW-1300
type: weakness
name: Content-similarity Tor phishing detection misses a clone whose attacker deliberately alters enough content to evade the similarity threshold
description: Because content-similarity phishing detection relies on a clone reusing enough of the legitimate site's original text, layout, or visual appearance to exceed a similarity threshold, an attacker who substantially rewrites or restructures the cloned content — beyond simply substituting payment or contact details — can push the similarity score below the detection threshold and evade detection entirely, while a threshold set low enough to catch such clones risks flagging unrelated, legitimately similar services as false positives.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1302
source_refs:
  - DFCite-1334
updated_at: 2026-08-15
status: complete
---

# Content-similarity Tor phishing detection misses a clone whose attacker deliberately alters enough content to evade the similarity threshold

## Summary

Every content-similarity metric available for this task — exact-hash equality, compression-based similarity, and perceptual image-hash similarity — depends on a shared threshold below which two pages are no longer considered a likely clone pair. An attacker aware of this can deliberately rewrite substantial portions of a cloned page's text or restyle its layout while preserving its phishing function, trading some of the "free" credibility a faithful clone provides for evasion of automated detection, and there is an inherent tension between setting the threshold loose enough to catch such altered clones and tight enough to avoid false-positively flagging unrelated services that happen to use similar templates or common web-building frameworks.

## Why It Matters

An investigator relying on content-similarity detection as a complete phishing-clone discovery method risks a false sense of coverage: a negative scan result does not establish that no phishing clone of a given service exists, only that no sufficiently-similar clone was found by the specific metrics and threshold used. Since the underlying anonymity of Tor already makes attacker attribution and takedown difficult, under-detecting deliberately-altered clones compounds an already difficult enforcement problem.

## Related Mitigations

- [[mitigations/Combine multiple independent similarity signals and lower per-signal thresholds with manual triage for Tor phishing detection]]

## Used By

- [[techniques/Detect phishing clone hidden services on the Tor network using content similarity metrics]]

## References

- [DFCite-1334] Steinebach, Zenglein, and Brandl, 2021, "Phishing detection on tor hidden services", FSI: Digital Investigation 36, 301117.
