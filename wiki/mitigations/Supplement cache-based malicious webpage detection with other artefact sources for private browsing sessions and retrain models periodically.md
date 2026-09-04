---
id: LWM-1070
type: mitigation
name: Supplement cache-based malicious webpage detection with other artefact sources for private browsing sessions and retrain models periodically
source_refs:
  - LWCite-1060
updated_at: 2026-08-10
status: complete
---

# Supplement cache-based malicious webpage detection with other artefact sources for private browsing sessions and retrain models periodically

## Summary

When investigating a private/incognito browsing session, do not rely on cache-based malicious webpage detection alone; look to other artefact sources (network logs, DNS records, memory artefacts) for evidence of malicious page visits, and keep the underlying AI model's training data current against newly emerging exploit kits and malicious page types.

## Addresses

- [[weaknesses/Private browsing mode leaves no browser cache for machine-learning-based malicious webpage detection to analyze]]

## How To Apply

Confirm whether the browsing session under investigation used a private/incognito mode before concluding an absence of cache-recovered malicious pages means no malicious activity occurred; where private mode is confirmed or suspected, pursue network-traffic, DNS, or memory-resident artefacts as an alternative evidence source. Separately, periodically retrain or update the detection model on newly collected malicious web page samples to maintain detection coverage against evolving exploit kits.

## References

- [LWCite-1060] Kim et al., 2021, "AIBFT: Artificial Intelligence Browser Forensic Toolkit", FSI: Digital Investigation 36.
