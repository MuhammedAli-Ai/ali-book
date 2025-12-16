---
sidebar_position: 2
title: Sensor Systems
---

# Sensor Systems: The Robot's Senses

Just as humans rely on sight, sound, and touch to navigate the world, robots rely on a suite of sensors to perceive their environment. In Physical AI, high-quality data is the fuel for intelligent decisions.

## 1. LiDAR (Light Detection and Ranging)

LiDAR uses laser pulses to measure distances, creating a precise 3D map of the environment (Point Cloud).

- **How it works**: Fires laser beams and measures the "Time of Flight" (ToF) for the light to bounce back.
- **Use Case**: Mapping (SLAM), Obstacle Avoidance.
- **Example Hardware**: Velodyne, Ouster, RPLIDAR.

> [!TIP]
> **2D vs 3D LiDAR**: 2D LiDAR scans a single plane (great for basic floor mapping), while 3D LiDAR scans the entire volume (essential for complex environments and humanoids).

## 2. Depth Cameras (RGB-D)

RGB-D cameras provide both color (RGB) and Depth (D) information.

- **How it works**: Uses stereovision (two lenses) or structured light (projecting a pattern) to calculate depth.
- **Use Case**: Object recognition, hand tracking, visual navigation.
- **Example Hardware**: **Intel RealSense D435i** (Recommended for this course), OAK-D.

### Code Example: Accessing Depth Data (Python)

```python
import pyrealsense2 as rs

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start streaming
pipeline.start(config)

try:
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        dist = depth_frame.get_distance(320, 240) # Get distance at center pixel
        print(f"Distance: {dist} meters")
finally:
    pipeline.stop()
```

## 3. IMU (Inertial Measurement Unit)

The IMU is the "inner ear" of the robot, helping it maintain balance and orientation.

- **Components**:
  - **Accelerometer**: Measures linear acceleration (gravity).
  - **Gyroscope**: Measures angular velocity (rotation).
  - **Magnetometer**: Measures magnetic north (heading).
- **Use Case**: Balancing a humanoid, dead reckoning navigation.
- **Example Hardware**: BNO055, MPU6050.

## 4. Proprioception (Encoders)

Robots need to know the position of their own body parts.

- **Encoders**: Measure the angle of motor joints.
- **Force/Torque Sensors**: Measure the strain on a limb (haptic feedback).

---

## Sensor Fusion

Rarely does a robot rely on a single sensor. **Sensor Fusion** (e.g., Kalman Filter) combines data from multiple sources (IMU + Odometer + Lidar) to reduce uncertainty and create a robust state estimate.

In the [next module](../week-03-05/ros2-architecture), we will learn how to process these sensor streams using **ROS 2**.
