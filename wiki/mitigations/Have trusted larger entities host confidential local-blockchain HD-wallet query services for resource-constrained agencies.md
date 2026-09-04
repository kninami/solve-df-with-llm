---
id: LWM-1104
type: mitigation
name: Have trusted larger entities host confidential local-blockchain HD-wallet query services for resource-constrained agencies
source_refs:
  - LWCite-1099
updated_at: 2026-08-10
status: complete
---

# Have trusted larger entities host confidential local-blockchain HD-wallet query services for resource-constrained agencies

## Summary

Where a local agency lacks the storage and compute resources for its own confidential local-blockchain HD-wallet query platform, have a trusted larger entity (state/federal law enforcement, or a university) host the service so the agency can query it without needing to run its own node or compromise investigation confidentiality.

## Addresses

- [[weaknesses/Forensically sound local-blockchain HD-wallet address derivation requires prohibitive storage and compute resources]]

## How To Apply

Establish a hosting relationship with a trusted larger entity capable of running and maintaining the blockchain query platform, taking advantage of its microservice-based architecture to distribute individual components across trusted parties as needed. Ensure the hosting arrangement itself preserves confidentiality guarantees appropriate to the sensitivity of the investigation, since the entire point of the local-blockchain design is avoiding disclosure to an untrusted third party.

## References

- [LWCite-1099] Thomas et al., 2022, "BlockQuery: Toward forensically sound cryptocurrency investigation", FSI: Digital Investigation 40.
