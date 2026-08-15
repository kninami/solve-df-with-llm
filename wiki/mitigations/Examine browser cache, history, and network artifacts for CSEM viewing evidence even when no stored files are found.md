---
id: DFM-2068
type: mitigation
name: Examine browser cache, history, and network artifacts for CSEM viewing evidence even when no stored files are found
source_refs:
  - DFCite-2071
updated_at: 2026-08-15
status: complete
---

# Examine browser cache, history, and network artifacts for CSEM viewing evidence even when no stored files are found

## Summary

Do not conclude an examination once a search for stored CSEM files returns no results; examine browser cache, history, thumbnail caches, and network/traffic artifacts for evidence of a viewing-only consumption pattern, since a substantial proportion of offenders view CSEM without storing it locally at all.

## Addresses

- [[weaknesses/Absence of stored CSEM files does not indicate absence of CSEM viewing or consumption]]

## How To Apply

Scope a CSEM examination to explicitly include viewing-evidence sources beyond stored-file search: browser history and cache (including cached thumbnails and page previews), DNS/network traffic logs where available, and any peer-to-peer or streaming client's own activity/session logs. Where a device search finds no stored CSEM files, document this specifically as "no stored files found" rather than as a general negative result, and continue to the viewing-evidence sources above before concluding the examination; where relevant, corroborate with account-level or ISP-level records that may capture access to CSEM-hosting infrastructure independent of what remains on the device.

## References

- [DFCite-2071] Steel, Newman, O'Rourke & Quayle, 2022, "Technical Behaviours of Child Sexual Exploitation Material Offenders", JDFSL 17(2). Motivates this mitigation via its finding that stored-file presence is neither sufficient nor necessary to determine consumption, and its finding that laptop/desktop browser use was the dominant viewing method.
