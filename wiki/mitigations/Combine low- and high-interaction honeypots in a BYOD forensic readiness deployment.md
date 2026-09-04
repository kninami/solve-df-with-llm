---
id: LWM-2062
type: mitigation
name: Combine low- and high-interaction honeypots in a BYOD forensic readiness deployment
source_refs:
  - LWCite-2063
updated_at: 2026-08-15
status: complete
---

# Combine low- and high-interaction honeypots in a BYOD forensic readiness deployment

## Summary

Deploy a mix of low-interaction honeypots (e.g., Dionaea, HoneyDroid, Cowrie, Glastopf, BOF, DTK, HoneyBot, GHH) for broad, low-risk coverage of common/known attack patterns, and high-interaction honeypots (e.g., Argos, Sebek, HoneySpider) for capturing novel or advanced attacker techniques, rather than relying on a single low-interaction honeypot alone.

## Addresses

- [[weaknesses/A low-interaction honeypot limits detection and collection of potential digital evidence in a BYOD forensic readiness framework]]

## How To Apply

Select honeypot types to match the organization's risk profile and monitoring capacity: use low-interaction honeypots for wide, low-maintenance coverage of a BYOD network, and add high-interaction honeypots where the organization can accept the higher operational risk (a high-interaction honeypot is a fuller, exploitable system that could itself be leveraged against other systems in the network if not carefully isolated) in exchange for the ability to observe novel exploit behavior. Store the resulting logs, profile data, and forensic evidence from both honeypot tiers in synchronized, time-consistent databases so incidents observed across tiers can be correlated during analysis.

## References

- [LWCite-2063] Asante & Amankona, 2021, "Digital Forensic Readiness Framework Based on Honeypot and Honeynet for BYOD", JDFSL 16(2). Proposes combining low- and high-interaction honeypot technologies within the DFR-BYOD framework's Technology domain specifically to overcome the detection limitation of a low-interaction-only deployment.
