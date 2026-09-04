---
id: LWM-1072
type: mitigation
name: Validate and update application wordlists per app version before relying on known-path extraction results
source_refs:
  - LWCite-1062
updated_at: 2026-08-10
status: complete
---

# Validate and update application wordlists per app version before relying on known-path extraction results

## Summary

Before treating a wordlist-based extraction tool's near-empty result for an application as evidence that the app stores little forensically relevant data, confirm the wordlist was built against (or has been validated for) the specific version of the application installed on the target device.

## Addresses

- [[weaknesses/Application version updates can eliminate or relocate artifacts targeted by wordlist-based known-path extraction]]

## How To Apply

Record the target application's version during acquisition, and check or update the extraction wordlist against that version before relying on a sparse result as conclusive. Where a wordlist has not been validated for the installed version, supplement automated extraction with manual file-system review to confirm whether relevant artifacts were relocated, renamed, or genuinely absent.

## References

- [LWCite-1062] Johnson et al., 2022, "Alt-tech social forensics: Forensic analysis of alternative social networking applications", FSI: Digital Investigation 42.
