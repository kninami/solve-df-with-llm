---
id: LWM-1196
type: mitigation
name: Recover the associated account credentials alongside an extracted 2FA secret key before attempting an authentication bypass
source_refs:
  - LWCite-1206
updated_at: 2026-08-13
status: complete
---

# Recover the associated account credentials alongside an extracted 2FA secret key before attempting an authentication bypass

## Summary

Plan 2FA-related evidence collection to recover the account's first-factor login credential (username/email and password) from the same or related sources — disk, memory, browser/app credential storage, or lawful legal process to the service provider — alongside the TOTP secret key, rather than treating key extraction in isolation as sufficient for account access.

## Addresses

- [[weaknesses/2FA bypass using an extracted TOTP secret key requires separately obtained account login credentials]]

## How To Apply

During disk and memory examination of a device with a 2FA app installed, also search for account names, email addresses, and any cached or stored credentials for the corresponding protected service — these were found stored in plain text alongside secret keys in several apps in the source study. Where local credentials are not recoverable, pursue other lawful avenues (e.g., credential-recovery workflows through the service provider, or previously seized credential material) before concluding that an authentication bypass is achievable, and document clearly in the investigation record which of the two factors (secret key, login credential) was actually verified.

## References

- [LWCite-1206] Berrios et al., 2023, "Factorizing 2FA: Forensic analysis of two-factor authentication applications", FSI: Digital Investigation 45.
