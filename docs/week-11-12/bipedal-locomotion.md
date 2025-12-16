---
sidebar_position: 1
title: Bipedal Locomotion
---

# Bipedal Locomotion

Walking on two legs is efficient for humans but incredibly hard for robots. It requires dynamic stability—the robot is constantly "falling forward" and catching itself.

## The Inverted Pendulum Model

The simplest model for a walking robot is the **Linear Inverted Pendulum Mode (LIPM)**.

- **Center of Mass (CoM)**: The point where all mass is concentrated.
- **Center of Pressure (CoP)**: The point on the foot applying force to the ground.
- **ZMP (Zero Moment Point)**: The point where horizontal forces are zero. To stay balanced, the ZMP must remain inside the support polygon (the feet area).

## Gait Generation

1.  **Trajectory Planning**: Calculate where the feet should go.
2.  **Inverse Kinematics**: Calculate joint angles to place feet at those spots.
3.  **Stabilization**: Adjust ankle torque using IMU feedback to keep the torso upright.

## Modern Approach: RL

Classical controls (ZMP) are rigid. Modern humanoids (like Unitree G1) use **Reinforcement Learning** policies trained in simulation, allowing them to recover from shoves and traverse uneven terrain naturally.
