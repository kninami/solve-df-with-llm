---
id: DFW-2067
type: weakness
name: Absence of stored CSEM files does not indicate absence of CSEM viewing or consumption
description: A substantial minority of CSEM offenders self-report never storing material at all and only viewing it, meaning the breadth and quantity of stored images/videos recovered from a device is not a reliable measure of the actual extent of an individual's CSEM consumption, and a device search that finds no stored CSEM files does not establish that no viewing occurred.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-2068
source_refs:
  - DFCite-2071
updated_at: 2026-08-15
status: complete
---

# Absence of stored CSEM files does not indicate absence of CSEM viewing or consumption

## Summary

19% of surveyed previously convicted CSEM offenders reported not storing CSEM at all, having only viewed it, and the study's authors explicitly conclude that "the breadth and quantity of images and videos found are not an accurate measure of the actual content consumption behaviour for a substantial proportion of respondents," further noting that "expecting the presence of images and videos to confirm illegal activity is therefore neither sufficient nor should it be necessary to determine consumption." As bandwidth increases and content persistence for on-demand availability continues, the authors anticipate viewing-without-storage may become increasingly common.

## Why It Matters

An investigator or examiner who treats the absence of recovered stored CSEM files as evidence that no offense occurred, or who scopes an examination around locating stored files as the primary success criterion, risks both under-collecting evidence (missing viewing-only activity captured in browser cache, history, or network artifacts rather than stored files) and misinterpreting a negative stored-file result as exculpatory when it is not — a determination the source study explicitly warns against making.

## Related Mitigations

- [[mitigations/Examine browser cache, history, and network artifacts for CSEM viewing evidence even when no stored files are found]]

## Used By

- [[techniques/Anticipate common CSEM-offender technical countermeasures during a forensic examination]]

## References

- [DFCite-2071] Steel, Newman, O'Rourke & Quayle, 2022, "Technical Behaviours of Child Sexual Exploitation Material Offenders", JDFSL 17(2). States that 19% of respondents reported viewing only, and explicitly warns that expecting stored images/videos to confirm illegal consumption "is neither sufficient nor should it be necessary."
