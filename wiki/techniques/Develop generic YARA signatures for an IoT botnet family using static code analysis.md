---
id: DFT-1223
type: technique
name: Develop generic YARA signatures for an IoT botnet family using static code analysis
description: Manually reverse-engineer and statically compare the source code of multiple variants within an IoT botnet family (e.g. Mirai or Qbot) to identify behavioral patterns common across variants — CPU-architecture targeting, bot control commands, scanning commands, obfuscation methods, and family-specific exploits — then encode those shared patterns as generic YARA rules that detect unseen variants of the family rather than only the specific samples analyzed.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1239
aliases:
  - IoT-Botnet Generic Rule-Set
  - Generic IoT botnet signature development
source_refs:
  - DFCite-1254
updated_at: 2026-08-13
status: complete
---

# Develop generic YARA signatures for an IoT botnet family using static code analysis

## Summary

Publicly released IoT botnet source code (e.g. Mirai's) lets adversaries rapidly produce new variants that evade signatures written against only the original samples. Manually analyzing the source code of several known variants within one botnet family to identify the behavioral patterns that persist across all of them — rather than signatures tied to one variant's specific strings or hashes — produces a generic rule-set that generalizes to variants not directly analyzed, including future ones that share the family's core design.

## Details

Static code analysis of each variant's source extracts the attacker's perspective across several categories: targeted CPU architectures, the specific commands used to control infected bots, scanning/propagation commands used to find new victims, obfuscation methods applied to hide the malware's behavior, and family-specific exploits or default-credential lists used for initial compromise. Patterns that recur across multiple variants of the same family are encoded as YARA rule conditions (text strings, hexadecimal strings, and regular expressions matched against a sample), producing a rule-set scoped to that family rather than to any single variant. The same process, repeated across families that share a lineage or common design influences (e.g. Qbot's own codebase overlap with Mirai-derived botnets), can also reveal cross-family detection opportunities, though a rule-set built for one family's patterns generally does not transfer well to an unrelated family.

## Examples

- Static analysis of 17 Mirai and Qbot variants produced family-specific generic rule-sets that, when tested against variants not used to build them, achieved 100% detection for both the Mirai and Qbot generic rule-sets on their respective families.
- A combined IoT-Botnet Generic Rule-Set, merging patterns identified across both families, was then tested against three further, previously unseen IoT botnet families (IRC-Bot, Perl-ShellBot, and TrickBot) and achieved detection rates of 98%, 96.79%, and 98.2% respectively.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Family-specific generic YARA signatures for IoT botnets fail to detect other unrelated botnet families]]

## References

- [DFCite-1254] Abbas et al., 2021, "Generic signature development for IoT Botnet families", FSI: Digital Investigation 38, 301224.
