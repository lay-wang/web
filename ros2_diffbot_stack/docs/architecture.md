# Architecture Overview

## Pipeline

1. Robot model (`URDF/Xacro`) is loaded by `robot_state_publisher`.
2. Gazebo spawns the robot and publishes simulated sensor streams.
3. LiDAR (`/scan`) and odometry (`/odom`) are consumed by SLAM Toolbox.
4. SLAM builds map (`/map`) and updates TF (`map -> odom -> base_link`).
5. Nav2 stack consumes map/TF and sends velocity commands (`/cmd_vel`).

## Key Topics

- `/scan`: LiDAR data
- `/odom`: wheel odometry
- `/tf`, `/tf_static`: frame transforms
- `/cmd_vel`: control command
- `/map`: generated map

## Key Frames

- `map`
- `odom`
- `base_link`
- `lidar_link`

## Integration Focus

- Launch orchestration for simulation, SLAM, and Nav2
- Parameter tuning for planner/controller stability
- End-to-end module debugging using `ros2 topic`, `tf2`, and `ros2 bag`
