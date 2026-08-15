---
id: DFT-2051
type: technique
name: Identify VoIP call participants from encrypted IM traffic using STUN correlation
description: The process of identifying which suspects (by IP address) participated in a voice or video call placed through an end-to-end-encrypted instant messaging application, by capturing and deep-packet-inspecting network traffic, extracting peer IP information from STUN protocol messages (or correlating traffic-flow features when STUN is absent), and compiling the results into a comprehensive Call Detailed Record without requiring physical access to any suspect's device.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-2051
aliases:
  - Network Forensic Approach (NFA) for VoIP/IM calls
source_refs:
  - DFCite-2052
updated_at: 2026-08-14
status: partial
---

# Identify VoIP call participants from encrypted IM traffic using STUN correlation

## Summary

Most instant messaging traffic is now end-to-end encrypted, making content-based analysis of the calls themselves impossible, and traditional device forensics requires physical access to a suspect's phone - often unavailable during early crime detection or when a device has been destroyed. An investigator instead captures network traffic passing through a monitored access point or switch, applies deep packet inspection to classify each flow's application and protocol, and exploits the fact that most IM voice/video calling still uses the STUN (Simple Traversal of User Datagram) protocol for NAT traversal - meaning STUN messages routinely reveal both call participants' actual IP addresses even though the call's audio/video content remains encrypted.

## Details

DFCite-2052's methodology proceeds through data collection (capturing and exporting IPFIX network flow data via nDPI, tagged with per-application STUN sub-signatures like STUN.Telegram, STUN.Apple/FaceTime, STUN.FacebookVoIP/WhatsAppCall, STUN.SignalVoIP, STUN.GoogleCloud/GoogleHangoutDuo), data preparation (deduplication, missing-value removal, and filtering to IM-call-relevant traffic only), data analysis (extracting call time, duration, packet counts, and byte sizes per flow), and a correlation module implementing two cases: Case 1 (STUN messages present) directly extracts peer IP information and application type from the STUN message itself and calculates call duration from its start/end timestamps; Case 2 (STUN absent, i.e. the generic "STUN.proto" case) instead compares each subscriber's traffic-flow object (start time, duration, protocol, packet count) against every other subscriber's object using a correlation index, returning the highest-correlated peer as the other call participant. Both cases feed a final CDR Extractor that maps identified IP pairs back to known subscriber identities via a pre-established user-mapping sheet, producing complete Call Detailed Records (source/destination target, application, duration, packet/byte counts) usable directly by law enforcement.

## Examples

- DFCite-2052's real-world test network: 8 target devices (4 iPhones, 4 Android phones) running WhatsApp, Signal, Facebook Messenger, Snapchat, and Telegram, monitored for 2 hours, yielding 10,344 raw records reduced to 9,079 after cleaning and 1,255 IM-call-relevant STUN records, with 25 of 27 attempted calls successfully identified and mapped to full CDRs (92.5% success rate).

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Open-source DPI classification limitations cause missed and misclassified IM calls in VoIP network forensics]]

## References

- [DFCite-2052] Sarhan et al., "VoIP network forensics of instant messaging calls", IEEE Access, 2024 — source of the STUN-based correlation methodology, CDR extraction process, and evaluation results described above.
