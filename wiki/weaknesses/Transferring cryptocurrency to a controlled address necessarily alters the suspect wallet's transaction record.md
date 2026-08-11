---
id: DFW-1013
type: weakness
name: Transferring cryptocurrency to a controlled address necessarily alters the suspect wallet's transaction record
description: Preserving a suspect's cryptocurrency by transferring it to an investigator-controlled address inherently creates a new transaction record on the suspect's wallet and reduces its balance to zero before device imaging occurs, modifying digital evidence that the second digital-evidence-preservation principle otherwise requires to remain unaltered.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-1013
source_refs:
  - DFCite-1007
updated_at: 2026-08-09
status: complete
---

# Transferring cryptocurrency to a controlled address necessarily alters the suspect wallet's transaction record

## Summary

Executing the "Transfer cryptocurrency" phase adds a new transaction to the suspect wallet's history and empties its cryptocurrency balance, both changes to the state of the digital evidence occurring before the device itself is forensically acquired. On the device side, live-access triage on Windows or Android devices similarly updates artifacts such as Link Files, Prefetch Files, MRU entries, event logs, browser memory, and SQLite database files as a side effect of accessing the wallet applications.

## Why It Matters

Digital evidence preservation principles generally require that original evidence not be altered, or that any unavoidable alteration be justified. Because this modification is a deliberate and unavoidable consequence of preventing a greater loss (the suspect emptying or hiding the cryptocurrency remotely), an investigator who fails to document and justify it risks the preservation being challenged, even though the underlying decision to preserve the asset was sound. The seed words, private keys, addresses, and other wallet-based data remain unaltered; only the transaction record and certain OS activity logs change.

## Related Mitigations

- [[mitigations/Document and justify unavoidable crypto-wallet modification with blockchain-confirmed records]]

## Used By

- [[techniques/Controlled-address cryptocurrency transfer preservation]]

## References

- [DFCite-1007] Taylor et al., 2022, "A comprehensive forensic preservation methodology for crypto wallets", FSI: Digital Investigation 42-43.
