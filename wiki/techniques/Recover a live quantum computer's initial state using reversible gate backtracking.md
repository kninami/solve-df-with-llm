---
id: DFT-1036
type: technique
name: Recover a live quantum computer's initial state using reversible gate backtracking
description: Recover a live quantum computer's known initial qubit preparation state by identifying which reversible logic gates were applied to build its current circuit and computationally reapplying them in exact reverse order, avoiding the need to directly observe or measure the live superposed/entangled system, which would otherwise collapse it and destroy the very state under investigation.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1037
aliases:
  - Reversible quantum gate backtracking for live quantum computer forensics
source_refs:
  - DFCite-1027
updated_at: 2026-08-09
status: complete
---

# Recover a live quantum computer's initial state using reversible gate backtracking

## Summary

Directly measuring or observing a quantum system in superposition forces a probabilistic collapse to a single basis state (the Observer Effect), and the No-Cloning Theorem prevents copying an unknown quantum state the way a classical drive could be imaged — both widely cited as reasons live forensics on quantum computers was assumed infeasible. This technique sidesteps both problems: rather than observing the system, the investigator determines which reversible gates (e.g., Pauli-X, Hadamard, CNOT) were applied and in what order, then applies those same gates again in exact reverse sequence, which — because the gates are unitary and reversible by construction — deterministically restores and reveals the system's known starting state without ever needing to measure the live, undisturbed circuit.

## Details

Reversible quantum gates (Pauli X/Y/Z, Hadamard, CNOT, Toffoli, cswap) can be undone by reapplying the same gate (self-inverse, e.g., Pauli-X) or the specific inverse gate in the opposite order from the original sequence, per the Principle of Deferred Measurement, which establishes that measurement can be delayed arbitrarily long, or avoided entirely, without changing the outcome. For entangled multi-qubit states (e.g., a Bell State), reversal requires applying the same CNOT and Hadamard gates in the correct reverse order and on the correct target/control qubits to fully disentangle and decode the state back to its original preparation. This is analogous, as the authors note, to connecting a USB drive to a forensic workstation and copying its contents without disturbing the original: the investigation captures how the system got to its current state without altering or ending that state through observation.

## Examples

- On IBM's `ibmq_lima` and `ibm-santiago` quantum systems, a qubit initialized to 0, flipped to 1 via Pauli-X, and then superposed via Hadamard was fully and correctly restored to its original preparation state by reapplying the Hadamard and Pauli-X gates in reverse order, confirmed by measurement showing the expected probability distribution.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Reversible gate backtracking cannot recover a quantum circuit's computed output]]

## References

- [DFCite-1027] Closser and Bou-Harb, 2022, "A live digital forensics approach for quantum mechanical computers", FSI: Digital Investigation 40.
