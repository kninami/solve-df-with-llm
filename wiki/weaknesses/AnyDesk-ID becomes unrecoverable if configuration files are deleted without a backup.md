---
id: LWW-1018
type: weakness
name: AnyDesk-ID becomes unrecoverable if configuration files are deleted without a backup
description: If a device's local AnyDesk configuration files (system.conf, service.conf) are deleted — whether deliberately by a user or as part of anti-forensic cleanup — the device's own AnyDesk-ID and any user-assigned Alias become permanently irretrievable from that device unless a backup of the configuration was separately preserved.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1018
source_refs:
  - LWCite-1012
updated_at: 2026-08-09
status: complete
---

# AnyDesk-ID becomes unrecoverable if configuration files are deleted without a backup

## Summary

AnyDesk's own documentation confirms that both the AnyDesk-ID and any configured Alias are stored within the `service.conf` configuration file, and that losing this file makes the ID and Alias unrecoverable unless restored from a backup. While AnyDesk uninstallation does not by default remove the ID or configuration files, a user (suspect or otherwise) can still manually delete them.

## Why It Matters

If an investigator relies solely on the seized device's own configuration files to establish its AnyDesk-ID, deliberate or incidental deletion of `service.conf`/`system.conf` before acquisition permanently forecloses that path — there is no fallback recovery mechanism on that device alone. This creates a specific incentive and opportunity for anti-forensic action by a suspect aware of AnyDesk's configuration-file dependency.

## Related Mitigations

- [[mitigations/Search the paired device's mutual logs and application backups for a missing AnyDesk-ID]]

## Used By

- [[techniques/Correlate remote-access session identifiers across devices]]

## References

- [LWCite-1012] Soni et al., 2024, "A forensic analysis of AnyDesk Remote Access application by using various forensic tools and techniques", FSI: Digital Investigation 48.
