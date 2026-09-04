---
id: LWW-1206
type: weakness
name: Ephemeral-message recovery completeness varies unpredictably by app, platform, and forensic tool
description: The proportion of disappearing-message content recoverable after expiry differs sharply and unpredictably between messaging apps, between Android and iOS, and between forensic tools, so an investigator cannot assume a result obtained for one app/platform/tool combination generalizes to another.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1206
source_refs:
  - LWCite-1218
updated_at: 2026-08-13
status: complete
---

# Ephemeral-message recovery completeness varies unpredictably by app, platform, and forensic tool

## Summary

Testing showed WhatsApp iOS retained nearly all data pre-expiry while WhatsApp Android retained almost none in the same test group, yet the pattern reversed for Snapchat (Android near-complete, iOS unrecoverable) and reversed again for Telegram (Android partially recoverable with manual review, iOS wholly unrecoverable). The choice of forensic tool compounded this: Cellebrite and XRY produced different recovery rates on the same device and app, and Cellebrite's physical extraction did not always outperform its own logical/advanced-logical extraction.

## Why It Matters

An investigator who validates a disappearing-message recovery procedure against one app/platform/tool combination and assumes it will transfer to a different combination risks either overstating what can be recovered (leading to an incomplete report presented as complete) or abandoning acquisition attempts that would in fact have succeeded on a different platform or with a second tool. Because the direction of the effect (which platform or tool performs better) is not consistent across apps, this cannot be corrected with a single fixed rule of thumb.

## Related Mitigations

- [[mitigations/Cross-validate disappearing-message recovery using multiple forensic tools and manual database review]]

## Used By

- [[techniques/Extract disappearing messages using multi-tool pre- and post-expiry acquisition]]

## References

- [LWCite-1218] Heath et al., 2023, "Forensic analysis of ephemeral messaging applications: Disappearing messages or evidential data?", FSI: Digital Investigation 46.
