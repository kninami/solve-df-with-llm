---
id: LWM-1125
type: mitigation
name: Pair DLAM with a traditional updatable fuzzy-hash blacklist for newly discovered files pending retraining
source_refs:
  - LWCite-1119
updated_at: 2026-08-12
status: complete
---

# Pair DLAM with a traditional updatable fuzzy-hash blacklist for newly discovered files pending retraining

## Summary

Maintain a conventional, instantly-updatable fuzzy-hash (ssdeep/TLSH) blacklist alongside a DLAM deployment, so a newly discovered blacklisted file can be detected immediately via direct hash comparison while a DLAM retraining or fine-tuning cycle incorporating that file is scheduled and completed.

## Addresses

- [[weaknesses/DLAM requires supervised retraining per blacklisted fragment, unlike signature-database-updatable fuzzy hashing]]

## How To Apply

Run both detection paths in the operational workflow: add newly discovered blacklisted files to the traditional fuzzy-hash lookup database immediately for coverage against exact or near-complete matches, and batch newly added files into a periodic DLAM retraining/fine-tuning cycle to bring small-fragment detection accuracy up to DLAM's level once training resources are available. Document which detection path (traditional hash comparison vs. DLAM) produced a given match, since their accuracy characteristics differ, particularly for small fragments.

## References

- [LWCite-1119] Uhlig et al., 2023, "Combining AI and AM - Improving approximate matching through transformer networks", FSI: Digital Investigation 45.
