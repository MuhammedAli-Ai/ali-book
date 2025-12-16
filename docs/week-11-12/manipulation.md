---
sidebar_position: 2
title: Manipulation
---

# Manipulation and Grasping

A humanoid without arms is just a fancy walker. **Manipulation** allows the robot to interact with the world.

## The 6-DoF Arm

Most humanoid arms have at least 6 Degrees of Freedom (DoF):
- Shoulder (3: Pitch, Roll, Yaw)
- Elbow (1: Pitch)
- Wrist (2: Pitch, Roll)

7-DoF arms are "redundant," meaning they can reach the same point in multiple poses (like you scratching your head with your elbow up or down).

## Inverse Kinematics (IK)

- **Forward Kinematics**: Given joint angles -> Where is the hand? (Easy)
- **Inverse Kinematics**: I want the hand *here* -> What are the joint angles? (Hard)

Popular solvers:
- **KDL**: Numerical solver (standard in ROS).
- **Trac-IK**: Faster/robuster numerical solver.
- **BioIK**: Evolution-based solver.

## MoveIt 2

**MoveIt 2** is the manipulation framework for ROS 2.
- **Motion Planning**: Avoiding obstacles while moving from A to B (OMPL).
- **Scene Monitor**: Keeping track of collision objects.
