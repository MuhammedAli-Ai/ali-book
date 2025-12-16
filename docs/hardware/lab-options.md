---
sidebar_position: 3
title: Lab Options
---

# Lab Options

Depending on budget, there are two paths for the "Body" of the robot.

## Option A: The Proxy Approach (Budget)
**Unitree Go2 Edu**

The Unitree Go2 is a remarkably capable quadruped (dog) robot. While not a humanoid, the principles of balancing and navigation transfer perfectly.

- **Cost**: ~$3,000 (Edu version with API access).
- **Pros**: Robust, unlikely to break if it falls, excellent ROS 2 support.

## Option B: The Ether Lab (Cloud-Native)

If hardware is impossible to acquire, we use the **Ether Lab**.

- **Concept**: Renting GPU instances on AWS/Azure to run high-fidelity simulations.
- **Cost**: AWS `g5.2xlarge` is ~$1.20/hour. This adds up (~$200/quarter), but requires zero upfront capex.
- **Workflow**: 
  1. Develop locally on VS Code.
  2. Remote-SSH into Cloud Instance.
  3. Visualize Isaac Sim via WebRTC streaming.
