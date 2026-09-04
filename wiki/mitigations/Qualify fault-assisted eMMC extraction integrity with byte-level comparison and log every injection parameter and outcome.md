---
id: LWM-1227
type: mitigation
name: Qualify fault-assisted eMMC extraction integrity with byte-level comparison and log every injection parameter and outcome
source_refs:
  - LWCite-1238
updated_at: 2026-08-13
status: complete
---

# Qualify fault-assisted eMMC extraction integrity with byte-level comparison and log every injection parameter and outcome

## Summary

Treat fault-induced unlock, effective access, complete extraction, and integrity qualification as four distinct, sequentially dependent outcomes rather than a single "unlocked" result, and only rely on a fault-assisted eMMC image evidentially after an explicit byte-level comparison against a nominal baseline confirms its integrity — or after the residual divergence rate and its uncertainty are transparently disclosed.

## Addresses

- [[weaknesses/Fault-assisted eMMC access restoration produces byte-level divergence that invalidates hash-equality verification]]

## How To Apply

Only attempt fault injection after all standard logical and physical acquisition paths have been exhausted and documented, and confirm the expected evidential value is proportionate to the risk of device damage. Log the delay, pulse setting, and interface-level observable outcome for every injection attempt so the operating parameter region is documented and reproducible. Once an image is obtained, compute a byte-level (not just hash-level) comparison against a nominal reference acquisition where one is available, report the divergence rate and its spatial distribution explicitly, and treat any post-unlock acquisition as forensically qualified only when divergence is bounded, quantified, and shown not to affect the interpretation of relevant artefacts — an apparently intact file-system structure alone is not sufficient to support a claim of data authenticity.

## References

- [LWCite-1238] Hugget et al., 2026, "Forensic qualification of fault-assisted access restoration on CMD42-locked eMMC: A case study", FSI: Digital Investigation 57, 302109.
