---
id: DFT-1116
type: technique
name: Acquire and preserve virtual host images across multiple cloud providers using a unified API workflow
description: Acquire snapshot/image copies of a case's virtual hosts (servers, databases) directly through each cloud service provider's own official API — abstracted behind a single API-operation library so the same forensic workflow controls AWS, Aliyun, ZStack, or other CSPs interchangeably — then hash-verify and transfer the images into a separate, access-controlled preservation cloud, tracking every image, snapshot, and piece of evidence through a file-traceability database so each can be traced back to its source and the investigator who handled it.
objective_ids:
  - DFO-1006
  - DFO-1010
weakness_ids:
  - DFW-1122
aliases:
  - CETS
  - Cloud Evidence Tracing System
source_refs:
  - DFCite-1116
updated_at: 2026-08-12
status: complete
---

# Acquire and preserve virtual host images across multiple cloud providers using a unified API workflow

## Summary

When case-relevant virtual hosts are deployed across multiple public cloud platforms (a hybrid or multi-CSP setup), traditional physical-preservation-based forensics does not scale, and each CSP's own control API differs in naming, parameters, and operation order. Structuring acquisition as a library of per-CSP API operation sequences behind a common control-module interface lets the same forensic workflow — obtain access, generate/export a live image or snapshot, hash and transfer it into a dedicated preservation cloud — be applied consistently regardless of which CSP hosts the target.

## Details

The workflow (adapted from the ISO/IEC 27043 Harmonized Digital Investigation Model) splits into acquisitive procedures (allowance/authorization, identification, collection, and acquisition of virtual host images and configuration) and a separated conservation/preservation procedures class (verification, marking with a case-linked version code, transportation, and redundant storage). Because the underlying APIs used (e.g. AWS/Aliyun `DescribeInstances`, `CreateImage`, `ExportImage`; ZStack `AddImage`) are each CSP's own official, documented API, only the operation sequencing and translation layer needs to be built and maintained per CSP, not a custom in-guest or hypervisor-level agent — avoiding the heavier CSP-cooperation burden of prior frameworks like FROST (which required the CSP to modify its own OpenStack deployment). A six-table file-traceability database (case, image, snapshot, evidence, operation, and report tables, cross-referenced by ID) records every intermediate file and the investigator action that produced it, so a piece of evidence cited in the final report can be traced back through its specific snapshot version to the original acquired image and the login/operation record that created it — addressing the evidence-management complexity created by a single case routinely spanning multiple images, multiple snapshot versions per image, and multiple evidence items per snapshot. Deployed operationally, the system reported acquiring over 2PB of case data and supporting 300+ cases across AWS, Aliyun, and ZStack.

## Examples

- In a cyber-attack case against a university, two compromised servers totaling 52GB were imaged and preserved through the CETS workflow after the university (as target owner) authorized the acquisition, with each resulting evidence item traceable through the file-traceability database back to its source snapshot and image.

## Related Objectives

- `DFO-1006` Acquire data
- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/API-based cloud host acquisition depends on cooperative authorization from the target owner or CSP]]

## References

- [DFCite-1116] Wu et al., 2022, "Cloud Evidence Tracing System: An integrated forensics investigation system for large-scale public cloud platform", FSI: Digital Investigation 41.
