---
id: LWM-2063
type: mitigation
name: Corroborate WHOIS-IP-derived phishing infrastructure information with independent leads before treating it as attacker identity
source_refs:
  - LWCite-2064
updated_at: 2026-08-15
status: complete
---

# Corroborate WHOIS-IP-derived phishing infrastructure information with independent leads before treating it as attacker identity

## Summary

Treat WHOIS/IP registrant and hosting-provider information recovered for a phishing site as a lead to be corroborated, not as confirmed identification of the attacker; pursue it through the hosting provider's own logs and legal process, and cross-check it against other independent evidence before naming a suspect or presenting the information as attacker identity.

## Addresses

- [[weaknesses/WHOIS-IP-based attribution of a phishing website identifies its hosting infrastructure, not necessarily the actual attacker]]

## How To Apply

Document WHOIS/IP results explicitly as "hosting infrastructure information" in case notes and reports rather than as attacker identity, and follow up with the hosting provider (via subpoena or mutual legal assistance where the host is in another jurisdiction) to obtain the actual customer/account details, connection logs, and payment records behind the IP allocation. Cross-reference any name or account surfaced this way against independent evidence — such as the recovered phishing site's own log file (see [[techniques/Recover a phishing website's captured victim data and server-side artifacts by mirroring its file structure]]), payment/exfiltration destinations, or other case artifacts — before concluding the registrant or hosting customer is the person who actually operated the phishing campaign, since bulletproof hosts, resellers, and compromised third-party systems are common in this space.

## References

- [LWCite-2064] Kara, 2021, "Don't Bite the Bait: Phishing Attack for Internet Banking (E-Banking)", JDFSL 16(5). Frames its own WHOIS/IP-lookup results as information "thought to belong to the attacker" rather than confirmed identity, implicitly recommending the cautious treatment this mitigation makes explicit.
