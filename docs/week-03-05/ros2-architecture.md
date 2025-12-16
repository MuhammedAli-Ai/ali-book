---
sidebar_position: 1
title: ROS 2 Architecture
---

# ROS 2 Architecture

The **Robot Operating System (ROS)** is not an actual OS (like Windows or Linux) but a middleware—a set of software libraries and tools that help you build robot applications. **ROS 2** is the latest version, designed for real-time systems, security, and production use.

## Core Concepts

### 1. The Computational Graph
A ROS system consists of many independent programs (Nodes) communicating with each other.

- **Nodes**: Executable processes (e.g., a "Camera Node", a "Motor Driver Node").
- **Messages**: The data structure exchanged between nodes.
- **Topics**: A named bus where nodes exchange messages (Publisher/Subscriber).
- **Services**: Request/Response communication (Client/Server).
- **Actions**: Long-running tasks with feedback (e.g., "Navigate to Kitchen").

### 2. DDS (Data Distribution Service)
Unlike ROS 1 (which used a custom protocol), ROS 2 is built on top of **DDS**, an industry standard for real-time communications.

- **Reliability**: Guarantees message delivery.
- **Discovery**: Nodes automatically find each other on the network.
- **QoS (Quality of Service)**: Tune communication for "Best Effort" (lossy, fast) or "Reliable" (guaranteed).

### 3. Client Libraries
ROS 2 supports multiple languages via client libraries.
- **rclpy**: Python client library (Focus of this course).
- **rclcpp**: C++ client library (For high performance).

## Installation

We will run ROS 2 Humble Hawksbill on **Ubuntu 22.04**.

> [!IMPORTANT]
> If you are on Windows, we recommend using WSL 2 (Windows Subsystem for Linux) or a Docker container.

```bash
# Set locale
locale  # check for UTF-8

# Enable Universe repo
sudo apt install software-properties-common
sudo add-apt-repository universe

# Add ROS 2 GPG key
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# Install ROS 2 Humble
sudo apt update
sudo apt install ros-humble-desktop
```

## Environment Setup

Always source your ROS environment before running commands:

```bash
source /opt/ros/humble/setup.bash
```

To save time, add it to your `.bashrc`:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```
