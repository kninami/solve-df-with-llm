---
id: LWM-1087
type: mitigation
name: Shift to dynamic analysis when static analysis of an obfuscated Android application becomes impractical
source_refs:
  - LWCite-1078
updated_at: 2026-08-10
status: complete
---

# Shift to dynamic analysis when static analysis of an obfuscated Android application becomes impractical

## Summary

When static analysis of an Android application is blocked by encrypted code or heavy junk-code insertion, shift to dynamic analysis (executing the app in an instrumented or monitored environment) rather than continuing to invest effort in static techniques that the obfuscation is specifically designed to defeat.

## Addresses

- [[weaknesses/Static analysis fails against Android applications using encrypted or junk-code-heavy obfuscation]]

## How To Apply

Before committing significant analyst time to static reverse engineering of a suspicious or malicious APK, run available obfuscation-detection tooling to identify whether encryption- or junk-code-based obfuscation is present; where it is, prioritize dynamic analysis (behavioral monitoring, runtime instrumentation, taint tracking) over further static effort, and budget for combined static+dynamic analysis capability given that obfuscation is becoming a default feature of developer tooling rather than an exceptional case.

## References

- [LWCite-1078] Zhang et al., 2021, "Android application forensics: A survey of obfuscation, obfuscation detection and deobfuscation techniques and their impact on investigations", FSI: Digital Investigation 39.
