---
id: DFW-1239
type: weakness
name: Family-specific generic YARA signatures for IoT botnets fail to detect other unrelated botnet families
description: A generic YARA rule-set built from the shared behavioral patterns of one IoT botnet family's variants detects that family well but generalizes poorly to a different, unrelated botnet family, since the two families' underlying source code, control commands, and obfuscation methods diverge even though both are classified as IoT botnets.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1240
source_refs:
  - DFCite-1254
updated_at: 2026-08-13
status: complete
---

# Family-specific generic YARA signatures for IoT botnets fail to detect other unrelated botnet families

## Summary

A Mirai-specific generic rule-set, built to detect any variant within the Mirai family, achieved only 1.74% detection when tested against Qbot samples — a different IoT botnet family. The reverse cross-family test showed the same pattern: a Qbot-specific generic rule-set achieved only 35.88% detection against IRC-Bot samples and 25% against TrickBot samples. Even the broader, combined IoT-Botnet Generic Rule-Set — built by merging patterns from both Mirai and Qbot — still fell short of 100% detection against further unrelated families tested (98% for IRC-Bot, 96.79% for Perl-ShellBot, 98.2% for TrickBot), meaning some samples of each unrelated family are still missed.

## Why It Matters

An investigator or defender who deploys a generic YARA rule-set developed for one IoT botnet family may substantially overestimate its coverage against the broader IoT botnet threat landscape, since a rule-set's high detection rate against its own family's variants does not predict its performance against a structurally unrelated family. New or emerging IoT botnet families not represented in the source families analyzed to build a rule-set are especially likely to be missed entirely.

## Related Mitigations

- [[mitigations/Combine multiple family-specific generic YARA rule-sets and periodically extend coverage to newly identified botnet families]]

## Used By

- [[techniques/Develop generic YARA signatures for an IoT botnet family using static code analysis]]

## References

- [DFCite-1254] Abbas et al., 2021, "Generic signature development for IoT Botnet families", FSI: Digital Investigation 38, 301224.
