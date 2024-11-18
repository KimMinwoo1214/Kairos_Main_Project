from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Node for video publishing
    img_publisher_node = Node(
        package='ros2_cv_webcam',
        executable='img_publisher',  # Replace with the actual executable name for your img_publisher
        name='img_publisher',
        output='screen'
    )

    # Node for detection status receiving
    detection_node = Node(
        package='ros2_cv_webcam',
        executable='detection',  # Replace with the actual executable name for your detection node
        name='detection',
        output='screen'
    )

    return LaunchDescription([
        img_publisher_node,
        detection_node
    ])
