from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    rviz = LaunchConfiguration('rviz')

    model_file = PathJoinSubstitution([
        FindPackageShare('diffbot_bringup'),
        'urdf',
        'diffbot.urdf.xacro',
    ])
    world_file = PathJoinSubstitution([
        FindPackageShare('diffbot_bringup'),
        'worlds',
        'simple.world',
    ])

    robot_description = {'robot_description': Command(['xacro ', model_file])}

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
        ),
        launch_arguments={'world': world_file}.items(),
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': use_sim_time}],
    )

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'diffbot', '-topic', 'robot_description'],
        output='screen',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', PathJoinSubstitution([FindPackageShare('diffbot_bringup'), 'rviz', 'nav.rviz'])],
        condition=IfCondition(rviz),
        output='screen',
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        DeclareLaunchArgument('rviz', default_value='true'),
        gazebo,
        rsp,
        spawn_robot,
        rviz_node,
    ])
