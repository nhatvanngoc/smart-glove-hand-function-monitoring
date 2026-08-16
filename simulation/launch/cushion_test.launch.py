"""
ROS2 Launch File - Cushion Test
=================================
Launch Gazebo + cushion + mannequin + controller for end-to-end testing.

Usage:
    ros2 launch simulation/launch/cushion_test.launch.py
"""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time", default="true")

    gazebo = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]),
        launch_arguments={"world": PathJoinSubstitution([
            FindPackageShare("gazebo_ros"), "worlds", "empty.world"
        ])}.items(),
    )

    cushion_spawn = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity", "air_cushion",
            "-file", "/home/user/adaptive_cushion_aac/simulation/urdf/cushion_simple.urdf",
        ],
        output="screen",
    )

    mannequin_spawn = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity", "mannequin",
            "-file", "/home/user/adaptive_cushion_aac/simulation/urdf/mannequin.urdf",
            "-z", "0.20",
        ],
        output="screen",
    )

    cushion_controller = Node(
        package="simulation",
        executable="cushion_controller_node.py",
        name="cushion_controller",
        output="screen",
        parameters=[{"use_sim_time": use_sim_time}],
    )

    tf_static = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0", "0", "0", "0", "0", "0", "world", "base_link"],
    )

    return LaunchDescription([
        DeclareLaunchArgument("use_sim_time", default_value="true"),
        gazebo,
        tf_static,
        cushion_spawn,
        mannequin_spawn,
        cushion_controller,
    ])
