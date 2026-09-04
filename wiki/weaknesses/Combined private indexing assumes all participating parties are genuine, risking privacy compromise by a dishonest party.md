---
id: LWW-2052
type: weakness
name: Combined private indexing assumes all participating parties are genuine, risking privacy compromise by a dishonest party
description: The combined Soundex-plus-CLK/multibit-tree private indexing method assumes every participating party behaves honestly (semi-honest/genuine), and its privacy guarantees can be jeopardized when a participating party is not genuine, without the base protocol itself detecting or preventing this.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2052
source_refs:
  - LWCite-2053
updated_at: 2026-08-14
status: partial
---

# Combined private indexing assumes all participating parties are genuine, risking privacy compromise by a dishonest party

## Summary

The source paper's own conclusion states plainly: "This system has a disadvantage in that privacy can be jeopardized when some of the parties are not genuine, necessitating more protective safety measures and communication." Like many privacy-preserving record linkage protocols, the combined Soundex/CLK indexing method is designed around a semi-honest threat model where participants follow the protocol correctly but try to learn more than they should from its outputs; it does not itself defend against a genuinely malicious party that deviates from the protocol (e.g. submitting crafted queries, or a compromised participant colluding with an outside adversary) to extract more information than intended.

## Why It Matters

If this method is used to link sensitive investigative records across multiple agencies or organizations, an investigator or data custodian should recognize that the privacy protection it offers depends entirely on every participant genuinely following the protocol; if one participating agency or organization (or an insider within one) is compromised or acting in bad faith, the protective encoding may not prevent the leakage of sensitive underlying identifying information about the individuals whose records are being linked.

## Related Mitigations

- [[mitigations/Vet participant honesty and add protocol-level safeguards before relying on combined private indexing across multiple parties]]

## Used By

- [[techniques/Link records across databases using combined phonetic-encoding and multibit-tree private indexing]]

## References

- [LWCite-2053] Desai and Shelake, 2022 — Section 5 "Conclusion and Future Work" explicitly identifies dishonest participating parties as a disadvantage of the proposed system requiring further protective measures.
