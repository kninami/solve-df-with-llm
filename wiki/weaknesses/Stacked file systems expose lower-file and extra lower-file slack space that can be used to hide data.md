---
id: LWW-1223
type: weakness
name: Stacked file systems expose lower-file and extra lower-file slack space that can be used to hide data
description: Because some stacked file systems align lower files to a fixed extent size or maximum chunk size, or allow arbitrary bytes to be appended directly past a lower file's logical end, data can be concealed in the resulting slack space without altering the upper file's displayed size or accessibility, in ways specific to each stacked file system's implementation.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1223
source_refs:
  - LWCite-1234
updated_at: 2026-08-13
status: complete
---

# Stacked file systems expose lower-file and extra lower-file slack space that can be used to hide data

## Summary

Experiments hiding data within stacked file systems found up to 64 KiB of usable lower-file slack per MooseFS chunk (between the block-aligned content and the CRC-checksum footer) and roughly 4 KiB of usable lower-file slack in eCryptfs's default 4 KiB extent padding, plus additional "extra lower file slack" that can be appended directly past a lower file's logical content in both MooseFS and eCryptfs without the upper file's size or accessibility changing; GlusterFS's distributed/replicated modes use no padding at all and so offer none of this concealment opportunity, while its dispersed (erasure-coded) mode has slack whose safe-to-use position and amount depends on the specific erasure-coding parameters.

## Why It Matters

Because upper-file-system-level tools only see the upper file's own reported size and content, they will not by themselves reveal data hidden in a lower file's slack or appended past its logical end; an examiner who does not separately compare an upper file's size against the sizes of its corresponding lower files, or who does not check for data beyond the last block boundary MooseFS's or eCryptfs's own algorithms would ever legitimately write, can overlook a viable and, for at least MooseFS and eCryptfs, non-trivially-sized data-hiding channel.

## Related Mitigations

- [[mitigations/Compare upper file sizes against their corresponding lower file sizes to detect data hidden in stacked-file-system slack space]]

## Used By

- [[techniques/Analyze a stacked file system by correlating its upper and lower file-system layers]]

## References

- [LWCite-1234] Hilgert, Lambertz and Baier, 2024, "Forensic implications of stacked file systems", DFRWS EU 2024; FSI: Digital Investigation 48, 301678.
