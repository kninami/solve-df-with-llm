---
id: DFT-1249
type: technique
name: Perform self-service memory introspection on a tenant's own cloud virtual machine
description: Run passive or active virtual machine introspection tools (e.g. Volatility) directly against a cloud tenant's own KVM-hosted virtual machine through a securely access-controlled introspection interface, without requiring the cloud provider's privileged host access, using one of three isolation flavors — a dedicated monitoring VM, a monitoring Docker container, or a network-exposed introspection socket.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1025
aliases:
  - KVMIveggur
  - Self-service VM introspection (VMI)
source_refs:
  - DFCite-1287
updated_at: 2026-08-14
status: complete
---

# Perform self-service memory introspection on a tenant's own cloud virtual machine

## Summary

Virtual machine introspection (VMI) — analyzing a running VM's memory and vCPU/device state from outside the guest — traditionally requires highly privileged host access that only the cloud provider holds, leaving a tenant unable to run memory forensics against their own VM without provider cooperation; an access-controlled architecture that exposes the hypervisor's native VMI capability through one of three isolated channels lets a tenant securely run their own introspection tooling in a self-service manner, closing the resource-layer VM-internal evidence gap that otherwise structurally limits cross-layer cloud attribution to Medium confidence.

## Details

The hypervisor exposes VMI capabilities as a UNIX domain socket, access to which is enforced so that only the VM's owner (or someone the owner has granted access) can reach it, and every monitored virtual machine gets its own dedicated introspection environment isolated from other tenants' VMs. Three isolation flavors trade off performance against attack surface: (1) a dedicated monitoring VM co-located with the target, using the `virtio-vsock` paravirtualized device driver already built into common hypervisor/guest stacks to carry the introspection socket, offering the strongest isolation (smallest attack surface, comparable to the hypervisor's own interface) and support for live migration of both VMs together; (2) a monitoring Docker container on the host, using a bind-mount to expose the introspection socket directly to a containerized monitoring library, offering the best measured performance (closest to running natively on the host) at the cost of exposing the container to the full host system-call interface; and (3) a network-exposed introspection socket, relayed from the hypervisor's UNIX socket to a TCP socket via `socat`, letting the introspection application run on a remote machine entirely off the host, with the smallest attack surface of the three (limited to the relay tool) but the highest latency, making it best suited to passive (asynchronous) rather than active (synchronous, control-flow-intercepting) introspection. All three flavors support both passive VMI (periodic external memory analysis with no impact on the target VM's execution, e.g. via Volatility) and active VMI (synchronous interception of the target's execution at specific points, e.g. hyper-breakpoints on system calls), and the architecture integrates with existing cloud management tooling (demonstrated against OpenNebula) so a provider can offer introspection-based digital forensics as a standard tenant-requestable service.

## Examples

- Running Volatility 3's `lsmod` plugin against a monitored VM via the Docker-container flavor (`FromDocker`) took execution time comparable to running the tool with full privileged (`Native`) root access on the host, while the dedicated-monitoring-VM (`Virtio`) and network-relay (`NetCoHost`/`NetRemote`) flavors were markedly slower for this passive-introspection benchmark.
- Deploying a modified version of the Sarracenia VMI-based SSH honeypot atop the architecture measured only a +4.5% to +13.7% function-tracing overhead on KVM (versus +18.4% to +25.5% for the same honeypot on Xen), demonstrating the architecture's practical viability for active, continuously-monitoring introspection applications such as deception technology.
- Live-migrating both the target VM and its dedicated monitoring VM together (using the existing `vsock` driver rather than custom migration code) completed without interrupting the introspection, whereas the paper notes conventional VMI implementations typically only migrate VM state and not any accompanying VMI application's state, ordinarily breaking continuous monitoring across a migration event.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Cross-layer correlation confidence is capped when resource-layer VM-internal artifacts are inaccessible]]

## References

- [DFCite-1287] Sentanoe, Dangl and Reiser, 2022, "KVMIveggur: Flexible, secure, and efficient support for self-service virtual machine introspection", DFRWS 2022 USA; FSI: Digital Investigation 42, 301397.
