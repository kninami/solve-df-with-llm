---
id: LWT-2067
type: technique
name: Anticipate common CSEM-offender technical countermeasures during a forensic examination
description: Prioritize forensic examination steps based on empirically documented base rates of the technical countermeasures previously convicted child sexual exploitation material (CSEM) offenders self-report using, rather than assuming encryption is the primary obstacle or that a single storage location captures the full extent of an offender's activity.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2067
aliases:
  - CSEM offender countermeasure base-rate profiling
source_refs:
  - LWCite-2071
updated_at: 2026-08-15
status: complete
---

# Anticipate common CSEM-offender technical countermeasures during a forensic examination

## Summary

A self-report survey of previously convicted CSEM offenders quantified which technical countermeasures they actually used, at what rate, and why, providing an empirical base-rate profile an investigator can use to prioritize what to specifically check for during an examination rather than treating all possible countermeasures as equally likely.

## Details

Among previously convicted CSEM offenders, the most common countermeasures were low-technical-sophistication actions rather than encryption: deletion of web browsing history (68%), use of peer-to-peer software (63%, itself both an acquisition method and a countermeasure against direct-download traceability), In-Private/incognito browsing (38%), hard-drive formatting (31%), secure-wiping software (31%), mislabeling a directory or storage device to disguise its contents (28%), individual-file encryption (18%), VPN usage (15%), Tor/dark-web access (22%), fake-name email accounts (13%), and whole-disk encryption (8%) — notably, encryption usage was not statistically higher in the CSEM-offender group than in a general-population reference group, meaning encryption should not be assumed to be the primary technical obstacle in a typical case. The most common gateway and overall-usage technologies were peer-to-peer software and traditional (open) websites rather than the dark web, and most offenders who used multiple technologies over time transitioned between the two lowest-barrier-to-entry ecosystems (web browsing and peer-to-peer) rather than escalating directly to more technically sophisticated platforms. This base-rate profile complements targeted examination techniques such as [[techniques/Recover hidden photos from an iOS vault application's residual artifacts]] and general anti-forensic-detection practice by indicating where examination effort is statistically most likely to pay off.

## Examples

- Given that mislabeled directories were self-reported by 28% of CSEM offenders as a storage countermeasure, an examiner can prioritize checking for directories with names inconsistent with their actual contents (verified by file signature/content rather than by name or extension) as a specifically likely evasion pattern, rather than a generic, low-priority possibility.
- Given that encryption usage was not elevated relative to the general population, an examiner should not assume an encrypted volume necessarily indicates deliberate CSEM concealment specifically, nor conclude that an unencrypted device is unlikely to contain CSEM.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Absence of stored CSEM files does not indicate absence of CSEM viewing or consumption]]

## References

- [LWCite-2071] Steel, Newman, O'Rourke & Quayle, 2022, "Technical Behaviours of Child Sexual Exploitation Material Offenders", JDFSL 17(2). Source of the self-reported countermeasure base rates, gateway/transition technology patterns, and storage-rationale findings.
