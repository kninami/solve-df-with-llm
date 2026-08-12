---
id: DFW-1053
type: weakness
name: Domain-specific cyber-threat ontologies require continuous manual updates to remain current
description: A domain-specific cyber-threat and evidence ontology's coverage is fixed at the point it was authored; because the underlying technology domain (e.g., smart city infrastructure) continues to evolve with new threats, device types, and attack techniques, the ontology can only remain accurate and useful through ongoing, manually intensive literature review and expert engagement to identify and add new concepts.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1053
source_refs:
  - DFCite-1043
updated_at: 2026-08-09
status: complete
---

# Domain-specific cyber-threat ontologies require continuous manual updates to remain current

## Summary

The authors state this limitation directly: "SCOPE only covers cybercrime in SCI. It thus may lack particular definitions found in other scenarios... as SCI is a continuously developing field with constant progress in cybersecurity. We can mitigate these issues by conducting extensive and in-depth literature reviews, engaging with experts in the domain to ensure proper coverage as well as continuous and iterative updating." This mirrors a broader pattern seen in the field: earlier general-purpose ontologies (UCO, CASE) similarly required ongoing extension work precisely because they lacked coverage for a newer domain (smart city infrastructure) when it emerged.

## Why It Matters

An investigator relying on a domain-specific ontology to identify all applicable threats, cybercrime classifications, or evidence types for a given infrastructure component may receive an incomplete answer if the ontology has not been updated to reflect a newly emerged threat, device category, or attack technique in that domain, without any signal from the tool that its coverage is out of date. Because the underlying domain evolves faster than any single publication cycle, this is an ongoing maintenance burden rather than a one-time completeness gap.

## Related Mitigations

- [[mitigations/Establish a scheduled review process for domain-specific ontology coverage]]

## Used By

- [[techniques/Map cyber threats and evidence using a domain-specific infrastructure ontology]]

## References

- [DFCite-1043] Tok et al., 2025, "A Smart City Infrastructure ontology for threats, cybercrime, and digital forensic investigation", FSI: Digital Investigation 52.
