---
id: LWW-2055
type: weakness
name: PII recovered from a used mobile device may belong to a previous owner rather than the current possessor
description: A substantial share of secondhand or previously-owned mobile devices still contain personally identifiable information belonging to a prior owner who made no attempt to remove it, so recovering identity-revealing content from a device does not by itself establish that this content belongs to the device's current possessor.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-2055
source_refs:
  - LWCite-2056
updated_at: 2026-08-14
status: partial
---

# PII recovered from a used mobile device may belong to a previous owner rather than the current possessor

## Summary

The source study found that of the 100 secondhand devices purchased, PII was retrievable and could fully identify the previous owner for 17% of the total sample, and that "in most cases, there had been no attempt to remove it" - five of the seventeen data-containing devices "appeared to have simply been switched off before selling them, with no encryption method activated and no security settings to prevent anyone from accessing the personal information." Multiple documented case examples recovered full names, home addresses, financial/bank details, contacts, browsing history, and thousands of photos belonging to a device's previous owner, entirely intact and readily accessible without specialist techniques.

## Why It Matters

An investigator examining a device of uncertain provenance - whether purchased secondhand as part of a sting operation, seized from a suspect who may have acquired it used, or recovered from an unknown source - risks misattributing recovered PII to the device's current possessor when it in fact belongs to an earlier owner who never wiped the device. Because the study found this discoverable identity information "readily available... without the use of specialized tools" in many cases, even a cursory examination could produce misleading identity-attribution conclusions unless the investigator actively checks for and rules out prior-ownership explanations.

## Related Mitigations

- [[mitigations/Corroborate device-recovered PII against independent evidence of current ownership before attributing it to a suspect]]

## Used By

- [[techniques/Recover personally identifiable information from a used mobile device using logical acquisition with manual fallback]]

## References

- [LWCite-2056] Angelopoulou et al., 2022 — Section 5 "Results" and Section 6 "Case Studies" document the 17% previous-owner-identifiable rate and multiple specific cases of fully recoverable prior-owner PII with no removal attempt.
