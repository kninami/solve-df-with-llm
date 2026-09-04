---
id: LWM-2073
type: mitigation
name: Cross-reference activity logs and duplicate-identifier checks to recover a tracking tag's pre-re-registration identity
source_refs:
  - LWCite-2078
updated_at: 2026-08-16
status: complete
---

# Cross-reference activity logs and duplicate-identifier checks to recover a tracking tag's pre-re-registration identity

## Summary

When a Bluetooth tracking tag's companion-app cache no longer reflects an earlier registration because the tag was re-registered, recover the earlier registration's identifier by cross-referencing the app's persistent activity log against cache-derived registration timestamps and model-specific duplicate-identifier checks, rather than relying on the cache alone.

## Addresses

- [[weaknesses/Re-registering a Bluetooth tracking tag overwrites cached identification data needed to recover its earlier registration]]

## How To Apply

Search the companion app's persistent activity log (e.g. `PersistentLogData.db`) for tag-creation and tag-deletion records tied to the device's deviceId, which survives across re-registrations even when the cache-stored logId does not. Combine the server-access timestamps recorded in the app's cache files with the model-specific registration information and duplicate-logId checks performed during the registration workflow to infer the identifier that was in use immediately before the re-registration. Document that a re-registration occurred and that the recovered pre-re-registration identifier was reconstructed indirectly, rather than read directly from a single artifact.

## References

- [LWCite-2078] Yang, Han, Kim, and Kim, 2025, "Samsung tracking tag application forensics in criminal investigations", FSI: Digital Investigation 52, 301875.
