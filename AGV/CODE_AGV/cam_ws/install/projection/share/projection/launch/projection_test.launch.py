from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='projection',
            executable='projector',
            name='projector',
            output='screen'
        ),
	Node(
            package='projection',
            executable='img_pub',
            name='img_pub',
            output='screen'
        ),
        Node(
            package='laserscan_to_pointcloud',
            executable='convert',
            name='laserscan_to_pointcloud',
            output='screen'
        )
    ])
