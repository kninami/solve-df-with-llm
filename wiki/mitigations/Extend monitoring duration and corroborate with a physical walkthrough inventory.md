---
id: DFM-1026
type: mitigation
name: Extend monitoring duration and corroborate with a physical walkthrough inventory
source_refs:
  - DFCite-1018
updated_at: 2026-08-09
status: complete
---

# Extend monitoring duration and corroborate with a physical walkthrough inventory

## Summary

Monitor for longer than the minimum needed for a snapshot to increase the chance of capturing intermittently-transmitting devices, and treat the RF-derived device list as a starting point to be confirmed and supplemented by a physical inventory once the scene is safely entered, rather than as an exhaustive final count.

## Addresses

- [[weaknesses/Passive RF monitoring cannot discover IoT devices that are not currently transmitting]]

## How To Apply

Where the operational situation permits, extend the pre-entry monitoring period beyond a brief snapshot; collecting communications over a longer period also enables building a timeline of the network and detecting devices that were added, removed, or relocated. After entry, physically survey the scene for IoT-capable devices that were silent during monitoring (powered off, charging, or between broadcast intervals) and cross-reference them against the RF-derived inventory, updating the evidence list accordingly rather than relying on the pre-entry scan alone.

## References

- [DFCite-1018] Jacob and Nisbet, 2022, "A forensic investigation framework for Internet of Things monitoring", FSI: Digital Investigation 42-43.
