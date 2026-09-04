---
id: LWW-1026
type: weakness
name: Passive RF monitoring cannot discover IoT devices that are not currently transmitting
description: Because passive RF signal monitoring relies entirely on observing a device's active wireless communications, any IoT device that is powered off, faulty, has its battery removed for charging, or is simply idle between its periodic broadcast intervals during the monitoring window will not be discovered, regardless of its physical presence at the scene.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1026
source_refs:
  - LWCite-1018
updated_at: 2026-08-09
status: complete
---

# Passive RF monitoring cannot discover IoT devices that are not currently transmitting

## Summary

The model's own stated limitation is that "communications required for the modelling will be absent from sensor and actuator devices that are faulty and devices with their batteries removed for charging." Additionally, even active battery-powered devices only transmit periodically (observed as infrequently as once per ~40 seconds in testing), so a very short monitoring window increases the chance of missing an otherwise-active device entirely.

## Why It Matters

A device count or location estimate produced by a brief monitoring session should not be treated as an exhaustive inventory of all IoT devices physically present at a scene — a device present but silent (charging, faulty, or simply between broadcast intervals) will simply not appear in the results, with no indication to the investigator that anything was missed. This is particularly significant given the method's core value proposition is informing search-and-seizure scope before entry; an undercount could cause a relevant device to be overlooked entirely if not corroborated by a subsequent physical walkthrough.

## Related Mitigations

- [[mitigations/Extend monitoring duration and corroborate with a physical walkthrough inventory]]

## Used By

- [[techniques/Discover IoT devices before entry using passive RF signal triangulation]]

## References

- [LWCite-1018] Jacob and Nisbet, 2022, "A forensic investigation framework for Internet of Things monitoring", FSI: Digital Investigation 42-43.
