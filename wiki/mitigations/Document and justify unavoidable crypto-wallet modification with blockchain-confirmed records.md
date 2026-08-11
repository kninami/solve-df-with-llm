---
id: DFM-1013
type: mitigation
name: Document and justify unavoidable crypto-wallet modification with blockchain-confirmed records
source_refs:
  - DFCite-1007
updated_at: 2026-08-09
status: complete
---

# Document and justify unavoidable crypto-wallet modification with blockchain-confirmed records

## Summary

Because transferring a suspect's cryptocurrency to a Controlled Address unavoidably alters the suspect wallet's transaction record, treat that alteration as a documented, justified exception rather than an unexplained deviation from evidence-preservation principles, supported by records that are independently verifiable on the blockchain.

## Addresses

- [[weaknesses/Transferring cryptocurrency to a controlled address necessarily alters the suspect wallet's transaction record]]

## How To Apply

For every cryptocurrency transfer performed during preservation, record the date and time of transfer, total amount, transaction fee, investigator's name, screenshots of each transaction step, a screenshot of blockchain confirmation, and the local fiat currency value at the time, then save the blockchain explorer record (e.g., an Etherscan.io export) as supporting documentation. Explicitly note in the case file that the modification was necessary to prevent loss of the cryptocurrency (per ISO/IEC 27037 balancing of evidence spoliation risk against evidentiary value), and confirm that non-transaction wallet data (seed words, private keys, addresses) remained unaltered throughout.

## References

- [DFCite-1007] Taylor et al., 2022, "A comprehensive forensic preservation methodology for crypto wallets", FSI: Digital Investigation 42-43.
