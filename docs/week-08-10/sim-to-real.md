---
sidebar_position: 3
title: Sim-to-Real Transfer
---

# Sim-to-Real Transfer

A robot that walks perfectly in Isaac Sim might fall immediately in the real world. This is the **Reality Gap**.

## Causes of the Reality Gap

1.  **Physics Mismatch**: Friction coefficients, motor damping, and cable mass are hard to model perfectly.
2.  **Sensor Noise**: Real cameras have motion blur and lighting artifacts.
3.  **Latency**: Real hardware has communication delays not present in perfectly synchronous simulation.

## Solving the Gap

### 1. Domain Randomization
During training, we intentionally vary the simulation parameters:
- Randomize friction of the floor.
- Randomize mass of the robot links.
- Add random noise to sensor inputs.

> If the AI learns to walk despite this chaos, it becomes robust enough to handle the "chaos" of the real world.

### 2. System Identification (SysID)
Measure the real robot carefully to tune the simulation parameters to match reality as closely as possible.

### 3. On-Policy Adaptation
The robot continues to learn slightly while deployed, adapting its policy to the minor differences it detects.

## The Deployment Pipeline

1.  **Train** in Isaac Lab (Massive Parallelism).
2.  **Export** Policy as ONNX file.
3.  **Deploy** to Jetson Orin Nano (using TensorRT).
4.  **Inference**: The Jetson runs the neural network to drive the real motors.
