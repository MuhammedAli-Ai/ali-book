---
sidebar_position: 3
title: Building Python Packages
---

# Building Python Packages

Now we will write our own ROS 2 code using Python. We will create a "Talker" (Publisher) and a "Listener" (Subscriber).

## 1. Create a Workspace

A workspace is a directory where you develop your ROS packages.

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

## 2. Create a Package

We use `ros2 pkg create` to generate the file structure.

```bash
ros2 pkg create --build-type ament_python my_py_pkg
```

This creates:
- `package.xml`: Metadata (dependencies, version).
- `setup.py`: Build configuration.
- `my_py_pkg/`: Folder for Python source code.

## 3. Write the Publisher Node

Create `~/ros2_ws/src/my_py_pkg/my_py_pkg/simple_publisher.py`:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher')
        # Create a publisher on topic 'chatter' with queue size 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = SimplePublisher()
    rclpy.spin(minimal_publisher) # Keep the node running
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## 4. Register the Executable

Open `setup.py` and add the entry point:

```python
entry_points={
    'console_scripts': [
        'talker = my_py_pkg.simple_publisher:main',
    ],
},
```

## 5. Build and Run

Go back to the root of the workspace:

```bash
cd ~/ros2_ws
colcon build --packages-select my_py_pkg
```

Source the workspace overlay:

```bash
source install/setup.bash
```

Run the node:

```bash
ros2 run my_py_pkg talker
```

You should see:
> [INFO] [simple_publisher]: Publishing: "Hello World: 0"
> [INFO] [simple_publisher]: Publishing: "Hello World: 1"

## Summary

You have successfully:
1. Created a workspace.
2. Created a Python package.
3. Wrote a Node class inheriting from `rclpy.node.Node`.
4. Setup a Publisher and Timer.
5. Built and ran the node.
