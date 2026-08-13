---
id: DFT-1173
type: technique
name: Detect USB attack platform usage from memory-resident diagnostic telemetry and DHCP artifacts
description: Scan a post-mortem Windows memory image for Windows diagnostic-telemetry JSON structures and DHCP client log entries — carving and repairing them where partially overwritten — to detect and identify use of a USB-based attack platform (e.g., a USB Rubber Ducky or Bash Bunny), even hours after the device was disconnected.
objective_ids:
  - DFO-1019
  - DFO-1017
weakness_ids:
  - DFW-1180
aliases:
  - Duck Hunt
  - usbhunt / dhcphunt Volatility plugins
source_refs:
  - DFCite-1182
updated_at: 2026-08-12
status: complete
---

# Detect USB attack platform usage from memory-resident diagnostic telemetry and DHCP artifacts

## Summary

USB-based attack platforms operate almost entirely in memory to minimize disk traces, but every action they invoke still passes through the host OS's drivers and network stack, both of which log activity that persists in RAM. This technique carves two categories of memory-resident evidence — Windows diagnostic-telemetry device events and DHCP client log entries — to detect and characterize USB attack platform usage on a live-triaged or post-mortem memory image.

## Details

Two open-source Volatility 3 plugins implement the technique. `usbhunt` scans memory for Windows diagnostic-telemetry JSON event structures (e.g., `DeviceConfig` and `InventoryDevicePnpAdd` events) that record a connected USB device's identifiers and configuration; because these structures can be partially overwritten by the time memory is acquired, the plugin includes a reconstruction algorithm that repairs JSON truncated at the start or end of the structure, recovering the device identifiers even from damaged copies. `dhcphunt` scans memory for `netsh`-logged DHCP client entries generated when an attack platform enumerates itself as a network interface (e.g., emulating a USB Ethernet/RNDIS adapter to request an IP lease), which can be used to detect and analyze other network-connected USB peripherals beyond the two platforms studied. Neither plugin depends on the originating memory region's Virtual Address Descriptor (VAD) still belonging to its original process, so artifacts remain findable even after process termination. Both artifact types were experimentally shown to remain recoverable in memory for at least 24 hours after the attack. This is distinct from, and complements, [[techniques/Reconstruct user activity timelines from Windows Diagnostics telemetry logs]], which parses the same broad category of Windows diagnostic-telemetry events from the on-disk `EventTranscript.db` rather than carving them from volatile memory; the memory-carving approach can recover device evidence even when the disk-based telemetry database has rotated out the relevant events or is unavailable.

## Examples

- Running `usbhunt` and `dhcphunt` against Windows 10 memory images taken after a Hak5 USB Rubber Ducky or Bash Bunny attack recovered device identifiers and DHCP log entries sufficient to definitively detect that a USB attack platform had been connected, even though the device itself was no longer physically present.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/Memory-carved JSON reconstruction fails to recover structures overwritten in their middle]]

## References

- [DFCite-1182] Thomas et al., 2021, "Duck Hunt: Memory forensics of USB attack platforms", FSI: Digital Investigation 37.
