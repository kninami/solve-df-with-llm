---
id: LWW-1264
type: weakness
name: DCNN-based port-scan covert-channel detection accuracy approaches chance level for low-bandwidth embeddings
description: A DCNN classifier trained to detect port-scan steganography loses most of its discriminating power against a covert channel that embeds fewer hidden bits per scan, since a lower embedding bandwidth leaves the destination-port sequence statistically closer to an ordinary randomized port scan, directly trading an adversary's steganographic capacity against the investigator's chance of detecting the channel at all.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1265
source_refs:
  - LWCite-1286
updated_at: 2026-08-14
status: complete
---

# DCNN-based port-scan covert-channel detection accuracy approaches chance level for low-bandwidth embeddings

## Summary

Testing a transfer-learned DCNN detector against covert channels embedding 256, 512, and 768 hidden bits per 1,000-port scan showed test accuracy rising from 54% (256 bits) to 68% (768 bits), meaning the detector performed only marginally better than chance against the lowest-bandwidth embedding tested, and an adversary willing to accept an even lower embedding rate could likely reduce detectability further at the cost of needing more port scans to transmit the same amount of data.

## Why It Matters

An investigator relying on this class of detector risks a false sense of security against a patient adversary who deliberately trades channel bandwidth for stealth: a slow-and-low covert channel spreading a small C2 payload across many port scans over an extended period is precisely the scenario where the detector is least effective, yet is also the more operationally realistic threat model for a persistent, cautious attacker (e.g. an advanced persistent threat) compared to the higher-bandwidth channels the detector handles better.

## Related Mitigations

- [[mitigations/Supplement DCNN covert-channel detection with firewall log-verbosity and multi-scan correlation indicators of compromise]]

## Used By

- [[techniques/Detect port-scan covert-channel steganography using a transfer-learned DCNN classifier]]

## References

- [LWCite-1286] Lamshöft, Neubert, Hielscher, Vielhauer and Dittmann, 2022, "Knock, knock, log: Threat analysis, detection & mitigation of covert channels in syslog using port scans as cover", DFRWS 2022 EU; FSI: Digital Investigation 40, 301335.
