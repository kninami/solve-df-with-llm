---
id: LWW-1080
type: weakness
name: IoT interconnectivity identification finds no relationship when the connected service retains no interconnection traces
description: The Identification of Interconnectivity phase can only reveal a relationship between two IoT services or devices if at least one of them retained an artifact recording the interconnection; if a service was used through an interconnection with other services but its own application or account data does not properly store any trace of that connection, the phase will fail to reveal the relationship even though the interconnection genuinely occurred.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1080
source_refs:
  - LWCite-1070
updated_at: 2026-08-10
status: complete
---

# IoT interconnectivity identification finds no relationship when the connected service retains no interconnection traces

## Summary

The authors observed this directly in one of their six experimental scenarios: although a "Bugs" service was used through interconnection with two different services ("Smart speaker" and "Google Home"), artifacts stored in the Bugs service's own package directories did not properly retain any trace of that interconnection, so the proposed framework could not reveal the relationship from that service's data alone. The authors state plainly: "if no traces of interconnectivity are stored anywhere, it is not possible to reveal the proper relationships even when a user has used a complex set of interconnected IoT services."

## Why It Matters

An investigator relying on the interconnectivity-identification phase to map out a suspect's full IoT ecosystem may conclude that two services or devices are unrelated purely because neither side's retained artifacts happen to record the connection, when in fact the interconnection existed — an absence-of-evidence gap that is indistinguishable, from the investigator's side, between "no interconnection occurred" and "the interconnection occurred but left no discoverable trace."

## Related Mitigations

- [[mitigations/Corroborate IoT interconnectivity gaps with server-side, network, or other independent evidence sources]]

## Used By

- [[techniques/Apply a structured IoT-specific digital forensic process model]]

## References

- [LWCite-1070] Kim et al., 2022, "An improved IoT forensic model to identify interconnectivity between things", FSI: Digital Investigation 44.
