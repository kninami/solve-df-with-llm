---
id: LWW-1157
type: weakness
name: Clients expand a resource-delimited digital forensic service level beyond its allocated remit
description: A client granted a quicker, lower-effort digital forensic Service Level may attempt to informally expand its investigative remit after allocation — termed "service level abuse" — effectively seeking the outcome of a higher service level while retaining the faster turnaround and lower resource commitment of the lower one, undermining the resource-delimited structure the Service Level system depends on.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1157
source_refs:
  - LWCite-1155
updated_at: 2026-08-12
status: complete
---

# Clients expand a resource-delimited digital forensic service level beyond its allocated remit

## Summary

The paper explicitly anticipates that, because some Service Levels offer quicker case turnaround, "efforts may be witnessed from clients to select a timely service level, then attempt to expand its investigative remit, essentially seeking a higher service from a lower service level" — coining this "service level abuse." Separately, service levels being incorrectly selected in the first place (whether by client error or deliberate abuse) is flagged as a risk that can lead to poor investigation outcomes.

## Why It Matters

If a DFS unit does not actively enforce the person-time and equipment-engaged-time resource delimiters intended to bound Levels 1-3, informal remit expansion converts a Service Level system's intended resource-management benefit into a source of hidden, undocumented resource drain — the very backlog and mismanagement problem the Service Level framework was designed to solve. Left unchecked, this also creates inconsistency across cases: two devices nominally allocated the same Service Level may in practice receive materially different amounts of examiner effort, undermining the transparency the framework is meant to provide to clients and undermining resource forecasting for the DFS unit.

## Related Mitigations

- [[mitigations/Enforce person-time and equipment-time resource delimiters on lower service levels to prevent scope expansion]]

## Used By

- [[techniques/Allocate a digital forensic service level using a structured decision model]]

## References

- [LWCite-1155] Horsman, 2021, "Defining 'service levels' for digital forensic science organisations", FSI: Digital Investigation 38.
