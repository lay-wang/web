from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    start_sim = LaunchConfiguration('start_sim')

    nav2_params = PathJoinSubstitution([
        FindPackageShare('diffbot_bringup'),
        'config',
        'nav2_params.yaml',
    ])

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('diffbot_bringup'), 'launch', 'sim.launch.py'])
        ),
        condition=IfCondition(start_sim),
        launch_arguments={'use_sim_time': use_sim_time, 'rviz': 'false'}.items(),
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('nav2_bringup'), 'launch', 'bringup_launch.py'])
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'params_file': nav2_params,
            'autostart': 'True',
            'slam': 'True',
        }.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        DeclareLaunchArgument('start_sim', default_value='false'),
        sim_launch,
        nav2_launch,
    ])
