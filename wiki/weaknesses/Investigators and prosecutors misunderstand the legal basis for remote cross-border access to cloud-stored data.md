---
id: LWW-2069
type: weakness
name: Investigators and prosecutors misunderstand the legal basis for remote cross-border access to cloud-stored data
description: A substantial proportion of surveyed prosecutorial and judicial representatives incorrectly believed police have procedural authority to remotely search foreign-hosted IT resources or that searching a foreign-operated web-based email inbox is legally permitted, and many representatives directed police to secure data from foreign servers directly as part of routine procedural activities despite lacking the legal basis to do so.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-2070
source_refs:
  - LWCite-2073
updated_at: 2026-08-15
status: complete
---

# Investigators and prosecutors misunderstand the legal basis for remote cross-border access to cloud-stored data

## Summary

A survey of 138 Polish prosecutorial and judicial representatives found that 33.3% of court employees and 22.4% of prosecutorial employees incorrectly believed Polish police have procedural rights to remotely search foreign-hosted IT resources and acquire digital evidence this way — a belief the paper states is wrong, since Polish legislators have never passed laws enabling remote search of IT systems located abroad. Similarly, 51.7% of prosecutorial employees and 32.1% of court employees incorrectly believed it is legal to search the content of an email inbox operated by a foreign provider via a web browser, when in fact this also does not comply with applicable legal regulations without a proper legal basis. Separately, the survey found that lack of knowledge about the correct legal basis was itself a leading cause of representatives commissioning police to secure data on foreign servers directly, as part of ordinary procedural activities (most often framed as a "search of an IT system"), even though the applicable legal regulations do not permit this without international legal assistance.

## Why It Matters

Evidence acquired on a mistaken belief that remote cross-border access was legally authorized risks being ruled improperly obtained and excluded from proceedings, undermining the case built on it; more broadly, systemic misunderstanding of the legal basis among the people directing evidence-collection activities (not just the technicians executing them) means the error can recur across many cases rather than being a one-off mistake, and the resulting delay or invalidation directly harms the timeliness and completeness of digital evidence available to the investigation.

## Related Mitigations

- [[mitigations/Train prosecutors and investigators on the Article 32 lawful-access exceptions and cross-border cooperation channels before cloud evidence acquisition]]

## Used By

- [[techniques/Acquire cross-border cloud evidence using a Budapest Convention Article 32 lawful-access basis]]

## References

- [LWCite-2073] Olber, 2021, "The Survey on Cross-Border Collection of Digital Evidence by Representatives from Polish Prosecutors' Offices and Judicial Authorities", JDFSL 16(3). Reports the specific percentages of surveyed representatives holding each incorrect legal belief, and states that Polish police "should not conduct" remote search activities police were nonetheless commissioned to perform.
