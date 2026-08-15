---
id: DFT-2009
type: technique
name: Reconstruct a data breach using data-breach-breakdown-phase chain-of-artifacts analysis
description: The process of investigating a data breach by categorizing evidence sources (host, network device, security device), mapping each discovered artifact to one of four data-breach-breakdown phases (infiltration, propagation, aggregation, exfiltration), correlating them into a chronological chain of artifacts, and mapping the resulting timeline and attack-flow analysis onto the 5WH (what/who/when/where/why/how) investigative questions.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-2009
aliases:
  - Data Breach Breakdown (DBB) framework
  - Chain of Artifacts (CoA) analysis for data breach investigation
source_refs:
  - DFCite-2009
updated_at: 2026-08-14
status: partial
---

# Reconstruct a data breach using data-breach-breakdown-phase chain-of-artifacts analysis

## Summary

An investigator responding to a suspected data breach classifies the organization's evidence sources into hosts, network devices, and security devices based on the network architecture, then examines each source for artifacts and assigns each artifact found to one of four Data Breach Breakdown (DBB) phases: infiltration (how the attacker gained access), propagation (how the attacker moved to the targeted data/system), aggregation (how the attacker accessed/harvested the target), and exfiltration (how the attacker moved the data out). The artifacts are linked into a Chain of Artifacts (CoA), timestamped for a timeline, and analyzed for the step-by-step attack flow, with the combined findings mapped directly onto the 5WH investigative questions.

## Details

DFCite-2009 structures content analysis as an iterative loop: identify the evidence source implicated by current trigger information (e.g. an indicator of compromise) using the host/network-device/security-device categorization and knowledge of the network architecture, extract relevant artifacts, map each to a single DBB phase, and repeat using newly found artifacts as trigger information for the next iteration until all four phases have a complete, correlated set of artifacts. The CoA is represented as a four-dimensional array (or equivalently a graph/linked-list) grouping artifacts by DBB phase while preserving cross-phase correlation links (e.g. shared timestamps, IPs, or process names). A fixed mapping table (5WH question -> which framework step answers it) then lets the investigator directly derive what was breached, who was involved, when, where the data resided, why the breach occurred, and how the attack unfolded, rather than reconstructing these answers ad hoc.

## Examples

- DFCite-2009's case study of a 300-employee food-processing company breached via spear phishing, a Zerologon (CVE-2020-1472) domain-admin privilege escalation, Mimikatz Golden Ticket / pass-the-ticket lateral movement, and exfiltration of file-server contents via a compressed RAR archive — fully answered via the framework's 5WH mapping in Table 8.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Forcing each data-breach artifact into a single DBB phase can misrepresent artifacts that span multiple attack phases]]

## References

- [DFCite-2009] Hakim et al., "A novel digital forensic framework for data breach investigation", IEEE Access, 2023 — source of the DBB-phase framework, Chain of Artifacts structure, and 5WH mapping table.
