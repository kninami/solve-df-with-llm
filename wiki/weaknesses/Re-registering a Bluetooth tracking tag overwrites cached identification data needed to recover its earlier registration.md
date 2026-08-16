---
id: DFW-2073
type: weakness
name: Re-registering a Bluetooth tracking tag overwrites cached identification data needed to recover its earlier registration
description: When a physical Bluetooth tracking tag is deleted from a companion app and then re-registered (to the same or a different account), the app's cache files are updated in place to reflect the new registration, overwriting identification data (such as the logId) associated with the tag's earlier registration and preventing that history from being recovered.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2073
source_refs:
  - DFCite-2078
updated_at: 2026-08-16
status: complete
---

# Re-registering a Bluetooth tracking tag overwrites cached identification data needed to recover its earlier registration

## Summary

Companion apps for Bluetooth tracking tags (e.g. Samsung SmartThings/SmartTag) retain a tag's deviceId in a persistent settings database even after the tag entry is deleted, which normally allows an investigator to recover a deleted tag's identity. However, if the same physical tag is deleted and then re-registered — a plausible anti-forensic or simply repeat-use scenario — the app's cache files, which store the model-specific registration identifiers (including the logId used to distinguish individual registration events), are updated in place to reflect only the current registration, silently losing the identifier data associated with the tag's prior registration.

## Why It Matters

An investigator relying solely on cache-file analysis to reconstruct a tag's full registration history could conclude a tag was registered only once, or miss an earlier registration under a different account or timeframe, because the evidence of that earlier registration was overwritten rather than deleted outright (which would at least leave a detectable gap). This is a genuine incompleteness risk distinct from outright deletion: the artifact silently updates rather than vanishing, so an examiner who is not specifically aware of this overwrite behavior may not think to look for corroborating evidence elsewhere.

## Related Mitigations

- [[mitigations/Cross-reference activity logs and duplicate-identifier checks to recover a tracking tag's pre-re-registration identity]]

## Used By

- [[techniques/Extract Bluetooth tracker companion-app geolocation artifacts from databases and memory]]

## References

- [DFCite-2078] Yang, Han, Kim, and Kim, 2025, "Samsung tracking tag application forensics in criminal investigations", FSI: Digital Investigation 52, 301875. Documents the cache-overwrite recovery-failure case observed when a Samsung SmartTag2 was re-registered during S.TASER's tool-validation testing.
