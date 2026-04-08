# Debug Notes (Template)

## 1) TF mismatch issue

- Symptom: Robot jumps in RViz when setting goal.
- Check:
  - `ros2 run tf2_tools view_frames`
  - verify map/odom/base_link chain is continuous
- Fix:
  - align frame names in SLAM/Nav2 parameter files

## 2) No scan data in RViz

- Symptom: LaserScan display has no points.
- Check:
  - `ros2 topic list | grep scan`
  - `ros2 topic echo /scan`
- Fix:
  - check Gazebo LiDAR plugin topic remapping and frame name

## 3) Nav2 does not move robot

- Symptom: Goal accepted but no motion.
- Check:
  - `ros2 topic echo /cmd_vel`
  - controller/planner server logs
- Fix:
  - tune velocity thresholds and local planner parameters

## 4) Suggested experiment log fields

- date
- launch command
- map quality notes
- parameter changes
- observed behavior
- final conclusion
