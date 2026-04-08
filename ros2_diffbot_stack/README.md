# ROS2 Differential Drive Integration Stack

This folder contains a complete ROS2 starter framework for a differential-drive robot project.

## Scope

- URDF/Xacro robot modeling
- Gazebo simulation
- LiDAR data access
- SLAM map building
- Nav2 autonomous navigation
- Launch orchestration and parameter tuning

## Layout

- `ros2_ws/src/diffbot_bringup/launch`: launch files for simulation, SLAM, Nav2
- `ros2_ws/src/diffbot_bringup/urdf`: robot model files
- `ros2_ws/src/diffbot_bringup/config`: parameter templates
- `ros2_ws/src/diffbot_bringup/worlds`: Gazebo world
- `ros2_ws/src/diffbot_bringup/rviz`: RViz configuration
- `docs/`: architecture and debugging notes

## Build and Run

```bash
cd ros2_ws
colcon build
source install/setup.bash

# start simulation
ros2 launch diffbot_bringup sim.launch.py

# start SLAM
ros2 launch diffbot_bringup slam.launch.py

# start navigation
ros2 launch diffbot_bringup nav.launch.py
```

## Suggested Next Steps

- Replace model dimensions with your own robot parameters.
- Add teleop and real-hardware bringup launch files.
- Record demonstration video and ros2 bag samples for portfolio use.
