---
id: DFT-1019
type: technique
name: Access a cloud account using captured credentials
description: Access a suspect's cloud-hosted account data by leveraging captured or extracted authentication material, via either of two approaches — querying the provider's own API directly with a captured bearer/access/refresh token, or migrating decrypted browser-stored session credentials to an investigator-controlled device so its browser can auto-login as the suspect — retrieving substantially more evidence than what is stored locally on the suspect's device.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1019
  - DFW-1055
aliases:
  - Captured-credential-based cloud account access
  - Cloud API acquisition via captured authentication tokens
source_refs:
  - DFCite-1013
  - DFCite-1045
updated_at: 2026-08-09
status: complete
---

# Access a cloud account using captured credentials

## Summary

Many applications and cloud services store only a thin local cache and instead serve most account data on-demand once a valid authentication credential is presented. An investigator who has extracted or reconstructed that credential — a bearer/access/refresh token from an app's local storage, or a browser's own encrypted session cookie/token — can present it back to the provider as though they were the legitimate user, retrieving substantially more evidence than local device extraction alone would yield, without needing the user's actual password.

## Details

**Direct API token use**: authentication mechanisms vary by provider and directly affect what is required to impersonate a user — some issue a long-lived bearer token invalidated only on re-registration, others issue a short-lived access token paired with a longer-lived refresh token that should be the acquisition target if the access token has already expired. Where tokens are stored in an OS-encrypted keychain (iOS), device passcode access is required; where stored in plaintext shared-preferences files (Android), the token can be read directly. Once authenticated, the API frequently exposes more granular data than the application UI displays, since it was not filtered for end-user presentation.

**Browser credential migration**: most browsers encrypt stored session credentials with a device-bound key (e.g., Windows DPAPI), so a naive copy of the encrypted credential store to a different machine will not work. Migration instead decrypts each credential on the source device (using the source device's own key material, e.g., from the Windows registry's SYSTEM/SECURITY hives), then re-encrypts it for the investigator's own device before inserting it into the investigator's installed browser, causing the browser's existing auto-login/"remember me"/trusted-device state to authenticate as the suspect — bypassing multi-factor authentication that would otherwise block a simple credential copy, since the receiving browser is presenting the same already-trusted session rather than a fresh login attempt.

## Examples

- Micromobility rental applications (Lime, TIER, Nextbike, Voi): each stored only a limited local subset of ride data, while the corresponding provider APIs returned substantially richer temporal, geo, and payment data once authenticated with a captured token.
- Migrating a suspect's Chrome (Chromium-based) session cookies from a Windows target device to an investigator's Windows device, by decrypting the DPAPI-protected credential using the target device's registry key material and re-encrypting it with the investigator device's own DPAPI key, successfully auto-logged into Google, Naver, and other accounts and retrieved chat history, cloud-stored files, and device location data.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Micromobility ride-history location data can be fabricated via provider APIs]]
- [[weaknesses/Browser credential migration cannot recover credentials from browsers that do not persist data]]

## References

- [DFCite-1013] Hilgert et al., 2021, "A forensic analysis of micromobility solutions", FSI: Digital Investigation 38.
- [DFCite-1045] Hur et al., 2023, "A study on cloud data access through browser credential migration in Windows environment", FSI: Digital Investigation 45.
