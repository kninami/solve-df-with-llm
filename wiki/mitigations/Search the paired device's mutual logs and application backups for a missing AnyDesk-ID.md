---
id: DFM-1018
type: mitigation
name: Search the paired device's mutual logs and application backups for a missing AnyDesk-ID
source_refs:
  - DFCite-1012
updated_at: 2026-08-09
status: complete
---

# Search the paired device's mutual logs and application backups for a missing AnyDesk-ID

## Summary

If a device's own AnyDesk configuration files have been deleted and no local backup exists, look for the same AnyDesk-ID recorded independently in the logs of any device it connected to, since remote-access sessions cause both endpoints to log each other's client ID.

## Addresses

- [[weaknesses/AnyDesk-ID becomes unrecoverable if configuration files are deleted without a backup]]

## How To Apply

When a suspect device's `service.conf`/`system.conf` has been deleted, seek out any device known or suspected to have connected to it via AnyDesk (from other evidence such as chat logs, network records, or witness statements), and examine that device's own trace/configuration files for the missing device's AnyDesk-ID. Also check for any backup of the AnyDesk configuration (per AnyDesk's own backup/restore mechanism) that may have been made before deletion, and consider whether a paid-license Alias registration might allow the provider to confirm association between an ID and account, subject to appropriate legal process.

## References

- [DFCite-1012] Soni et al., 2024, "A forensic analysis of AnyDesk Remote Access application by using various forensic tools and techniques", FSI: Digital Investigation 48.
