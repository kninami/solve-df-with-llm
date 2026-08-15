---
id: DFT-1277
type: technique
name: Decode a Nintendo 3DS StreetPass meet.dat database to identify proximate devices and their owners
description: Parse the Nintendo 3DS's StreetPass Mii Plaza NAND database file (meet.dat) to recover the MAC addresses, System IDs, and Mii-creation timestamps of other consoles that have physically passed within Wi-Fi range of the device, establishing evidence that two specific consoles (and their owners) were once in close physical proximity.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1287
aliases:
  - meet.dat StreetPass Mii Plaza decoding
source_refs:
  - DFCite-1318
updated_at: 2026-08-15
status: complete
---

# Decode a Nintendo 3DS StreetPass meet.dat database to identify proximate devices and their owners

## Summary

StreetPass passively exchanges Mii avatar data between Nintendo 3DS consoles that come within Wi-Fi range of each other, and every received Mii is retained in a structured database (`meet.dat`) on the NAND. Because each received-Mii record embeds the originating console's MAC address, its System ID, the device type it was created on, and a creation timestamp, decoding this structure gives an investigator direct evidence that two specific consoles — and by extension their owners — were once in close physical proximity, independent of any network or account data.

## Details

`meet.dat` lives at `sysdata/<region-code>/00000000` on the 3DS NAND, where the region code (`00020218` for the US, `00020228` for the EU, `00020208` for Japan) identifies the console's configured region. The first entry (offset 0x04) holds the console owner's own Mii. The shared-Mii database proper begins with the `MTDB` magic bytes at offset 0x70, followed by a 2-byte entry count (a maximum of 1,000 entries, with `0xFFFF` indicating an empty list) and a lookup table of 14-byte entries (each holding a 4-byte Mii ID and 6-byte MAC address of the Mii's creator) running through offset 0x3727. The full 264-byte shared Mii character entries themselves begin at offset 0x3730, and include the originating device type (3DS, Wii, Switch, etc.), System ID, Mii ID, MAC address, country, state, and the Mii's day/month of creation and creation timestamp (seconds since January 1, 2010). This decoding extends a prior 16-tool suite for Nintendo 3DS artifact extraction with an additional structure not previously documented for forensic use.

## Examples

- Applied across a 47-console secondhand-market case study, `meet.dat` StreetPass data (containing another console's MAC address and Mii-creation time) was recovered from 9 of the 47 consoles (19.2%), providing direct evidence of physical proximity between specific devices.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Nintendo 3DS network location data is limited to country and state, insufficient for precise geolocation]]

## References

- [DFCite-1318] Read, Xynos, Sutherland, Bovee, and Tamburro, 2024, "Nintendo 3DS forensics: A secondhand case study", FSI: Digital Investigation 50, 301815.
