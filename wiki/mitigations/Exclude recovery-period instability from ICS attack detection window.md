---
id: LWM-1001
type: mitigation
name: Exclude recovery-period instability from ICS attack detection window
source_refs:
  - LWCite-1001
updated_at: 2026-08-09
status: complete
---

# Exclude recovery-period instability from ICS attack detection window

## Summary

Explicitly model and flag the post-attack system-stabilization period as a distinct state from active attack behavior, so that elevated irregularity scores during recovery are not reported as an extension of the attack window.

## Addresses

- [[weaknesses/ICS anomaly score remains elevated during post-attack recovery causing false positives]]

## How To Apply

When reviewing anomaly-inference output, cross-reference the sustained-high-score tail following a detected attack against the known process recovery time for the affected asset type before including it in the reported attack duration. Where possible, add a secondary "recovery" label distinct from "attack" in the scoring pipeline output so investigators can visually and programmatically separate the two phases when reconstructing the incident timeline.

## References

- [LWCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
