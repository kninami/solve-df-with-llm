---
id: LWM-1310
type: mitigation
name: Supplement static-feature ransomware clustering with dynamic sandbox execution for obfuscated or video-threat samples
source_refs:
  - LWCite-1345
updated_at: 2026-08-15
status: complete
---

# Supplement static-feature ransomware clustering with dynamic sandbox execution for obfuscated or video-threat samples

## Summary

For an Android sample that static-feature clustering does not confidently classify — a plausible sign of obfuscation or a non-textual (video-based) ransom-note delivery mechanism — execute the sample in an isolated sandbox to extract dynamic/run-time behavioral features as a complementary detection signal.

## Addresses

- [[weaknesses/RansomDroid's static-feature extraction is defeated by source-code obfuscation]]

## How To Apply

Treat [[techniques/Detect Android ransomware using unsupervised clustering of reverse-engineered static features]] as one layer of a defense-in-depth detection pipeline rather than a complete solution. For samples where static analysis yields degraded or unclear feature extraction (a signal of possible obfuscation) or that display significant video content rather than static images/text, route the sample to dynamic analysis in an isolated sandbox (such as CuckooDroid) to extract run-time behavioral features — file-system encryption activity, screen-lock/overlay behavior, network communication with command-and-control infrastructure — and combine the dynamic signal with the static-clustering result before making a final detection determination.

## References

- [LWCite-1345] Sharma, Krishna, and Kumar, 2021, "RansomDroid: Forensic analysis and detection of Android Ransomware using unsupervised machine learning technique", FSI: Digital Investigation 37, 301168.
