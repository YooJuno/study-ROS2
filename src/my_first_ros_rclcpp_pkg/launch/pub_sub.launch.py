#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Correctly initialize the namespace configuration
    ros_namespace = LaunchConfiguration('namespace')

    return LaunchDescription([
        # Declare the namespace launch argument with a name and description
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Namespace for the robot'
        ),
        
        # Node for subscriber
        Node(
            package='my_first_ros_rclpy_pkg',
            executable='helloworld_subscriber',
            namespace=ros_namespace,
            name='subscriber',
            output='screen'
        ),
        
        # Node for publisher
        Node(
            package='my_first_ros_rclpy_pkg',
            executable='helloworld_publisher',
            namespace=ros_namespace,
            name='publisher',
            output='screen'
        ),
    ])