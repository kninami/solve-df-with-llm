---
id: DFM-1308
type: mitigation
name: Seek zxcrypt key material from a live or powered device before relying on dead-disk MinFS analysis
source_refs:
  - DFCite-1343
updated_at: 2026-08-15
status: complete
---

# Seek zxcrypt key material from a live or powered device before relying on dead-disk MinFS analysis

## Summary

Before a Fuchsia device is powered down and only dead-disk analysis remains possible, prioritize capturing zxcrypt key material or an unencrypted view of the MinFS partition (via live acquisition, memory forensics, or device-provided export functionality where available), since dead-disk-only analysis of an encrypted MinFS partition may be unable to recover its content at all.

## Addresses

- [[weaknesses/Fuchsia's zxcrypt encryption subsystem can block dead-disk examination of MinFS partition content]]

## How To Apply

When a Fuchsia device is encountered powered on or accessible in a live state, prioritize live-acquisition approaches (memory capture, live file system export, or key extraction via any device-specific debugging/development interface) that might yield zxcrypt key material or decrypted MinFS content, rather than immediately powering down the device for [[techniques/Parse Google Fuchsia's Zircon-FVM disk structures for dead-disk forensic analysis]] alone. Where only a powered-down device is available, document the zxcrypt obstacle explicitly in the case file and treat MinFS content as potentially unrecoverable pending further research into the platform's key-management mechanisms, rather than assuming absence of visible content indicates absence of relevant data.

## References

- [DFCite-1343] Jarrett and Morris, 2021, "Purple dawn: Dead disk forensics on Google's Fuchsia operating system", FSI: Digital Investigation 39, 301269.
