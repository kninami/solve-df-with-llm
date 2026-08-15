---
id: DFT-1282
type: technique
name: Assess an application's log adequacy for forensic use against a five-task taxonomy
description: Determine whether an application's logging implementation can support incident response and forensic analysis by systematically checking, through source-code review and log-statement extraction, whether its logs contain the specific data elements (timestamps, unique identifiers, user-action detail, and error/exception context) required to perform five forensic tasks — timeline construction, event correlation, execution partitioning, misuse detection, and attack detection.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1292
aliases:
  - Application log forensic-adequacy taxonomy
source_refs:
  - DFCite-1323
updated_at: 2026-08-15
status: complete
---

# Assess an application's log adequacy for forensic use against a five-task taxonomy

## Summary

Application logs are frequently assumed to be a useful forensic and incident-response resource, but their design is almost always driven by debugging needs rather than security or forensic requirements. Systematically mapping an application's actual logging output against a fixed taxonomy of five forensic tasks it needs to support — rather than assuming logs are adequate — reveals concrete, per-application gaps (missing timestamps, missing correlation identifiers, incomplete user-action coverage) that would otherwise only surface during an actual investigation, when it is too late to fix them.

## Details

The five forensic tasks assessed are: (1) **timeline activity** — can the log's events be placed in chronological order, which requires a timestamp on each relevant entry; (2) **event correlation** — can multiple log entries belonging to the same user session, request, or transaction be linked together, which requires a unique identifier (UID) carried across the related entries; (3) **execution partitioning** — can activity be separated by the specific user, process, or component responsible; (4) **misuse detection** — do logs capture enough detail about user actions to identify policy violations or abuse of legitimate functionality; (5) **attack detection** — do logs record enough detail about failed and successful attack attempts (not just generic errors) to identify that an attack occurred and what its outcome was. Applying this taxonomy requires reviewing an application's source code, extracting every log-statement call site, and manually evaluating each one against the five tasks' data requirements, rather than relying on the application's own documentation of its logging behavior (which may not describe the actual implementation accurately).

## Examples

- Applied to 60 open-source applications, this taxonomy-driven review found 29 applications omitted timestamps entirely from at least some relevant log entries, 23 did not include unique identifiers needed for event correlation, more than half produced predominantly unstructured, text-only log events (complicating automated parsing for any of the five tasks), and 35 applications logged exceptions inadequately for attack- or misuse-detection purposes.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Open-source application logs commonly omit timestamps and unique identifiers needed for forensic event correlation]]

## References

- [DFCite-1323] Azahari and Balzarotti, 2024, "On the inadequacy of open-source application logs for digital forensics", FSI: Digital Investigation 49, 301750.
