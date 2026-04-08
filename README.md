# Differential Drive Robot based on ROS2: Mapping and Navigation System

This repository contains a ROS2 differential-drive robot integration project, including robot modeling, Gazebo simulation, LiDAR mapping, and Nav2 autonomous navigation.

## Project Goal

Build a complete ROS2-based mobile robot pipeline covering:

- Robot model construction (URDF/Xacro)
- Gazebo simulation and sensor integration
- ROS2 topic/service/TF communication
- LiDAR-based SLAM map building
- Nav2 waypoint and goal navigation
- RViz visualization and debugging

## Main Implementation

The ROS2 project is under:

`ros2_diffbot_stack/ros2_ws/src/diffbot_bringup`

Core modules:

- `launch/`: simulation, SLAM, and navigation launch files
- `urdf/`: differential-drive robot model
- `config/`: SLAM and Nav2 parameter files
- `worlds/`: Gazebo world file
- `rviz/`: RViz display config
- `docs/`: architecture notes and debugging records

## Quick Start (ROS2 Humble)

```bash
cd ros2_diffbot_stack/ros2_ws
colcon build
source install/setup.bash

# 1) Start simulation
ros2 launch diffbot_bringup sim.launch.py

# 2) Start SLAM mapping
ros2 launch diffbot_bringup slam.launch.py

# 3) Start Nav2 navigation
ros2 launch diffbot_bringup nav.launch.py
```

## Skills Demonstrated

- ROS2 package and launch orchestration
- URDF/Xacro robot modeling
- Gazebo + RViz simulation workflow
- LiDAR data access and map construction
- Nav2 stack configuration and tuning
- Multi-module debugging and integration

## Notes

This project is built as a practical entry-level robotics software portfolio focused on engineering implementation and reproducible experiments.
