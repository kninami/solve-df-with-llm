---
id: LWT-1203
type: technique
name: Build a device-wide password-reuse profile from passwords recovered across multiple weakly-secured apps
description: Recover the plaintext or weakly-hashed secret values used to lock several different apps on the same seized device, and pool them into a candidate password list, exploiting the common real-world behavior of users reusing the same or similar passwords across services to attempt unlocking a separate, more strongly protected app or account with the same device.
objective_ids:
  - DFO-1016
weakness_ids:
  - LWW-1212
aliases:
  - Cross-app password pool inference
source_refs:
  - LWCite-1224
updated_at: 2026-08-13
status: complete
---

# Build a device-wide password-reuse profile from passwords recovered across multiple weakly-secured apps

## Summary

Because most consumer apps that offer a "lock" feature protect the underlying secret value poorly (plaintext, a fast hash, or a fixed/derivable key), an investigator who recovers the secret value from every weakly-secured app on a device accumulates a candidate password list that reflects the device owner's actual password habits, which can then be tried against a different, more strongly protected app or account on the same device.

## Details

Recovering secret values across multiple apps on the same device is more informative in aggregate than recovering any single app's secret value alone: general password-reuse statistics (over half of users reuse identical or similar passwords across different services) suggest that a strongly protected app's password is likely to appear, in identical or lightly modified form, among the passwords recovered from the device's other, weaker apps. This turns what looks like a series of isolated low-value findings (one four-digit PIN here, one recoverable password there) into a device-specific candidate wordlist that can meaningfully increase the odds of successfully unlocking or decrypting a target that would otherwise require an infeasible brute-force search.

## Examples

- Recovering a plaintext or trivially-hashed four-digit PIN from a note-taking app, a similarly weak password from a diary app, and a longer freeform password from a third app on the same device, then combining all three (plus common mangling variants) into a device-specific wordlist to attempt against a separately encrypted, strongly-protected app on the same device.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/A password recovered from one weakly-secured app is only a candidate for other protected data on the device]]

## References

- [LWCite-1224] Shin et al., 2022, "Forensic analysis of note and journal applications", FSI: Digital Investigation 40.
