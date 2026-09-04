---
id: LWT-1189
type: technique
name: Extract a TOTP secret key from a 2FA app to bypass two-factor authentication
description: Forensically examine a 2FA authenticator application's on-disk storage across mobile and desktop platforms to recover its TOTP secret key and associated account metadata, then use the recovered key to independently generate valid one-time passcodes and authenticate to the protected account without the original device.
objective_ids:
  - DFO-1016
weakness_ids:
  - LWW-1196
aliases:
  - 2FA application forensic artifact extraction
  - TOTP secret key extraction and OTP replication
source_refs:
  - LWCite-1206
updated_at: 2026-08-13
status: complete
---

# Extract a TOTP secret key from a 2FA app to bypass two-factor authentication

## Summary

Time-based One-Time Password (TOTP) authenticator apps calculate their six-digit codes locally from a secret key established when an account is added, so an investigator who recovers that key from the device's storage can independently reproduce valid codes for the protected account on any other device or app instance, without needing to seize, unlock, or continuously operate the original device.

## Details

Across fifteen popular 2FA applications (including FreeOTP, Google Authenticator, Microsoft Authenticator, Twilio Authy, Aegis, and others) tested on rooted/jailbroken Android and iOS devices and a Windows VM, forensic disk imaging (physical images via tools such as Magnet Acquire and ArtEx on mobile, targeted file-system acquisition on Windows) recovered account names in plain text from 80% of apps, the issuer/service name from 93%, and — critically — the TOTP secret key itself, in plain text or a reversibly encoded form, from 73% of apps. Network traffic capture proved largely unproductive because the 2FA apps compute OTPs entirely locally and the authenticated services themselves commonly use certificate pinning, blocking interception; four apps additionally supported an application-lock PIN, which in some configurations also encrypted on-disk data, changing what was recoverable. Once a secret key is extracted, loading it into a fresh instance of a 2FA app (on any platform) reproduces identical OTPs to the original, which were then used to successfully log in to the corresponding 2FA-protected social media/cloud accounts (Facebook, Twitter) in a controlled proof-of-concept, confirming the extracted key alone is sufficient to regenerate valid authentication codes.

## Examples

- Twilio Authy was the only tested app requiring a phone number during setup, and that number was recoverable from the Android disk image; more generally, timestamps recording when an account was added to the 2FA app were found in 53% of apps tested.
- A secret key extracted from a Google Authenticator instance on one platform was manually entered into a separate 2FA app instance; the generated one-time codes matched across all tested devices/platforms and successfully authenticated to the originating social media account.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/2FA bypass using an extracted TOTP secret key requires separately obtained account login credentials]]

## References

- [LWCite-1206] Berrios et al., 2023, "Factorizing 2FA: Forensic analysis of two-factor authentication applications", FSI: Digital Investigation 45.
