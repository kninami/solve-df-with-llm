---
id: DFM-1302
type: mitigation
name: Combine multiple independent similarity signals and lower per-signal thresholds with manual triage for Tor phishing detection
source_refs:
  - DFCite-1334
updated_at: 2026-08-15
status: complete
---

# Combine multiple independent similarity signals and lower per-signal thresholds with manual triage for Tor phishing detection

## Summary

Rather than relying on a single high-confidence similarity threshold that a determined attacker can evade, combine multiple independent similarity signals (text-content similarity, visual/screenshot similarity, and onion-address-prefix similarity) at lower individual thresholds, and route the resulting larger candidate set through human triage rather than fully automated flagging.

## Addresses

- [[weaknesses/Content-similarity Tor phishing detection misses a clone whose attacker deliberately alters enough content to evade the similarity threshold]]

## How To Apply

When applying [[techniques/Detect phishing clone hidden services on the Tor network using content similarity metrics]], compute text-content similarity, rendered-screenshot perceptual-hash similarity, and onion-address-prefix similarity independently rather than relying on any single metric alone, and flag a candidate pair for review if any one signal exceeds a deliberately lower threshold — accepting a higher manual-review workload in exchange for catching clones that evade any one specific metric. Periodically re-crawl and re-compare previously-cleared onion services, since a legitimate service can be cloned at any time after an initial scan, and prioritize manual review of candidates involving services with known phishing history or high-value targets (financial services, whistleblower drop-boxes).

## References

- [DFCite-1334] Steinebach, Zenglein, and Brandl, 2021, "Phishing detection on tor hidden services", FSI: Digital Investigation 36, 301117.
