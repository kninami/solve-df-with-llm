---
id: DFT-2062
type: technique
name: Attribute a phishing website's hosting infrastructure using WHOIS and IP lookup
description: Resolve a suspect phishing website's domain to its hosting IP address, then query a WHOIS/IP-intelligence service for that IP's registrant, network, and abuse-contact information, as a step toward reaching whoever operates or controls the infrastructure behind the phishing attack.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-2062
aliases:
  - Domain/IP WHOIS attribution of phishing infrastructure
source_refs:
  - DFCite-2064
updated_at: 2026-08-15
status: complete
---

# Attribute a phishing website's hosting infrastructure using WHOIS and IP lookup

## Summary

After confirming a phishing site's domain, resolve the domain to the IP address it is actually hosted at and submit that IP to a WHOIS/IP-intelligence lookup service to retrieve registrant, network block, hosting provider, and abuse-contact details — information that can be pursued further (e.g., via legal process to the hosting provider) to try to identify who controls the phishing infrastructure.

## Details

Determining the internet subscriber to whom a suspicious IP is assigned is one of the most widely used methods of reaching an attacker in forensic investigations: once the phishing domain's actual hosting IP is identified, a WHOIS/IP-intelligence lookup (e.g., via a domain-and-IP-intelligence service) returns the IP's network block, registrant/organization, and abuse-contact information. This complements [[techniques/Recover a phishing website's captured victim data and server-side artifacts by mirroring its file structure]] as a downstream step once the site's domain and hosting details are known — the mirrored site confirms what data was captured and how, while the WHOIS/IP lookup pursues who is responsible for the infrastructure serving it.

## Examples

- Resolving the phishing domain `isbanh.com` to its hosting IP address and querying it via a WHOIS/IP lookup service surfaced the IP's network block, registrant organization, and abuse-contact details, information that the investigation treated as a lead toward the party responsible for the phishing infrastructure.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/WHOIS-IP-based attribution of a phishing website identifies its hosting infrastructure, not necessarily the actual attacker]]

## References

- [DFCite-2064] Kara, 2021, "Don't Bite the Bait: Phishing Attack for Internet Banking (E-Banking)", JDFSL 16(5). Describes resolving the suspect phishing domain to its hosting IP and querying it via a WHOIS/IP-intelligence lookup service as the method used to reach information "thought to belong to the attacker."
