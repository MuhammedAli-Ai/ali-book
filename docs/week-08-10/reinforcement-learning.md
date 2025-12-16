---
sidebar_position: 2
title: Reinforcement Learning
---

# Reinforcement Learning (RL) for Robotics

Traditional robotics relies on manually designed controllers (if *this* then *that*). **Reinforcement Learning (RL)** allows robots to *learn* how to walk or grasp by trial and error in simulation.

## The RL Loop

1.  **Agent**: The robot.
2.  **Environment**: The simulation (Isaac Sim).
3.  **Action**: The motor commands sent to joints.
4.  **State**: The sensor readings (angles, IMU).
5.  **Reward**: Positive points for walking forward, negative for falling.

> **Goal**: Maximize cumulative reward.

## Isaac Gym (Isaac Lab)

Training a humanoid to walk takes millions of steps. Doing this in real-time Gazebo would take years. **Isaac Lab** runs thousands of robots in parallel on a single GPU.

- **Parallel Simulation**: Simulating 4096 robots simultaneously.
- **GPU PhysX**: Physics calculations happen on the GPU, avoiding CPU bottlenecks.

## Example: Training a Biped

1.  **Define Reward Function**:
    ```python
    reward = velocity_x * 1.0  # Reward moving forward
    reward -= energy_cost * 0.1 # Penalize using too much power
    if fallen:
        reward -= 100 # Big penalty for falling
    ```

2.  **Start Training**: The neural network starts with random twitching.
3.  **Convergence**: After minutes (or hours), the policy converges to a stable walking gait.
