---
id: LWT-2069
type: technique
name: Acquire cross-border cloud evidence using a Budapest Convention Article 32 lawful-access basis
description: Determine and document the specific lawful basis for accessing cloud-stored digital evidence located in another jurisdiction before acquiring it — either mutual legal assistance/a formal cooperation instrument (e.g. a European Investigation Order), or one of the Council of Europe Cybercrime Convention's two recognized direct-access exceptions (the data is publicly available, or a person legally authorized to disclose it has given voluntary consent) — rather than assuming remote search authority the investigator does not actually have.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-2069
aliases:
  - Cross-border cloud evidence acquisition legal-basis determination
source_refs:
  - LWCite-2073
updated_at: 2026-08-15
status: complete
---

# Acquire cross-border cloud evidence using a Budapest Convention Article 32 lawful-access basis

## Summary

Before an investigator or prosecutor attempts to secure digital evidence stored on a server located outside their national jurisdiction, the applicable lawful basis must be identified and documented. Absent a mutual legal assistance request, a European Investigation Order, or another formal cross-border cooperation instrument, the Council of Europe's Cybercrime Convention (Budapest Convention, CETS No. 185) recognizes only two exceptions permitting direct access to data stored abroad without the other state's prior consent: the data is publicly available (open-source), or a person who has the lawful authority to disclose the data has given voluntary, legally effective consent.

## Details

Formal cross-border cooperation channels include mutual legal assistance requests (the traditional but often slow and resource-intensive route), a European Investigation Order (within the EU), and the Cybercrime Convention's 24/7 contact-point network, which is intended to enable urgent preservation requests and technical consultation between national points of contact without going through a full mutual legal assistance process. Where these formal channels are impractical for the case's urgency, the two Article 32 exceptions are the only recognized direct-access routes: public availability (e.g., data openly accessible on the internet without authentication) and voluntary lawful consent (e.g., a cloud account holder or another person legally entitled to disclose the account's contents agrees to provide access or credentials). Neither exception authorizes a unilateral remote search of a foreign-hosted system, and neither exception is satisfied merely because a service provider's login interface happens to be reachable from the investigator's own jurisdiction. This technique complements broader multi-source cloud/IoT acquisition guidance, such as [[techniques/Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources]], by addressing the specific legal-basis question that must be resolved before any cross-border cloud-API or remote-access acquisition step is legally sound.

## Examples

- A prosecutor seeking evidence from a cloud account whose provider is headquartered abroad first confirms whether the target data is already publicly accessible (satisfying the public-availability exception) or whether the account holder is willing to voluntarily disclose their credentials or authorize access (satisfying the consent exception); absent either, the prosecutor initiates a mutual legal assistance request or, within the EU, a European Investigation Order, rather than directing police to access the foreign server directly.
- A national Cybercrime Bureau's 24/7 contact point is used to obtain urgent data-preservation assistance from a foreign counterpart authority while a formal mutual legal assistance request is still being prepared, preventing evidence loss during the request's processing time.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Investigators and prosecutors misunderstand the legal basis for remote cross-border access to cloud-stored data]]

## References

- [LWCite-2073] Olber, 2021, "The Survey on Cross-Border Collection of Digital Evidence by Representatives from Polish Prosecutors' Offices and Judicial Authorities", JDFSL 16(3). Source of the Article 32 public-availability/voluntary-consent exception framework, the 24/7 contact-point mechanism, and the survey evidence of practitioner misunderstanding of these bases.
