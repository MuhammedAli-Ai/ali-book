---
sidebar_position: 1
title: Workstation Requirements
---

# Digital Twin Workstation

Because Physical AI relies heavily on simulation (Isaac Sim) and deep learning, a powerful workstation is mandatory.

## Component Breakdown

| Component | Minimum Spec | Ideal Spec | Reason |
| :--- | :--- | :--- | :--- |
| **GPU** | NVIDIA RTX 4070 Ti (12GB) | NVIDIA RTX 4090 (24GB) | Isaac Sim Ray Tracing + VRAM for LLMs |
| **CPU** | Intel Core i7 (13th Gen) | AMD Ryzen 9 7950X | Physics calculations |
| **RAM** | 32 GB DDR5 | 64 GB DDR5 | Large scenes in Unity/Isaac |
| **Storage** | 1TB NVMe SSD | 2TB NVMe Gen4 | Fast asset loading |
| **OS** | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS | ROS 2 Standard |

## Laptop vs Desktop

**Desktops are highly recommended.** Laptop GPUs ("RTX 4070 Mobile") are significantly weaker than their desktop counterparts and often overheat during long training runs.

If you *must* use a laptop, ensure it has good cooling and a Thunderbolt port for potential eGPU future-proofing.
