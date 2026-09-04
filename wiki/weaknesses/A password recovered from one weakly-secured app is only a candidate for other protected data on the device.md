---
id: LWW-1212
type: weakness
name: A password recovered from one weakly-secured app is only a candidate for other protected data on the device
description: A secret value recovered from a weakly-protected app is not a confirmed credential for any other app, account, or encrypted container on the same device; it is only a candidate value that may or may not have been reused, and treating it as a confirmed match without independently verifying it against the target risks a false or unsupported attribution.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1212
source_refs:
  - LWCite-1224
updated_at: 2026-08-13
status: complete
---

# A password recovered from one weakly-secured app is only a candidate for other protected data on the device

## Summary

Password-reuse rates, while common, are not universal — the same study cited to motivate cross-app password inference reports roughly half of users reuse passwords, meaning roughly half do not, or reuse only partially (e.g., a shared root with per-service suffixes). A password recovered from one app on a device is therefore a probabilistic candidate for unlocking a different app or account, not a demonstrated fact about that other app's credential.

## Why It Matters

Presenting a device-wide "password profile" as though it establishes the credential for a specific, unrelated protected item overstates the evidentiary weight of the finding and risks misleading a reader (or a court) into treating an unverified guess as a confirmed unlock. The risk is compounded because the inference is being used specifically in cases where the target app or account is more strongly protected precisely because a successful match cannot be independently confirmed without actually applying the candidate password and observing whether it succeeds.

## Related Mitigations

- [[mitigations/Treat cross-app password-reuse inferences as unverified candidates until tested against the target]]

## Used By

- [[techniques/Build a device-wide password-reuse profile from passwords recovered across multiple weakly-secured apps]]

## References

- [LWCite-1224] Shin et al., 2022, "Forensic analysis of note and journal applications", FSI: Digital Investigation 40.
