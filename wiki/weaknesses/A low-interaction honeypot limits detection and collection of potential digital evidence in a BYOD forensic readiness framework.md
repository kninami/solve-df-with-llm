---
id: LWW-2061
type: weakness
name: A low-interaction honeypot limits detection and collection of potential digital evidence in a BYOD forensic readiness framework
description: A BYOD digital forensic readiness framework built around a single low-interaction honeypot (a simulated system with limited services) cannot capture or identify novel or advanced attack techniques, including zero-day exploits, restricting the security incidents it can detect and the potential digital evidence it can collect.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2062
source_refs:
  - LWCite-2063
updated_at: 2026-08-15
status: complete
---

# A low-interaction honeypot limits detection and collection of potential digital evidence in a BYOD forensic readiness framework

## Summary

An earlier honeyd-based BYOD digital forensic readiness model relied on a single low-interaction honeypot as its decoy agent to collect potential digital evidence (PDE). Low-interaction honeypots simulate services rather than providing full systems for an attacker to exploit, so they cannot capture or identify new exploits such as zero-day attacks, and are also comparatively easy for advanced or skilled attackers to detect and avoid. The result is a structural gap between the framework's ISO/IEC 27043-aligned evidence-collection goals and what a low-interaction-only deployment can actually observe.

## Why It Matters

If an organization deploys BYOD forensic readiness tooling that relies solely on low-interaction honeypots, it may develop a false sense of security-incident coverage: sophisticated attackers who recognize or route around the simulated services will neither be detected nor leave PDE behind, meaning the most consequential intrusions (rather than routine, easily-simulated ones) are exactly the kind most likely to go unrecorded.

## Related Mitigations

- [[mitigations/Combine low- and high-interaction honeypots in a BYOD forensic readiness deployment]]

## Used By

- [[techniques/Assess and design for digital forensic readiness]]

## References

- [LWCite-2063] Asante & Amankona, 2021, "Digital Forensic Readiness Framework Based on Honeypot and Honeynet for BYOD", JDFSL 16(2). States that low-interaction honeypots "do not allow the capturing or identification of new exploits such as zero-day attacks" and identifies this as the limitation of the prior honeyd-based BYOD DFR model this paper improves on.
