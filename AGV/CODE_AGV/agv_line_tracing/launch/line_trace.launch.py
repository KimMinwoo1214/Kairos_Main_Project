from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    yellow_pub_node = Node(
        package='agv_line_tracing',
        executable='y_pub',
        name='yellow_pub',
        output='screen',
    )

    yellow_sub_node = Node(
        package='agv_line_tracing',
        executable='y_sub',
        name='yellow_sub',
        output='screen',
    )

    return LaunchDescription([
        yellow_pub_node,
        yellow_sub_node
    ])
