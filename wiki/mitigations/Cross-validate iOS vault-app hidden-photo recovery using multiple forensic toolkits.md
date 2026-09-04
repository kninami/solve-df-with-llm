---
id: LWM-2064
type: mitigation
name: Cross-validate iOS vault-app hidden-photo recovery using multiple forensic toolkits
source_refs:
  - LWCite-2066
updated_at: 2026-08-15
status: complete
---

# Cross-validate iOS vault-app hidden-photo recovery using multiple forensic toolkits

## Summary

Where a device contains one or more vault/photo-vault applications, process the acquired image with more than one forensic toolkit (e.g., Cellebrite, Axiom, and/or a comparable alternative) and combine their results, since each toolkit's parsing logic recognizes a different subset of vault-app artifact formats.

## Addresses

- [[weaknesses/Forensic toolkit completeness in recovering iOS vault-app hidden photos varies unpredictably by app and tool]]

## How To Apply

When a vault application is identified on a device (by its disguised icon, package name, or install record), do not rely on a single forensic toolkit's report of "no hidden photos found" as conclusive; re-process the same image with at least one additional toolkit, and where feasible manually inspect the User Data partition for the vault app's own storage directory (custom-extension thumbnail files, app-specific SQLite databases, or unusually-named image files) rather than depending solely on automated artifact recognition, since obfuscation techniques (non-standard file extensions, custom database schemas) that evade one tool's detection logic frequently do not evade another's.

## References

- [LWCite-2066] Gilbert & Seigfried-Spellar, 2022, "Forensic Discoverability of iOS Vault Applications", JDFSL 17(1). States that using more than one forensic application "provides the most correct and whole picture of what evidence is on the phone," based on the study's own finding that each of three toolkits missed different vault-app artifacts.
