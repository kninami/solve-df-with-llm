---
id: LWM-1056
type: mitigation
name: Independently validate ICS monitoring tool performance overhead and self-tamper resistance before deployment
source_refs:
  - LWCite-1046
updated_at: 2026-08-09
status: complete
---

# Independently validate ICS monitoring tool performance overhead and self-tamper resistance before deployment

## Summary

Before deploying a project-file integrity monitoring and restoration tool on a production ICS engineering workstation, independently measure its resource overhead and evaluate whether its own monitoring database and process can be tampered with or disabled by an attacker who has compromised the workstation.

## Addresses

- [[weaknesses/ICS project-file monitoring and restoration tooling lacks its own performance and security evaluation]]

## How To Apply

Run a resource-overhead assessment (CPU, memory, disk I/O impact) of the monitoring tool on a representative test EWS before production deployment, given the paramount importance of ICS availability. Separately, harden the tool's own storage and process (e.g., write-once or append-only logging, running the monitoring database on a separate secured host rather than the same EWS being monitored, restricting write access to the version-history database) so that an attacker capable of compromising the EWS's project files cannot also silently disable or falsify the monitoring record itself.

## References

- [LWCite-1046] Shin et al., 2022, "A study on command block collection and restoration techniques through detection of project file manipulation on engineering workstation of industrial control system", FSI: Digital Investigation 40.
