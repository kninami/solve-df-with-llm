---
id: LWW-2053
type: weakness
name: Drone firmware bundles severely outdated OS kernels with many unpatched known vulnerabilities despite being labeled the latest release
description: A drone's most recently released firmware update can still bundle an operating-system kernel that is years out of date and carries dozens to hundreds of publicly known, unpatched vulnerabilities, and firmware is often distributed via unauthenticated public vendor-website downloads rather than a secure over-the-air update mechanism.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2053
source_refs:
  - LWCite-2054
updated_at: 2026-08-14
status: partial
---

# Drone firmware bundles severely outdated OS kernels with many unpatched known vulnerabilities despite being labeled the latest release

## Summary

The source paper's own firmware analysis found that "the operating system was seriously outdated; however, the version of the operating system is about three years old," even though the extracted firmware was the manufacturer's latest publicly available release, and that this specific Linux kernel version had 192 associated known vulnerabilities (43.8% denial-of-service). The paper separately identifies that "the old-fashioned style of providing firmware to be downloaded from the vendor website is considered a notable threat, which could lead to a targeted cyber attack on these devices," since attackers gain easy access to the full firmware image for reverse engineering or, potentially, distribution of a maliciously modified version.

## Why It Matters

A drone whose firmware runs a heavily outdated, vulnerable OS kernel is exposed to a wide range of known exploitation techniques (particularly denial-of-service), which is directly relevant to a forensic investigator assessing whether a drone's anomalous behavior, crash, or data-integrity issue during operation could be attributable to a cyberattack exploiting a known, unpatched vulnerability rather than mechanical failure or operator error - a distinction that materially affects the investigation's conclusions. This is compounded when the manufacturer distributes firmware over public, unauthenticated channels, since a targeted attacker could substitute a maliciously modified firmware image without the operator's knowledge.

## Related Mitigations

- [[mitigations/Adopt authenticated OTA firmware updates and continuous kernel patching for drone fleets before an incident occurs]]

## Used By

- [[techniques/Assess drone firmware security using static analysis and entropy profiling]]

## References

- [LWCite-2054] Salamh et al., 2021 — Section 4.1 reports the outdated-kernel finding and vulnerability count from the Zino Hubsan firmware analysis, and Section 4.1's discussion identifies public vendor-website firmware distribution as a notable attack vector.
