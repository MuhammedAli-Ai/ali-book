---
sidebar_position: 1
title: Gazebo Setup
---

# Robot Simulation with Gazebo

Testing code on a real robot is risky and expensive. A 100kg humanoid falling over can cost thousands of dollars and cause injury. **Simulation** allows us to test safely.

## What is Gazebo?

Gazebo is the de-facto open-source simulator for ROS. It handles:
- **Physics**: Gravity, friction, collisions (using engines like ODE or Bullet).
- **Rendering**: Visualizing the world.
- **Sensors**: Simulating camera feeds, LiDAR rays, and IMU data.

## Installation

Gazebo usually comes with `ros-humble-desktop`. To ensure you have the necessary packages:

```bash
sudo apt install ros-humble-gazebo-ros-pkgs
```

## Running a Simulation

Launch the default world:

```bash
ros2 launch gazebo_ros gazebo.launch.py
```

You should see an empty world with a ground plane and a sun light source.

## Spawning a Robot

We can spawn entities into the world. Let's spawn a simple box.

1. Create a URDF file (we will learn this in the next chapter).
2. Run the spawn node:

```bash
ros2 run gazebo_ros spawn_entity.py -file my_robot.urdf -entity my_robot
```

## Bridging ROS and Gazebo

The `gazebo_ros_pkgs` provides plugins that bridge the gap:
- **Gazebo** simulates the world.
- **Plugins** publish sensor data to ROS topics (e.g., `/camera/image_raw`).
- **Plugins** subscribe to ROS control topics (e.g., `/cmd_vel`) to move the simulated robot.

> [!NOTE]
> Modern physical AI often requires "Photorealistic" simulation. While Gazebo is great for physics, we will explore **NVIDIA Isaac Sim** and **Unity** later for better visuals.
