---
sidebar_position: 2
title: Nodes and Topics
---

# Nodes and Topics

The **Publisher-Subscriber** model is the most common communication pattern in ROS 2. It allows nodes to stream data (like sensor readings) without knowing which other nodes are listening.

## Understanding Nodes

A robot is a system of nodes. For a mobile robot, you might have:
1. `camera_node` (Publishes images)
2. `motor_node` (Subscribes to velocity commands)
3. `brain_node` (Subscribes to images, Publishes velocity)

### CLI Commands

Check running nodes:
```bash
ros2 node list
```

Get info about a specific node:
```bash
ros2 node info /my_node
```

## Understanding Topics

Topics are the "pipes" data flows through.

- **Publishers** send data to a topic.
- **Subscribers** receive data from a topic.

### CLI Commands

List active topics:
```bash
ros2 topic list
```

See the data on a topic in real-time:
```bash
ros2 topic echo /topic_name
```

Publish a message manually (for testing):
```bash
ros2 topic pub /chatter std_msgs/msg/String "data: 'Hello ROS'"
```

## Hands-on: Turtlesim

Let's use the built-in simulator to visualize this.

1. **Start the simulator**:
   ```bash
   ros2 run turtlesim turtlesim_node
   ```
   *You should see a window with a turtle.*

2. **Control the turtle** (in a new terminal):
   ```bash
   ros2 run turtlesim turtle_teleop_key
   ```
   *Use arrow keys to move.*

3. **Inspect the Graph**:
   ```bash
   rqt_graph
   ```
   *This tool visualizes the nodes (`/teleop_turtle`, `/turtlesim`) and the topic (`/turtle1/cmd_vel`) connecting them.*

## Message Types

Every topic has a defined **Message Type**.

Check the type of a topic:
```bash
ros2 topic type /turtle1/cmd_vel
# Output: geometry_msgs/msg/Twist
```

Check the structure of that interface:
```bash
ros2 interface show geometry_msgs/msg/Twist
```

Output:
```
Vector3  linear
	float64 x
	float64 y
	float64 z
Vector3  angular
	float64 x
	float64 y
	float64 z
```

This tells us that to move the turtle, we need to send linear (forward) and angular (turn) velocities.
