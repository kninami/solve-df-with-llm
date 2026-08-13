---
id: DFW-1186
type: weakness
name: A superuser can delete, modify, or disable local logs and services without leaving a local trace
description: An administrator or attacker with superuser (root/administrative) privileges can delete command history and log files, alter log entries to implicate someone else, or disable the logging service and monitoring alerts entirely, and every one of the artifacts that would normally record that activity is itself within the superuser's own privilege domain and can be tampered with by the same access.
categories:
  - ASTM_INCOMP
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1186
source_refs:
  - DFCite-1189
updated_at: 2026-08-13
status: complete
---

# A superuser can delete, modify, or disable local logs and services without leaving a local trace

## Summary

Four documented real-world case types illustrate the range of this problem: deleting shell command history to hide a planted logic bomb; modifying network logs to frame another administrator; disabling monitoring alerts and deleting root passwords to operate undetected; and disabling the system logging service entirely to prevent any log generation in the first place. In each case, the superuser's legitimate administrative access is exactly the access needed to erase, alter, or prevent the evidence of the illicit activity, so an investigation confined to the local system finds nothing anomalous.

## Why It Matters

An investigator who treats a compromised or suspect server's own local logs, command history, and audit trail as the ground truth of what happened has no way to distinguish "nothing occurred" from "a privileged user erased or disabled the evidence of what occurred," because both situations look identical from the local system alone. This is a structural gap rather than a tooling gap: no amount of better local log analysis closes it, since the same privilege that grants legitimate administrative authority also grants the ability to defeat local logging.

## Related Mitigations

- [[mitigations/Replicate forensically relevant logs to an isolated, hash-chained server outside superuser control]]

## Used By

- [[techniques/Assess and design for digital forensic readiness]]

## References

- [DFCite-1189] Manral and Somani, 2021, "Establishing forensics capabilities in the presence of superuser insider threats", FSI: Digital Investigation 38, 301263.
