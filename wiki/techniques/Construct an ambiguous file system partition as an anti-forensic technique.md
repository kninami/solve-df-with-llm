---
id: LWT-1068
type: technique
name: Construct an ambiguous file system partition as an anti-forensic technique
description: Construct a single file system partition that contains two fully functional, independently-parseable file systems at once — a "host" file system whose structures are recognized normally, and a "guest" file system integrated into regions the host considers unused or reusable (e.g. sparse regions, unused metadata fields, or areas the host will not overwrite under normal use) — so that different forensic tools or manual analyses can disagree about, or entirely miss, part of the partition's actual content depending on which file system they parse.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1073
aliases:
  - Ambiguous file system partition construction as an anti-forensic technique
source_refs:
  - LWCite-1063
updated_at: 2026-08-10
status: complete
---

# Construct an ambiguous file system partition as an anti-forensic technique

## Summary

Unlike steganography, an ambiguous file system partition has no distinction between "cover" and "hidden" content and requires no decoding step to access the guest data — both file systems are fully functional and directly mountable/parseable on their own terms. Because typical file systems encountered in forensic analysis are normally unambiguous, a deliberately constructed ambiguous partition is a corner case that can expose gaps in forensic tools that assume a partition contains exactly one file system.

## Details

The paper demonstrates the construction is achievable in practice by integrating a fully functional FAT32 guest file system into the structures of an Ext3 host and, separately, into an HFS+ host, and by integrating two guest file systems (HFS+ and FAT32) simultaneously into a single Btrfs host partition. Testing common forensic tools against these constructed examples exposed deficiencies: tools tuned to recognize only the host (or only the guest) file system's signatures and structures can miss the other file system's content entirely, or misreport the partition's actual contents. The authors develop a taxonomy of ambiguous file system partitions and note that complete ambiguity is not achievable in every case: essential structural data for a file system type still tends to occur at fixed, predictable positions, which can be used heuristically to reduce (though not eliminate) the ambiguity and distinguish a likely host from a likely guest.

## Examples

- A FAT32 file system was integrated into the free-space and metadata structures of an Ext3 partition such that both file systems remained independently mountable and functional, and common forensic tools tested against the resulting image failed to surface one of the two file systems' content.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Forensic tools parsing an ambiguous partition detect only one embedded file system, missing the other's content]]

## References

- [LWCite-1063] Schneider et al., 2022, "Ambiguous file system partitions", FSI: Digital Investigation 42.
