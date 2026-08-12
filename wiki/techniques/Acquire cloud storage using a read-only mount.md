---
id: DFT-1021
type: technique
name: Acquire cloud storage using a read-only mount
description: Acquire data from a suspect's cloud storage account by mounting it as a local, OS-enforced read-only filesystem before copying, so that accidental write commands are blocked at the operating-system level rather than relying solely on tool-level safeguards.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1021
aliases:
  - Read-only mount-based cloud storage acquisition
  - rclone read-only mount acquisition
source_refs:
  - DFCite-1014
updated_at: 2026-08-09
status: complete
---

# Acquire cloud storage using a read-only mount

## Summary

A general-purpose cloud storage access tool that can mount a remote storage account as a local filesystem (e.g., via a FUSE-based driver) can be mounted in read-only mode, causing the operating system itself — not just the acquisition tool — to reject any write attempt. This gives an investigator a forensically safer acquisition path than a plain copy command, where accidentally reversing the source/destination could modify or delete evidence on the remote account.

## Details

Because the read-only enforcement happens via standard OS filesystem mechanisms (mount flags), it holds regardless of which program subsequently tries to write to the mount point — GUI drag-and-drop, a shell copy command, or any other application will all be rejected identically. This is a stronger safety property than a tool's own `--dry-run` flag, which merely simulates an operation without OS-level enforcement. After mounting read-only, files are copied out using ordinary OS file-copy tools, and multi-cloud tools built on a common backend abstraction can apply this same read-only mount procedure uniformly across many different cloud storage providers using one acquisition workflow.

## Examples

- Mounting a suspect's FTP or cloud remote with `rclone mount remote: /mnt/ --read-only` and then attempting `cp test.file /mnt/` returned a `Read-only file system` error at the OS level, confirming write-protection independent of the copy method used.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Read-only mount cloud acquisition does not preserve original directory timestamps]]

## References

- [DFCite-1014] Breitinger et al., 2022, "A forensic analysis of rclone and rclone's prospects for digital forensic investigations of cloud storage", FSI: Digital Investigation 43.
