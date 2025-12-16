---
sidebar_position: 2
title: Physical AI Edge Kit
---

# The Physical AI Edge Kit

For the real-world component (Weeks 3-5 and Capstone), you need an "Edge AI" setup that can mount on a robot.

## 1. The Brain: NVIDIA Jetson

We use the **NVIDIA Jetson Orin** series. These are miniature supercomputers.

- **Recommended**: **Jetson Orin Nano (8GB)** (~$250)
  - 40 TOPS of AI performance.
  - Good for inference and basic ROS 2.
- **Pro**: **Jetson Orin NX (16GB)**
  - 100 TOPS.
  - Required if running heavy VLA models locally.

## 2. The Eyes: Intel RealSense

Standard Webcams are not enough. We need Depth.

- **Model**: **Intel RealSense D435i** (~$350)
  - Global Shutter (no motion blur).
  - Built-in IMU.
  - Reliable stereo depth indoors.

## 3. Interaction: Audio

- **Mic Array**: **Seeed ReSpeaker 4-Mic Array** (~$70)
  - LED ring (programmable).
  - Beamforming (locating where sound comes from).
