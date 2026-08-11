---
id: DFT-1047
type: technique
name: Structured open-source intelligence investigation methodology
description: Conduct an Open Source Intelligence (OSINT) investigation as a repeatable, multi-phase process — information needs and strategy, planning and preparation, collection, processing/validation, analysis, and distribution and evaluation — rather than treating OSINT as an unstructured, ad hoc search of public sources such as social media, search engines, and public records.
objective_ids:
  - DFO-1014
weakness_ids:
  - DFW-1048
aliases:
  - OSINT methodology
source_refs:
  - DFCite-1038
updated_at: 2026-08-09
status: complete
---

# Structured open-source intelligence investigation methodology

## Summary

OSINT collects information about people, organizations, and objects from freely available public sources — social media, search engines, public records, news media, and online maps — to support both proactive investigation (before a formal case exists) and reactive case work. Applying it as a structured, repeatable six-phase process, rather than one-off searching, is intended to make the resulting intelligence product more reliable, reproducible, and traceable for investigative and evidentiary purposes.

## Details

Common component techniques include: reviewing and hardening the investigator's own computer/anonymization setup (VPN, Tor, dedicated non-attributable accounts) before beginning; using approved internet browsers with verified, non-modifiable evidence-preservation behavior; creating investigation-specific (non-personal) social media search accounts subject to platform verification requirements; using search-engine operators for targeted queries; reverse image search to identify where/what a photo depicts or to identify an unknown person appearing across multiple online images; and Google Maps/Street View for physical location context (noting that Street View imagery can be several years out of date). These component techniques are meant to be applied within the structured six-phase process (strategy, planning, collection, validation, analysis, distribution) so that findings can be systematically verified and reported, rather than used piecemeal.

## Examples

- Norwegian Police University College's Bachelor of Policing program teaches this methodology and its component techniques (Tor browser, reverse image search, Google Street View, social media search) as part of its Digital Policing and Forensic Science curriculum before students' year of practical training in police districts.

## Related Objectives

- `DFO-1014` Find potential digital evidence sources

## Related Weaknesses

- [[weaknesses/Practicing OSINT investigators execute only the collection phase and skip the methodology's other phases]]

## References

- [DFCite-1038] Larsen et al., 2023, "A quantitative study of the law enforcement in using open source intelligence techniques through undergraduate practical training", FSI: Digital Investigation 47.
