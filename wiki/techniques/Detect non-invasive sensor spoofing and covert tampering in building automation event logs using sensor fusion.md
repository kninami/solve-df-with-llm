---
id: DFT-2086
type: technique
name: Detect non-invasive sensor spoofing and covert tampering in building automation event logs using sensor fusion
description: Cross-reference event log records from multiple independent sensor types covering the same physical space in a building automation and control system (BACS) or home automation system (HAS) -- e.g. a PIR (passive infrared) motion sensor alongside a CO2 sensor -- to detect non-invasive spoofing (injecting false presence events) or covert evasion (avoiding triggering a sensor while physically present) that a single sensor type's log alone would not reveal.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2084
aliases:
  - Ghost in the building
  - BACS/HAS non-invasive attack detection via sensor fusion
source_refs:
  - DFCite-2104
updated_at: 2026-08-16
status: complete
---

# Detect non-invasive sensor spoofing and covert tampering in building automation event logs using sensor fusion

## Summary

Building automation and control systems (BACS) and home automation systems (HAS) log sensor readings and actuator states as the evidentiary basis for crime scene reconstruction, but individual sensor types can each be non-invasively deceived without leaving any distinguishing trace in their own event log: a PIR sensor can be spoofed into registering false presence, or evaded by shielding a person's thermal signature, and a CO2 sensor can similarly be evaded by preventing exhaled breath from reaching it. Fusing readings from two or more sensor types that independently cover the same physical space lets an analyst cross-check whether one sensor's account of an event is corroborated or contradicted by another, revealing tampering that neither sensor's log alone would expose.

## Details

Attacks against BACS/HAS sensors are non-invasive when they do not cause physical harm or alteration to the targeted sensor -- for example, using a thermal-emitting drone to trigger a PIR sensor's presence detection from outside, or using an emergency blanket or inflatable-mattress air container to shield a person's thermal signature or exhaled CO2 from being registered. A spoofing attack injects a false event (e.g. fabricating presence where none existed); a covert attack instead evades detection entirely (e.g. a person physically present but never registered). Because a PIR sensor is a passive thermal-motion detector and a CO2 sensor measures a physically distinct property (infrared absorption by exhaled gas), an attack effective against one sensor type does not automatically fool the other operating in the same space: the same event log analysis technique proposed here checks whether a claimed presence/absence event is consistent across both sensor types' independent records, flagging a mismatch (e.g. a CO2 reading consistent with occupancy but no corresponding PIR trigger, or vice versa) as an indicator of possible tampering with one of the sensor channels.

## Examples

- A drone flown along an indoor route past several PIR-equipped rooms successfully triggered sequential PIR sensor activations matching the drone's flight path, demonstrating that a PIR sensor cannot by itself distinguish a genuine human presence event from a thermal-emitting object deliberately introduced to spoof one.
- Concealing a person behind an emergency blanket, and separately behind an inflatable mattress used as an air-collection container for exhaled breath, successfully evaded detection by PIR and CO2 sensors respectively in toilets not otherwise connected to the tested BACS, with no event log record generated despite genuine physical presence -- illustrating a covert (rather than spoofing) attack.
- Injecting spoofed event log records into a Home Automation System (HAS) controller via a configured spoofing attack device (leveraging the RFXtrx433E transceiver and the KAKU/PT2272 remote-control protocol) demonstrated the same class of non-invasive log-record injection is feasible for actuator-triggered events, not only sensor readings, extending the technique's relevance beyond BACS sensor fusion to HAS actuator event verification.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Non-invasive sensor spoofing and covert attacks against a single building-automation sensor type leave no distinguishing trace in its own event log]]

## References

- [DFCite-2104] Bengtsson, Johnny, 2025, "The ghost in the building: Non-invasive spoofing and covert attacks on automated buildings", FSI: Digital Investigation 52, 301880.
