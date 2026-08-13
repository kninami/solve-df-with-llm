---
id: DFM-1212
type: mitigation
name: Treat cross-app password-reuse inferences as unverified candidates until tested against the target
source_refs:
  - DFCite-1224
updated_at: 2026-08-13
status: complete
---

# Treat cross-app password-reuse inferences as unverified candidates until tested against the target

## Summary

Use passwords recovered from a device's weakly-secured apps only as a candidate wordlist for attempting access to another, more strongly protected app or account, and only report a match once it has actually been tested and confirmed to succeed against the specific target.

## Addresses

- [[weaknesses/A password recovered from one weakly-secured app is only a candidate for other protected data on the device]]

## How To Apply

Compile recovered secret values from every weakly-secured app on the device, along with common mangling variants (case changes, digit suffixes, punctuation substitutions), into a device-specific candidate wordlist, and use it as an input to a targeted dictionary attack against the more strongly protected item rather than assuming any single recovered value is directly applicable. Report only confirmed successful unlocks in case findings, and where an unlock attempt fails or cannot be tested (e.g., due to a lockout policy), state explicitly that the candidate passwords are unverified rather than implying the target credential is known.

## References

- [DFCite-1224] Shin et al., 2022, "Forensic analysis of note and journal applications", FSI: Digital Investigation 40.
