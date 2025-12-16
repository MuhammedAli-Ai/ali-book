---
sidebar_position: 1
title: NVIDIA Isaac SDK
---

# NVIDIA Isaac Platform

For high-performance robotics, especially humanoids requiring massive parallel simulation, **NVIDIA Isaac** is the industry leader. It leverages the power of RTX GPUs to accelerate both simulation and perception.

## Isaac Sim

Built on **NVIDIA Omniverse**, Isaac Sim offers:
- **Ray Tracing**: Physically accurate light simulation.
- **USD (Universal Scene Description)**: A powerful file format for 3D worlds.
- **Domain Randomization**: Automatically changing lighting and textures to train robust AI models.

### Installation Requirements
- **OS**: Ubuntu 20.04/22.04 or Windows 10/11.
- **GPU**: RTX 2070 or higher (RTX 4090 recommended for heavy workloads).
- **RAM**: 32GB+.

## Isaac ROS

NVIDIA provides hardware-accelerated ROS 2 packages optimized for Jetson and discrete GPUs.

### Key Packages:
- **Isaac ROS VSLAM**: Visual SLAM using stereo cameras (more robust than standard SLAM).
- **Isaac ROS Nvblox**: 3D reconstruction for collision avoidance on the GPU.
- **Isaac ROS GEMs**: Optimized algorithms for image processing.

## Setup on Jetson Orin

The **Physical AI Edge Kit** (Jetson Orin Nano) is designed to run Isaac ROS.

1. **Flash JetPack**: Ensure you are running JetPack 6.0+.
2. **Install Docker**: Isaac ROS runs inside Docker containers to manage dependencies involving CUDA and TensorRT.
3. **Run the Container**:
   ```bash
   scripts/run_dev.sh
   ```
