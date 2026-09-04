---
id: LWT-1026
type: technique
name: Discover IoT devices before entry using passive RF signal triangulation
description: Before entering a scene, passively monitor the radio frequencies used by low-rate, short-range IoT wireless protocols (e.g., Zigbee, ZWave, IEEE 802.15.4) from multiple positions around its perimeter to discover, count, and estimate the physical locations of IoT devices without alerting an occupant or triggering evidence destruction.
objective_ids:
  - DFO-1014
weakness_ids:
  - LWW-1026
aliases:
  - Passive RF signal triangulation for pre-entry IoT device discovery
source_refs:
  - LWCite-1018
updated_at: 2026-08-09
status: complete
---

# Discover IoT devices before entry using passive RF signal triangulation

## Summary

IoT sensor/actuator devices increasingly resemble ordinary physical objects, making them easy for investigators to overlook during conventional search-and-seizure. Because these devices continuously broadcast and respond to low-rate wireless traffic that is often more resilient through obstacles than Wi-Fi/Bluetooth, capturing that traffic from outside a scene's boundary — using radio modules capable of sensing the relevant channels — lets investigators discover the presence, approximate count, and general location of IoT devices before deciding how and where to search.

## Details

The process has three stages. First (Observe), radio modules positioned around a target's perimeter identify occupied frequency channels and capture real-time traffic between static and mobile IoT nodes. Second (Analyze), network-management and control data embedded in the captured low-rate traffic is extracted to build the logical topology of datalinks between nodes, distinguishing which nodes belong to the same network via addressing/identification information — this stage can be skipped if speed is more urgent than full topology mapping. Third (Utilize), the known positions of the monitoring radio modules are used to deduce candidate locations for static source nodes (nodes within each monitor's limited range), merge overlapping candidate arrangements from multiple monitors, and then similarly derive positions for mobile nodes relative to the static nodes they communicate with.

## Examples

- A SmartThings Zigbee/ZWave hub with two battery-powered sensors was monitored using a Kinetis USB-KW24D512 radio module at varying distances (0-10m and 45-55m) through six wall types; the mains-powered hub's broadcasts remained largely monitorable at the longer distance for most wall types, while the two battery-powered sensors' communications dropped substantially (median 33% decrease across wall types, over 65-80% for some).

## Related Objectives

- `DFO-1014` Find potential digital evidence sources

## Related Weaknesses

- [[weaknesses/Passive RF monitoring cannot discover IoT devices that are not currently transmitting]]

## References

- [LWCite-1018] Jacob and Nisbet, 2022, "A forensic investigation framework for Internet of Things monitoring", FSI: Digital Investigation 42-43.
