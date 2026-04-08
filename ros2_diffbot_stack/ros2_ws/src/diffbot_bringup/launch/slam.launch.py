from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    start_sim = LaunchConfiguration('start_sim')

    slam_params = PathJoinSubstitution([
        FindPackageShare('diffbot_bringup'),
        'config',
        'slam_params.yaml',
    ])

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('diffbot_bringup'), 'launch', 'sim.launch.py'])
        ),
        condition=IfCondition(start_sim),
        launch_arguments={'use_sim_time': use_sim_time, 'rviz': 'false'}.items(),
    )

    slam = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[slam_params, {'use_sim_time': use_sim_time}],
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        DeclareLaunchArgument('start_sim', default_value='true'),
        sim_launch,
        slam,
    ])
