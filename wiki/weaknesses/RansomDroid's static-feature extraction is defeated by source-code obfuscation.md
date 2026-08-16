---
id: DFW-1308
type: weakness
name: RansomDroid's static-feature extraction is defeated by source-code obfuscation
description: Because RansomDroid's detection relies entirely on statically reverse-engineering an APK's source code, decompiled strings, images, and intents to extract its discriminating features, an app whose developer has applied code obfuscation techniques can prevent reliable extraction of those features, and the framework separately does not capture ransom threats delivered via video rather than static images/text.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1310
source_refs:
  - DFCite-1345
updated_at: 2026-08-15
status: complete
---

# RansomDroid's static-feature extraction is defeated by source-code obfuscation

## Summary

The authors explicitly list among the framework's limitations that "the proposed framework may not work well if the attackers applied obfuscation techniques to make the source code unclear," and separately that it "may not work well if the attackers displayed videos on the mobile screens (rather than images and text) to threaten victims into paying the ransom" — both direct consequences of the framework depending entirely on static reverse engineering rather than any run-time/dynamic feature extraction.

## Why It Matters

An investigator relying on RansomDroid-style static-feature detection against an obfuscated or video-ransom-note ransomware sample risks a false negative: the malicious app is not flagged as ransomware because its discriminating static features (extracted strings, images, intents) cannot be reliably recovered or were never present in a static, textual form to begin with. Since ransomware authors have every incentive to adopt obfuscation to evade exactly this kind of static analysis, this is not a hypothetical edge case but an expected evasion strategy that should be assumed present in at least some real-world samples.

## Related Mitigations

- [[mitigations/Supplement static-feature ransomware clustering with dynamic sandbox execution for obfuscated or video-threat samples]]

## Used By

- [[techniques/Detect Android ransomware using unsupervised clustering of reverse-engineered static features]]

## References

- [DFCite-1345] Sharma, Krishna, and Kumar, 2021, "RansomDroid: Forensic analysis and detection of Android Ransomware using unsupervised machine learning technique", FSI: Digital Investigation 37, 301168.
