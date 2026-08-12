---
id: DFT-1013
type: technique
name: Preserve cryptocurrency by transferring it to a controlled address
description: Insert a "Transfer cryptocurrency" phase before data acquisition and hashing in the digital forensics process, moving a suspect's cryptocurrency from hosted, unhosted, or paper wallets into a freshly created, LEA-controlled address to prevent the funds from being moved, hidden, or lost before the device itself is imaged.
objective_ids:
  - DFO-1010
weakness_ids:
  - DFW-1013
aliases:
  - Controlled-address cryptocurrency transfer preservation
  - crypto wallet triage and transfer
source_refs:
  - DFCite-1007
updated_at: 2026-08-09
status: complete
---

# Preserve cryptocurrency by transferring it to a controlled address

## Summary

Extending the DFRWS digital forensics process model (Palmer, 2001), a three-phase methodology -- conduct triage, secure the cryptocurrency, then proceed with standard digital forensics best practice to secure the device -- is performed before the usual "Acquire data" / "Hash the data" steps, because cryptocurrency stored in an accessible wallet is fragile and can be moved, spent, or hidden in a single second if not preserved first.

## Details

Triage locates crypto artifacts (wallet applications, credentials, seed words, encrypted containers) via direct device access rather than forensic tooling, since forensic imaging takes longer and does not itself neutralize the risk of the suspect remotely emptying the wallet. Once located, the investigator transfers cryptocurrency from the suspect's hosted wallet (e.g., an exchange, via account freeze or direct transfer), unhosted wallet (web, mobile, desktop, or hardware, via direct transfer using the suspect's own device and application), or paper wallet/seed phrase (via an intermediary wallet) into a fresh Controlled Address created on an LEA-managed device, then verifies the transaction on both the suspect wallet and a blockchain explorer before proceeding to standard device seizure procedures.

## Examples

- Experimental validation moved 0.0017 ETH from five suspect wallet types (Blockchain.com web wallet, Exodus desktop wallet, Coinomi mobile wallet, Trezor hardware wallet, and a discovered paper wallet/seed phrase) into a Ledger Nano X-based Controlled Wallet, verifying each transfer via Etherscan.io.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Transferring cryptocurrency to a controlled address necessarily alters the suspect wallet's transaction record]]

## References

- [DFCite-1007] Taylor et al., 2022, "A comprehensive forensic preservation methodology for crypto wallets", FSI: Digital Investigation 42-43.
