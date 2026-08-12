---
id: DFW-1056
type: weakness
name: ICS project-file monitoring and restoration tooling lacks its own performance and security evaluation
description: Proposed project-file integrity monitoring and restoration tooling for ICS engineering workstations has not itself been evaluated for computational resource overhead, detection/recovery speed, or resistance to an attacker who targets the monitoring tool or its version-history database directly, leaving open whether the tool is practical to run continuously or trustworthy under active attack.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1056
source_refs:
  - DFCite-1046
updated_at: 2026-08-09
status: complete
---

# ICS project-file monitoring and restoration tooling lacks its own performance and security evaluation

## Summary

The authors state this explicitly as future work: "the research does not include performance and security tests for it. If the system impact, performance, and security test results for it are successful, it is thought that it will be very useful in practice. Future studies will be focused on an evaluation of the developed tool's performance using official data, such as its efficiency of computer resources and recovery speed, and its security."

## Why It Matters

A monitoring tool that continuously runs on an ICS engineering workstation could itself introduce unacceptable resource overhead in an environment where availability is paramount, or could become a target: if an attacker sophisticated enough to compromise the EWS can also tamper with or disable the monitoring tool or its version-history database, the detection and restoration capability could be silently defeated without an operator's knowledge. Without a dedicated evaluation of these properties, an organization cannot yet assess whether deploying such a tool is safe or effective for a specific operational environment.

## Related Mitigations

- [[mitigations/Independently validate ICS monitoring tool performance overhead and self-tamper resistance before deployment]]

## Used By

- [[techniques/Monitor and restore ICS project-file integrity continuously]]

## References

- [DFCite-1046] Shin et al., 2022, "A study on command block collection and restoration techniques through detection of project file manipulation on engineering workstation of industrial control system", FSI: Digital Investigation 40.
