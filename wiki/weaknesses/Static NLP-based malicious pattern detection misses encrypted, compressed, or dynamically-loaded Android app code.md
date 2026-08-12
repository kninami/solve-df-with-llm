---
id: DFW-1089
type: weakness
name: Static NLP-based malicious pattern detection misses encrypted, compressed, or dynamically-loaded Android app code
description: Because the SIMP model performs static analysis on an app's own bytecode, it cannot correctly analyze compressed or encrypted Android Java bytecode, cannot process a dynamically-linked third-party library that is not bundled inside the app itself, and will not detect malicious code that an app only downloads and loads at runtime (dynamic code loading) rather than shipping statically.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1089
source_refs:
  - DFCite-1081
updated_at: 2026-08-10
status: complete
---

# Static NLP-based malicious pattern detection misses encrypted, compressed, or dynamically-loaded Android app code

## Summary

The authors state this directly as a limitation: "our technique requires that the malicious code be available for such (static) analysis. A dynamically linked third party library, which is not included in the app, will not be processed. Compressed or encrypted Android apps (Java bytecodes) will not be correctly analyzed by our technique. If an app requires to download malicious code upon initial execution (i.e., dynamic code loading), such apps will also not be correctly analyzed."

## Why It Matters

A malware author aware of this class of static-analysis-based detector can trivially evade it by encrypting or compressing the app's bytecode, packaging the actual malicious logic in an external dynamically-linked library, or deferring the malicious payload to a post-install download — meaning a "benign" classification from this technique alone provides no assurance against these common evasion strategies, and should not be treated as a definitive clearance.

## Related Mitigations

- [[mitigations/Supplement static NLP-based malware pattern detection with dynamic analysis for encrypted, compressed, or dynamically-loaded Android code]]

## Used By

- [[techniques/Detect Android malware families using similarity scoring]]

## References

- [DFCite-1081] Alam, 2021, "Applying Natural Language Processing for detecting malicious patterns in Android applications", FSI: Digital Investigation 39.
