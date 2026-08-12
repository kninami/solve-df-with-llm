---
id: DFW-1037
type: weakness
name: Reversible gate backtracking cannot recover a quantum circuit's computed output
description: Reversible gate backtracking is confined to input collection: it can deterministically recover a quantum circuit's known initial preparation state from its applied gate sequence, but it does not capture or reconstruct computations that occur beyond that initial input, so any information from the circuit's actual computed output (which by nature requires measurement, or is not recoverable by simply reversing the input gates) remains inaccessible to this technique.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1037
source_refs:
  - DFCite-1027
updated_at: 2026-08-09
status: complete
---

# Reversible gate backtracking cannot recover a quantum circuit's computed output

## Summary

The authors explicitly state this as a limitation of their demonstrated approach: "the gate reversal approach does not capture computations beyond the initial input of quantum gates. Data passed from a state of superposition and measured may be inaccessible and not captured by the reversal." For example, the original preparation state of a qubit is obscured, and it becomes "nearly impossible to back-trace the gates without measurement at some point along the circuit" if the investigator does not already know that initial value.

## Why It Matters

An investigator applying this technique should understand it as a method for verifying or deriving a circuit's known starting configuration, not as a general-purpose means of recovering everything the quantum computer computed — a categorically different scope than, for example, imaging a classical hard drive's full contents. Overstating what the technique can recover risks presenting an incomplete forensic account of a quantum computation as though it were complete, particularly for any prime-number-factoring or other output-generating computation whose result is not derivable purely from the initial input state.

## Related Mitigations

- [[mitigations/Capture applied gate sequence and measured output together rather than relying on reversal for output]]

## Used By

- [[techniques/Recover a live quantum computer's initial state using reversible gate backtracking]]

## References

- [DFCite-1027] Closser and Bou-Harb, 2022, "A live digital forensics approach for quantum mechanical computers", FSI: Digital Investigation 40.
