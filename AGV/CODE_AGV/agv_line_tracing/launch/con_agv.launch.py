from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Node for teleoperation
    teleop_node = Node(
        package='agv_line_tracing',
        executable='condition',
        name='condition',
        output='screen'
    )

    # Node for wheel control
    wheel_control_node = Node(
        package='agv_line_tracing',
        executable='con',
        name='wheel_control',
        output='screen'
    )

    return LaunchDescription([
        teleop_node,
        wheel_control_node
    ])
