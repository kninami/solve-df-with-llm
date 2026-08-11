---
id: DFM-1037
type: mitigation
name: Capture applied gate sequence and measured output together rather than relying on reversal for output
source_refs:
  - DFCite-1027
updated_at: 2026-08-09
status: complete
---

# Capture applied gate sequence and measured output together rather than relying on reversal for output

## Summary

Use reversible gate backtracking specifically to recover or verify a quantum circuit's known initial input state, and separately capture the circuit's applied gate log and any measured output through other means, rather than expecting gate reversal alone to reconstruct computational results.

## Addresses

- [[weaknesses/Reversible gate backtracking cannot recover a quantum circuit's computed output]]

## How To Apply

Record the full sequence of gates applied to a quantum circuit of forensic interest as they are applied (a gate log), since this is the input the reversal technique itself depends on. For any output the investigation needs, ensure it is captured through an actual measurement event (accepting the resulting collapse of that specific qubit) or through other classical logging of the computation's output at the point it interfaces with classical hardware, rather than assuming it can be derived after the fact purely by reversing the input gates.

## References

- [DFCite-1027] Closser and Bou-Harb, 2022, "A live digital forensics approach for quantum mechanical computers", FSI: Digital Investigation 40.
