---
id: DFW-1073
type: weakness
name: Forensic tools parsing an ambiguous partition detect only one embedded file system, missing the other's content
description: When a single partition is deliberately constructed to contain two fully functional file systems (a host and a hidden guest), common forensic tools tested against such partitions exhibit deficiencies — recognizing and reporting only the file system their parser targets while missing the other file system's content entirely, rather than flagging the partition as ambiguous or containing unexplained additional structure.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1073
source_refs:
  - DFCite-1063
updated_at: 2026-08-10
status: complete
---

# Forensic tools parsing an ambiguous partition detect only one embedded file system, missing the other's content

## Summary

The authors constructed ambiguous partitions (FAT32 integrated into Ext3 or HFS+ hosts, and HFS+ plus FAT32 both integrated into a single Btrfs host) and tested common forensic tools against them, exhibiting deficiencies: tools that recognize the host file system's structures do not report the presence of the fully functional guest file system coexisting within the same partition, and vice versa for tools that happen to recognize the guest's signatures instead.

## Why It Matters

Because ambiguous partitions are a corner case rather than something that occurs naturally, their existence specifically threatens investigations where a sophisticated adversary has deliberately hidden a second, fully functional file system inside an ostensibly ordinary partition — a forensic examiner who trusts a single tool's report of "this partition contains file system X" may never learn that a second, independently mountable file system Y was also present and unreported.

## Related Mitigations

- [[mitigations/Heuristically check for essential file-system structural data at unexpected fixed positions to flag possible ambiguous partitions]]

## Used By

- [[techniques/Ambiguous file system partition construction as an anti-forensic technique]]

## References

- [DFCite-1063] Schneider et al., 2022, "Ambiguous file system partitions", FSI: Digital Investigation 42.
