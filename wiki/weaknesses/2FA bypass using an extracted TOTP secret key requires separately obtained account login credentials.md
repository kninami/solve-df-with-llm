---
id: LWW-1196
type: weakness
name: 2FA bypass using an extracted TOTP secret key requires separately obtained account login credentials
description: An extracted TOTP secret key only reproduces the second authentication factor; without the account's first-factor login credential (username/password), the recovered key alone is insufficient to access the protected account, so an investigator who extracts only the key may incorrectly conclude the account is now accessible.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1196
source_refs:
  - LWCite-1206
updated_at: 2026-08-13
status: complete
---

# 2FA bypass using an extracted TOTP secret key requires separately obtained account login credentials

## Summary

The demonstrated TOTP bypass reproduces a valid one-time passcode, but logging into the protected service still requires the account's own username/email and password. The source paper notes credentials must be obtained separately — for example, from the same disk image (account names and email addresses were found in plain text alongside secret keys in several apps), from memory, or through other means such as credential stuffing — and the bypass proof-of-concept assumes an identical OTP-generation algorithm was used consistently across the tested apps.

## Why It Matters

An investigator who successfully extracts a 2FA secret key but stops there has not yet demonstrated account access; presenting the extracted key alone as evidence that the account "can be accessed" overstates what has actually been achieved and may lead to wasted effort attempting login without the first factor, or to an incomplete account of what access was actually verified during the investigation. Correctly scoping and documenting what was and was not verified (key extraction versus full authentication) is important for the reproducibility and defensibility of any subsequent access to the account.

## Related Mitigations

- [[mitigations/Recover the associated account credentials alongside an extracted 2FA secret key before attempting an authentication bypass]]

## Used By

- [[techniques/Extract a TOTP secret key from a 2FA app to bypass two-factor authentication]]

## References

- [LWCite-1206] Berrios et al., 2023, "Factorizing 2FA: Forensic analysis of two-factor authentication applications", FSI: Digital Investigation 45.
