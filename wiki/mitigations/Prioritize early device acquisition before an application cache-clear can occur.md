---
id: LWM-1022
type: mitigation
name: Prioritize early device acquisition before an application cache-clear can occur
source_refs:
  - LWCite-1015
updated_at: 2026-08-09
status: complete
---

# Prioritize early device acquisition before an application cache-clear can occur

## Summary

Given how trivially and effectively an Android cache-clear destroys streaming-application evidence, prioritize securing and acquiring a relevant mobile device as early as possible once identified, and treat any observed cache-clear timestamp as a potential anti-forensic indicator worth investigating in its own right.

## Addresses

- [[weaknesses/Android application cache-clear operation purges recoverable streaming video artifacts]]

## How To Apply

When a streaming application is identified as forensically relevant, prioritize seizing and imaging the device before the suspect has further opportunity to interact with it, since no special tooling is required for them to purge the evidence. During analysis, note any file-deletion timestamps recovered via filesystem metadata (e.g., `istat`) that align with a plausible cache-clear event, as this timing itself can be evidentially significant (e.g., suggesting the suspect was aware of and reacting to the investigation). Because caching behavior varies significantly by application and even by content type (live vs. replay) within the same application, test the specific application version in question rather than assuming behavior observed for one streaming platform generalizes to another.

## References

- [LWCite-1015] García Murias et al., 2023, "A forensic analysis of streaming platforms on Android OS", FSI: Digital Investigation 44.
