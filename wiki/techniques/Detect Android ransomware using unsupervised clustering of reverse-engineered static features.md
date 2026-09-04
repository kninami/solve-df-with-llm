---
id: LWT-1298
type: technique
name: Detect Android ransomware using unsupervised clustering of reverse-engineered static features
description: Detect both locker- and crypto-type Android ransomware — including previously unseen variants — by reverse-engineering an APK to extract forensically-derived static features (such as app-switching intents, on-screen ransom-note text, text embedded in images, and native-language encoding misuse) and clustering apps with a Gaussian Mixture Model after feature selection and dimensionality reduction, avoiding the reliance on antivirus-vendor-supplied labels that supervised detection methods require.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1308
aliases:
  - RansomDroid
source_refs:
  - LWCite-1345
updated_at: 2026-08-15
status: complete
---

# Detect Android ransomware using unsupervised clustering of reverse-engineered static features

## Summary

Supervised Android ransomware detection depends on antivirus vendors providing accurate, complete labels — but mislabeling is common (one study found only 47% of Android ransomware apps were correctly labeled by most antivirus software), and supervised approaches cannot detect ransomware families absent from their labeled training data. RansomDroid instead uses in-depth reverse engineering and forensic analysis to extract novel static features that prior literature had not captured, then applies unsupervised clustering to group and detect ransomware without depending on historical labels, letting it flag previously unseen (zero-day) ransomware in real time.

## Details

Prior static-feature Android ransomware literature was found to lack several significant feature categories: intents that switch a user from one app to another (used by lockers to keep a ransom-note screen persistently on top), text displayed on the user's screen in the app's native/local language, strings embedded within images (rather than only in code or manifest text), and encoding methods misused by malicious apps to render native-language ransom text. RansomDroid extracts these alongside conventional static features via reverse engineering, then applies feature selection and Principal Component Analysis (PCA) for dimensionality reduction before clustering with a Gaussian Mixture Model (GMM), which offers a flexible, probabilistic approach to modeling the resulting dataset compared to harder clustering boundaries. Because the technique works from static features derived by reverse engineering the APK rather than requiring the sample to be executed, it avoids the sandboxing/execution overhead and environment-fidelity concerns that dynamic-feature-based detection methods face.

## Examples

- The GMM-with-Variance-Threshold-and-PCA configuration achieved 98.08% accuracy and a 98.12% F-score in 44 milliseconds, outperforming other tested unsupervised machine learning techniques for Android ransomware detection.
- Unlike a comparison supervised-learning locker-detection framework that achieved higher accuracy specifically for locker ransomware but could not detect crypto ransomware at all, RansomDroid detects both locker and crypto ransomware types without depending on antivirus-vendor labels, and is applicable to real-time detection scenarios where historical labeled examples of a specific new variant do not yet exist.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/RansomDroid's static-feature extraction is defeated by source-code obfuscation]]

## References

- [LWCite-1345] Sharma, Krishna, and Kumar, 2021, "RansomDroid: Forensic analysis and detection of Android Ransomware using unsupervised machine learning technique", FSI: Digital Investigation 37, 301168.
