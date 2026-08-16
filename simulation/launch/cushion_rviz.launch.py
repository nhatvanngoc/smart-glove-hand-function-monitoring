"""
ROS2 Launch File - RViz visualization for cushion
==================================================
Launch RViz with cushion visualization.

Usage:
    ros2 launch simulation/launch/cushion_rviz.launch.py
"""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", "/home/user/adaptive_cushion_aac/simulation/config/cushion.rviz"],
        output="screen",
    )

    return LaunchDescription([rviz])
