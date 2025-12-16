---
sidebar_position: 2
title: URDF and SDF
---

# Universal Robot Description Format (URDF)

To simulate a robot, we must describe its physical properties: shape, size, mass, and how joints connect. **URDF** is an XML format used in ROS for this purpose.

## Structure of a URDF

A robot is made of **Links** (rigid bodies) connected by **Joints**.

```xml
<robot name="simple_bot">

  <!-- Base Link -->
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.5 0.5 0.2"/>
      </geometry>
      <material name="blue"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.5 0.5 0.2"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="10"/>
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/>
    </inertial>
  </link>

  <!-- Wheel Link -->
  <link name="right_wheel">
    <visual>
      <geometry>
         <cylinder length="0.05" radius="0.1"/>
      </geometry>
    </visual>
    ...
  </link>

  <!-- Joint connecting Base to Wheel -->
  <joint name="base_to_wheel" type="continuous">
    <parent link="base_link"/>
    <child link="right_wheel"/>
    <axis xyz="0 1 0"/>
    <origin xyz="0 -0.3 0"/>
  </joint>

</robot>
```

## Key Components

1.  **Visual**: What the robot looks like (meshes, colors).
2.  **Collision**: Simplified geometry used for physics calculations. Low poly = faster simulation.
3.  **Inertial**: Mass and Moment of Inertia. Crucial for realistic physics.

## SDF (Simulation Description Format)

While ROS uses URDF, Gazebo uses **SDF** internally. SDF is more capable (describing entire worlds, lights, and multiple robots). Gazebo automatically converts URDF to SDF, but for complex simulations, you might write SDF directly.

## Xacro (XML Macros)

Writing raw XML is verbose. **Xacro** allows us to use variables and macros to keep URDFs clean.

```xml
<xacro:property name="wheel_radius" value="0.1" />
<cylinder radius="${wheel_radius}" ... />
```
