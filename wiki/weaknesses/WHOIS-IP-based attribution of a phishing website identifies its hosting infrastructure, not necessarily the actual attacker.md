---
id: DFW-2062
type: weakness
name: WHOIS-IP-based attribution of a phishing website identifies its hosting infrastructure, not necessarily the actual attacker
description: A WHOIS/IP lookup of a phishing site's hosting IP returns the registrant, network operator, or hosting-provider contact for that infrastructure, which is frequently a bulletproof host, reseller, or compromised third party rather than the individual who actually operated the phishing campaign, risking misattribution if treated as direct identification of the attacker.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-2063
source_refs:
  - DFCite-2064
updated_at: 2026-08-15
status: complete
---

# WHOIS-IP-based attribution of a phishing website identifies its hosting infrastructure, not necessarily the actual attacker

## Summary

The case study's own reporting is careful to describe the WHOIS/IP-derived registrant and network information only as data "thought to belong to the attacker," rather than confirmed attacker identity — a deliberate hedge that reflects a structural limitation of the method: WHOIS and IP-intelligence records describe who registered or operates the hosting infrastructure, which is commonly a hosting provider, reseller, proxy, or an unrelated compromised system, not necessarily the individual who built and operated the phishing content.

## Why It Matters

Treating a WHOIS/IP hit as if it were the attacker's identity risks pursuing legal process against, or drawing conclusions about, a hosting provider or an unrelated compromised party rather than the actual operator of the phishing campaign, which can misdirect an investigation, waste investigative resources, and — if presented in a report or testimony without appropriate caveats — create a misleading association between the infrastructure record and the true perpetrator.

## Related Mitigations

- [[mitigations/Corroborate WHOIS-IP-derived phishing infrastructure information with independent leads before treating it as attacker identity]]

## Used By

- [[techniques/Recover a phishing website's captured victim data and server-side artifacts by mirroring its file structure]]
- [[techniques/Attribute a phishing website's hosting infrastructure using WHOIS and IP lookup]]

## References

- [DFCite-2064] Kara, 2021, "Don't Bite the Bait: Phishing Attack for Internet Banking (E-Banking)", JDFSL 16(5). Repeatedly describes the WHOIS/IP-derived information as data "thought to belong to the attacker" rather than confirmed attacker identity.
