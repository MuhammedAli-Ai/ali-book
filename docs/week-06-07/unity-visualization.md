---
sidebar_position: 3
title: Unity Visualization
---

# Unity Visualization

While Gazebo is the standard, game engines like **Unity** and **Unreal Engine** are becoming popular for robotics because of their superior rendering capabilities.

## Why Unity?

- **Photorealism**: Better lighting, shadows, and textures. Essential for training Vision AI.
- **Physics**: Unity's PhysX is robust.
- **VR/AR**: Inspect your robot in Virtual Reality.

## The ROS-TCP-Connector

Unity communicates with ROS 2 using the **ROS-TCP-Connector** package.

1.  **ROS Side**: Runs a "Endpoint" node that acts as a server.
    ```bash
    ros2 run ros_tcp_endpoint default_server_endpoint --params-file params.yaml
    ```
2.  **Unity Side**: The robotics package connects to this IP/Port.

## Visualizing a URDF in Unity

Unity provides a **URDF Importer** tool.

1.  Install the "URDF Importer" package in Unity.
2.  Drag and drop your `.urdf` file into the Assets folder.
3.  Unity automatically creates GameObjects with:
    - Meshes for visuals.
    - Colliders for physics.
    - ArticulationBodies for joints (critical for stable physics).

## Digital Twins

A **Digital Twin** is a virtual replica that matches the real robot's state in real-time. By streaming sensor data from the real robot to Unity, we can visualize what the robot "thinks" is happening, even if we are miles away.
