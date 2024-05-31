# Written by Juan Pablo Gutiérrez
# 30 05 2024

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='diff_drive_robot',
            executable='velocity_listener',
            name='velocity_node',
            parameters=[{'use_sim_time': True}] 
        ),
    ])